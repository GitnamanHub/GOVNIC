# 🔧 Virtual Environment Setup for macOS

## Why Virtual Environment?

The error you encountered is due to macOS's newer Python installations using "externally managed environments" (PEP 668). This prevents installing packages globally to protect the system Python installation.

## Solution: Virtual Environment

We've updated the project to use Python virtual environments, which:

- ✅ Isolates project dependencies
- ✅ Avoids system Python conflicts
- ✅ Works with all macOS Python installations
- ✅ Prevents permission issues

## Updated Setup Process

### 1. Quick Setup (Recommended)

```bash
./setup_mac.sh
```

This script automatically:

- Creates a virtual environment (`venv/`)
- Installs all dependencies in the virtual environment
- Trains the ML models
- Provides next steps

### 2. Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train models
python utils/train_nic_classifier.py
python utils/generate_scheme_embeddings.py
```

## Running the Application

### Option 1: One-command startup

```bash
source venv/bin/activate
python run_app.py
```

### Option 2: Manual startup

```bash
# Terminal 1: Backend
source venv/bin/activate
cd backend && uvicorn main:app --reload

# Terminal 2: Frontend
source venv/bin/activate
cd frontend && streamlit run app.py
```

### Option 3: Using activation script

```bash
./activate.sh
```

## Important Notes

1. **Always activate the virtual environment** before running any Python commands:

   ```bash
   source venv/bin/activate
   ```

2. **You'll see `(venv)` in your terminal prompt** when the virtual environment is active

3. **To deactivate** the virtual environment:

   ```bash
   deactivate
   ```

4. **The virtual environment is project-specific** - it won't affect other Python projects

## Troubleshooting

### "Virtual environment not found"

```bash
./setup_mac.sh
```

### "Permission denied"

```bash
chmod +x setup_mac.sh
chmod +x activate.sh
```

### "Command not found" after activation

Make sure you're in the project directory and the virtual environment exists:

```bash
ls -la venv/
```

## File Structure

```
GovBizConnect/
├── venv/                    # Virtual environment (created by setup)
├── backend/
├── frontend/
├── utils/
├── setup_mac.sh            # Mac setup script
├── activate.sh             # Virtual environment activation
└── ...
```

## Benefits of This Approach

- ✅ Works with all macOS Python installations
- ✅ No system Python conflicts
- ✅ Isolated dependencies
- ✅ Easy to clean up (just delete `venv/` folder)
- ✅ Reproducible environment across different machines
