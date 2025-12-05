import time
import random

def get_mock_ai_response(question, filters, session_id):
    """
    Simulates a response from AWS Bedrock.
    In the real project, this calls boto3.retrieve_and_generate.
    """
    
    # Simulate network latency
    time.sleep(1)
    
    # Mock Logic: Generate a response based on the question or filters
    company = filters.get('customer_company', 'Unknown Company')
    brand = filters.get('brand', 'Unknown Brand')
    
    response_templates = [
        f"Based on the incident logs for **{company}** regarding **{brand}**, here is a suggested solution:",
        f"I found a similar case for **{brand}** at **{company}**. The recommended steps are:",
    ]
    
    intro = random.choice(response_templates)
    
    # Generic solution content
    solution = """
    1. **Check Connectivity:** Verify that the device is reachable via ping.
    2. **Review Logs:** Check the system logs for any error messages around the time of the incident.
    3. **Restart Service:** If the issue persists, try restarting the affected service.
    4. **Update Firmware:** Ensure the device is running the latest stable firmware version.
    """
    
    full_response = f"{intro}\n{solution}\n\n*Source: Mock Incident Knowledge Base*"
    
    # Mock Metadata/Citations
    metadata = [
        {
            'incident_datetime': '2023-05-12',
            'customer_company': company,
            'brand': brand,
            'model': filters.get('model', 'Generic Model'),
            'incident_url': 'http://mock-kb-link.com/incident/123'
        }
    ]
    
    return {
        'answer': full_response,
        'metadata': metadata,
        'sessionId': session_id
    }
