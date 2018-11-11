# 印出 urls 這個list裡面，檔案出現最多的前三個，並顯示出現次數
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]
# The program should print out
# a.txt 3
# b.txt 2
# c.jpg 2

filez,top1,=[],[]
for i in urls:
    filenamez=(i.split('/'))
    filename=filenamez[len(filenamez)-1]
    filez.append(filename)

namelist=list(set(filez))
for ii in namelist:
    top1.append({'檔名':ii,'countz':filez.count(ii)})
ccccc = sorted(top1, key=lambda d: d['countz'], reverse=True)
z=0
for iii in ccccc:
    if z<3:
        print(iii['檔名'],iii['countz'])
    z+=1