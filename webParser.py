
#Create a Virtual environment and add dependencies to that environment as needed for the project,
#  do not create global dependencies

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

# This prints the entire HTML structured elements of the site
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

# For/In loop checks for following parameters in the html script and pull text ouput from all that match
# The output is Job Title, company name and location for each job listing as a organized text.

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
   
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()


# print(results.prettify())

