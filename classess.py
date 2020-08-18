
class employee:

    def __init__(self,name,last,pay):#condturctor __init__,self instane of the class you call it diffrent also
        self.name=name
        self.last=last
        self.pay=pay
        self.email=name+"."+last+"."+"@gmail.com"


n1=employee("rahul","virat",50000000)
#n2=employee()
print(n1.email)
