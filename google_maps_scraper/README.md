# Google Maps Supermarket Scraper

This project scrapes data of supermarkets near Washington from Google Maps, including name, address, phone number, and website.  
The extracted data is saved into a CSV file, which you can find in this project folder.

## How It Works

- The scraper uses Selenium to navigate Google Maps and collect supermarket information.
- The collected data is stored in `markets.csv`.

## ChromeDriver

For simplicity, the ChromeDriver executable is included in this project folder.  
Make sure to use the ChromeDriver version compatible with your installed Chrome browser.

If you want to update or replace ChromeDriver, you can download it from:  
https://sites.google.com/chromium.org/driver/

## How to Run

1. Install dependencies:  
```bash
pip install -r requirements.txt