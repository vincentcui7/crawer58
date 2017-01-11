import time
from page_parsing import url_list

while True:
    print(url_list.find().count())     #这里的count()是pymongo里的函数，用于记录统计
    time.sleep(5)
