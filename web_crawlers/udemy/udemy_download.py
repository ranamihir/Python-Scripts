from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import sys
import os
import time

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

courses = {
    "Shell-Scripting-Linux": 'https://citigroup.udemy.com/shell-scripting-linux/learn/v4/content'
}

browser = webdriver.Chrome('C:/Python34/chromedriver.exe')
url = 'https://citigroup.udemy.com/'
browser.get(url)
username = browser.find_element_by_name('USER')
username.send_keys('as48677')
password = browser.find_element_by_name('PASSWORD')
password.send_keys('c03u5thermo')
submit = browser.find_element_by_class_name('ButtonSm')
submit.click()
for course in courses:
    print('Checking for ' + course + '...')
    course_path = 'Udemy/' + course + '/'
    if not os.path.exists(course_path):
        os.makedirs(course_path)
    f = open(course_path + course.lower() + '-urls.txt', 'a')
    url = courses[course]
    video_count = 0
    while 1:
        try:
            print(video_count)
            browser.get(url)
            time.sleep(30)
            tooltip_containers = browser.find_elements_by_class_name('tooltip-container')
            for tooltip_container in tooltip_containers:
                if tooltip_container.text == 'All Sections':
                    tooltip_container.click()
                    break
            time.sleep(5)
            videos = browser.find_elements_by_class_name('lecture__item__link')
            video = videos[video_count]
            video.click()
            time.sleep(10)
            div = browser.find_element_by_class_name('asset-container')
            download_url = div.find_element_by_tag_name('div').find_element_by_tag_name('video').get_attribute('src')
            f.write(download_url + '\n')
            name = course_path + browser.find_element_by_class_name('course-info__section').text.strip(' ') + '.mp4'
            print('Name: ' + name)
            if not os.path.exists(name):
                urllib.request.urlretrieve(download_url, name, reporthook)
        except Exception as e:
            print(str(e.args[0]))
            pass
        finally:
            video_count += 1
            if video_count >= len(videos):
                break
    f.close()
