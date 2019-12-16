def lowest(a, b):    
  n=min(len(a),len(b))
  for i in range(n):  
    if(a[i]!=b[i]):  
      return a[:i]  
  else:  
    return a[:n] 

def getAns(d):
  r=""  
  n = len(d) 
  for i in range(n):  
    for j in range(i+1,n):  
      x = lowest(d[i:n],d[j:n]) 
      if(len(x) > len(r)):  
        r=x;
  return r  

fin=open("whereami.in")
fin.readline()
thing=fin.readline().rstrip()
fin.close()

x=len(getAns(thing))
fout=open("whereami.out", "w")
fout.write(str(x+1)+"\n")
fout.close()
