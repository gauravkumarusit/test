
n=input("enter value of n \n")
m=input("enter value of m \n")
if (n>0 and n<20 and m>0 and m<20):
    l=list()
    r=list()
    x=list()
    sum=0
    for i in range(0,n):
        p=raw_input("enter %d th sequence of length %d"%(i,m))
        l.append(p)   
    print l
    s2=" "
    for s3 in range(0,n):
        
        s4=list(l[s3])
        print s4
        s5=s2.join(s4)
        l[s3]=s5
        
            
    print l
    mycount=1
    
    
    
    for k in range(0,n):
        mycount=1
        while (mycount>0):
            mycount=0
            for i in range(0,n):
                r=list()
                for j in range(0,(2*m-1)):
                    print ("vlaue of l[%d][%d] is %s"%(i,j,l[i][j]))
                    if l[i][j]=="1":
                        r.append(j)
                        print r
                if len(r)==k+1:
                        x.extend(r)
                        print x
                        sum=sum+(k+1)*(k+1)
                        mycount=mycount+1
                        print "sum int %d"%sum
                        for y in r:
                            for a in range(0,n):
                                b=l[a].split(" ")
                                b[(y/2)]="0"
                                s=" "
                                c=s.join(b)
                                l[a]=c
                               # sum=sum+(k+1)*(k+1)
                               # print sum
        
    print "sum =%d"%sum
    print l
        
    
    


       
        

    
