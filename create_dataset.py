import pandas as pd
import random
import os


def create_sample_data():
    os.makedirs("data", exist_ok=True)

    names = [
        "Asha", "Ravi", "Sita", "Rahul", "Meena",
        "John", "Kavya", "Arjun", "Divya", "Sai",
        "Priya", "Kiran", "Anjali", "Vamsi", "Sneha",
        "Nikhil", "Pooja", "Manoj", "Deepika", "Charan"
    ]

    cities = [
        "Guntur", "Vijayawada", "Hyderabad", "Bangalore", "Chennai"
    ]

    genders = [
        "Male", "Female"
    ]

    categories = [
        "Beauty", "Electronics", "Fashion", "Grocery"
    ]

    products = {
        "Beauty": ["Face Cream", "Shampoo", "Lipstick"],
        "Electronics": ["Headphones", "Smart Watch", "Keyboard"],
        "Fashion": ["Saree", "Kurti", "T-Shirt"],
        "Grocery": ["Rice Bag", "Oil Packet", "Sugar"]
    }

    customer_data = []
    for i in range(1, 101):
        category = random.choice(categories)
        customer_data.append({
            "customer_id": 1000 + i,
            "name": random.choice(names) + str(i),
            "age": random.randint(18, 60),
            "gender": random.choice(genders),
            "city": random.choice(cities),
            "category": category,
            "total_spent": random.randint(2000, 50000),
            "purchase_count": random.randint(1, 20),
            "last_purchase_days": random.randint(1, 180),
            "churn": random.choice([0, 1]),
            "product": random.choice(products[category])
        })

    customer_df = pd.DataFrame(customer_data)
    customer_df.to_csv("data/old_customers.csv", index=False)

    product_list = [
        {"product_name": "Face Cream", "category": "Beauty", "current_stock": 25, "min_stock": 20},
        {"product_name": "Shampoo", "category": "Beauty", "current_stock": 15, "min_stock": 20},
        {"product_name": "Lipstick", "category": "Beauty", "current_stock": 10, "min_stock": 15},
        {"product_name": "Headphones", "category": "Electronics", "current_stock": 5, "min_stock": 10},
        {"product_name": "Smart Watch", "category": "Electronics", "current_stock": 8, "min_stock": 12},
        {"product_name": "Keyboard", "category": "Electronics", "current_stock": 18, "min_stock": 10},
        {"product_name": "Saree", "category": "Fashion", "current_stock": 20, "min_stock": 15},
        {"product_name": "Kurti", "category": "Fashion", "current_stock": 30, "min_stock": 25},
        {"product_name": "T-Shirt", "category": "Fashion", "current_stock": 40, "min_stock": 30},
        {"product_name": "Rice Bag", "category": "Grocery", "current_stock": 50, "min_stock": 20},
        {"product_name": "Oil Packet", "category": "Grocery", "current_stock": 35, "min_stock": 25},
        {"product_name": "Sugar", "category": "Grocery", "current_stock": 18, "min_stock": 20}
    ]

    products_df = pd.DataFrame(product_list)
    products_df.to_csv("data/products.csv", index=False)


if __name__ == "__main__":
    create_sample_data()
    print("✅ Sample data files created in data/old_customers.csv and data/products.csv")
