from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)

if __name__ == '__main__':
    pool = Pool()                              # 创建进程池，每个进程占用一个cpu核心，目前是自动分配
    pool.map(get_all_links_from,channel_list.split())      # 把函数放到进程池里
