#!/bin/bash

# GovBizConnect Virtual Environment Activation Script

echo "🔧 Activating GovBizConnect virtual environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run the setup script first:"
    echo "  ./setup_mac.sh"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "✅ Virtual environment activated!"
echo ""
echo "🚀 Available commands:"
echo "  python run_app.py                    # Start the full application"
echo "  python utils/train_nic_classifier.py # Train NIC classifier"
echo "  python utils/generate_scheme_embeddings.py # Generate embeddings"
echo "  python test_api.py                   # Test the API"
echo ""
echo "🔧 Manual startup:"
echo "  cd backend && uvicorn main:app --reload"
echo "  cd frontend && streamlit run app.py"
echo ""
echo "🌐 Access points:"
echo "  Frontend: http://localhost:8501"
echo "  Backend: http://localhost:8000"
echo ""
echo "💡 To deactivate the virtual environment, run: deactivate" 