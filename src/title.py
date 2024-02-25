import requests
import sys
from bs4 import BeautifulSoup
from logger import logging
from exception import CustomException

def get_channel_name(url):
    try:
        logging.info('Scrapping the title')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        link = soup.find_all(name="title")[0]
        title = str(link)
        title = title.replace("<title>","")
        title = title.replace("</title>","")
        channel_name = soup.find("span", itemprop="author").next.next['content']
        logging.info('Scrapping completed')

        return (channel_name, title)
    
    except Exception as e:
        logging.info('Error occured during scraping the title')
        raise CustomException(e, sys)

