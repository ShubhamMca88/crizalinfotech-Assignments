import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def load_dataset(file_path):
    return pd.read_csv(file_path)

def train_naive_bayes(train_data, train_labels):
    vectorizer = CountVectorizer()
    train_vectors = vectorizer.fit_transform(train_data)
    
    model = MultinomialNB()
    model.fit(train_vectors, train_labels)
    
    return model, vectorizer

def evaluate_model(model, vectorizer, test_data, test_labels):
    test_vectors = vectorizer.transform(test_data)
    predictions = model.predict(test_vectors)
    accuracy = accuracy_score(test_labels, predictions)
    return accuracy

if __name__ == "__main__":
    # Load datasets
    train_df = load_dataset('train.csv')
    test_df = load_dataset('test.csv')
    
    train_texts = train_df['text'].values
    train_labels = train_df['label'].values
    test_texts = test_df['text'].values
    test_labels = test_df['label'].values
    
    # Train Naive Bayes model
    nb_model, vectorizer = train_naive_bayes(train_texts, train_labels)
    
    # Evaluate model
    accuracy = evaluate_model(nb_model, vectorizer, test_texts, test_labels)
    print("Accuracy: {:.2f}%".format(accuracy * 100))
