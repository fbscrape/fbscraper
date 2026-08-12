<div align="center">

# 🕷️ fbscraper

A Python-based Playwright scraper for collecting publicly accessible Facebook page content.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## ⚠️ Disclaimer

This project is provided for educational and research purposes.

Automated access to Facebook may be restricted by Facebook's Terms of Service and other applicable policies. You are responsible for ensuring that your use of this software is authorized and lawful.

Do not use this project to access accounts, groups, or content that you are not authorized to access.

---

## 📖 Overview

**fbscraper** is a Python-based browser automation project using [Playwright](https://playwright.dev/) to collect publicly accessible Facebook content.

The current script, `fbscraperv1.py`, uses a Chromium browser session and can extract information from Facebook posts and comments.

The project currently focuses on:

* Playwright-based browser automation
* Chromium browser support
* Persistent browser sessions
* Facebook post extraction
* Comment extraction
* JSON output
* Basic dynamic-content handling

---

## 📋 Requirements

Before installing the project, make sure you have:

* Python 3.10 or newer
* Git
* Internet access
* A supported operating system:

  * Windows
  * Linux
  * macOS

Check your Python installation:

```bash
python --version
```

On Linux/macOS, you may need:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/fbscrape/fbscraper.git
cd fbscraper
```

---

## 2. Create a virtual environment

Using a virtual environment keeps the project's Python dependencies separate from your system Python installation.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal should show something similar to:

```text
(venv)
```

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install the project requirements

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

The current requirements are:

* `playwright`
* `playwright-stealth`

---

## 5. Install the Playwright browser

Playwright requires browser binaries in addition to the Python package.

Install Chromium:

```bash
playwright install chromium
```

If the `playwright` command is not available, use:

```bash
python -m playwright install chromium
```

To install all Playwright-supported browsers instead:

```bash
playwright install
```

---

# ✅ Verify the Installation

Check Playwright:

```bash
python -c "import playwright; print('Playwright installed successfully')"
```

Check `playwright-stealth`:

```bash
python -c "import playwright_stealth; print('playwright-stealth installed successfully')"
```

If both commands complete successfully, the Python dependencies are installed.

---

# 💻 Usage

The current version of the project is run directly through:

```bash
python fbscraperv1.py
```

On systems where `python3` is the Python command:

```bash
python3 fbscraperv1.py
```

The script opens a Chromium browser and uses the configured Facebook group URL in `fbscraperv1.py`.

---

## 🔧 Configuration

The current configuration is defined directly in `fbscraperv1.py`.

For example:

```python
GROUP_URL = "https://www.facebook.com/groups/elcasbah/"
TARGET_POSTS = 2
PROFILE_DIR = Path("./fb_stealth_profile")
```

### `GROUP_URL`

The Facebook group URL that the script processes.

Example:

```python
GROUP_URL = "https://www.facebook.com/groups/example/"
```

### `TARGET_POSTS`

Controls the target number of posts processed by the script.

Example:

```python
TARGET_POSTS = 2
```

### `PROFILE_DIR`

Directory used for the persistent browser profile.

Example:

```python
PROFILE_DIR = Path("./fb_stealth_profile")
```

The profile directory may contain browser/session data. Do not share it publicly or commit it to Git.

---

# 📁 Project Structure

A typical installation looks like:

```text
fbscraper/
├── fbscraperv1.py
├── requirements.txt
├── README.md
├── LICENSE
└── venv/
```

After running the program, a browser profile directory may also be created:

```text
fbscraper/
├── fbscraperv1.py
├── requirements.txt
├── README.md
├── LICENSE
├── fb_stealth_profile/
└── venv/
```

---

# 🔐 Browser Session Data

The script uses a persistent browser profile.

The profile directory may contain cookies, login/session information, and other browser data.

For this reason:

* Do not upload `fb_stealth_profile/` to GitHub.
* Do not share the directory with other people.
* Do not commit it to the repository.
* Add it to `.gitignore`.

Recommended `.gitignore` entry:

```gitignore
venv/
fb_stealth_profile/
__pycache__/
*.pyc
```

---

# 🛠️ Troubleshooting

## `python` is not recognized

Try:

```bash
python3 --version
```

If Python is not installed, install Python and ensure it is added to your system PATH.

On Windows, enable **Add Python to PATH** during installation.

---

## `pip` is not recognized

Use Python to invoke pip:

```bash
python -m pip install -r requirements.txt
```

---

## Playwright browser is missing

Run:

```bash
python -m playwright install chromium
```

---

## `playwright_stealth` cannot be imported

Reinstall the dependency:

```bash
python -m pip install --upgrade playwright-stealth
```

Then verify:

```bash
python -c "import playwright_stealth; print('OK')"
```

---

## Virtual environment is not active

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

---

# 🔄 Updating the Project

To update an existing clone:

```bash
git pull
```

Then update the Python dependencies:

```bash
python -m pip install --upgrade -r requirements.txt
```

If the Playwright version changes, reinstall the browser:

```bash
python -m playwright install chromium
```

---

# 📦 Quick Installation

For Linux/macOS:

```bash
git clone https://github.com/fbscrape/fbscraper.git
cd fbscraper

python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python -m playwright install chromium

python fbscraperv1.py
```

For Windows:

```powershell
git clone https://github.com/fbscrape/fbscraper.git
cd fbscraper

python -m venv venv
venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python -m playwright install chromium

python fbscraperv1.py
```

---

# 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
