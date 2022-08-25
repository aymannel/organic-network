from bs4 import BeautifulSoup
import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='(%(levelname)-s) %(asctime)s %(message)s', datefmt='%d-%m %H:%M:%S')

class ReactionScraper:
    def __init__(self):
        if os.path.exists('source.html'):       # caching strategy / only need to perform HTTP request once
            logging.info('Page source via "source.html"')
            with open('source.html') as file:
                self.soup = BeautifulSoup(file.read(), 'lxml')

        else:
            logging.info('Page source via requests')
            rq = requests.get('https://www.organic-chemistry.org/namedreactions/')
            try:
                assert rq.status_code == 200
                logging.info('HTTP request successful')

                self.soup = BeautifulSoup(rq.text, 'lxml')
                with open('source.html', 'w') as file:
                    file.write(self.soup.prettify())

            except:
                logging.error('HTTP request unsuccessful')
                pass

        self.scrape()

    def get_reactions(self):
        self.soup.
        
    
ReactionScraper()
