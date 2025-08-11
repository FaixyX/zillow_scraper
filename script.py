import requests
import json
import time
from apis import get_api_config, update_search_cookie, update_referer_header, get_available_property_types
from agent_scraper import scrape_agent_data

def fetch_page(page_number, api_config):
    """Function to make a single page request"""
    # Create a copy of the base data for this page
    json_data = api_config['base_json_data'].copy()
    
    # Update the requestId for each page
    json_data['requestId'] = page_number
    
    # Add pagination to searchQueryState if it doesn't exist
    if 'pagination' not in json_data['searchQueryState']:
        json_data['searchQueryState']['pagination'] = {}
    
    # Update pagination for this page
    json_data['searchQueryState']['pagination']['currentPage'] = page_number
    
    # Update cookies and headers for this page
    page_cookies = api_config['cookies'].copy()
    page_cookies['search'] = update_search_cookie(
        api_config['cookies']['search'], 
        page_number, 
        api_config['search_cookie_pattern']
    )
    
    page_headers = api_config['headers'].copy()
    page_headers['referer'] = update_referer_header(
        api_config['headers']['referer'], 
        page_number, 
        api_config['referer_pattern']
    )
    
    response = requests.put('https://www.zillow.com/async-create-search-page-state', 
                          cookies=page_cookies, headers=page_headers, json=json_data)
    return response

def extract_properties(response_json):
    """Extract only the specific fields from the response"""
    properties = []
    
    # Look for properties in different possible locations in the response
    if 'cat1' in response_json and 'searchResults' in response_json['cat1']:
        search_results = response_json['cat1']['searchResults']
        if 'listResults' in search_results:
            properties = search_results['listResults']
        elif 'mapResults' in search_results:
            properties = search_results['mapResults']
    
    # Extract only the requested fields
    extracted_data = []
    for prop in properties:
        if isinstance(prop, dict):
            extracted_prop = {
                'detailUrl': prop.get('detailUrl', ''),
                'statusType': prop.get('statusType', ''),
                'location_title': prop.get('statusText', ''),
                'address': prop.get('address', ''),
                'units': prop.get('units', ''),
                'latLong': prop.get('latLong', ''),
                'providerListingId': prop.get('providerListingId', ''),
                'zpid': prop.get('zpid', '')  # Added ZPID extraction
            }
            extracted_data.append(extracted_prop)
    
    return extracted_data

def get_agent_data_for_properties(properties, delay_between_requests=1):
    """
    Get agent data for all properties that have ZPIDs
    
    Args:
        properties (list): List of property dictionaries
        delay_between_requests (int): Delay between agent requests
    
    Returns:
        list: Updated properties list with agent details embedded
    """
    properties_with_zpid = [prop for prop in properties if prop.get('zpid')]
    
    if not properties_with_zpid:
        print("No properties with ZPIDs found. Skipping agent data collection.")
        return properties
    
    print(f"\nCollecting agent data for {len(properties_with_zpid)} properties...")
    
    # Create a copy of properties to modify
    updated_properties = properties.copy()
    
    for i, prop in enumerate(properties_with_zpid):
        zpid = prop['zpid']
        print(f"Fetching agent data for ZPID {zpid} ({i+1}/{len(properties_with_zpid)})")
        
        try:
            # Get agent data for this ZPID
            agent_info = scrape_agent_data(zpid, 'agent')
            
            if agent_info and agent_info.get('agent_details'):
                # Find the property in the updated list and add agent details
                for j, updated_prop in enumerate(updated_properties):
                    if updated_prop.get('zpid') == zpid:
                        # Only add the agent_details section
                        updated_properties[j]['agent_details'] = agent_info['agent_details']
                        print(f"✅ Successfully fetched agent data for ZPID {zpid}")
                        break
            else:
                print(f"❌ Failed to fetch agent data for ZPID {zpid}")
            
            # Add delay between requests to be respectful
            if i < len(properties_with_zpid) - 1:  # Don't delay after the last request
                time.sleep(delay_between_requests)
                
        except Exception as e:
            print(f"❌ Error fetching agent data for ZPID {zpid}: {e}")
            continue
    
    print(f"\nAgent data collection complete! Successfully fetched data for {len([p for p in updated_properties if p.get('agent_details')])} properties.")
    return updated_properties

