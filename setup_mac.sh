#!/bin/bash

# GovBizConnect Mac Setup Script
echo "🚀 Setting up GovBizConnect on macOS..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    echo "You can download it from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 is available"

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip in virtual environment
echo "📦 Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully"

# Train models if they don't exist
if [ ! -f "backend/models/nic_classifier.pkl" ]; then
    echo "🤖 Training NIC classifier..."
    python utils/train_nic_classifier.py
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to train NIC classifier"
        exit 1
    fi
else
    echo "✅ NIC classifier already exists"
fi

if [ ! -f "backend/models/scheme_embeddings.pkl" ]; then
    echo "🤖 Generating scheme embeddings..."
    python utils/generate_scheme_embeddings.py
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to generate scheme embeddings"
        exit 1
    fi
else
    echo "✅ Scheme embeddings already exist"
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To start the application, run:"
echo "  source venv/bin/activate"
echo "  python run_app.py"
echo ""
echo "Or start manually:"
echo "  source venv/bin/activate"
echo "  cd backend && uvicorn main:app --reload"
echo "  cd frontend && streamlit run app.py"
echo ""
echo "Access the application at:"
echo "  Frontend: http://localhost:8501"
echo "  Backend: http://localhost:8000"
echo ""
echo "💡 Remember to activate the virtual environment before running any commands:"
echo "  source venv/bin/activate" 