fbscraper

A powerful and flexible Python-based scraper for extracting public data from Facebook.
Features

    Extract posts, comments, and user profiles from Facebook pages and groups.
    Export data to JSON or CSV formats.
    Bypass basic anti-bot mechanisms using configurable delays and headers.
    Proxy support to prevent IP blocking.

Prerequisites

    Python 3.8 or higher
    A Facebook account (if scraping requires authentication)

Installation

    Clone the repository:

    git clone https://github.com/fbscrape/fbscraper.gitcd fbscraper

    Create and activate a virtual environment:
    bash


    
     
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
     
     

    Install the required dependencies:
    bash
     
      
     
     
    pip install -r requirements.txt
     
     

Configuration

Rename .env.example to .env and add your Facebook credentials and proxy settings:
env
 
  
 
 
FB_EMAIL=your_email@example.com
FB_PASSWORD=your_password
USE_PROXY=False
PROXY_IP=127.0.0.1:8080
 
 
Usage

Run the main scraper script:
bash
 
  
 
 
python main.py --url "https://www.facebook.com/page" --output output.json
 
 
Disclaimer

This tool is for educational purposes only. Scraping Facebook may violate their Terms of Service. Use it at your own risk. Ensure you comply with all local laws and website terms of service before scraping any data.
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
text
 
  
 
 

### 3. `requirements.txt`
Even if you have a `setup.py` or `pyproject.toml`, a `requirements.txt` makes it easy for people to install dependencies quickly. (Adjust based on your actual imports).

```text
requests>=2.31.0
beautifulsoup4>=4.12.2
lxml>=4.9.3
selenium>=4.15.0
python-dotenv>=1.0.0
pandas>=2.1.4