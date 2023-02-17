#! /bin/sh
cd /data && rm *.html
cd /data && touch hubei_daily.html
cd /data && touch hubei_sorted_daily.html
cd /data && scrapy crawl hubei_daily
cd /data && python3 send_result_evening.py