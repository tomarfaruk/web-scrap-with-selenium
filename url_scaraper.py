from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
import csv
import io
import urllib
import codecs
from time import sleep

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(r"chromedriver.exe")

# print("program written by omar faruk @umorfarukcse@gmail.com from bangladesh")
with io.open('profile_datails100t.csv', 'a', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    for i in range(1, 2500):
        print('\n\n')

        print(i)
        try:
            # get uri for page load
            uri = f"https://www.panpages.my/locations/my3-kuala-lumpur/listings?page={i}&per_page=20"
            # call uri
            driver.get(uri)
            time.sleep(1)
            # find the targeted urls
            links = driver.find_elements_by_css_selector(".fn.org>a")
            write_first_lik = True

            for l in links:
                link = "null"
                try:
                    link = l.get_attribute('href')
                    if write_first_lik:
                        writer.writerow([r''+link, i])
                    else:
                        writer.writerow([r''+link])
                    print(l.get_attribute('href'))
                except Exception as e:
                    print(e)
                    writer.writerow(["null"])
                write_first_lik = False

        except Exception as e:
            print(e)
            # if page nto loaded sleep for 5m and write a message in csv
            writer.writerow([f"can't load {i} number page "+uri])
            time.sleep(300)

driver.close()
