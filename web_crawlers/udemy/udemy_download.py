from selenium import webdriver
import urllib.request
import sys
import os
import time


def reporthook(blocknum, blocksize, totalsize):
    readsofar = (blocknum * blocksize)
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d mb / %d mb" % (
            percent, len(str(totalsize)), readsofar/(1024*1024), totalsize/(1024*1024))
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

courses = {
    "Shell-Scripting-Linux": 'https://citigroup.udemy.com/shell-scripting-linux/learn/v4/content',
    "Learning-Python-for-Data-Analysis-and-Visualization": "https://citigroup.udemy.com/learning-python-for-data-analysis-and-visualization/learn/v4/content"
}

browser = webdriver.Chrome('C:/Python34/chromedriver.exe')
url = 'https://citigroup.udemy.com/'
browser.get(url)
username = browser.find_element_by_name('USER')
username.send_keys('<username>')
password = browser.find_element_by_name('PASSWORD')
password.send_keys('<password>')
submit = browser.find_element_by_class_name('ButtonSm')
submit.click()

for course in courses:
    # Initially store the names of all videos for each course
    indices = []
    index_count = 0
    names = []
    video_count = 1
    sections = []
    print('Storing names of videos of the course \'' + course.replace('-', ' ') + '\'...')
    url = courses[course]
    browser.get(url)
    time.sleep(30)
    tooltip_containers = browser.find_elements_by_class_name('tooltip-container')
    for tooltip_container in tooltip_containers:
        if tooltip_container.text == 'All Sections':
            tooltip_container.click()
            break
    time.sleep(30)
    items = browser.find_elements_by_class_name('lecture__item')
    for item in items:
        if item.find_element_by_class_name('lecture__item__link__time').text:
            names.append(str(video_count) + '. ' + item.find_element_by_class_name('lecture__item__link__name').text.strip(' ') + '.mp4')
            video_count += 1
            indices.append(index_count)
        index_count += 1
    print('Found ' + str(video_count-1) + ' videos.\n')

    print('Downloading videos of the course \'' + course.replace('-', ' ') + '\'...')
    course_path = 'Udemy/' + course + '/'
    if not os.path.exists(course_path):
        os.makedirs(course_path)
    f = open(course_path + course.lower() + '-urls.txt', 'a')
    url = courses[course]
    video_count = 0
    for index in indices:
        try:
            if not os.path.exists(course_path + names[video_count]):
                browser.get(url)
                time.sleep(30)
                tooltip_containers = browser.find_elements_by_class_name('tooltip-container')
                for tooltip_container in tooltip_containers:
                    if tooltip_container.text == 'All Sections':
                        tooltip_container.click()
                        break
                time.sleep(5)
                videos = browser.find_elements_by_class_name('lecture__item__link')
                video = videos[index]
                video.click()
                time.sleep(10)
                div = browser.find_element_by_class_name('asset-container')
                download_url = div.find_element_by_tag_name('div').find_element_by_tag_name('video').get_attribute('src')
                f.write(names[video_count] + ':\t' + download_url + '\n')
                print('File being downloaded:\t' + names[video_count])
                urllib.request.urlretrieve(download_url, course_path + names[video_count], reporthook)
        except Exception as e:
            print(str(e.args[0]))
            pass
        finally:
            video_count += 1
    f.close()
