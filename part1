# 考題 for Backend Engineer
# Programming
# Part 1
# Counting
# Given a list of urls, print out the top 3 frequent filenames.
# ex.
# Given
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

filez,top1,z,x=[],[],{},[]
for i in urls:
    filenamez=(i.split('/'))
    filename=filenamez[len(filenamez)-1]
    filez.append(filename)

namelist=list(set(filez))

for i in namelist:
    z[filez.index(i)]=i
    x.append(filez.index(i))

temp=x.sort(reverse=True)
n=0
for ii in x:
    if n <3:
        top1.append([z[ii],ii])
        n+=1
for iii in top1:
    print(iii[0],iii[1])
