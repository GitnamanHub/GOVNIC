# GovBizConnect

A full-stack AI application that provides NIC (National Industrial Classification) code predictions and government scheme recommendations for businesses based on their descriptions.

## Features

- **NIC Code Prediction**: Uses a trained TF-IDF + SVM classifier to predict the most relevant NIC code
- **Government Scheme Recommendations**: Provides top 5 government schemes based on semantic similarity
- **Modern Web Interface**: Clean Streamlit frontend for easy interaction
- **RESTful API**: FastAPI backend with structured endpoints

## Project Structure

```
GovBizConnect/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── models/                 # Trained models and data
│   │   ├── nic_classifier.pkl
│   │   ├── scheme_embeddings.pkl
│   │   └── scheme_metadata.pkl
│   └── data/                   # Training datasets
│       ├── nic_codes.csv
│       └── govt_schemes.csv
├── frontend/
│   └── app.py                  # Streamlit application
├── utils/
│   ├── train_nic_classifier.py
│   └── generate_scheme_embeddings.py
├── requirements.txt
└── README.md
```

## Installation

### macOS Setup (Recommended)

1. Clone the repository
2. Run the Mac setup script:
   ```bash
   ./setup_mac.sh
   ```
   This creates a virtual environment and installs all dependencies.

### Manual Installation

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training Models

1. Train the NIC classifier:

   ```bash
   source venv/bin/activate
   python utils/train_nic_classifier.py
   ```

2. Generate scheme embeddings:
   ```bash
   source venv/bin/activate
   python utils/generate_scheme_embeddings.py
   ```

### Running the Application

1. Start the FastAPI backend:

   ```bash
   source venv/bin/activate
   cd backend
   uvicorn main:app --reload
   ```

2. Start the Streamlit frontend:

   ```bash
   source venv/bin/activate
   cd frontend
   streamlit run app.py
   ```

3. Open your browser and navigate to `http://localhost:8501`

## API Endpoints

- `POST /get_nic`: Get NIC code prediction

  - Input: `{"description": "business description"}`
  - Output: `{"nic_code": "predicted_code", "confidence": 0.95}`

- `POST /get_schemes`: Get government scheme recommendations
  - Input: `{"description": "business description"}`
  - Output: `{"schemes": [{"name": "scheme_name", "description": "scheme_desc", "similarity": 0.85}]}`

## Technologies Used

- **Backend**: FastAPI, scikit-learn, sentence-transformers
- **Frontend**: Streamlit
- **ML Models**: TF-IDF + SVM classifier, Sentence embeddings
- **Data Processing**: Pandas, NumPy
