import streamlit as st
import requests
import json
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="GovBizConnect",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .scheme-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .nic-code {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
    }
    .confidence-score {
        font-size: 1.2rem;
        color: #28a745;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# API configuration
API_BASE_URL = "http://localhost:8000"

def check_api_health():
    """Check if the API is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def get_nic_prediction(description: str) -> Dict:
    """Get NIC code prediction from API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/get_nic",
            json={"description": description},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
        return None

def get_scheme_recommendations(description: str) -> List[Dict]:
    """Get scheme recommendations from API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/get_schemes",
            json={"description": description},
            timeout=10
        )
        response.raise_for_status()
        return response.json()["schemes"]
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🏛️ GovBizConnect</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-powered NIC code prediction and government scheme recommendations</p>', unsafe_allow_html=True)
    
    # Check API health
    if not check_api_health():
        st.error("⚠️ Backend API is not running. Please start the FastAPI server first.")
        st.info("To start the backend, run: `cd backend && uvicorn main:app --reload`")
        return
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        **GovBizConnect** helps businesses:
        
        • Get the most relevant NIC code for their business
        • Find applicable government schemes and programs
        • Make informed decisions about government support
        
        Simply describe your business and get instant recommendations!
        """)
        
        st.header("🔧 Setup Instructions")
        st.markdown("""
        1. Run the Mac setup script:
           ```bash
           ./setup_mac.sh
           ```
        
        2. Activate virtual environment:
           ```bash
           source venv/bin/activate
           ```
        
        3. Start the backend:
           ```bash
           cd backend && uvicorn main:app --reload
           ```
        """)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Business Description")
        
        # Text input
        business_description = st.text_area(
            "Describe your business activities in detail:",
            placeholder="e.g., We manufacture electronic components and provide software development services for mobile applications...",
            height=150,
            help="Provide a detailed description of your business activities, products, or services"
        )
        
        # Submit button
        if st.button("🚀 Get Recommendations", type="primary", use_container_width=True):
            if business_description.strip():
                with st.spinner("Analyzing your business description..."):
                    # Get NIC prediction
                    nic_result = get_nic_prediction(business_description)
                    
                    # Get scheme recommendations
                    schemes_result = get_scheme_recommendations(business_description)
                    
                    if nic_result and schemes_result:
                        # Display results
                        st.success("✅ Analysis complete!")
                        
                        # NIC Code Result
                        with col2:
                            st.header("🏷️ Predicted NIC Code")
                            st.markdown(f'<div class="result-box"><div class="nic-code">{nic_result["nic_code"]}</div><div class="confidence-score">Confidence: {nic_result["confidence"]:.2%}</div></div>', unsafe_allow_html=True)
                        
                        # Scheme Recommendations
                        st.header("📋 Recommended Government Schemes")
                        st.markdown("Here are the top 5 government schemes most relevant to your business:")
                        
                        for i, scheme in enumerate(schemes_result, 1):
                            with st.container():
                                st.markdown(f"""
                                <div class="scheme-card">
                                    <h4>#{i} {scheme['name']}</h4>
                                    <p><strong>Description:</strong> {scheme['description']}</p>
                                    <p><strong>Relevance Score:</strong> {scheme['similarity']:.2%}</p>
                                </div>
                                """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a business description.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>Built with ❤️ using FastAPI, Streamlit, and AI</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 