def scrape_zillow_properties(property_type='rental', max_pages=3, delay_between_requests=2, collect_agent_data=True, agent_delay=1):
    """
    Main function to scrape Zillow properties and optionally collect agent data
    
    Args:
        property_type (str): 'rental' or 'sale'
        max_pages (int): Maximum number of pages to scrape
        delay_between_requests (int): Delay between requests in seconds
        collect_agent_data (bool): Whether to collect agent data for properties
        agent_delay (int): Delay between agent requests in seconds
    
    Returns:
        list: List of properties with agent details embedded (if collected)
    """
    # Get the API configuration for the specified property type
    try:
        api_config = get_api_config(property_type)
    except ValueError as e:
        print(f"Error: {e}")
        print(f"Available property types: {get_available_property_types()}")
        return []
    
    print(f"Starting {property_type} properties scraping - will fetch up to {max_pages} pages...")
    
    all_properties = []
    all_raw_responses = []
    page = 1
    
    while page <= max_pages:
        print(f"Fetching page {page}...")
        
        try:
            response = fetch_page(page, api_config)
            
            if response.status_code == 200:
                response_json = response.json()
                
                # Store raw response
                raw_response_data = {
                    'page': page,
                    'status_code': response.status_code,
                    'response_data': response_json,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                all_raw_responses.append(raw_response_data)
                
                page_properties = extract_properties(response_json)
                
                if not page_properties:
                    print(f"No more properties found on page {page}. Stopping pagination.")
                    break
                
                all_properties.extend(page_properties)
                print(f"Found {len(page_properties)} properties on page {page}")
                
                # Check if we've reached the end of results
                if len(page_properties) == 0:
                    print("No more properties found. Stopping pagination.")
                    break
                    
            else:
                print(f"Error on page {page}: Status code {response.status_code}")
                print(f"Response text: {response.text[:200]}")
                
                # Store error response
                error_response_data = {
                    'page': page,
                    'status_code': response.status_code,
                    'error': True,
                    'response_text': response.text,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                all_raw_responses.append(error_response_data)
                break
                
        except json.JSONDecodeError:
            print(f"Invalid JSON response on page {page}")
            print(f"Response status code: {response.status_code}")
            print("Response text:", response.text[:500])
            
            # Store JSON decode error response
            error_response_data = {
                'page': page,
                'status_code': response.status_code if 'response' in locals() else 'N/A',
                'error': True,
                'error_type': 'json_decode_error',
                'response_text': response.text if 'response' in locals() else 'N/A',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            all_raw_responses.append(error_response_data)
            break
        except Exception as e:
            print(f"Error processing page {page}: {e}")
            
            # Store general error response
            error_response_data = {
                'page': page,
                'error': True,
                'error_type': 'general_error',
                'error_message': str(e),
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            all_raw_responses.append(error_response_data)
            break
        
        page += 1
        
        # Add delay between requests to be respectful to the server
        if page <= max_pages:
            print(f"Waiting {delay_between_requests} seconds before next request...")
            time.sleep(delay_between_requests)
    
    # Collect agent data if requested and embed it directly into properties
    if collect_agent_data and all_properties:
        all_properties = get_agent_data_for_properties(all_properties, agent_delay)
    
    # Save properties with embedded agent data to JSON file
    try:
        output_filename = api_config['output_filename']
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(all_properties, f, indent=2, ensure_ascii=False)
        
        print(f"\nScraping complete!")
        print(f"Total {property_type} properties extracted: {len(all_properties)}")
        print(f"Total pages fetched: {page - 1}")
        print(f"Properties with agent data: {len([p for p in all_properties if p.get('agent_details')])}")
        print(f"Data saved to {output_filename}")
        
    except Exception as e:
        print(f"Error saving data: {e}")
    
    # Save raw response data to JSON file
    try:
        raw_output_filename = f"raw_{api_config['output_filename']}"
        with open(raw_output_filename, 'w', encoding='utf-8') as f:
            json.dump(all_raw_responses, f, indent=2, ensure_ascii=False)
        
        print(f"Raw response data saved to {raw_output_filename}")
        
    except Exception as e:
        print(f"Error saving raw response data: {e}")
    
    return all_properties

def main():
    """Main function with user interaction"""
    print("Zillow Property Scraper with Agent Data Collection")
    print("=" * 50)
    
    # Show available property types
    available_types = get_available_property_types()
    print(f"Available property types: {', '.join(available_types)}")
    
    # Get user input
    while True:
        property_type = input(f"\nEnter property type ({'/'.join(available_types)}): ").lower().strip()
        if property_type in available_types:
            break
        print(f"Invalid property type. Please choose from: {', '.join(available_types)}")
    
    # Get pagination settings
    try:
        max_pages = int(input("Enter maximum number of pages to scrape (default: 3): ") or "3")
        delay = int(input("Enter delay between requests in seconds (default: 2): ") or "2")
    except ValueError:
        print("Using default values: max_pages=3, delay=2")
        max_pages = 3
        delay = 2
    
    # Ask about agent data collection
    collect_agent = input("\nCollect agent data for properties? (y/n, default: y): ").lower().strip()
    collect_agent = collect_agent != 'n'  # Default to True unless user explicitly says 'n'
    
    agent_delay = 1
    if collect_agent:
        try:
            agent_delay = int(input("Enter delay between agent requests in seconds (default: 1): ") or "1")
        except ValueError:
            print("Using default agent delay: 1 second")
            agent_delay = 1
    
    # Start scraping
    result = scrape_zillow_properties(
        property_type, 
        max_pages, 
        delay, 
        collect_agent_data=collect_agent,
        agent_delay=agent_delay
    )
    
    if result:
        print(f"\nSuccessfully scraped {len(result)} {property_type} properties!")
        
        if result and result[0].get('agent_details'): # Check if the first property has agent_details
            print(f"Successfully collected agent data for {len([p for p in result if p.get('agent_details')])} properties!")
            
            # Show some agent data examples
            print("\nAgent data examples:")
            for i, prop in enumerate(result[:3]):
                if prop.get('agent_details', {}).get('first_name'):
                    agent_name = f"{prop['agent_details']['first_name']} {prop['agent_details']['last_name']}"
                    print(f"  ZPID {prop['zpid']}: {agent_name}")
                if i >= 2:  # Show only first 3 examples
                    break
        else:
            print("No agent data was collected.")
    else:
        print(f"\nNo {property_type} properties were scraped.")

if __name__ == "__main__":
    main()