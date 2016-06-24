from selenium import webdriver
import urllib.request
import sys
import os
from os.path import isfile, join
import time
import shutil


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


def replace(s):
    return s.replace('\\', '').replace('/', ',').replace(':', ' -').replace('*', '').replace('?', '.').replace('\"', '\'').replace('<', '').replace('>', '').replace('|', '')


courses = {
    # "Shell-Scripting-Linux": 'https://citigroup.udemy.com/shell-scripting-linux/learn/v4/content',
    # "Learning-Python-for-Data-Analysis-and-Visualization": "https://citigroup.udemy.com/learning-python-for-data-analysis-and-visualization/learn/v4/content",
    # "Data Analysis in Python with Pandas": "https://citigroup.udemy.com/data-analysis-in-python-with-pandas/learn/v4/content",
    # "Data Science: Deep Learning in Python": "https://citigroup.udemy.com/data-science-deep-learning-in-python/learn/v4/content",
    # "Build Web Apps with React JS and Flux": "https://citigroup.udemy.com/learn-and-understand-reactjs/learn/v4/content",
    # "Project Management Professional: Prep for PMP": "https://citigroup.udemy.com/pmp-exam-prep-everything-you-must-know-to-pass-the-pmp-exam/learn/v4/content",
    # "Master Project Risk Management - 5 PDUs": "https://citigroup.udemy.com/project-risk-management-5-pdus/learn/v4/content",
    # "Business Management - Organisational Culture Change Training": "https://citigroup.udemy.com/business-create-organisational-culture-change/learn/v4/content",
    # "Statistics for Management (MBA) - Foundation of Analytics": "https://citigroup.udemy.com/statistics-by-example/learn/v4/content",
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
    # Initially store the names of all videos for each course
    indices = []
    index_count = 0
    names = []
    video_count = 1
    print('Storing names of videos of the course \'' + replace(course).replace('-', ' ') + '\'...')
    url = courses[course]
    browser.get(url)
    time.sleep(30)
    tooltip_containers = browser.find_elements_by_class_name('tooltip-container')
    for tooltip_container in tooltip_containers:
        if tooltip_container.text == 'All Sections':
            tooltip_container.click()
            break
    time.sleep(10)
    items = browser.find_elements_by_class_name('lecture__item')
    for item in items:
        if item.find_element_by_class_name('lecture__item__link__time').text:
            names.append(replace(str(video_count) + '. ' + item.find_element_by_class_name('lecture__item__link__name').text.strip(' ')) + '.mp4')
            video_count += 1
            indices.append(index_count)
        index_count += 1
    print('Found ' + str(video_count-1) + ' videos.\n')

    # Downloading all videos with proper names
    print('Downloading videos of the course \'' + course.replace('-', ' ') + '\'...')
    course_path = 'Udemy/' + replace(course) + '/'
    if not os.path.exists(course_path):
        os.makedirs(course_path)
    f = open(course_path + 'Download Urls.txt', 'a')
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
                time.sleep(10)
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
            print('Download Failed. ' + str(e.args[0]))
            pass
        finally:
            video_count += 1
    f.close()

    # Put videos in correct folders
    browser.get(url)
    time.sleep(30)
    print('Rearranging videos of the course \'' + course.replace('-', ' ') + '\' in correct folders...')
    tooltip_containers = browser.find_elements_by_class_name('tooltip-container')
    for tooltip_container in tooltip_containers:
        if tooltip_container.text == 'All Sections':
            tooltip_container.click()
            break
    time.sleep(10)
    sections = browser.find_elements_by_class_name('curriculum-navigation__section')
    global_video_count = 0
    section_titles = []
    for i, section in enumerate(sections):
        section_title = str(i+1) + '. ' + replace(section.find_element_by_class_name('curriculum-navigation__section__title').text.strip(' '))
        section_titles.append(section_title)
        print(section_title)
        if not os.path.exists(course_path + section_title):
            os.makedirs(course_path + section_title)
        num_videos = 0
        items = section.find_elements_by_class_name('lecture__item')
        for item in items:
            if item.find_element_by_class_name('lecture__item__link__time').text:
                num_videos += 1
        local_video_count = 0
        while local_video_count < num_videos:
            try:
                shutil.move(course_path + names[global_video_count + local_video_count], course_path + section_title + '/' + names[global_video_count + local_video_count])
            except Exception as e:
                print('Rearranging Failed. ' + str(e.args[0]))
                pass
            finally:
                local_video_count += 1
        global_video_count += num_videos

    # Safely quit browser
    browser.quit()

    # Remove Empty folders
    for section_title in section_titles:
        section_path = course_path + section_title
        num_files = len([f for f in os.listdir(section_path) if isfile(join(section_path, f))])
        if not num_files:
            print('Removing empty directory \'' + section_title + '\'...')
            os.rmdir(section_path)

    # Delete 'Download Urls.txt' file if all videos haves been downloaded
    if len(names) == global_video_count:
        os.remove(f.name)
