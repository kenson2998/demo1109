import requests
from bs4 import BeautifulSoup as BS4
html = 'https://www.ptt.cc/bbs/Beauty/index.html'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
re = requests.get(html, headers = headers)
# • 日期
# • 作者
# • 標題
# • 內文
# • 看板名稱
req=BS4(re.text)
date,auth,title,content,bs=[],[],[],[],''
bs=req.title.text
# for i in (req.find_all('div',attrs={'class':'date'})):
#     date.append(i.text)
z=0
for i in req.find_all('div',attrs={'class':'title'}):
    title.append(i.text)
    try:
        r=requests.get('https://www.ptt.cc/'+i.a.get('href'), headers = headers)
        con=BS4(r.text)
        ccc=con.find_all('meta',content)
        content.append(ccc)
            for i in con.find_all('span',class_="article-meta-value"):
                auth.append(i.text)
    except:
        
        print('pass',z)
    z+=1
print(len(date),len(auth))
for ii in range(len(date)):
    
    print('日期:',date[ii])
    print('作者:',auth[ii])
    print('標題:',title[ii])
    print('內文:',content[ii])
print('看板名稱:',bs)
