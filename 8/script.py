from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Step 1: Preprocess the user-item interaction data
def preprocess_data(file_path):
    reader = Reader(line_format='user item rating', sep=',', skip_header=True)
    data = Dataset.load_from_file(file_path, reader=reader)
    return data

# Step 2: Apply collaborative filtering
def apply_collaborative_filtering(data):
    trainset, testset = train_test_split(data, test_size=0.25, random_state=42)
    
    # Use user-based collaborative filtering
    algo = KNNBasic(sim_options={'user_based': True})
    algo.fit(trainset)
    
    return algo, trainset, testset

# Step 3: Generate recommendations
def generate_recommendations(algo, user_id, top_n=5):
    # Get a list of all items
    all_items = algo.trainset.all_items()
    item_inner_ids = [algo.trainset.to_inner_iid(item) for item in all_items]
    
    # Predict ratings for all items
    predictions = [(item, algo.predict(uid=user_id, iid=algo.trainset.to_raw_iid(item)).est) for item in item_inner_ids]
    
    # Sort and get top N recommendations
    recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)[:top_n]
    recommendations = [(algo.trainset.to_raw_iid(item), rating) for item, rating in recommendations]
    
    return recommendations

# Step 4: Evaluate the system using Mean Absolute Error (MAE)
def evaluate_system(algo, testset):
    predictions = algo.test(testset)
    mae = accuracy.mae(predictions)
    return mae

if __name__ == "__main__":
    file_path = 'user_item_ratings.csv'
    
    # Preprocess the data
    data = preprocess_data(file_path)
    
    # Apply collaborative filtering
    algo, trainset, testset = apply_collaborative_filtering(data)
    
    # Generate recommendations for a specific user
    user_id = '1'  # User ID should be a string
    recommendations = generate_recommendations(algo, user_id)
    print(f"Top recommendations for user {user_id}:")
    for item_id, rating in recommendations:
        print(f"Item {item_id} with estimated rating {rating:.2f}")
    
    # Evaluate the system
    mae = evaluate_system(algo, testset)
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
