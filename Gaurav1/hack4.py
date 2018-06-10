def main():
    
    from math import sqrt
    from math import pow
   
    inp=raw_input().split()
    inp=map(int,inp)
    print inp
    n=inp[0]
    c=inp[1]
    f=0
    print n
    print c
    t=list()
    if n>=1 and n<=200  and c>=0 and c<=100000:
        for i in range(0,n):
            temp=raw_input().split()
            temp=map(int,temp)
            if temp[0]>=-10000 and temp[0]<=10000 and temp[1]>=-10000 and temp[1]<=10000 and temp[2]>=0 and temp[2]<=15 and temp[3]>=1 and temp[3]<=200:
                t.append(temp)
            else:
                f=1
                break
        print t
        
        if f==0:
            tree=list()
            count=list()
            counter=0
            for i in range(0,n):
                poss=list()
                for j in range(0,n):
                    if i!=j:
                        if t[j][3]>=t[j][2]:
                           # if sqrt(pow((t[i][0]-t[j][0]),2) + pow((t[i][1]-t[j][1]),2)) <=c:
                            calci=sqrt(pow((t[i][0]-t[j][0]),2) + pow((t[i][1]-t[j][1]),2))
                            print calci
                            if calci<=c:
                                poss.append(j)
                    
                tree.append(poss)
                count.append(len(tree[i])) 
                if count[i]==n-1:
                    counter=counter+1
                               
            
            print tree
            print count
            print counter
                    
              
main()
