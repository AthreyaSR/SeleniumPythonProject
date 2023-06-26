if 5 > 3 :
    print("5 is greater than 3")
num = -2

if num > 0:
    print("positive")
elif num == 0 :
    print("number is zero")
else:
    print("negative")

num = [-2,-1,0,1,-2]
for val in num:
    print(val)

city = ["agra", "bombay", "goa"]
num = len(city)

i =0

while i < num:
    i=i+1
print("Number of cities:",i)