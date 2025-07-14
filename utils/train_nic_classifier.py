import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os

def train_nic_classifier():
    """
    Train a TF-IDF + SVM classifier for NIC code prediction
    """
    print("Loading NIC codes dataset...")
    
    # Load the dataset
    data_path = "backend/data/nic_codes.csv"
    df = pd.read_csv(data_path)
    
    print(f"Dataset loaded with {len(df)} samples")
    print(f"Number of unique NIC codes: {df['nic_code'].nunique()}")
    
    # Split the data
    X = df['description']
    y = df['nic_code']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Create the pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2),
            stop_words='english',
            min_df=2,
            max_df=0.95
        )),
        ('classifier', LinearSVC(
            random_state=42,
            max_iter=1000,
            C=1.0
        ))
    ])
    
    print("Training the classifier...")
    pipeline.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    model_path = "backend/models/nic_classifier.pkl"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)
    
    print(f"\nModel saved to: {model_path}")
    
    # Test with a sample
    test_description = "Software development and mobile app creation"
    prediction = pipeline.predict([test_description])[0]
    confidence = np.max(pipeline.decision_function([test_description]))
    
    print(f"\nSample prediction:")
    print(f"Description: {test_description}")
    print(f"Predicted NIC Code: {prediction}")
    print(f"Confidence: {confidence:.4f}")

if __name__ == "__main__":
    train_nic_classifier() 