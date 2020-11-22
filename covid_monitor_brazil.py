import requests
import bs4
import time


def Covid():
    cases1='0'
    deaths1='0'
    recovered1='0'
   
    while True:
        times = time.ctime().split()        
        req = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')
        soup = bs4.BeautifulSoup(req.text,'lxml')
        
        cases = soup.find_all('div',{'class':'maincounter-number'})[0].find('span').text
        deaths = soup.find_all('div',{'class':'maincounter-number'})[1].find('span').text
        recovered = soup.find_all('div',{'class':'maincounter-number'})[2].find('span').text
        
        
        if cases!=cases1 or deaths!=deaths1 or recovered!=recovered1:
            print(f'''
                  \033[31m_____________________________________________\033[m
                  
                  \033[36mAt {times[3]} of {times[2]}/{times[1]}/{times[4]}\033[m
                  
                  Cases: {cases}
                  Deaths: {deaths}
                  Recovered: {recovered}
                  \033[31m_____________________________________________\033[m
            ''')
            cases1=cases
            deaths1=deaths
            recovered1=recovered
            
    
Covid()
