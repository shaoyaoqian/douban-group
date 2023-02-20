#! /bin/sh
cd /data && rm *.html
cd /data && touch changjiang_daily.html tech_daily.html hubei_daily.html youth_daily.html economic_daily.html people_daily.html
cd /data && touch changjiang_daily_sorted.html tech_daily_sorted.html hubei_daily_sorted.html youth_daily_sorted.html economic_daily_sorted.html people_daily_sorted.html
cd /data && scrapy crawl tech_daily && scrapy crawl youth_daily && scrapy crawl hubei_daily && scrapy crawl changjiang_daily && scrapy crawl people_daily && scrapy crawl economic_daily
cd /data && python3 send_result_morning.py