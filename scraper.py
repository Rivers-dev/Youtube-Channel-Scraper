from selenium import webdriver
from selenium.webdriver.common.by import By

defaulturl = 'https://www.youtube.com/'
channels = [
    'https://www.youtube.com/c/KalleHallden/videos',
    'https://www.youtube.com/c/JomaOppa/videos'
]

driver = webdriver.Firefox(executable_path=r)
f = open('data.txt', 'a')
driver.get(defaulturl)

for c in range(len(channels)):
    driver.get(channels[c])
    channelName = driver.find_element(By.CLASS_NAME, 'style-scope ytd-channel-name').text
    f.write('\nFrom ' + channelName + '\n')
    print('\nFrom ' + channelName + '\n')
    el = driver.find_element(By.ID, 'video-title')
    print(el.text + '\n')
    f.write(el.text + '\n')
driver.close()