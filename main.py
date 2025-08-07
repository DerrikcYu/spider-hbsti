from datetime import date
# current_date = date.today()
# print(current_date.month)
# print(current_date.day)
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from src.send_email import SendMailToMe
import requests
import lxml

item={
    'noticeTitle':[],
    'noticeType':[],
    'noticeUrl':[],
    'noticeDate':[],
    'noticeContent':[],
}

sendmail = SendMailToMe()
now = date.today()
print('今天的日期是：',now)
##===============================================工业和信息化部-政策动态
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
        print(a[i].text)
        print(a[i]['href'])
        print(t[i].text)
        # item['noticeTitle'] = a[i].text
        # item['noticeUrl'] = a[i]['href']
        # item['noticeDate'] = t[i].text
        date_content = t[i].text
        type_content = '工信部科技政策资讯'
        if str(now) != str(date_content):
            item['noticeTitle'].append(a[i].text)
            item['noticeUrl'].append(a[i]['href'])
            item['noticeDate'].append(t[i].text)
            item['noticeType'].append(type_content)
        # if str(item['noticeDate']) == '2025-08-06':
        #     try:
        #         content_html = requests.get(item['noticeUrl']).content.decode('utf-8')
        #     except:
        #         item['noticeUrl'] = 'https://www.miit.gov.cn/' + item['noticeUrl']
        #         content_html = requests.get(item['noticeUrl']).content.decode('utf-8')
        #     print(content_html)
        #     content_lxml = lxml.etree.HTML(content_html)
        #     content_table = content_lxml.xpath(
        #         '//div[@class="w980 center cmain"]//div/text() | //div[@class="ccontent center"]//p/text()')
        #     print(content_table)
        #     item['noticeContent'] = []
        #     for j, p in enumerate(content_table):
        #         # p = p.xpath('string(.)')
        #         # print('p:::::',p)
        #         p = p.replace('\xa0', ' ')
        #         p = p.replace('\u3000', ' ').strip()
        #         item['noticeContent'].append(p)
        #     print(item['noticeContent'])
        # else:
        #     print(str(now), '______', str(item['noticeDate']))
        #     continue
            #========================发送邮件=========================

            # item['noticeContent']='了解内容详情请点击链接'
            # sendmail.process_item(item)
    browser.close()
#====================================================
#=====================浙江科技========================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://kjt.zj.gov.cn/col/col1229080140/index.html") #
    page.wait_for_timeout(3000)
    content = page.content()
    soup = BeautifulSoup(content, "html.parser")
    # print(soup)
    # for t in soup.select(".title"):
    #     print(t.text)
    a = soup.select('li>a[href].skipAutoFix')  # 得到一个所有a标签的集合
    for i in range(0, len(a)):  # 遍历所有的a标签
        if len(a[i].text) <= 7:
            continue
        url_content = 'https://kjt.zj.gov.cn'+str(a[i]['href'])
        type_content = '浙江科技政策资讯'
        dateLIST = a[i]['href'].split('/')
        date_content = date(int(dateLIST[2]),int(dateLIST[3]),int(dateLIST[4]))
        if str(now) == str(date_content):
            item['noticeTitle'].append(a[i]['title'])
            item['noticeUrl'].append(url_content)
            item['noticeDate'].append(date_content)
            item['noticeType'].append(type_content)
        # print(item['noticeDate'])
        #========================发送邮件=========================
        # item['noticeContent']='了解内容详情请点击链接'
    browser.close()
sendmail.process_item(item)

##====================================================
##=====================浙江科技========================