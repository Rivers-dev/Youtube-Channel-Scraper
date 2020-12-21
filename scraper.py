from selenium import webdriver
from selenium.webdriver.common.by import By

defaulturl = 'https://www.youtube.com/'
channels = [
    'https://www.youtube.com/c/KalleHallden/videos',
    'https://www.youtube.com/c/JomaOppa/videos'
]

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(firefox_options = options, executable_path=r'/home/connort/Documents/YoutubeScraper/geckodriver')

driver.minimize_window()
driver.get(defaulturl)
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
    print(el.get_attribute('href'))
    f.write(el.get_attribute('href') + '\n')
    print()
driver.close()
