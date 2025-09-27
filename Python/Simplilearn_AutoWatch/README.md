# Simplilearn AutoWatch

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 

A Python automation tool designed to help Simplilearn users efficiently complete course viewing requirements.

## Overview

Simplilearn AutoWatch is a lightweight Python script that automates the video watching process on Simplilearn's learning platform. The tool uses Selenium WebDriver to simulate user interactions, allowing for seamless progress through course content.

<p align="center">
   <img src="/sample1.png" alt="Simplilearn Login Page" width="500"/>
</p>

<div align="center"><em>Screenshot: Simplilearn Login Page</em></div>

## Features

- Automatic login to Simplilearn
- Continuous video progress monitoring
- Maintains session activity

## Prerequisites

- Python 3.7+
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone this repository:
```bash
git clone https://github.com/kayden-vs/simplilearn_autowatch.git
cd simplilearn_autowatch
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Install Google Chrome (if not already installed):
   - **Ubuntu/Debian**: `sudo apt install google-chrome-stable`
   - **Windows/macOS**: Download from [Google Chrome website](https://www.google.com/chrome/)

4. Install ChromeDriver:
   - **Ubuntu/Debian**: 
     ```bash
     wget https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
     unzip chromedriver_linux64.zip
     sudo mv chromedriver /usr/local/bin/
     ```
   - **Windows**: Download from [ChromeDriver website](https://chromedriver.chromium.org/downloads) and add to PATH
   - **macOS**: `brew install --cask chromedriver`

## Usage

1. Edit `video-bot.py` with your Simplilearn credentials:
```python
email = "your_email@example.com"
password = "your_password"
```

2. **Important**: Before running the script, manually log in to Simplilearn and ensure the course you want to complete is at the top of your "My Learnings" section. The script will click the first "Continue Watching" button it finds.

3. Run the script:
```bash
python video-bot.py
```

4. The script will automatically:
   - Log in to your Simplilearn account
   - Click on the "Continue Watching" button for your course
   - Monitor video progress until completion

<p align="center">
   <img src="/sample2.png" alt="My Learning Page - Script in Action" width="500"/>
</p>

<div align="center"><em>Screenshot: My Learning page showing the script in action</em></div>

## Disclaimer

This tool is designed for educational purposes and personal convenience. Users are responsible for ensuring they comply with Simplilearn's terms of service.

## License

MIT
