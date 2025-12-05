import streamlit as st
from src.services.data_service import load_data

def render_sidebar():
    """
    Renders the sidebar with dynamic cascading filters.
    """
    st.sidebar.header("Filter Incidents")
    
    # Load Data
    df = load_data()
    if df.empty:
        st.sidebar.error("No data available.")
        return {}

    # Initialize Session State for Filters if not exists
    if 'filters' not in st.session_state:
        st.session_state.filters = {
            'company': '-',
            'incident_type': '-',
            'brand': '-',
            'model': '-'
        }

    # --- Filter 1: Company ---
    company_options = ['-'] + sorted(df['customer_company'].unique().tolist())
    # Ensure current selection is valid
    current_company = st.session_state.filters['company']
    if current_company not in company_options:
        current_company = '-'
        
    selected_company = st.sidebar.selectbox(
        "Select Company",
        company_options,
        index=company_options.index(current_company),
        key='sb_company'
    )
    st.session_state.filters['company'] = selected_company

    # --- Filter Logic: Filter DataFrame based on Company ---
    filtered_df = df.copy()
    if selected_company != '-':
        filtered_df = filtered_df[filtered_df['customer_company'] == selected_company]

    # --- Filter 2: Incident Type ---
    type_options = ['-'] + sorted(filtered_df['incident_type'].unique().tolist())
    current_type = st.session_state.filters['incident_type']
    if current_type not in type_options:
        current_type = '-'
        
    selected_type = st.sidebar.selectbox(
        "Select Incident Type",
        type_options,
        index=type_options.index(current_type),
        key='sb_type'
    )
    st.session_state.filters['incident_type'] = selected_type

    # --- Filter Logic: Filter DataFrame based on Type ---
    if selected_type != '-':
        filtered_df = filtered_df[filtered_df['incident_type'] == selected_type]

    # --- Filter 3: Brand ---
    brand_options = ['-'] + sorted(filtered_df['brand'].unique().tolist())
    current_brand = st.session_state.filters['brand']
    if current_brand not in brand_options:
        current_brand = '-'
        
    selected_brand = st.sidebar.selectbox(
        "Select Brand",
        brand_options,
        index=brand_options.index(current_brand),
        key='sb_brand'
    )
    st.session_state.filters['brand'] = selected_brand

    # --- Filter Logic: Filter DataFrame based on Brand ---
    if selected_brand != '-':
        filtered_df = filtered_df[filtered_df['brand'] == selected_brand]

    # --- Filter 4: Model ---
    model_options = ['-'] + sorted(filtered_df['model'].unique().tolist())
    current_model = st.session_state.filters['model']
    if current_model not in model_options:
        current_model = '-'
        
    selected_model = st.sidebar.selectbox(
        "Select Model",
        model_options,
        index=model_options.index(current_model),
        key='sb_model'
    )
    st.session_state.filters['model'] = selected_model
    
    # Reset Button
    if st.sidebar.button("Reset Filters"):
        st.session_state.filters = {
            'company': '-',
            'incident_type': '-',
            'brand': '-',
            'model': '-'
        }
        st.rerun()

    return st.session_state.filters
