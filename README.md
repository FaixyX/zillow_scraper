# Zillow Property Scraper

A comprehensive Python-based web scraping tool for extracting property listings and agent information from Zillow. This project provides a robust, configurable solution for real estate data collection with built-in rate limiting and data enrichment capabilities.

## 🏗️ Project Overview

The Zillow Property Scraper is designed to extract comprehensive real estate data from Zillow's search results, including property details, location information, and associated agent contact information. The system is built with modularity in mind, separating concerns between API configurations, data extraction, and agent information retrieval.

### Key Features

- **Multi-Property Type Support**: Scrapes both rental and sale properties
- **Agent Data Integration**: Automatically collects agent contact information for properties
- **Configurable Pagination**: Supports multi-page scraping with customizable limits
- **Rate Limiting**: Built-in delays to respect server resources and avoid detection
- **Data Enrichment**: Combines property listings with agent details in a single dataset
- **Flexible Output**: Generates both processed and raw response data files

### Architecture Design

The project follows a modular architecture pattern:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   script.py     │    │   apis.py       │    │ agent_scraper.py│
│   (Main Logic)  │◄──►│   (API Config)  │◄──►│   (Agent Data)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Output Files  │    │   HTTP Requests │    │   GraphQL API   │
│   (JSON)        │    │   (Zillow)      │    │   (Agent Info)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 File and Directory Structure

```
zillow/
├── script.py                          # Main scraping orchestration script
├── apis.py                           # API configurations and helper functions
├── agent_scraper.py                  # Agent data extraction module
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore patterns
├── README.md                         # This documentation file
├── venv/                             # Python virtual environment
├── __pycache__/                      # Python bytecode cache
├── zillow_rental_data.json           # Processed rental property data
├── zillow_sale_data.json             # Processed sale property data
├── raw_zillow_rental_data.json       # Raw API responses for rentals
└── raw_zillow_sale_data.json         # Raw API responses for sales
```

### Core Components

#### `script.py` - Main Orchestration Module
- **Purpose**: Central coordination script that manages the entire scraping workflow
- **Key Functions**:
  - `scrape_zillow_properties()`: Main scraping function with configurable parameters
  - `fetch_page()`: Handles individual page requests with proper pagination
  - `extract_properties()`: Parses API responses to extract property information
  - `get_agent_data_for_properties()`: Enriches properties with agent contact details
  - `main()`: Interactive command-line interface for user configuration

#### `apis.py` - Configuration Management
- **Purpose**: Centralized storage for all API configurations, cookies, headers, and request parameters
- **Configurations**:
  - `RENTAL_API_CONFIG`: Complete setup for rental property scraping
  - `SALE_API_CONFIG`: Complete setup for sale property scraping  
  - `AGENT_API_CONFIG`: GraphQL configuration for agent data retrieval
- **Helper Functions**:
  - `get_api_config()`: Retrieves configuration for specified property type
  - `update_search_cookie()`: Updates pagination in search cookies
  - `update_referer_header()`: Updates pagination in referer headers

#### `agent_scraper.py` - Agent Data Module
- **Purpose**: Specialized module for extracting agent contact information using Zillow's GraphQL API
- **Key Functions**:
  - `scrape_agent_data()`: Main function for agent data extraction
  - `fetch_agent_data()`: Makes GraphQL requests to Zillow's agent API
  - `extract_agent_info()`: Parses GraphQL responses to extract agent details

## 🚀 Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd zillow
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scraper**
   ```bash
   python script.py
   ```

### Quick Start Guide

Here's the complete sequence to get up and running:

```bash
# 1. Clone the repository
git clone <repository-url>

# 2. Navigate to the project folder
cd zillow

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 5. Install required dependencies
pip install -r requirements.txt

# 6. Run the scraper
python script.py
```

The script will then prompt you for:
- Property type (rental/sale)
- Maximum pages to scrape
- Delay between requests
- Whether to collect agent data
- Delay between agent requests

### Environment Configuration

The project uses hardcoded API configurations that include:
- Authentication cookies and session tokens
- User-Agent strings
- Request headers and parameters
- Geographic search boundaries

**Note**: These configurations are pre-configured for Texas-based searches but can be modified in `apis.py` for different regions or search criteria.

## 💻 Usage and Examples

### Basic Usage

Run the interactive scraper:
```bash
python script.py
```

The script will prompt you for:
- Property type (rental/sale)
- Maximum pages to scrape
- Delay between requests
- Whether to collect agent data
- Delay between agent requests

### Programmatic Usage

```python
from script import scrape_zillow_properties

# Scrape rental properties
properties = scrape_zillow_properties(
    property_type='rental',
    max_pages=5,
    delay_between_requests=2,
    collect_agent_data=True,
    agent_delay=1
)

# Scrape sale properties
properties = scrape_zillow_properties(
    property_type='sale',
    max_pages=3,
    delay_between_requests=3,
    collect_agent_data=True,
    agent_delay=2
)
```

### Command-Line Examples

```bash
# Quick rental scrape (3 pages, default delays)
echo -e "rental\n3\n2\ny\n1" | python script.py

# Sale properties with custom settings
echo -e "sale\n5\n3\ny\n2" | python script.py
```

## 🔧 Configuration and Customization

### Modifying Search Parameters

Edit `apis.py` to customize:
- Geographic boundaries (`mapBounds`)
- Search filters (`filterState`)
- Region selection (`regionSelection`)
- Output filenames

### Adjusting Rate Limits

Modify delays in the main script:
- `delay_between_requests`: Time between page requests
- `agent_delay`: Time between agent data requests

### Adding New Property Types

1. Create new configuration in `apis.py`
2. Add to `get_api_config()` function
3. Update `get_available_property_types()`

