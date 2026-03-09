from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:
    def __init__(self):
        self.url = "http://learn-co-curriculum.github.io/site-for-scraping/courses"

    def get_page(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.content, 'html.parser')

    def get_courses(self):
        doc = self.get_page()
        articles = doc.find_all('article', class_='post')
        return [a for a in articles if a.find('h2')]

    def make_courses(self):
        courses = []
        course_elements = self.get_courses()
        for element in course_elements:
            title = element.find('h2').text.strip()
            schedule = element.find('em', class_='date').text.strip()
            description = element.find('p').text.strip()
            course = Course(title=title, schedule=schedule, description=description)
            courses.append(course)
        return courses
