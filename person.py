class person:
    c=0
    def __init__(self,a,b,c):
        self.name=a
        self.gender=b
        self.age=c
        person.c = person.c + 1
    def ShowInfo(self):
        print("name:",self.name)
        print("gender:",self.gender)
        print("age:",self.age)
    @classmethod
    def countis(cls):
        print('no. of objects created:',cls.c)
        

