

from bs4 import BeautifulSoup
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

response = requests.get("https://jobs.dou.ua/", headers=headers).text

soup = BeautifulSoup(response, "lxml")

vacancies = []
lowSkillVacancies = [] 

#Gets count of offers for each vacancy
offersCount = soup.findAll("em")

#Gets names of vacancies and links to them, then incert it inside a dictionary
catlink = soup.findAll(class_ = "cat-link")

#Gets number of low skill requirements
for link in catlink:
    response = requests.get(link.get('href') + "&exp=0-1", headers=headers).text
    soup = BeautifulSoup(response, "lxml")
    num = soup.find("h1").text[0:2]
    lowSkillVacancies.append(int(num) if num.isnumeric() else 0)


for i in range(len(catlink or offersCount)):
    vacancies.append({
        "name" : catlink[i].text,
        "link" : catlink[i].get('href'),
        "count" :  int(offersCount[i].getText()),
        "newbieCount" : lowSkillVacancies[i], 
        "percent" : round(lowSkillVacancies[i] / int(offersCount[i].getText()) * 100)
    })


outputList = sorted(vacancies, key = lambda i: i['percent'], reverse=True)

for i in range(len(outputList)):
    print("Count of newbie vacancies for ", outputList[i]["name"], "is", outputList[i]["percent"], "%")








