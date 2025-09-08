from pymongo import MongoClient

# Your MongoDB connection string
MONGO_URI = "mongodb+srv://iamraushan7542_db_user:raushan123@cluster0.psf0jvr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def setup_database():
    client = MongoClient(MONGO_URI)
    db = client["expense_tracker"]  # Database name
    transactions = db["transactions"]  # Collection name
    
    # MongoDB is schemaless, so you don’t need to "create" tables
    print("✅ MongoDB connected and ready!")
    return transactions

if __name__ == "__main__":
    setup_database()
