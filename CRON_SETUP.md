# Cron Job Setup for MyFitPrice.in

## Amazon Scraper
Runs daily at 6:00 AM

Command:
0 6 * * * /path/to/venv/bin/python /path/to/project/manage.py amazon_scraper >> /path/to/logs/amazon_scraper.log 2>&1

## Flipkart Scraper
Runs daily at 6:05 AM

Command:
5 6 * * * /path/to/venv/bin/python /path/to/project/manage.py flipkart_scraper >> /path/to/logs/flipkart_scraper.log 2>&1
