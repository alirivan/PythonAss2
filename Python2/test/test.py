from main import ParseArticle

#par.scrapInformation('bitcoin')
#par.scrapInformation('cardano')
par = ParseArticle();

a = input('Please write crypto currency name: ')
par.scrapInformation(a)