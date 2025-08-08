import json

products = [
    {
        "name": "AirZoom Running Shoes",
        "price": 89.99,
        "category": "Shoes",
        "description": "Lightweight running shoes designed for speed and comfort.",
        "rating": 4.5
    },
    {
        "name": "TrailBlaze Hiking Boots",
        "price": 120.0,
        "category": "Shoes",
        "description": "Durable hiking boots with superior grip for rough terrains.",
        "rating": 4.7
    },
    {
        "name": "Comfy Cotton T-Shirt",
        "price": 19.99,
        "category": "Clothing",
        "description": "Soft, breathable cotton t-shirt available in multiple colors.",
        "rating": 4.2
    },
    {
        "name": "SlimFit Jeans",
        "price": 49.99,
        "category": "Clothing",
        "description": "Stylish slim-fit jeans made with stretchable fabric.",
        "rating": 4.3
    },
    {
        "name": "SmartWatch X200",
        "price": 199.99,
        "category": "Electronics",
        "description": "Feature-rich smartwatch with heart rate monitor and GPS.",
        "rating": 4.6
    },
    {
        "name": "Wireless Earbuds Pro",
        "price": 149.99,
        "category": "Electronics",
        "description": "Noise-cancelling wireless earbuds with long battery life.",
        "rating": 4.4
    },
    {
        "name": "Classic Leather Wallet",
        "price": 39.99,
        "category": "Accessories",
        "description": "Handmade leather wallet with multiple compartments.",
        "rating": 4.8
    },
    {
        "name": "Sunshine Sunglasses",
        "price": 25.0,
        "category": "Accessories",
        "description": "UV protection sunglasses with stylish frames.",
        "rating": 4.1
    },
    {
        "name": "Yoga Mat Pro",
        "price": 35.0,
        "category": "Fitness",
        "description": "Eco-friendly non-slip yoga mat, 6mm thick.",
        "rating": 4.5
    },
    {
        "name": "Protein Powder 2lb",
        "price": 59.99,
        "category": "Fitness",
        "description": "High-quality whey protein for muscle recovery.",
        "rating": 4.7
    }
]

with open("products.json", "w") as f:
    json.dump(products, f, indent=4)

print("products.json file generated.")