## 📊 Data Output Structure

### Processed Property Data

Each property contains:
```json
{
  "detailUrl": "Property detail page URL",
  "statusType": "FOR_RENT/FOR_SALE",
  "location_title": "Property name/description",
  "address": "Full property address",
  "units": "Unit information (for multi-unit properties)",
  "latLong": {
    "latitude": 29.764585,
    "longitude": -97.99949
  },
  "providerListingId": "External listing ID",
  "zpid": "Zillow Property ID",
  "agent_details": {
    "first_name": "Agent first name",
    "last_name": "Agent last name",
    "email": "Agent email",
    "phone": "Agent phone number",
    "photo_url": "Agent profile photo URL"
  }
}
```

### Raw Response Data

Raw data includes:
- Complete API responses
- Request metadata (page, timestamp, status codes)
- Error information for failed requests
- Full response structure for debugging

## 🛠️ Development and Contributing

### Code Style Guidelines

- Follow PEP 8 Python style guide
- Use descriptive function and variable names
- Include comprehensive docstrings for all functions
- Maintain consistent error handling patterns

### Testing Protocol

1. Test with small page limits first
2. Verify data extraction accuracy
3. Check rate limiting effectiveness
4. Validate output file formats

### Adding New Features

1. **New Data Fields**: Modify `extract_properties()` in `script.py`
2. **New API Endpoints**: Add configurations to `apis.py`
3. **Enhanced Filtering**: Extend `filterState` in API configurations
4. **Data Export Formats**: Add new export functions

### Debugging Tips

- Enable verbose logging by modifying print statements
- Check raw response files for API structure changes
- Monitor HTTP status codes and response headers
- Use browser developer tools to verify API endpoints

## 🚨 Troubleshooting and Common Issues

### Rate Limiting and Blocking

**Symptoms**: HTTP 429, 403, or empty responses
**Solutions**:
- Increase delays between requests
- Rotate User-Agent strings
- Use proxy rotation (not implemented)
- Check for IP-based blocking

### API Structure Changes

**Symptoms**: JSON parsing errors, missing data fields
**Solutions**:
- Examine raw response files
- Update field extraction logic
- Check Zillow's API documentation
- Verify cookie and header validity

### Authentication Issues

**Symptoms**: Empty results, authentication errors
**Solutions**:
- Update cookies in `apis.py`
- Refresh session tokens
- Verify referer headers
- Check for CAPTCHA requirements

### Data Quality Issues

**Symptoms**: Missing agent data, incomplete property information
**Solutions**:
- Verify ZPID validity
- Check agent API endpoint status
- Validate GraphQL query structure
- Review error handling in agent scraper

## 🔮 Future Maintenance and Enhancements

### Recommended Improvements

1. **Configuration Management**
   - Move hardcoded values to environment variables
   - Add configuration file support (YAML/JSON)
   - Implement configuration validation

2. **Error Handling and Recovery**
   - Add retry mechanisms for failed requests
   - Implement exponential backoff
   - Add comprehensive logging system

3. **Data Processing**
   - Add data validation and cleaning
   - Implement duplicate detection
   - Add data export to databases (PostgreSQL, MongoDB)

4. **Scalability Features**
   - Add multi-threading support
   - Implement distributed scraping
   - Add queue-based job processing

5. **Monitoring and Analytics**
   - Add scraping metrics collection
   - Implement success/failure tracking
   - Add performance monitoring

### Maintenance Considerations

- **API Monitoring**: Zillow frequently updates their API structure
- **Cookie Management**: Session tokens expire and need regular updates
- **Rate Limit Adjustments**: Server-side limits may change
- **Legal Compliance**: Ensure compliance with Zillow's Terms of Service

## 📋 Dependencies

### Core Dependencies

- **requests**: HTTP library for API communication
- **json**: Built-in JSON processing
- **time**: Built-in time utilities
- **re**: Built-in regular expression support

### Optional Enhancements

Consider adding these packages for enhanced functionality:
- **pandas**: Data manipulation and analysis
- **sqlalchemy**: Database integration
- **logging**: Advanced logging capabilities
- **click**: Enhanced command-line interface
- **pydantic**: Data validation and serialization

## 📄 License and Legal Considerations

### Important Legal Notice

This tool is provided for educational and research purposes only. Users must:

1. **Comply with Zillow's Terms of Service**
2. **Respect robots.txt and rate limiting**
3. **Use data responsibly and ethically**
4. **Not violate any applicable laws or regulations**

### Usage Restrictions

- Do not use for commercial purposes without proper licensing
- Respect intellectual property rights
- Follow fair use guidelines
- Implement appropriate data retention policies

## 🤝 Contributing Guidelines

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes** following the code style guidelines
4. **Test thoroughly** with various property types and configurations
5. **Submit a pull request** with detailed description of changes

### Code Review Process

- All changes require review before merging
- Ensure backward compatibility
- Add appropriate tests and documentation
- Follow the established error handling patterns

### Reporting Issues

When reporting bugs or issues:
1. Include Python version and environment details
2. Provide error messages and stack traces
3. Describe steps to reproduce the issue
4. Include relevant configuration details

## 📞 Support and Community

### Getting Help

- Check this README for common solutions
- Review the troubleshooting section
- Examine raw response files for debugging
- Check for similar issues in the repository

### Contributing to Documentation

- Keep this README updated with new features
- Add examples for new functionality
- Document configuration changes
- Include troubleshooting steps for new issues

---

**Disclaimer**: This tool is designed for educational purposes. Users are responsible for ensuring compliance with all applicable laws, terms of service, and ethical guidelines. The developers are not responsible for any misuse of this software.

**Last Updated**: December 2024
**Version**: 1.0.0
**Python Compatibility**: 3.7+
