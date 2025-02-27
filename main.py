from bs4 import BeautifulSoup
import requests

print("Enter the skills that you not familiar with.")
unfamiliar_skill=input(">")
print(f"Filtering {unfamiliar_skill}")

url="https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation="
req=requests.get(url)
soup=BeautifulSoup(req.content, 'lxml')
jobs=soup.find_all("div",class_ ='srp-job-bx')
for job in jobs:
    posted_days=job.find('span',class_="posting-time").text.split()[0]
    postedays=int(posted_days)

    if postedays<10:
     company_name=job.find("span",class_="srp-comp-name").text.replace(" ","")
     skills=job.find("div", class_= "srp-keyskills").text
     salary=job.find("div", class_="srp-sal").text.replace(" ","")
     work_place=job.find("div", class_="srp-loc").text.replace(" ","")
     Experience=job.find("div",class_="srp-exp").text.replace(" ","")
     if unfamiliar_skill not in skills:
        print(f"Company_name: {company_name}")
        print(f"Skills: {skills.strip()}")
        print(f"Salary: {salary}")
        print(f"Work_place: {work_place}")
        print(f"Experience: {Experience}")
        print()



