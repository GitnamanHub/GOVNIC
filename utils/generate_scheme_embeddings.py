import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

def generate_scheme_embeddings():
    """
    Generate sentence embeddings for government schemes using sentence-transformers
    """
    print("Loading government schemes dataset...")
    
    # Load the dataset
    data_path = "backend/data/govt_schemes.csv"
    df = pd.read_csv(data_path)
    
    print(f"Dataset loaded with {len(df)} schemes")
    
    # Initialize the sentence transformer model
    print("Loading sentence transformer model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for scheme descriptions
    print("Generating embeddings...")
    scheme_descriptions = df['description'].tolist()
    embeddings = model.encode(scheme_descriptions, show_progress_bar=True)
    
    print(f"Generated embeddings shape: {embeddings.shape}")
    
    # Create metadata dictionary
    scheme_metadata = {
        'scheme_names': df['scheme_name'].tolist(),
        'descriptions': df['description'].tolist(),
        'embeddings': embeddings
    }
    
    # Save embeddings and metadata
    embeddings_path = "backend/models/scheme_embeddings.pkl"
    metadata_path = "backend/models/scheme_metadata.pkl"
    
    os.makedirs(os.path.dirname(embeddings_path), exist_ok=True)
    
    # Save embeddings
    with open(embeddings_path, 'wb') as f:
        pickle.dump(embeddings, f)
    
    # Save metadata
    with open(metadata_path, 'wb') as f:
        pickle.dump(scheme_metadata, f)
    
    print(f"Embeddings saved to: {embeddings_path}")
    print(f"Metadata saved to: {metadata_path}")
    
    # Test similarity search
    test_query = "small business loan micro enterprise"
    test_embedding = model.encode([test_query])
    
    # Calculate similarities
    similarities = cosine_similarity(test_embedding, embeddings)[0]
    
    # Get top 5 similar schemes
    top_indices = np.argsort(similarities)[::-1][:5]
    
    print(f"\nTest query: '{test_query}'")
    print("Top 5 similar schemes:")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. {df.iloc[idx]['scheme_name']} (similarity: {similarities[idx]:.4f})")
        print(f"   Description: {df.iloc[idx]['description']}")
        print()

if __name__ == "__main__":
    generate_scheme_embeddings() 