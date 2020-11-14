from selenium import webdriver
import time
import requests, time, random
from bs4 import BeautifulSoup
import pandas
import csv
import io
import urllib
import codecs
# import linked.links



# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(r"C:\Users\tomar\Downloads\chromedriver.exe")

#driver.get method() will navigate to a page given by the URL address
driver.get(r"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(0.5)

username = driver.find_element_by_id('username')

# # send_keys() to simulate key strokes
##username.send_keys('enriquerodriguage@gmail.com')
username.send_keys('umorfarukcse@gmail.com')

# # locate password form by_class_name
password = driver.find_element_by_id('password')

# # send_keys() to simulate key strokes
##password.send_keys('somnumbulistjamil123456789@@@')
password.send_keys('t1234567')

login_btn = driver.find_element_by_class_name('btn__primary--large')
login_btn.click()

url = r"https://www.linkedin.com/in/mir-mahfuz/detail/contact-info/"

driver.get(url)
time.sleep(3)
html = driver.page_source



soup = BeautifulSoup(html, 'html.parser')

# soup = soup.findAll(recursive=True)
# //emai collection
email_address = user_name = profile_image = current_work = ''
try:
    contact_info = soup.findAll("section", {"class": "ci-email"})[0]
    email_address = contact_info.select('div a')[0]['href'].strip()
    print(email_address)
except:
    print("email not found")
    pass

try:
    user_profile_html = soup.findAll("main", {"class": "core-rail"})[0]

    user_name = user_profile_html.select('.pv-top-card--list.inline-flex.align-items-center li')[0].get_text().strip()
    profile_image = user_profile_html.select('div.presence-entity.pv-top-card__image.presence-entity--size-9.ember-view img')[0]['src']
    current_work = user_profile_html.select('h2.mt1.t-18.t-black.t-normal')[0].get_text().strip()
except:
    print("error in user profile ")




about = user_profile_html.select('ul.pv-top-card--list.pv-top-card--list-bullet.mt1 li')
address = number_of_friend = contact_link = ''
try:
    if len(about) ==3 :
        address = about[0].get_text().strip()
        number_of_friend = about[1].get_text().strip()
        contact_link = about[2].select('a')[0]['href']
        print(contact_link)
except:
    print("error")
    pass
experiences = user_profile_html.select('ul.pv-top-card--experience-list li')
exp1 = exp2 = ''
try:
    exp1 = experiences[0].get_text().strip()
    exp2 = experiences[1].get_text().strip()
except:
    print('experience not found ')
print()
print(exp1, exp2)


with io.open('profile_datails.csv', 'w+', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Email', 'Link', 'Current status', 'experience1', 'experience2', 'address', 'number of friends', 'contact link', 'profile image'])

    writer.writerow([user_name, email_address, url, current_work, exp1, exp2, address, number_of_friend, contact_link, profile_image]) 


