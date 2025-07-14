#!/usr/bin/env python3
"""
Test script for GovBizConnect API
"""

import requests
import json
import time

API_BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_nic_prediction():
    """Test NIC prediction endpoint"""
    print("\n🔍 Testing NIC prediction endpoint...")
    
    test_cases = [
        "Software development and mobile app creation",
        "Manufacturing of electronic components",
        "Retail sale of food and beverages",
        "Construction of residential buildings"
    ]
    
    for description in test_cases:
        try:
            response = requests.post(
                f"{API_BASE_URL}/get_nic",
                json={"description": description},
                timeout=10
            )
            print(f"\nDescription: {description}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f"NIC Code: {result['nic_code']}")
                print(f"Confidence: {result['confidence']:.4f}")
            else:
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

def test_scheme_recommendations():
    """Test scheme recommendations endpoint"""
    print("\n🔍 Testing scheme recommendations endpoint...")
    
    test_cases = [
        "small business loan micro enterprise",
        "agriculture farming irrigation",
        "software technology startup"
    ]
    
    for description in test_cases:
        try:
            response = requests.post(
                f"{API_BASE_URL}/get_schemes",
                json={"description": description},
                timeout=10
            )
            print(f"\nDescription: {description}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                schemes = result['schemes']
                print(f"Found {len(schemes)} schemes:")
                for i, scheme in enumerate(schemes[:3], 1):  # Show top 3
                    print(f"  {i}. {scheme['name']} (similarity: {scheme['similarity']:.4f})")
            else:
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("🧪 Testing GovBizConnect API")
    print("=" * 40)
    
    # Wait a bit for backend to be ready
    print("⏳ Waiting for backend to be ready...")
    time.sleep(2)
    
    # Test health
    if not test_health():
        print("❌ Backend is not running. Please start the backend first.")
        return
    
    # Test NIC prediction
    test_nic_prediction()
    
    # Test scheme recommendations
    test_scheme_recommendations()
    
    print("\n✅ API testing completed!")

if __name__ == "__main__":
    main() 