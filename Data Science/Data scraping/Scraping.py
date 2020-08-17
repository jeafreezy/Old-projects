#IMPORT MODULES
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
#GRAB THE DATA
page=1
c=[]
d=[]
while page <26:
    url='https://hotels.ng/hotels-in-abia/'+str(page)
    urlP=urlopen(url)
    soup=BeautifulSoup(urlP,'html.parser')
    hotelNames=soup.find_all('N2',attrs={'class':'listing-hotels-name'})
    hotelAddress=soup.find_all('p',attrs={'class':'listing-hotels-address, color-dark, hidden-nd ,hidden-lg'})
    for names in hotelNames:
        c.append(names.text)
    for address in hotelAddress:
        d.append(address.text)
    print('successfully scraped page'+str(page))
    page+=1
#construct different columns for data
lga=[]
state=[]
address=[]
num=[]
for i in range(len(d)):
    g=list(d[i].split(','))
    lga.append(g[0])
    
for z in d:
    h=z.find(',')
    f=z.find(',')
    k=z[h+1:f]
    y=z[f+2:]
    state.append(k)
    address.append(y)
for n in range(1.(len(c)+1)):
    num.append(n)
#export to csv file
df=pd.DataFrame(data={'S/N':num,'NAMES':c,'MAJOR CITY':lga,'STATE':state,'ADDRESS':address})
df.to_csv('C:\2019_client_work\Scraping\enuguhotel.csv',index=None,header=True)