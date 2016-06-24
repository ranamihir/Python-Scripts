from selenium import webdriver
import os
from os import listdir
from os.path import isdir, isfile, join
import time


def sorting_function_indexed(f):
    return int(f.split('.')[0])


def sorting_function_proper(f):
    return int(f.split('.')[1])

courses = {
    "Shell-Scripting-Linux": 'https://citigroup.udemy.com/shell-scripting-linux/learn/v4/content',
    "Learning-Python-for-Data-Analysis-and-Visualization": "https://citigroup.udemy.com/learning-python-for-data-analysis-and-visualization/learn/v4/content"
}


def indexed_rename(course_path):
    video_count = 1
    folder_count = 1
    num_folders = len([f for f in listdir(course_path) if isdir(join(course_path, f))])

    while folder_count <= num_folders:
        path = course_path + str(folder_count)
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for f in sorted(files, key=sorting_function_indexed):
            try:
                os.rename(path + '/' + f, path + '/' + str(folder_count) + '.' + str(video_count) + '.mp4')
            except:
                pass
            finally:
                video_count += 1
        folder_count += 1


def proper_rename():
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
        course_path = 'C:/Users/ranamihir/Documents/Softwares & Tutorials/Udemy/' + course.replace('-', ' ') + '/'
        indexed_rename(course_path)
        print('Renaming videos of the course  \'' + course.replace('-', ' ') + '\'...')
        names = []
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
                names.append(item.find_element_by_class_name('lecture__item__link__name').text.strip(' ') + '.mp4')

        video_count = 0
        folder_count = 1
        num_folders = len([f for f in listdir(course_path) if isdir(join(course_path, f))])
        while folder_count <= num_folders:
            file_path = course_path + str(folder_count)
            files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
            for f in sorted(files, key=sorting_function_proper):
                try:
                    path = course_path + str(folder_count) + '/'
                    os.rename(path + f, path + f.split('.')[1] + '. ' + names[video_count].replace('/', ',').replace(':', ' - '))
                except:
                    pass
                finally:
                    video_count += 1
            folder_count += 1

proper_rename()