import metapy
import numpy as np
import os

# Step 1: Preprocess the text data
def preprocess_data(dataset_path):
    # Create an inverted index config
    cfg = """
    stop-words = ../data/lemur-stopwords.txt

    [[analyzers]]
    method = "ngram-word"
    ngram = 1
    filter = "default"
    """
    
    with open('config.toml', 'w') as f:
        f.write(cfg)

    idx = metapy.index.make_inverted_index('config.toml')
    dset = metapy.learn.Dataset(idx)
    return dset

# Step 2: Apply K-means clustering
def apply_kmeans(dset, num_clusters):
    # Initialize K-means
    kmeans = metapy.clustering.KMeans(num_clusters)
    
    # Fit the model
    cluster_assignments = kmeans.fit(dset)
    
    return kmeans, cluster_assignments

# Step 3: Print cluster centroids
def print_cluster_centroids(kmeans, idx):
    term_id_to_word = {v: k for k, v in idx.term_id_mapping().items()}
    
    print("Cluster centroids:")
    for i, centroid in enumerate(kmeans.centroids()):
        print(f"Cluster {i}:")
        for term_id, weight in enumerate(centroid):
            if weight > 0:
                print(f"  {term_id_to_word[term_id]}: {weight}")

if __name__ == "__main__":
    dataset_path = 'sample_dataset.txt'
    num_clusters = 3  # Example: we want to cluster into 3 groups
    
    # Preprocess the data
    dset = preprocess_data(dataset_path)
    
    # Apply K-means clustering
    kmeans, cluster_assignments = apply_kmeans(dset, num_clusters)
    
    # Print cluster centroids
    idx = metapy.index.make_inverted_index('config.toml')
    print_cluster_centroids(kmeans, idx)

    # Clean up the config file
    os.remove('config.toml')
