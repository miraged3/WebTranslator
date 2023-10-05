import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

print("彩云翻译工具")
print("by Mirage 2023.10.5")
print("使用前请确认待翻译文件trans.txt已放在本目录")
print("正在启动chromedriver...")
browser = webdriver.Chrome()
browser.get('https://fanyi.caiyunapp.com/')
print('等待网页加载...')
time.sleep(3)
inputArea = browser.find_element(By.CLASS_NAME, 'textinput')
fileName = 'Translate-' + time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime()) + '.txt'
result = open(fileName, 'w', encoding='utf-8')
current = 0
i = 0
if os.path.exists('log') and os.path.getsize('log') != 0:
    current = int(open('log', encoding='utf-8', errors='ignore').read())
else:
    open('log', 'w', encoding='utf-8')
target = ''
lines = 0
print('正在加载进度...')
for line in open('trans.txt', encoding='utf-8', errors='ignore'):
    while i <= current:
        i += 1
        break
    if i > current:
        if len(target) + len(line) >= 4000:
            target = target + line
            print(line)
            lines += 1
            inputArea.send_keys(target)
            print('等待返回结果...')
            print('行数：' + str(lines))
            time.sleep(random.randint(600, 1000) / 100)
            text_target = browser.find_element(By.XPATH, '//*[@id="texttarget"]')
            print(text_target.text)
            result.write(text_target.text)
            result.write('\n')
            inputArea.clear()
            target = ''
            current = current + lines
            open('log', 'r+', encoding='utf-8', errors='ignore').truncate()
            open('log', 'r+', encoding='utf-8', errors='ignore').write(str(current))
            lines = 0
            result.flush()
            time.sleep(random.randint(600, 1000) / 100)
        else:
            target = target + line
            print(line)
            lines += 1

browser.quit()
browser.stop_client()
