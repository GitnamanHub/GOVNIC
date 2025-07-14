# 🚀 Quick Start Guide

## Prerequisites

- Python 3.8 or higher (use `python3` command)

## macOS Quick Setup

For macOS users, use the setup script:
```bash
./setup_mac.sh
```

## One-Command Setup

Run the startup script to automatically:

1. Train the NIC classifier
2. Generate scheme embeddings
3. Start both backend and frontend

```bash
source venv/bin/activate
python run_app.py
```

## Manual Setup (Alternative)

If you prefer to run steps manually:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Models

```bash
python utils/train_nic_classifier.py
python utils/generate_scheme_embeddings.py
```

### 4. Start Backend

```bash
source venv/bin/activate
cd backend
uvicorn main:app --reload
```

### 5. Start Frontend (in new terminal)

```bash
source venv/bin/activate
cd frontend
streamlit run app.py
```

## Access the Application

- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Test the API

Run the test script to verify everything works:

```bash
source venv/bin/activate
python test_api.py
```

## Usage

1. Open the frontend in your browser
2. Enter a business description
3. Click "Get Recommendations"
4. View the predicted NIC code and recommended government schemes

## Example Business Descriptions

- "Software development and mobile app creation"
- "Manufacturing of electronic components"
- "Retail sale of food and beverages"
- "Construction of residential buildings"
- "Small business loan micro enterprise"

## Troubleshooting

- **Backend not starting**: Check if port 8000 is available
- **Frontend not loading**: Check if port 8501 is available
- **Model training errors**: Ensure you have sufficient disk space and internet connection
- **API errors**: Check the backend logs for detailed error messages
