import os
import glob
import shutil

path = 'D:/ranamihir/Documents/Softwares & Tutorials/DeepLearningTV Tutorials/Deep Learning Simplified/'

os.chdir(path)
names = glob.glob("*.mp4")

for video_count, filename in enumerate(names):
    num = filename.replace(' (Deep Learning SIMPLIFIED)', '').replace('.mp4', '')[(filename.index('Ep. ')+4):]
    shutil.move(path + filename, path + num + '. ' + filename[:filename.index('Ep. ')].strip(' - ').strip('_').replace('_', "-") + '.mp4')