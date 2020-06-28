class employee:
          def __new__(cls):
                    print("__new__()")
                    inst=object.__new__(cls)
                    return inst
          def __init__(self):
                    print("__init__()")
                    self.name="kiran"
                    self.salary=10000
          def __str__(self):
                return "name= "+self.name + " salary= "+str(self.salary)

                    
e1=employee()

print(e1)
print(e1.name)
