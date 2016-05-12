__author__ = 'Matthew'

from bs4 import BeautifulSoup
from selenium                                       import webdriver
from time import sleep
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from worker.models import JobDescription

class requester_firefox(object):
    def __init__(self):
        self.selenium_browser = webdriver.Firefox()
        self.selenium_browser.set_page_load_timeout(300)

    def __del__(self):
        self.selenium_browser.quit()
        self.selenium_browser = None

    def __call__(self, url):
        try:
            self.selenium_browser.get(url)
            the_page = self.selenium_browser.page_source
        except Exception:
            the_page = ""
        return the_page

class GetSeekJobDescription:

    def __init__(self):
        self.test = requester_firefox()

        sleep(2)

        self.get_search_results()
        self.get_pages()

    def get_search_results(self):
        self.seek_search_url = 'http://www.seek.com.au/jobs-in-information-communication-technology/in-australia/#dateRange=3&workType=0&industry=6281&occupation=&graduateSearch=false&salaryFrom=0&salaryTo=999999&salaryType=annual&companyID=&advertiserID=&advertiserGroup=&keywords=&displaySuburb=&seoSuburb=&where=&whereId=&whereIsDirty=false&isAreaUnspecified=false&location=&area=&nation=3000&sortMode=ListedDate&searchFrom=filters&searchType=%5C'
        self.all_links = []

        seen_jobs = set()
        reset = False
        searching = True
        page_no = 1
        while searching:
            result = self.test(self.seek_search_url + '&page=' + str(page_no)).encode("ascii", "ignore")

            soup = BeautifulSoup(result, 'html.parser')

            url_links = soup.findAll("a", { "class" : "job-title" })

            for url_link in url_links:
                if url_link['href'][5:13] not in seen_jobs:
                    self.all_links.append(url_link['href'])
                    seen_jobs.add(url_link['href'][5:13])

            if len(url_links) == 0:
                searching = False
            else:
                page_no += 1

    def get_pages(self):
        self.seek_base_url = 'http://www.seek.com.au/'
        for url in self.all_links:
            result = self.test(self.seek_base_url + url).encode("ascii", "ignore")

            soup = BeautifulSoup(result, 'html.parser')

            job_description = JobDescription()
            job_description.url = url

            try:
                job_description.heading = soup.findAll("div", { "class" : "grid_6" })[1].h1.getText()
                body = soup.find("div", { "id" : "jobTemplate" }).getText()
                job_description.body = re.sub("(?s).*?(--&gt;)", "\\1", body, 1)[7:].strip()
            except:
                continue

            try:
                job_description.address_locality = soup.find("span", { "itemprop" : "addressLocality" }).getText()
            except:
                job_description.address_locality = ''

            try:
                job_description.address_region = soup.find("span", { "itemprop" : "addressRegion" }).getText()
            except:
                job_description.address_region = ''

            try:
                job_description.work_type = soup.find("div", { "itemprop" : "employmentType" }).getText()
            except:
                job_description.work_type = ''

            try:
                job_description.classification = soup.find("span", { "itemprop" : "industry" }).getText()
            except:
                job_description.classification = ''

            if job_description.classification != '':
                try:
                    sub_classification = soup.find("span", { "itemprop" : "industry" }).parent.getText()
                    job_description.sub_classification = re.sub(re.escape(job_description.classification), '', sub_classification).strip()
                except:
                    job_description.sub_classification = ''

            job_description.save()

