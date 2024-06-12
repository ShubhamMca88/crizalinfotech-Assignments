import metapy
import toml
import os

# Step 1: Preprocess the text data
def preprocess_data(dataset_path):
    # Create an inverted index config
    cfg = """
    stop-words = "../data/lemur-stopwords.txt"
    dataset = "../sample_dataset.txt"

    [[analyzers]]
    method = "ngram-word"
    ngram = 1
    filter = "default"
    """
    
    with open('config.toml', 'w') as f:
        f.write(cfg)

    idx = metapy.index.make_inverted_index('config.toml')
    return idx

# Step 2: Train the LDA model
def train_lda_model(idx, num_topics, num_iters):
    lda_inf = metapy.topics.ldamodel(idx, num_topics, alpha=0.1, beta=0.01, max_iters=num_iters)
    return lda_inf

# Step 3: Print top words in each topic
def print_top_words(lda_inf, idx, num_topics, num_top_words):
    term_id_to_word = {v: k for k, v in idx.term_id_mapping().items()}
    
    print("Top words per topic:")
    for topic_id in range(num_topics):
        top_words = lda_inf.top_k_terms(topic_id, num_top_words)
        print(f"Topic {topic_id}:")
        for term_id, weight in top_words:
            print(f"  {term_id_to_word[term_id]}: {weight}")

if __name__ == "__main__":
    dataset_path = 'sample_dataset.txt'
    num_topics = 3  # Example: we want to extract 3 topics
    num_iters = 1000  # Number of iterations to train the model
    num_top_words = 10  # Number of top words to display per topic
    
    # Preprocess the data
    idx = preprocess_data(dataset_path)
    
    # Train the LDA model
    lda_inf = train_lda_model(idx, num_topics, num_iters)
    
    # Print top words in each topic
    print_top_words(lda_inf, idx, num_topics, num_top_words)

    # Clean up the config file
    os.remove('config.toml')
