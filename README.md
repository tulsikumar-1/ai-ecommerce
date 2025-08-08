# AI Enhanced E-Commerce Product Catalog

## Overview
A modular Python app that provides an AI-powered natural language product search using the OpenRouter API.

## Features
- Static product catalog in JSON
- LLM-based parsing of search queries (category, price, rating)
- Modular structure with error handling
- Streamlit web UI

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Generate products JSON:
```bash
python generate_products.py
```

3. Set OpenRouter API key:
```bash
export OPENROUTER_API_KEY="your-api-key"
```

## Usage

Run the app:
```bash
streamlit run app.py
```

## Live Demo
You can try the app live here: [Live Demo](https://ai-ecommerce-tulsi-kumar.streamlit.app)



## AI Feature
Option A: Smart Product Search using OpenRouter and Deepseek models to interpret queries.

## Bonus Blockchain integration idea
This AI-powered search can be integrated with blockchain features such as:

- **Token-gated pricing:** Only allow users holding certain tokens to see discounted prices.
- **On-chain user preferences:** Store user search preferences and product likes on-chain for personalization.
- **Loyalty smart contracts:** Reward users with tokens for purchases or searches, encouraging engagement.
