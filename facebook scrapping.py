import http.cookiejar
import urllib.request
import requests
import bs4
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

authentication_url ="https://m.facebook.com/login.php"
payload = {
    'email':"",
    'pass':""
}
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
#print(contents)

url = "https://mbasic.facebook.com/arjun.bist.10048379/friends?lst=100031039264400%3A100031039264400%3A1544535110&refid=17"
t=0
z=0
c=0
m=1
j=1
k=0
num=0
while True:
    data = requests.get(url,cookies=cj)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    if soup.find("div",{"id":"m_more_friends"})==None:
        t=1
        
        
    for i in soup.find_all('a'):
        
        if z==1 and m==2:
            c=1
            if(j<=1):
                j=j+1
                continue
        if z==1 and m==1:
            c=1
            if(j<=9):
                j=j+1
                continue
        if i.text.lower()=="menu":
            z=1
            continue
        if i.text.lower()=="see more friends":
            break
            
        if c==1:
            if i.text.lower()=="ਪੰਜਾਬੀ":
                break
            print(i.text)
            data2 = requests.get("https://mbasic.facebook.com"+i['href'],cookies=cj)
            soup2 = bs4.BeautifulSoup(data2.text, 'html.parser')
            images = soup2.findAll('a')
            
            for image in images:
                try:
                    if(image.get('id')[0:3]=="u_0"):
                        data3 = requests.get("https://mbasic.facebook.com"+image['href'],cookies=cj)
                        soup3 = bs4.BeautifulSoup(data3.text, 'html.parser')
                        kl= soup3.findAll('img')
                        for kl1 in kl:
                            if(k==1):
                                
                                urllib.request.urlretrieve(kl1['src'], str(num) +'.jpg')
                                num=num+1
                                k=k+1
                                break
                            k=k+1
                        
                    if(k==2):
                        k=0
                        break
                except:
                    continue
            
    
    
    if t==1:
        break
    link= soup.find("div",{"id":"m_more_friends"})
    tag=link.a['href']
    tag="https://mbasic.facebook.com"+ tag
    url=tag;
    z=0
    m=2
    c=0
    j=1
    

