#! /bin/sh
cd /data && rm *.html
cd /data && touch changjiang_daily.html tech_daily.html hubei_daily.html youth_daily.html 
cd /data && touch changjiang_sorted_daily.html tech_sorted_daily.html hubei_sorted_daily.html youth_sorted_daily.html 
cd /data && scrapy crawl tech_daily && scrapy crawl youth_daily && scrapy crawl hubei_daily && scrapy crawl changjiang_daily
cd /data && python3 send_result.py