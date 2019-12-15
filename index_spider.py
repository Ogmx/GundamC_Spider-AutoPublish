import requests
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import detail_spider
import auto_publish

def get_page_index(pageNo):
    data={
        'pageNo': pageNo,                   #起始页面号
        'month': '',
        'year': '',
        'listType': 'group',
        'groupType': 'groupbypublishdate',
        'navigation': 'pagination',
        'pageLimit': '5',                  #数量
        'numberOfArticles': '1',
        'dateType': 'publishdate',
        'category': 'news',
        'subCategory': 'hot-topics',            #频道，模型：gunpla 、资讯：info 、 游戏：games 、热门话题：hot-topics
        'disableDate': 'true',
        'filterSeriesTags': '',
        'filterSubCategoryTags':'',
        'regionFilters': '',
        'country': 'cn',
        'language': 'zh-cn',
        '_': '1573126892893'
    }
    url='https://cn.gundam.info/bin/gundam/articles/list?'+ urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    n = len(data['data'])
    for i in range(n):
        pub_time = data['data'][i]['heading']
        pub_time = str(pub_time).replace(".","-").split(" ")[0]
        print(pub_time)
        m = len(data['data'][i]['articles'])
        for j in range(m):
            title = data['data'][i]['articles'][j]['title']
            if 'summaryText' in data['data'][i]['articles'][j]:
                shorttitle = data['data'][i]['articles'][j]['summaryText']
            else:
                shorttitle=""
            url = "https://cn.gundam.info"+data['data'][i]['articles'][j]['url']
            picname = "https://cn.gundam.info"+data['data'][i]['articles'][j]['displayImage']
            print("正在处理 :" + data['data'][i]['articles'][j]['title'])
            html = get_page_detil(url)
            parse_page_detail(html,title,shorttitle,picname,pub_time)

            # print(data['data'][i]['articles'][j]['title'])
            # print(data['data'][i]['articles'][j]['url'])
            # print(data['data'][i]['articles'][j]['displayImage'])
            # print(data['data'][i]['articles'][j]['summaryText'])


       # print(len(data['data'][i]['articles']))
           # yield  data['data'][i]['articles'][j]['title']
    # if data and 'articles' in data.keys():
    #     for item in data.get('articles'):
    #         yield item.get('title')

def get_page_detil(url):
    print("正在访问页面数据...")
    response = requests.get(url)
    try:
        if response.status_code==200:
            return response.text
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_detail(html,title,shorttitle,picname,pub_time):
    soup = BeautifulSoup(html,'lxml')
    #title = soup.find_all(attrs={'class':"c-heading_text js-episode-title"})[0].text
    #subtitle = soup.find_all(attrs={'class':"c-articleTitle_mainText c-text js-episode-summary-text"})[0].text
    #for x in soup.find_all('div', attrs={'class': "c-text section",'class':"sw06-gallery parbase section"}):
       # print(x)
    print("正在处理页面数据...")
    data = soup.find_all(attrs={'class': "l-container l-container-align- giflC-detailArticle"})
    data_str = str(data)
    temp = data_str.rfind('<div class="gl01-headingTitle parbase section">')
    data_str = data_str[:temp]
    data_str = data_str.split('<!-- /[GL15] -->', 1)[1]
    data_str = data_str[8:]
    #data_str = data_str.replace('<a class="c-modal_trigger c-gallery_itemLink" href="', '<img src="')
    data_str = data_str.replace('/content/', "https://cn.gundam.info/content/")

    #index = data_str.find('<!-- [GL16] -->')
    #while index != -1:
    #    end = data_str.find('<!-- /[GL16] -->', index)
    #    data_str = data_str[:index] + data_str[end + 17:]
    #    index = data_str.find('<!-- [GL16] -->')
    print("正在发布...")
    auto_publish.auto_publish(title,shorttitle,picname,data_str,pub_time)
    print("发布成功")

def main():
    html = get_page_index(1)
    parse_page_index(html)

if __name__=='__main__':
    main()
