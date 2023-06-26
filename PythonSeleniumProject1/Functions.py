def hello():
    print("Hello")
hello()

def Hi(name = "Mohan"):
    print("hi " + name)
Hi("manu")

def sum(a,b):
    result= a+b
    print("Sum is ",result )
sum(10,20)

def Returnsum(a,b):
    """This is the function to return the resultant value to the assigned variable x """
    return a+b
x= Returnsum(1,20)
print(x)


