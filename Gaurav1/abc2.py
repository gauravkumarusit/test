import re

def mat (x,*y):
    sum=x
    for m in y:
        sum=sum+m
    return(sum) 



p=mat(10,20,40)
print p

b="jjjgjgjkgjk  10.54.6.56 lhjlhjh ljjj67   56.4.6.8 hljhjl hlkhh"
u=re.search("(\d+)\.(\d+)\.(\d+)\.(\d+)",b).group()
print u
u=re.search("(\d+)\.(\d+)\.(\d+)\.(\d+)",b).group(2)
print u
u=re.findall("(\d+)\.(\d+)\.(\d+)\.(\d+)",b)
for q in u:
    print q

if p>0 :
    print "positive"
    
elif p<0:
    print "negative"
else:
    print "zero"
    


