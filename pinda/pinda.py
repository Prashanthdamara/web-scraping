from bs4 import BeautifulSoup
import openpyxl
import requests
from requests import exceptions

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'banquet hall'
sheet.append(['title','address','number'])


try:

    web_add = 'https://pinda.in/search?s=banquet%20hall&page='
    for page in range(1,101):
        source = requests.get(web_add+str(page))
        source.raise_for_status

        soup = BeautifulSoup(source.text,'html.parser')

        banquet = soup.find('div',class_ = 'fullmain').find_all('div',class_ = 'adrsitem')
            
        for ban in banquet:
            title = ban.find('ul').find('li').find('h4').a.text
            address = ban.find('ul').find('li').find('ul').text.splitlines()[1]
            p_number =  ban.find('ul').find('li').find('ul').text.splitlines()[2]
                

            
            sheet.append([title,address,p_number])


except exceptions as e:
    print(e)


excel.save('banquethallind.xlsx')
