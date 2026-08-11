🕷️ fbscraper

A powerful and flexible Python-based web scraper for extracting public data from Facebook. This tool allows you to gather posts, comments, and page information efficiently while respecting rate limits and handling anti-bot mechanisms.
📋 Table of Contents

    Features
    Prerequisites
    Installation
    Configuration
    Usage
    Disclaimer
    License

✨ Features

    Data Extraction: Scrape posts, comments, and user profiles from Facebook pages and groups.
    Export Formats: Save extracted data in JSON or CSV formats.
    Anti-Bot Bypass: Configurable delays and custom headers to mimic human behavior.
    Proxy Support: Route traffic through HTTP/HTTPS proxies to prevent IP blocking.
    Headless Mode: Run the browser in the background without opening a GUI.

⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.8+ installed on your machine.
    Google Chrome or Mozilla Firefox browser installed (if using Selenium/Playwright).
    A Facebook account (required for accessing some restricted pages).

🚀 Installation

    Clone the repository:

    git clone https://github.com/fbscrape/fbscraper.gitcd fbscraper

    Create and activate a virtual environment:
    bash
     
      
     
     
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
     
     

    Install the required dependencies:
    bash
     
      
     
     
    pip install -r requirements.txt
     
     

🔧 Configuration

This scraper uses environment variables to keep your credentials secure. 

    Rename the .env.example file to .env:
    bash
     
      
     
     
    mv .env.example .env
     
     

    Open the .env file and add your Facebook credentials and settings:
    env
     
      
     
     
    # Facebook Credentials
    FB_EMAIL=your_email@example.com
    FB_PASSWORD=your_super_secret_password

    # Scraper Settings
    HEADLESS=True
    MIN_DELAY=2
    MAX_DELAY=5

    # Proxy Settings (Optional)
    USE_PROXY=False
    PROXY_HTTP=http://user:pass@ip:port
     
     

💻 Usage

Run the scraper from the command line using Python. Below is an example command:
bash
 
  
 
 
python main.py --url "https://www.facebook.com/TargetPage" --output "data/output.json" --limit 50
 
 
Command Line Arguments
Argument
	
Description
	
Required
	
Default
--url	The URL of the Facebook page, group, or profile to scrape.	Yes	-
--output	The filename to save the scraped data (supports .json and .csv).	No	output.json
--limit	Maximum number of posts/comments to scrape.	No	100
  
⚠️ Disclaimer

This tool is for educational purposes only. Scraping Facebook may violate their Terms of Service (ToS). The authors of this repository are not responsible for any misuse of this tool, account bans, or legal actions taken by Facebook. Use it at your own risk and ensure you comply with all local laws and website terms of service.
📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
```
    
     
