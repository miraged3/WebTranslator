import time

from selenium import webdriver

print("彩云翻译工具")
print("by Mirage 2021.5.17")
print("使用前请确认待翻译文件trans.txt已放在本目录")
print("正在启动chromedriver...")
browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://fanyi.caiyunapp.com/')
print('等待网页加载...')
time.sleep(3)
inputArea = browser.find_element_by_class_name('textinput')
fileName = 'Translate-' + time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime()) + '.txt'
result = open(fileName, 'w', encoding='utf-8')
target = ''
lines = 0
for line in open('trans.txt', encoding='utf-8', errors='ignore'):
    if len(target) + len(line) >= 4500:
        target = target + line
        lines += 1
        print(target)
        inputArea.send_keys(target)
        print('等待返回结果...')
        print('行数：' + str(lines))
        time.sleep(6)
        for index in range(lines):
            xpath = '//div[@id=\'texttarget\']/p[' + str(index + 1) + ']/span'
            text = browser.find_element_by_xpath(xpath)
            print(text.text)
            result.write(text.text)
            result.write('\n')
        result.flush()
        inputArea.clear()
        lines = 0
        target = ''
    else:
        target = target + line
        lines += 1

browser.quit()
browser.stop_client()
