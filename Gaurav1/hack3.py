n=input("enter value of n \n")
eot=list()
m=list()
z=list()
comat=list()

lent=raw_input("enter length of %d salmons"%(n)).split()
sot=raw_input("enter time of %d salmon"%(n)).split()

lent = map(int, lent)
sot = map(int, sot)

print lent[0]
print lent[1]
print lent[2]
print sot

for i in range(0,n) :
 temp=lent[i]+sot[i]
 eot.append(temp)

print eot
mini=min(sot)
maxi=max(eot)

print mini
print maxi

for i in range(mini,maxi+1):
    print i
    z=list()
    for j in range(0,n):
        if i>=sot[j] and i<=eot[j] :
            z.append(j)
        
    print z
    comat.append(z)  
print comat 

corr=list()
corrlen=list()

for i in range(0,maxi-mini+1):
    for j in range(0,maxi-mini+1):
        temp=list(set(comat[i]) | set(comat[j]))
        corr.append(temp)
        corrlen.append(len(temp))

print corr
print corrlen
print max(corrlen)
     
    
    

    
    
         
            
        
    







    
    
        