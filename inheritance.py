class quad:
    def __init__(self,a,b,c,d):
        self.s1=a
        self.s2=b
        self.s3=c
        self.s4=d
    def perimeter(self):
        p=self.s1+self.s2+self.s3+self.s4
        print("perimeter of quadrilateral:",p)

class rect(quad):
    def __init__(self,a,b,c=None,d=None):
        super().__init__(a,b,c,d)
        self.s3=self.s1
        self.s4=self.s2


        

        
        
