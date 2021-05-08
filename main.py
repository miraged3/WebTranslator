import time

from selenium import webdriver

browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://fanyi.youdao.com/')
print('等待网页加载...')
time.sleep(3)
inputArea = browser.find_element_by_id('inputOriginal')
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
        time.sleep(6)
        output = browser.find_element_by_id('transTarget')
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
    else:
        target = target + line
        lines += 1

browser.quit()
browser.stop_client()
