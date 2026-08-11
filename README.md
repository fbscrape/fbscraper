<div align="center">
  
# 🕷️ fbscraper

A powerful and flexible Python-based web scraper for extracting public data from Facebook.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📖 Overview
**fbscraper** is a tool designed to extract public data (posts, comments, page info) from Facebook. It handles dynamic content loading, implements rate-limiting to avoid bans, and supports proxy routing.

> ⚠️ **Warning:** This tool is for educational purposes only. Scraping Facebook may violate their Terms of Service. Use it at your own risk.

## ✨ Features
- 🔄 **Dynamic Scraping:** Uses Selenium/Playwright to load dynamic content.
- 🛡️ **Anti-Bot Bypass:** Custom headers and configurable delays to mimic human behavior.
- 🌐 **Proxy Support:** Route requests through HTTP/HTTPS proxies.
- 📄 **Export Formats:** Save scraped data easily to JSON or CSV.

## 🚀 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/fbscrape/fbscraper.git
cd fbscraper