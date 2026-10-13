# GOVNIC / GovBizConnect

GovBizConnect is a full-stack application that predicts National Industrial Classification (NIC) codes from business descriptions and recommends potentially relevant government schemes.

## What it does

- **NIC code prediction:** Uses a TF-IDF + SVM classifier to predict a relevant NIC code.
- **Scheme recommendations:** Ranks government schemes using semantic similarity.
- **Web interface:** Streamlit frontend for entering business descriptions and viewing results.
- **API:** FastAPI backend with interactive API documentation.

## Tech stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** Streamlit
- **Machine learning:** scikit-learn, TF-IDF, SVM, sentence-transformers
- **Data processing:** pandas, NumPy

## Repository layout

```text
backend/       API, model artifacts, and source datasets
frontend/      Streamlit user interface
utils/         Scripts for training the NIC classifier and generating embeddings
requirements.txt
run_app.py
setup_mac.sh
QUICKSTART.md
```

## Setup

### Prerequisites

- Python 3.8 or newer
- `pip`
- Internet access for installing Python packages and downloading any required model assets

### Recommended quick start on macOS

```bash
git clone https://github.com/GitnamanHub/GOVNIC.git
cd GOVNIC
chmod +x setup_mac.sh
./setup_mac.sh
source venv/bin/activate
python run_app.py
```

The setup script is intended to create a virtual environment, install dependencies, and prepare the model artifacts. If you prefer manual setup, follow [QUICKSTART.md](QUICKSTART.md).

### Access the application

When both services start successfully:

- **Streamlit frontend:** http://localhost:8501
- **FastAPI:** http://localhost:8000
- **Interactive API docs:** http://localhost:8000/docs

To run the backend and frontend separately, see the manual instructions in [QUICKSTART.md](QUICKSTART.md).

## API overview

The README documents these endpoints:

- `POST /get_nic` — predicts an NIC code from a business description.
- `POST /get_schemes` — returns scheme recommendations for a business description.

Open the interactive API docs after starting the backend to inspect the current request and response schemas.

## Current limitations to communicate clearly

Predictions and scheme recommendations are model outputs, not official eligibility decisions or government advice. Users should verify NIC classifications and scheme requirements with authoritative sources before relying on the results.

## Development notes

- Python bytecode, virtual environments, editor folders, and macOS Finder metadata are local artifacts and should not be committed.
- The repository includes generated model artifacts under `backend/models/`; keep these only if they are intentionally versioned for reproducibility and deployment.
- Keep datasets and model artifacts documented with their source, license, date, and regeneration steps.

## License and data

Add the project license and explicit dataset/model provenance before inviting reuse. Confirm redistribution rights for the datasets and any derived artifacts.
