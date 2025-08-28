from pymongo import MongoClient
db = None

def init_db(uri):
    global db
    client = MongoClient(uri)
    db = client.get_default_database()

def get_user_stats(user_id):
    return db.stats.find_one({"user_id": user_id}) or {
        "user_id": user_id, "played": 0, "won": 0, "lost": 0, "draw": 0
    }

def update_stats(user_id, result):
    stats = get_user_stats(user_id)
    stats["played"] += 1
    stats[result] += 1
    db.stats.replace_one({"user_id": user_id}, stats, upsert=True)
