                                            # Lists [] : Changes allowed

my_List = ["Goa","kerla"," Goa",245]
print(my_List)
my_List[2]="new Delhi"
print(my_List)
print(len(my_List))

my_List.append("Shimoga")
print(my_List)
my_List.insert(2,"Jaipur")
print(my_List)
my_List.remove("new Delhi")
print(my_List)

del my_List[1]
print(my_List)

my_List.pop(1)
print(my_List)

my_List.reverse()
print(my_List)

my_List2= ["Rohan", "Jio",[1,2,3,4],['a','b','c']]
print(my_List2[1:3])
print(my_List2[3][2])
print(my_List[2] +" "+ my_List2[1])
for val in my_List:
    print(val)

                                        # Tuples () : Changes not allowed

my_Tuple = ("Mango","banana","Grapes")
my_Tuple2 = ("Orange",2, 4, (6,7,8,9),["abc","hjh"])

print(my_Tuple)
print(my_Tuple[1])
print(my_Tuple[-1])
print(my_Tuple[0:1])

for val in my_Tuple:
    print(val)

print(len(my_Tuple))
print(my_Tuple2[4][1])
my_Tuple2[4][1] = "JAI"
print(my_Tuple2)
print(8 in my_Tuple2)
print(2 in my_Tuple2)

                                     # SETS{} : unordered,unindexed,no duplicates allowed

my_SET= {"Tea","coffee","Ice"}
my_SET2 = {"dFS",2,3,('A','B','C')}

print(my_SET)
for val in my_SET:
    print(val)

print("Tea" in my_SET)

my_SET.update(["sugar","Chilli"])
print(my_SET)
my_SET.remove("coffee")
print(my_SET)

# To change list to set
my_List_To_Change = [1,2, "vssg"]
print(my_List_To_Change)
converted_to_Set = set(my_List_To_Change)
print(converted_to_Set)

# UNION | INTERSECTION | SYMMETRIC

A = {'a','b',1,2,3}
B = {'b','c',5,6,8}
print(A.union(B))
print(A|B)

print(A.intersection(B))
print(A&B)

print(A.difference(B))
print(A-B)

# To print unique elements of both Sets
print(A.symmetric_difference(B))

print(A^B)

                                        # Dictionary {K:V}

my_Dict={
    "STD" : 10,
    "Name": "Anu",
    "Score":"95%"
}
print(my_Dict)
print(my_Dict["STD"])
print(my_Dict.get("Name"))
print(my_Dict.values())

for x in my_Dict:
    print(x)
    print(my_Dict[x])

for x,y in my_Dict.items():
    print(x,y)

my_Dict["Name"]="bhoomi"
print(my_Dict)

my_Dict["color"]="white"
print(my_Dict)

my_Dict.pop("color")
print(my_Dict)