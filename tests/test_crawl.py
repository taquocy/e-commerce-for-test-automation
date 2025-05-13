import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.vnexpress_crawler import VnExpressCrawler


crawler = VnExpressCrawler(headless=True)
articles = crawler.crawl("https://vnexpress.net/suc-khoe")
crawler.save_to_csv(articles, "vnexpress_health.csv")
crawler.close()
