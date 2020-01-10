from urllib import request
from bs4 import BeautifulSoup
url = 'https://www.atmarkit.co.jp/ait/subtop/di/'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

print(soup)