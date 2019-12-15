import urllib.error, urllib.request, urllib.parse
import http.cookiejar
from requests_toolbelt import MultipartEncoder
from uuid import uuid4
import  time
import requests
import random
#获取登录后cookie
def get_cookie():
    url = 'https://www.gundamc.com/admin/login.php'
    values={'gotopage':'/admin/index.php','dopost':'login','userid':'admin','pwd':'woshiai9561'}
    postdata = urllib.parse.urlencode(values).encode()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Host':'www.gundamc.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers'}

    #将cookie保存在本地，并命名为cookie.txt
    cookie_filename = 'cookie.txt'
    cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie_aff)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(url, postdata, headers)
    try:
        response = opener.open(request)
    except urllib.error.URLError as e:
        print(e.reason)

    cookie_aff.save(ignore_discard=True, ignore_expires=True)

    # for item in cookie_aff:
    #     print('Name ='+ item.name)
    #     print('Value ='+ item.value)

#使用cookie登陆target_url
def auto_publish(title,shorttitle,picname,maintext,pub_time):
    url = 'https://www.gundamc.com/admin/article_add.php'
    # 加载cookie
    #cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
    #cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    data=MultipartEncoder(
        fields={
            'channelid':'1',
            'dopost':'save',
            'title':title,
            'shorttitle':shorttitle,
            'redirecturl':'',
            'tags':'',
            'weight':'190',
            #'litpic':('filename',''),
            'picname':picname,
            'source':'',
            'writer':'',
            'typeid':'1',                   #频道 1：资讯 、 3：模玩
            'typeid2':'',
            'writer':'',
            'keywords':'',
            'description':'',
            'dede_addonfields':'',
            'remote':'1',
            'autolitpic':'1',
            'sptype':'hand',
            'spsize':'5',
            'body':maintext,
            'voteid':'',
            'notpost':'0',
            'click':str(random.randint(1,100)),
            'sortup':'0',
            'color':'',
            'ishtml':'0',
            'money':'0',
            'arcrank':'0',
            'pubdate':pub_time,
            'filename':'',
            'templet':''
        }
    )
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        #'Cookie':'Hm_lvt_7f241e3bed2c6f19ec03c38631079837=1573556002,1573628782; DedeUserID=1; DedeUserID__ckMd5=f672ab8777fee8ed; DedeLoginTime=1573629094; DedeLoginTime__ckMd5=7a5c166fcb74d210; Hm_lpvt_7f241e3bed2c6f19ec03c38631079837=1573628782; PHPSESSID=bs721tirublie3t2mfdkt45l89; _csrf_name_fc6c04a7=9d75e84c77bf2136cc9c83a6437e3e2a; _csrf_name_fc6c04a7__ckMd5=4e3b5435185a8895',
        #'Cookie': 'Hm_lvt_7f241e3bed2c6f19ec03c38631079837=1573556002; Hm_lpvt_7f241e3bed2c6f19ec03c38631079837=1573556002; PHPSESSID=p8tqo6p8jephh6pjsgv650bo0n; _csrf_name_fc6c04a7=1e3073d56232a53b89e439b0d3323042; _csrf_name_fc6c04a7__ckMd5=c45416154d9eb241',
        'Cookie':'Hm_lvt_7f241e3bed2c6f19ec03c38631079837=1576389330,1576391667; _csrf_name_fc6c04a7=92e3f1e85146f808a82cc4e619dfc35c; _csrf_name_fc6c04a7__ckMd5=2f64ab567e1f7bb6; ENV_GOBACK_URL=%2Fmember%2Fcontent_list.php%3Fchannelid%3D1; PHPSESSID=h9siv5lcglsrphffo64ok0gft5; Hm_lpvt_7f241e3bed2c6f19ec03c38631079837=1576391704; last_vtime=1576391669; last_vtime__ckMd5=5d048f4b8a22af7a; last_vid=admin; last_vid__ckMd5=da542bfa7e984578; DedeUserID=71; DedeUserID__ckMd5=2e8e921c922d3b38; DedeLoginTime=1576392027; DedeLoginTime__ckMd5=bc3d5562a663a35f',
        'Connection': 'keep-alive',
        'Host':'www.gundamc.com',
        'Origin':'https://www.gundamc.com',
        'Referer':'https://www.gundamc.com/admin/article_add.php',
        'Content-Type':data.content_type
    }
    r = requests.post(url,data=data,headers=headers)
    #print(r.text)

#def main():
#    get_cookie()
#    title = "Test"
#    shorttitle="Test_subtitle"
#    picname=""
#    maintext="Test123"
#    for i in range(1):
#        auto_publish(title,shorttitle,picname,maintext)


#if __name__=='__main__':
#    main()
