class MyClass:
    name ="john"

    def __init__(self,name,name2,age):
        self.name = name
        self.age = age
        self.name2 ="Ram"

    def sum(self,a,b):
        print(a+b)
x= MyClass("raghu","",20)
print(x.age)
print(x.name)
print(x.name2)
x.sum(20,40)
# observe the changes post "del " i.e, default name gets printed
del x.name
print(x.name)