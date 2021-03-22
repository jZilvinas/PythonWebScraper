from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

main_url = 'https://kinect.lt'

def PlaystationsUrls(urls):
    uClient = uReq(main_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    playstation4 = page_soup.findAll('a', {'id': 'st_advanced_ma_11'})
    ps4tmp = playstation4[0]

    playstation3 = page_soup.findAll('a', {'id': 'st_advanced_ma_17'})
    ps3tmp = playstation3[0]

    playstation4_url = ps4tmp.get('href')
    playstation3_url = ps3tmp.get('href')

    urls.append(playstation4_url)
    urls.append(playstation3_url)
    return urls
    

def getPSGamesUrls(psUrls, psGamesUrls):
    uClient = uReq(psUrls)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    gameImgLink = page_soup.findAll('a', {'class': 'product_img_link'})

    for item in gameImgLink:
        psGamesUrls.append(item.get('href'))

    return psGamesUrls   


def collectPsGamesdata(psGamesUrls, messyText):
    for item in psGamesUrls:
        scraping_url = item
        uClient = uReq(scraping_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, 'html.parser')

        tmpData = []

        name = page_soup.findAll('h1', {'class': 'product_main_name'})
        pureName = name[0]
        tmpData.append(pureName.text)

        price = page_soup.findAll('span', {'id': 'our_price_display'})
        purePrice = price[0]
        tmpData.append(purePrice.text)

        availability = page_soup.findAll('span', {'id': 'availability_value'})
        pureAvailability = availability[0]
        tmpData.append(pureAvailability.text)

        table = page_soup.findAll('table', {'class': 'table-data-sheet table-bordered'})
        tmpVar = table[0]

        tableText = tmpVar.findAll('td')
        
        for item in tableText:
            tmpData.append(item.text)

        messyText.append(tmpData)
    
    return messyText


def makeTextPureAgain(messyText, pureText):
    for line in messyText:
        almostPureText = []
        if len(line) == 19:
            almostPureText.append(line[0])
            almostPureText.append(line[10])
            almostPureText.append(line[18])
            priceStr = line[1].split(' ', 1)
            price = priceStr[0]
            price = price.replace(',', '.')
            almostPureText.append(price)
            almostPureText.append(line[4])
            almostPureText.append(line[2])
            almostPureText.append(line[8])
            pureText.append(almostPureText)
        else: 
            def search(var):
                if var in line:
                    i = line.index(var)
                    almostPureText.append(line[i+1])
                else:
                    almostPureText.append('N/A')

            vars = ['Žaidimo žanras', 'Platforma', 'Išleidimo data', 'PEGI reitingas']
            almostPureText.append(line[0])
            search(vars[0])
            search(vars[1])
            priceStr = line[1].split(' ', 1)
            price = priceStr[0]
            price = price.replace(',', '.')
            almostPureText.append(price)
            search(vars[2])
            almostPureText.append(line[2])
            search(vars[3])
            pureText.append(almostPureText)
            
    return pureText
    
def toJson(purePS4Text, purePS3Text):
    listOflists = [purePS4Text, purePS3Text]
    datatoWrite = {}
    datalist= []

    for NameOfList in listOflists:
        for item in NameOfList:
            tempdata={}
            tempdata['name'] = item[0]
            tempdata['platform'] = item[1]
            tempdata['genre'] = item[2]
            tempdata['price'] = item[3]
            tempdata['release_date'] = item[4]
            tempdata['availability'] = item[5]
            tempdata['pegi'] = item[6]
            datalist.append(tempdata)

    datatoWrite ['Games'] = datalist

    with open(jsonFileName, 'w') as data_output:
        json.dump(datatoWrite, data_output, indent=2)

def run(psUrls,theList):
    getPSGamesUrls(psUrls[0], theList[0][0])
    collectPsGamesdata(theList[0][0], theList[0][1])
    makeTextPureAgain(theList[0][1], theList[0][2])
                                    
def run2(psUrls,theList):
    getPSGamesUrls(psUrls[1], theList[1][0])
    collectPsGamesdata(theList[1][0], theList[1][1])
    makeTextPureAgain(theList[1][1], theList[1][2])



#RUN CODE
jsonFileName = 'gamesData.json'
psUrls = []
ps4GamesUrls = []
ps3GamesUrls = []
messyPS4Text = []
purePS4Text = []
messyPS3Text = []
purePS3Text = []
theList = [[ps4GamesUrls, messyPS4Text, purePS4Text],[ps3GamesUrls, messyPS3Text, purePS3Text]]

print('Single-threaded webscraper collecting data from {}... Please wait..'.format(main_url))

PlaystationsUrls(psUrls)

run(psUrls, theList)
run2(psUrls, theList)

toJson(purePS4Text, purePS3Text)

print()
print('Single-threaded webscraper done. Games data saved in {}.'.format(jsonFileName))

