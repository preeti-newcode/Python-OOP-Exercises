#Prime Class 
class prime:
    value=[]
    start=0
    end=0
    def __init__(self,start,end):
        self.start=start
        self.end=end
    
    def findPrime(self):
        for x in range(self.start,self.end+1):
            for y in range(2,x,1):
                if x%y==0:
                    break
            else:
                self.value.append(x)
    
    def output(self):
        return self.value
    

#Main Body
value=input("Enter range to find prime number between them (10 20)\n")
v1,v2=value.split()
v1,v2=int(v1),int(v2)

o=prime(v1,v2)
o.findPrime()
print("Prime Number between",v1,"and",v2,":\n",o.output())
            
