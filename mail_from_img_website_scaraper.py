from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
import csv
import urllib
import codecs
from time import sleep
import io
import requests
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def get_text(xpath):
    try:
        return driver.find_element_by_xpath(xpath).text
    except Exception as e:
        print("error on parsing item"+str(e))
        return ''


def get_mail_address(url):
    try:
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        # print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
        text = pytesseract.image_to_string(img)
        print('........')

        print(text.split('\n'))
        return text.split('\n')[0]
    except Exception as e:
        print("mail can't convert to text")
        return ''


def det_mail_url():
    try:
        links = driver.find_elements_by_css_selector(".e-mail")
        url = links[0].get_attribute('src')
        if url:
            return get_mail_address(url)
        return ''
    except Exception as e:
        print("mail url not found")
        return ''


def get_text_by_css(css):
    try:
        return driver.find_element_by_css_selector(css).text
    except Exception as e:
        print('not found by css ')
        return ''


links = []
with io.open('file.csv', 'r', newline='',) as csv_file:
    myreader = csv.reader(csv_file)

    for r in reversed(list(myreader)):
        link = r[0]
        print(link)
        links.append(link)
csv_file.close()
print(len(links))
print(',,,,,,,,,')

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(r"chromedriver.exe")

# driver.get method() will navigate to a page given by the URL address

try:
    # open a new csv file
    with io.open('profile_datails.csv', 'w+', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Link', 'Name', 'Mail', 'Phone', 'Website'])
        for count, link in enumerate(reversed(links), start=1):

            print('\n\n\n')
            print(count, link)
            if(len(link) <= 8):
                continue

            try:
                driver.get(link)
                name = mail = phone = website = ''
                try:
                    mail = det_mail_url()
                    phone = get_text_by_css(
                        ".url.arrow-right.phone-number>span")
                    name = get_text_by_css("#listing-name")
                    website = get_text_by_css(".arrow-right.website>span")

                    if not website and not mail:
                        print(
                            'mail and website not found so no need to write csv file\n')
                        continue

                    print(mail, phone, name, website)
                    writer.writerow([link, name, mail, phone,  website])
                except Exception as e:
                    writer.writerow([link,  name, mail, phone, website])
                    print("mail phone name error"+str(e))
            except Exception as e:
                print("advance error"+str(e))
            # time.sleep(2)

except Exception as e:
    print("main error"+str(e))

driver.close()
