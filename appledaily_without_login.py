from bs4 import BeautifulSoup
import urllib3

url = input("input url:")
#url test 'https://hk.news.appledaily.com/local/realtime/article/20190422/59515907/?utm_campaign=hkad_social_hk.nextmedia&utm_medium=social&utm_source=facebook&utm_content=link_post&fbclid=IwAR2E1JAMMtztQ2LYyMkht4IWCl7MmGYdjZCUyEJVmWLgyQljpymwj4-WHgs'

http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data , 'html.parser')
stories = soup.find_all('p')
for s in stories:
    print(s.text)
