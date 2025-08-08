import streamlit as st
import json
import os
import re
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    st.error("⚠️ OPENROUTER_API_KEY not found. Please set it in your .env file.")
    st.stop()

# --- Pydantic Model for validating LLM output ---
class AnswerOutput(BaseModel):
    matched_products: list[str]

# --- Helper to create prompt ---
def get_prompt_template(question, context, format_instructions):
    return f"""
You are an assistant that helps users find products based on natural language queries.

User query: "{question}"

Here is the product catalog:
{context}

{format_instructions}
"""

# --- OnlineLLM class ---
class OnlineLLM:
    def __init__(self, api_key: str):
        openai.api_base = "https://openrouter.ai/api/v1"
        openai.api_key = api_key
        self.model = "deepseek/deepseek-r1:free"  # Your free tier model

    def generate_answer(self, question: str, retrieved_chunks: list[dict]) -> AnswerOutput:
        # Prepare context string from product list
        context = "\n".join(
            [f"{p['name']} (${p['price']}, Category: {p['category']}, Rating: {p['rating']})" for p in retrieved_chunks]
        )
        format_instructions = "Return only a JSON array of product names that match the query."

        prompt = get_prompt_template(question, context, format_instructions)

        max_retries = 3

        for attempt in range(1, max_retries + 1):
            try:
                st.write(f"[Attempt {attempt}] Calling LLM...")
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0,
                    max_tokens=300,
                )
                raw_text = response["choices"][0]["message"]["content"]
                st.write("LLM raw response:", raw_text)

                # Extract JSON array from response
                json_array_str = re.search(r"\[.*\]", raw_text, re.DOTALL).group(0)
                matched_names = json.loads(json_array_str)

                # Validate output
                validated = AnswerOutput(matched_products=matched_names)
                return validated

            except Exception as e:
                st.warning(f"Attempt {attempt} failed: {e}")

        # Return empty if all attempts fail
        return AnswerOutput(matched_products=[])

# --- Load product data ---
@st.cache_data
def load_products():
    with open("data/products.json", "r") as f:
        return json.load(f)

def filter_products(products, category, max_price):
    filtered = products
    if category != "All":
        filtered = [p for p in filtered if p["category"] == category]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    return filtered

# Instantiate LLM once
llm = OnlineLLM(api_key=OPENROUTER_API_KEY)

def ai_smart_search(query, products):
    answer = llm.generate_answer(query, products)
    matched_names = answer.matched_products
    matched_products = [p for p in products if p["name"] in matched_names]
    return matched_products

# --- Streamlit UI ---
st.title("🛍️ E-Commerce Product Catalog")

products = load_products()

# Sidebar filters
st.sidebar.header("Filter Products")

categories = ["All"] + sorted(list({p["category"] for p in products}))
selected_category = st.sidebar.selectbox("Category", categories)

max_price = st.sidebar.slider("Max Price", min_value=0, max_value=250, value=250, step=5)

st.sidebar.markdown("---")
st.sidebar.header("Smart NLP Search")
query = st.sidebar.text_input("Search (e.g. 'running shoes under $100 with good reviews')")

st.subheader("Products")

if query.strip():
    with st.spinner("Searching with AI..."):
        try:
            matched_products = ai_smart_search(query, products)
            if matched_products:
                st.write(f"### Search Results for: \"{query}\"")
                display_products = matched_products
            else:
                st.write("No products matched your search.")
                display_products = []
        except Exception as e:
            st.error(f"Error during AI search: {e}")
            display_products = []
else:
    display_products = filter_products(products, selected_category, max_price)

if display_products:
    for p in display_products:
        st.markdown(f"""
**{p['name']}**  
Category: {p['category']}  
Price: ${p['price']:.2f}  
Rating: {p['rating']}  
{p['description']}
""")
        st.markdown("---")
else:
    st.write("No products to display.")
