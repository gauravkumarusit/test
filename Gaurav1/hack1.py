def main():

    def minimum (x,*y):
        m=[x]
        for i in y:
            m.append(i)
      #  print m   
        m.sort()
      #  print m  
        mini=min(m)
        return mini   
    
    
    b=input("enter value for blue\n")
    g=input("enter value for green\n")
    r=input("enter value for red\n")
    y=input("enter value for yellow\n")
    print b,g,r,y
    
    mini=minimum(b,g,r,y)
    sum=mini*4
    d={"blue":b,"green":g,"red":r,"yellow":y}
    o=min(d, key=lambda k: d[k])
    #print  "this is minimum %s"%o
    
    if o=="red":
        if r!=0:
            sum=sum+b+g-2*mini
        else:
            sum=sum+b-mini
    elif o=="yellow":
        sum=sum+b+g+1-2*mini
    elif o=="blue":
        mini2=minimum(r-mini,g-mini,y-mini)
        sum=sum+minimum(r-mini,g-mini,y-mini)*3
        d1={"green":g,"red":r,"yellow":y}
        o1=min(d1, key=lambda k: d[k])
        if o1=="red":
            sum=sum+0
        elif o1=="yellow":
            if r!=0:
                sum=sum+g-mini-mini2+1
        elif o1=="green":
            sum=sum+minimum(r-mini-mini2,y-mini-mini2)*2
            d2={"red":r,"yellow":y}
            o2=min(d2, key=lambda k: d[k])
            if o2=="red":
                sum=sum+0
            elif (o2=="yellow" and (r-mini-mini2)!=0):
                sum=sum+1
                
    elif o=="green":
        mini2=minimum(b-mini,r-mini,y-mini)
        sum=sum+minimum(b-mini,r-mini,y-mini)*3
        d1={"blue":b,"red":r,"yellow":y}
        o1=min(d1, key=lambda k: d[k])
        if o1=="red":
            sum=sum+b-mini-mini2
        elif o1=="yellow":
            sum=sum+b-mini-mini2+1
        elif o1=="blue":
            sum=sum+minimum(r-mini-mini2,y-mini-mini2)*2
            d2={"red":r,"yellow":y}
            o2=min(d2, key=lambda k: d[k])
            if o2=="red":
                sum=sum+0
            elif (o2=="yellow" and (r-mini-mini2)!=0):
                sum=sum+1            
        
            
              
    print sum        
        
main()        
    

    
    
    


    
 





