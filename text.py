class student:
    me='Abhimanyu'
    def __init__(self,name,regd,mark):
        self.name=name
        self.regd=regd
        self.mark=mark
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.regd,self.mark)
        print(self.brand,self.cpu,self.ram)
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
        def show4(self):
            print(self.brand,self.cpu,self.ram)
    def info(cls):
        return cls.me
        
    
s1=student("abhi",1571,8.6)
s2=student("aks",1571,8.0)
lap1=student.laptop()
lap2=student.laptop()

s1.show()
# print(s1.info())
# print(s1.name,s1.regd)
# print(s2.name,s2.regd,s2.mark)
# print(lap1.brand,lap2.cpu)

