# 🍎 macOS Setup Guide for GovBizConnect

This guide is specifically tailored for macOS users with Python 3 installed.

## Prerequisites

- **macOS** (any recent version)
- **Python 3.8+** (use `python3` command)

## Quick Setup (Recommended)

1. **Clone the repository** (if not already done)

   ```bash
   git clone <repository-url>
   cd GovBizConnect
   ```

2. **Run the Mac setup script**
   ```bash
   ./setup_mac.sh
   ```

This script will automatically:

- ✅ Check if Python 3 is installed
- ✅ Create a virtual environment
- ✅ Install all required dependencies
- ✅ Train the NIC classifier model
- ✅ Generate scheme embeddings
- ✅ Provide next steps

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

### 4. Start the Application

**Option A: One-command startup**

```bash
source venv/bin/activate
python run_app.py
```

**Option B: Manual startup**

```bash
# Terminal 1: Start backend
source venv/bin/activate
cd backend
uvicorn main:app --reload

# Terminal 2: Start frontend
source venv/bin/activate
cd frontend
streamlit run app.py
```

## Access the Application

- **🌐 Frontend**: http://localhost:8501
- **🔧 Backend API**: http://localhost:8000
- **📚 API Documentation**: http://localhost:8000/docs

## Testing

Test the API to ensure everything works:

```bash
source venv/bin/activate
python test_api.py
```

## Troubleshooting

### Common Issues

1. **"python3: command not found"**

   - Install Python 3 from https://www.python.org/downloads/
   - Or use Homebrew: `brew install python3`

2. **Virtual environment issues**

   - Make sure to activate the virtual environment: `source venv/bin/activate`
   - If venv doesn't exist, run the setup script: `./setup_mac.sh`

3. **Port already in use**

   - Kill processes using ports 8000 or 8501:

   ```bash
   lsof -ti:8000 | xargs kill -9
   lsof -ti:8501 | xargs kill -9
   ```

4. **Permission denied on setup script**

   ```bash
   chmod +x setup_mac.sh
   ```

5. **Model training fails**
   - Ensure you have internet connection (for downloading models)
   - Check available disk space
   - Make sure virtual environment is activated: `source venv/bin/activate`
   - Try running with verbose output:
   ```bash
   python -v utils/train_nic_classifier.py
   ```

### Getting Help

- Check the logs in the terminal where you started the services
- Verify all models are created in `backend/models/`
- Ensure both backend and frontend are running simultaneously

## File Structure After Setup

```
GovBizConnect/
├── venv/                           # ✅ Virtual environment
├── backend/
│   ├── models/
│   │   ├── nic_classifier.pkl      # ✅ Created by setup
│   │   ├── scheme_embeddings.pkl   # ✅ Created by setup
│   │   └── scheme_metadata.pkl     # ✅ Created by setup
│   └── ...
├── setup_mac.sh                    # ✅ Mac setup script
└── ...
```

## Next Steps

After successful setup:

1. Open http://localhost:8501 in your browser
2. Enter a business description
3. Get instant NIC code predictions and government scheme recommendations!

## Example Usage

Try these business descriptions:

- "Software development and mobile app creation"
- "Manufacturing of electronic components"
- "Small business loan micro enterprise"
- "Agriculture farming irrigation"
