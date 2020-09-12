import requests
from bs4 import BeautifulSoup
##import mysql.connector

URL = 'https://th.indeed.com/jobs?q=software+engineer&l=Thailand'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'lxml')

results = soup.find_all('div',attrs={'data-tn-component':'organicJob'})
for job_data in results:
    company = job_data.find('span',attrs={"class":"company"})
    company_final = company.text.strip()
    job = job_data.find('a',attrs={"data-tn-element":"jobTitle"})
    job_final = job.text.strip()

    print(company_final)
    print(job_final)