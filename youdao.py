import os
import random
import time

from selenium import webdriver

print("有道翻译工具")
print("by Mirage 2021.5.19")
print("使用前请确认待翻译文件trans.txt已放在本目录")
print("正在启动chromedriver...")
browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://fanyi.youdao.com/')
print('等待网页加载...')
time.sleep(3)
inputArea = browser.find_element_by_id('inputOriginal')
fileName = 'Translate-' + time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime()) + '.txt'
result = open(fileName, 'w', encoding='utf-8')
target = ''
lines = 0
current = 0
i = 0
if os.path.exists('log'):
    current = int(open('log', encoding='utf-8', errors='ignore').read())
else:
    open('log', 'w', encoding='utf-8')
print('正在加载进度...')
for line in open('trans.txt', encoding='utf-8', errors='ignore'):
    while i <= current:
        i += 1
        break
    if len(target) + len(line) >= 4500:
        target = target + line
        lines += 1
        print(target)
        inputArea.send_keys(target)
        print('等待返回结果...')
        print('行数：' + str(lines))
        time.sleep(6)
        for index in range(lines):
            xpath = '//div[@id=\'transTarget\']/p[' + str(index + 1) + ']/span'
            text = browser.find_elements_by_xpath(xpath)
            for index2 in range(len(text)):
                print(text[index2].text)
                if text[index2].text != '\n' and text[index2].text != '':
                    result.write(text[index2].text)
            result.write('\n')
        result.flush()
        inputArea.clear()
        lines = 0
        target = ''
        time.sleep(random.randint(600, 1000) / 100)
    else:
        target = target + line
        lines += 1

browser.quit()
browser.stop_client()
