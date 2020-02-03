from selenium import webdriver
import time
import requests, time, random
from bs4 import BeautifulSoup
import pandas
import csv
import io
import urllib
import codecs



# # specifies the path to the chromedriver.exe
driver = webdriver.Chrome(r"C:\Users\tomar\Downloads\chromedriver.exe")

# # driver.get method() will navigate to a page given by the URL address
driver.get(r"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(.5)

username = driver.find_element_by_id('username')

# # send_keys() to simulate key strokes
username.send_keys('mail@gmail.com')

# # locate password form by_class_name
password = driver.find_element_by_id('password')

# # send_keys() to simulate key strokes
password.send_keys('password')

login_btn = driver.find_element_by_class_name('btn__primary--large')
login_btn.click()

url = r"https://www.linkedin.com/mynetwork/invite-connect/connections/"

driver.get(url)

SCROLL_PAUSE_TIME = 3

# # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(5):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    #Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    #print(new_height)
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0," + str(last_height-2000) + ");")
        time.sleep(1)
        
    last_height = new_height
    print(i)


html = driver.page_source
# driver.close()
time.sleep(3)

soup = BeautifulSoup(html, 'html.parser')
connection_page = soup.findAll("section", {"class": "mn-connections"})[0]
# write html in file 
file2 = open("MyFile2.txt","w", encoding="utf-8")
file2.write(str(connection_page))
file2.close()
# print(connection_page)



# url = r'./MyFile2.txt'
# html = codecs.open(url, 'r', 'utf-8').read()

connection = connection_page.findAll(
    "header", {"class": "mn-connections__header"})[0].h1.text

friend_profiles_links = connection_page.findAll("a", {"class": "mn-connection-card__link"})

links = []

# open csv file for save all friends profile link 
with io.open('profile_links.csv', 'w+', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['link'])

    for friend_profile in friend_profiles_links:
        # user name
        name = friend_profile.find("span", {"class": "mn-connection-card__name"}).text.strip()
        # user profile link 
        link = friend_profile['href']
        # link = friend_profile.select('span')[1].get_text()

        links.append(link)

        print(name, link)  
        # write the link in csv file      
        writer.writerow([r'https://www.linkedin.com'+link])  


# save profile informations

# open a new csv file for save user details  
if links:
    with io.open('profile_datails.csv', 'w+', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Email', 'phone', 'website', 'Link', 'Current status', 'experience1', 'experience2', 'address', 'number of friends', 'profile image'])
        
        for link in links:
            url = r"https://www.linkedin.com" + link + r"detail/contact-info/"
            # got to single user profile 
            driver.get(url)
            time.sleep(3) #wait 3s for loading page you can change time depend on device and internet speed
            html = driver.page_source

            soup = BeautifulSoup(html, 'html.parser')

            # soup = soup.findAll(recursive=True)
            # //emai collection
            email_address = user_name = profile_image = current_work = phone = website = ''

            # website link 
            try:
                contact_info = soup.findAll("section", {"class": "ci-websites"})[0]
                website = contact_info.select('ul li a')[0]['href']
                print(website)
            except:
                print("website not found")
                pass

            # email address 
            try:
                contact_info = soup.findAll("section", {"class": "ci-email"})[0]
                email_address = contact_info.select('div a')[0]['href'].strip()
                print(email_address)
            except:
                print("email not found")
                pass

            # phone number 
            try:
                contact_info = soup.findAll("section", {"class": "ci-phone"})[0]
                phone = contact_info.select('ul li')[0].get_text()
                print(phone)
            except:
                print("phone not found")
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
            
            writer.writerow([user_name, email_address, phone, website, url, current_work, exp1, exp2, address, number_of_friend, contact_link, profile_image]) 



