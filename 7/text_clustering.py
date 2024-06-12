import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Preprocess the text data
def preprocess_data(filename):
    with open(filename, 'r') as file:
        documents = [line.strip() for line in file.readlines()]
    return documents

# Step 2: Apply K-means clustering
def apply_kmeans(documents, num_clusters):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    cluster_assignments = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    return X, cluster_assignments, centroids, vectorizer

# Step 3: Evaluate clustering quality using silhouette score
def evaluate_clustering(X, cluster_assignments):
    silhouette_avg = silhouette_score(X, cluster_assignments)
    return silhouette_avg

if __name__ == "__main__":
    num_clusters = 3  # Example: we want to cluster into 3 groups
    
    # Preprocess the data
    documents = preprocess_data('dataset.txt')
    
    # Apply K-means clustering
    X, cluster_assignments, centroids, vectorizer = apply_kmeans(documents, num_clusters)
    
    # Print cluster centroids
    print("Cluster centroids (top terms per cluster):")
    terms = vectorizer.get_feature_names_out()
    order_centroids = centroids.argsort()[:, ::-1]
    for i in range(num_clusters):
        print(f"Cluster {i}:")
        for ind in order_centroids[i, :10]:  # Top 10 terms per cluster
            print(f" {terms[ind]}")
    
    # Evaluate clustering quality
    silhouette_avg = evaluate_clustering(X, cluster_assignments)
    print("Silhouette Score:", silhouette_avg)
