#!/usr/bin/env python3
"""
GovBizConnect Startup Script
This script trains the models and starts the application
"""

import subprocess
import sys
import os
import time
import requests
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_backend_health():
    """Check if backend is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    print("🚀 Starting GovBizConnect Application")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("backend").exists() or not Path("frontend").exists():
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Step 1: Check if virtual environment exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found. Please run the setup script first:")
        print("   ./setup_mac.sh")
        sys.exit(1)
    
    # Step 2: Train NIC classifier
    if not Path("backend/models/nic_classifier.pkl").exists():
        if not run_command("python utils/train_nic_classifier.py", "Training NIC classifier"):
            print("❌ Failed to train NIC classifier")
            sys.exit(1)
    else:
        print("✅ NIC classifier already exists, skipping training")
    
    # Step 3: Generate scheme embeddings
    if not Path("backend/models/scheme_embeddings.pkl").exists():
        if not run_command("python utils/generate_scheme_embeddings.py", "Generating scheme embeddings"):
            print("❌ Failed to generate scheme embeddings")
            sys.exit(1)
    else:
        print("✅ Scheme embeddings already exist, skipping generation")
    
    # Step 4: Start backend
    print("\n🔧 Starting FastAPI backend...")
    backend_process = subprocess.Popen(
        "cd backend && uvicorn main:app --reload --host 0.0.0.0 --port 8000",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for backend to start
    print("⏳ Waiting for backend to start...")
    for i in range(30):  # Wait up to 30 seconds
        if check_backend_health():
            print("✅ Backend is running!")
            break
        time.sleep(1)
    else:
        print("❌ Backend failed to start within 30 seconds")
        backend_process.terminate()
        sys.exit(1)
    
    # Step 5: Start frontend
    print("\n🌐 Starting Streamlit frontend...")
    frontend_process = subprocess.Popen(
        "cd frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0",
        shell=True
    )
    
    print("\n🎉 GovBizConnect is now running!")
    print("=" * 50)
    print("📱 Frontend: http://localhost:8501")
    print("🔧 Backend API: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the application")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping GovBizConnect...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Application stopped")

if __name__ == "__main__":
    main() 