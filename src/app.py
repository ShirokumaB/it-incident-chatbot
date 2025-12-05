import streamlit as st
import sys
import os
import time

# Add the project root to python path to allow imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from src.components.sidebar import render_sidebar
from src.services.ai_service import get_mock_ai_response

# Page Config
st.set_page_config(page_title="Incident Chatbot (Portfolio Demo)", page_icon="🤖")

st.title("🤖 IT Incident Knowledge Base Chatbot")
st.markdown("""
This is a **Portfolio Demo** of an RAG-based chatbot designed to help IT engineers find solutions to incidents.
*   **Frontend:** Streamlit
*   **Data Logic:** Pandas (Dynamic Filtering)
*   **Backend:** Mock AI Service (Simulating AWS Bedrock)
""")

# --- Sidebar ---
filters = render_sidebar()

# --- Chat Interface ---

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "mock-session-123"

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Describe the incident (e.g., 'Server connection failed')"):
    # Display User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Call Mock AI Service
        with st.spinner("Searching Knowledge Base..."):
            result = get_mock_ai_response(prompt, filters, st.session_state.session_id)
            answer = result['answer']
            
        # Streaming Effect
        for chunk in answer.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
        # Display Citations
        if result.get('metadata'):
            st.markdown("---")
            st.markdown("**Reference Cases:**")
            for meta in result['metadata']:
                st.info(f"📅 {meta['incident_datetime']} | 🏢 {meta['customer_company']} | 💻 {meta['brand']} {meta['model']}")

    # Save Assistant Message
    st.session_state.messages.append({"role": "assistant", "content": full_response})
