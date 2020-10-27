import requests
from bs4 import BeautifulSoup
##import mysql.connector
number = 0
while number < 10:
    URL = 'https://th.indeed.com/jobs?q=software+engineer&l=Thailand&start=' + str(number)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    results = soup.find_all('div',attrs={'data-tn-component':'organicJob'})
    for job_data in results:
        company = job_data.find('span',attrs={"class":"company"})
        company_final = company.text.strip()
        location = job_data.find('span',attrs={"class":"location accessible-contrast-color-location"})
        location_final = location.text.strip()
        job = job_data.find('a',attrs={"data-tn-element":"jobTitle"})
        job_final = job.text.strip()
##  salary = job_data.find('span',attrs={"class":" })
##  salary_final = salary.text.strip()

        print(company_final)
        print(job_final)
        print(location_final)
##  print(salary_final)
