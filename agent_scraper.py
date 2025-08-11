import requests
import json
import time
from apis import get_api_config, get_available_property_types

def fetch_agent_data(zpid, api_config):
    """
    Function to fetch agent data for a specific ZPID
    
    Args:
        zpid (str): The Zillow Property ID
        api_config (dict): API configuration
    
    Returns:
        requests.Response: The API response
    """
    # Update the ZPID in the configuration
    updated_params = api_config['params'].copy()
    updated_params['zpid'] = str(zpid)
    
    updated_json_data = api_config['base_json_data'].copy()
    updated_json_data['variables']['zpid'] = int(zpid)
    updated_json_data['variables']['contactFormRenderParameter']['zpid'] = int(zpid)
    
    # Make the GraphQL request
    response = requests.post(
        api_config['endpoint'],
        params=updated_params,
        cookies=api_config['cookies'],
        headers=api_config['headers'],
        json=updated_json_data
    )
    
    return response

def extract_agent_info(response_json):
    """
    Extract agent information from the GraphQL response
    
    Args:
        response_json (dict): The JSON response from the API
    
    Returns:
        dict: Extracted agent information
    """
    agent_info = {
        'zpid': None,
        'property_address': {},
        'agent_details': {},
        'property_details': {},
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    try:
        # Extract property information
        if 'data' in response_json and 'property' in response_json['data']:
            property_data = response_json['data']['property']
            
            # Property address
            agent_info['property_address'] = {
                'street_address': property_data.get('streetAddress', ''),
                'city': property_data.get('city', ''),
                'state': property_data.get('state', ''),
                'zipcode': property_data.get('zipcode', ''),
                'country': property_data.get('country', '')
            }
            
            # Property details
            agent_info['property_details'] = {
                'zpid': property_data.get('zpid', ''),
                'price': property_data.get('price', ''),
                'bedrooms': property_data.get('bedrooms', ''),
                'bathrooms': property_data.get('bathrooms', ''),
                'living_area': property_data.get('livingArea', ''),
                'home_type': property_data.get('homeType', ''),
                'home_status': property_data.get('homeStatus', ''),
                'zestimate': property_data.get('zestimate', ''),
                'mls_id': property_data.get('mlsid', ''),
                'hdp_url': property_data.get('hdpUrl', '')
            }
            
            agent_info['zpid'] = property_data.get('zpid', '')
        
        # Extract agent information from showcase
        if 'data' in response_json and 'showcase' in response_json['data']:
            showcase_data = response_json['data']['showcase']
            
            if 'showingTimePlusAgent' in showcase_data:
                agent_data = showcase_data['showingTimePlusAgent']
                
                agent_info['agent_details'] = {
                    'first_name': agent_data.get('firstName', ''),
                    'last_name': agent_data.get('lastName', ''),
                    'email': agent_data.get('email', ''),
                    'phone': agent_data.get('phone', ''),
                    'photo_url': agent_data.get('agentPhotoUrl', '')
                }
        
        # Extract contact form data if available
        if 'data' in response_json and 'property' in response_json['data']:
            property_data = response_json['data']['property']
            
            if 'contactFormRenderData' in property_data:
                contact_form_data = property_data['contactFormRenderData']
                if contact_form_data and 'data' in contact_form_data:
                    agent_info['contact_form_data'] = contact_form_data['data']
        
    except Exception as e:
        print(f"Error extracting agent info: {e}")
        agent_info['error'] = str(e)
    
    return agent_info

def scrape_agent_data(zpid, property_type='agent'):
    """
    Main function to scrape agent data for a specific ZPID
    
    Args:
        zpid (str): The Zillow Property ID
        property_type (str): Property type (default: 'agent')
    
    Returns:
        dict: Extracted agent information (no files saved)
    """
    # Get the API configuration for agent data
    try:
        api_config = get_api_config(property_type)
    except ValueError as e:
        print(f"Error: {e}")
        print(f"Available property types: {get_available_property_types()}")
        return None
    
    print(f"Fetching agent data for ZPID {zpid}...")
    
    try:
        response = fetch_agent_data(zpid, api_config)
        
        if response.status_code == 200:
            response_json = response.json()
            
            # Extract agent information
            agent_info = extract_agent_info(response_json)
            
            if agent_info and agent_info.get('agent_details'):
                print(f"✅ Successfully fetched agent data for ZPID {zpid}")
                return agent_info
            else:
                print(f"❌ No agent details found for ZPID {zpid}")
                return None
                
        else:
            print(f"❌ Error: Status code {response.status_code}")
            return None
            
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON response for ZPID {zpid}")
        return None
    except Exception as e:
        print(f"❌ Error processing ZPID {zpid}: {e}")
        return None

# Remove the main function and file saving functionality
# This script is now used as a module by script.py

# The main function has been removed since agent_scraper.py is now only used as a module
# All agent data is embedded directly into properties in the main script 