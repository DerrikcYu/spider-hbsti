from datetime import date
current_date = date.today()
print(current_date.month)
print(current_date.day)
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from src.send_email import SendMailToMe
item={
    'noticeTitle':'',
    'noticeType':'',
    'noticeUrl':'',
    'noticeDate':'',
    'noticeContent':'',
}
s=1
sendmail = SendMailToMe()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.miit.gov.cn/xwfb/gxdt/index.html") #
    page.wait_for_timeout(3000)
    content = page.content()

    soup = BeautifulSoup(content, "html.parser")
    # print(soup)
    # for t in soup.select(".title"):
    #     print(t.text)
    a = soup.select('.fl')  # 得到一个所有a标签的集合
    t = soup.select('.fr')
    for i in range(0, len(a)):  # 遍历所有的a标签
        # if a[i]['href'] == '/lianzai/':
        print(a[i].text)
        print(a[i]['href'])
        print(t[i].text)
        item['noticeTitle'] = a[i].text
        item['noticeUrl'] = a[i]['href']
        item['noticeDate'] = t[i].text
        item['noticeType'] = '科技政策资讯'
        item['noticeContent']= '测试内容'
        sendmail.process_item(item)
    browser.close()
