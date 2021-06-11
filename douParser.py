

from bs4 import BeautifulSoup
import requests
import datetime

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

url = "https://jobs.dou.ua/"

response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, "lxml")

categoriesDict = {} #Here category names and links are stored
lowSkillVacancies = [] 
resultingList = []


#Gets count of offers for each vacancy
totalOffersCount = soup.findAll("em")

for i in range(len(totalOffersCount)): totalOffersCount[i] = int(totalOffersCount[i].getText())


#Gets names of vacancies and links to them, then incert it inside a dictionary
catlink = soup.findAll(class_ = "cat-link")

for i in range(len(catlink)):
    categoriesDict[catlink[i].text] = catlink[i].get('href') + "&exp=0-1"

#Gets count of low skill vacancies   
for i in categoriesDict.values():
    response = requests.get(i, headers=headers).text
    soup = BeautifulSoup(response, "lxml")
    num = soup.find("h1").text[0:2]
    lowSkillVacancies.append(int(num) if num.isnumeric() and not "   " else 0)


date = datetime.datetime.now().strftime("%d %B %Y")

#Outputs the result of parsing
print(f"Dou.ua vacancies dump for {date}")
n = 0 # for iteration purpose :)
for i in categoriesDict:
    print(f" Count of newbie vacancies for {i} is {round(lowSkillVacancies[n] / totalOffersCount[n] * 100)}%")
    n += 1





