# Importing modules that are essential to web scraping
import requests
from bs4 import BeautifulSoup
# Passing in a User Agent header in the url which will bypass the security placed on the site
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
r = requests.get('https://connect2concepts.com/connect2/?type=circle&key=8E2C21D2-6F5D-45C1-AF9E-C23AEBFDA68B', headers=headers)

# Obtaining the html of the website and storing it in soup
soup = BeautifulSoup(r.text, "html5lib")

# Finding all div elements with the style: text-align:center
# This div elements contain the strings of data we need.
things = soup.find_all("div", style="text-align:center;")

# Defining a dictionary no_Of_People to store the information
no_Of_People = {}

# Using a for loop to iterate through the list of things
for line in things:
    # Since No Of People is always placed after ")", we will break up the
    # Sentence at the bracket
    temp = line.text.split(")")

    # This line of code will store both the name of the place and the amount of people there in the dictionary
    no_Of_People[temp[0].split("(")[0]] = int(temp[1].split("U")[0][-1])

# Prints Dictionary
print(no_Of_People)