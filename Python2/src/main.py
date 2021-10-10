import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

class ParseArticle:
    def scrapInformation(self, nameOfCurrency):

        URL = 'https://coinmarketcap.com/currencies/' + nameOfCurrency + '/news/'
        r = requests.get(URL, 'html.parser').text
        soup= BeautifulSoup(r,'lxml')
        
        header=soup.h2.text
        
        print(header, '\n')
        
        Text = soup.text.strip()
        cnt = 0
        for i in range(len(Text)):
            print(Text[i], end = '')
            if Text[i] == ' ':
                cnt += 1
                
            if cnt == 8:
                print('\n', end = '')
                cnt = 0
                
        print()
        print('-------------------------------------')
        print('\n\n\n')