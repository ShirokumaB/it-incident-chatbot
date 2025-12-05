# IT Incident Knowledge Base Chatbot

## 📌 Project Overview
This project is a **Retrieval-Augmented Generation (RAG) Chatbot** designed to assist IT engineers in resolving incidents efficiently. It acts as an intelligent interface that allows users to query a knowledge base of past incident logs using natural language.

**Note:** This is a *Portfolio Version* of the project developed during my internship. For confidentiality, it uses **Mock Data** and a **Simulated AI Service** instead of real company data and live AWS Bedrock credentials.

## 🚀 Key Features
*   **Interactive Chat Interface:** Built with **Streamlit**, featuring real-time streaming responses and chat history management.
*   **Dynamic Data Filtering:** Implemented complex **Pandas** logic to create cascading dropdown filters (Company → Incident Type → Brand → Model), ensuring users narrow down their search context effectively.
*   **RAG Architecture Simulation:** Demonstrates the core concept of retrieving relevant metadata (filters) and passing them to an LLM for context-aware answers.

## 🛠 Tech Stack
*   **Frontend:** Python, Streamlit
*   **Data Manipulation:** Pandas
*   **Architecture:** RAG (Retrieval-Augmented Generation) Concept

## 📂 Project Structure
```
Portfolio_Incident_Chatbot/
├── data/
│   └── mock_incidents.csv    # Simulated database of IT incidents
├── src/
│   ├── app.py                # Main application entry point
│   ├── components/
│   │   └── sidebar.py        # UI Component for Dynamic Filters
│   └── services/
│       ├── data_service.py   # Logic to load and process CSV data
│       └── ai_service.py     # Mock service simulating AWS Bedrock API
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## ⚙️ How to Run
1.  **Clone the repository**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    streamlit run src/app.py
    ```

## 💡 What I Learned
Through this project, I gained hands-on experience in:
*   Building data-driven web applications with **Streamlit**.
*   Handling **State Management** in a stateless web framework.
*   Implementing **Business Logic** to filter and structure data for AI consumption.
*   Understanding the workflow of **Generative AI** applications in an enterprise context.
