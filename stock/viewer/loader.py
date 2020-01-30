import sys
import os
import unicodedata

module_parent_dir_path = os.path.abspath(os.path.join(__file__))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it


from django.utils.timezone import now
from bs4 import BeautifulSoup
import requests
from viewer.models import StockQuotes
import datetime


class Loader:
    def __init__(self):
        url = "https://www.bankier.pl/gielda/notowania/akcje"
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")

    # Simply get all of the codes from page
    def get_codes(self):
        columns = self.soup.find_all('td', class_="colWalor")
        codes = []
        for col in columns:
            code = col.text.rstrip()  # getting rid of whitespaces
            codes.append(code.splitlines()[1])  # getting rid of \n signs
        return codes

    # Simply get all of the titles from page
    def get_titles(self):
        columns = self.soup.find_all('td', class_="colWalor")
        names = []
        for col in columns:
            names.append(col.find('a')['title'])
        return names

    # Simply get all of the courses from page
    def get_courses(self):
        columns = self.soup.find_all('td', class_="colKurs")
        values = []
        for col in columns:
            try:
                value = col.text
                value = str(value.replace(',', '.'))
                values.append(float(value))
            except ValueError:
                # used this cause of some weird input signs called non-breaking space in Latin1 (ISO 8859-1)
                value = col.text
                value = value.replace('\xa0', ' ')  # this solution is not the best one but for now it works
                value = value.split(' ')[1]
                value = str(value.replace(',', '.'))
                values.append(float(value))
        return values

    def save_to_db(self, courses, codes, titles):
        size = len(courses)
        for i in range(size):
            data = {'code':codes[i], 'title':titles[i] ,'course':courses[i]}
            quote = StockQuotes.objects.filter(code=data['code'], name=data['title']).first()
            if quote:
                self.update(quote, data)
            else:
                self.create(data)

    def create(self, data):
        quote = StockQuotes.objects.create(code=data['code'], name=data['title'], price=data['course'])
        quote.save()

    def update(self, quote, data):
        quote.price = data['course']
        quote.date = now()
        quote.save()


def run():
    l = Loader()
    courses = l.get_courses()
    codes = l.get_codes()
    titles = l.get_titles()
    l.save_to_db(courses, codes, titles)
