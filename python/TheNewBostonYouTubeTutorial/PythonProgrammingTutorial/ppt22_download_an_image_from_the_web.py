import random
import urllib.request
# To allow Python to interface with operating system
import os

"""
#####################################
# Algorithm will save images in the #
# same directory script is located. #
#####################################
def download_web_image(url):
    name = random.randrange(1,50)
    file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, file_name)

download_web_image("https://cdn.fstoppers.com/styles/large-16-9/s3/lead/2018/11/dlsr.jpg")
"""


def download_web_image(url):
    path = ""
    name = random.randrange(1, 50)
    file_name = "ppt22_image_from_web" + str(name) + ".jpg"
    urllib.request.urlretrieve(url, "../TheNewBostonYouTubeTutorial/ppt_downloads/" + file_name)


download_web_image("https://cdn.fstoppers.com/styles/large-16-9/s3/lead/2018/11/dlsr.jpg")
