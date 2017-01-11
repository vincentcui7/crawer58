from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info3']
# spider 1

def get_links_from(channel,pages,who_sells=1):
    # http://bj.58.com/shouji/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):                  # 判断是否有标题，有标题才爬
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass                                 # 没有标题，就不爬
        # Nothing!

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script',type='text/javascript').get('src').split('/')
    if no_longer_exist:                      # 在大规模抓取中，之前爬取的商品链接有可能因为交易完成而失效，所以爬取商品详情前必须先判断是否404页面，防止程序中途报错
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d a')[0].stirpped_strings) if soup.find_all('span','c_25d') else None
        item_info.insert_one({'title':title,'price':price,'date':date,'area':area})
        print({'title':title,'price':price,'date':date,'area':area})

# get_item_info('http://bj.58.com/shouji/27581195128625x.shtml')
