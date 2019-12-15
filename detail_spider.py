import requests
import urllib
import json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def get_page_detil():
    url = "https://cn.gundam.info/news/gunpla/news_gunpla_20191101_002.html"
    response = requests.get(url)
    try:
        if response.status_code==200:
            return response.text
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    data = soup.find_all(attrs={'class': "l-container l-container-align- giflC-detailArticle"})
    data_str = str(data)
    temp = data_str.rfind('<div class="gl01-headingTitle parbase section">')
    data_str = data_str[:temp]
    data_str = data_str.split('<!-- /[GL15] -->', 1)[1]
    data_str = data_str[8:]
    data_str = data_str.replace('<a class="c-modal_trigger c-gallery_itemLink" href="','<img src="')
    data_str=data_str.replace('/content/',"https://cn.gundam.info/content/")
    index = data_str.find('<!-- [GL16] -->')
    while index != -1:
        end = data_str.find('<!-- /[GL16] -->',index)
        data_str = data_str[:index]+data_str[end+17:]
        index = data_str.find('<!-- [GL16] -->')
    print(data_str)


def main():
    html = get_page_detil()
    parse_page_detail(html)

if __name__=='__main__':
    main()
