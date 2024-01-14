a=5
b=3.14
var="india123"

# print(type(a)) #integer
# print(type(b)) #float
# print(type(var)) #string

#arithmetic operations - PEDMAS concept

v1=16
v2=20
v3=10

# print(v1+v2)
# print(v1-v2)
# print(v1*v2)
# print(v1/v2)
# print(v1%v2)

#relational operator - returns in boolean

# print(v1>v2)
# print(v1<v2)
# print(v1>=v2)
# print(v1<=v2)
# print(v1!=v2)

#logical operator

# print(v1>v2 and v1!=v2)
# print(v1<v2 or v1!=v2)
# print(not(v1>v2))

#conditional statement

# if(v1>v2):
#     print("v1 is greater")
# elif(v1<v2):
#     print("v2 is greater")
# else:
#     print("v1 and v2 are equal")

# if((v1>v2) and (v1>v3)):
#     print("v1 is greatest")
# elif((v2>v1) and (v2>v3)):
#     print("v2 is greatest")
# else:
#     print("v3 is greatest")

# print("Even Range")
# for i in range(2,11,2):
#     print(i)

# print("Odd Range")
# for i in range(1,11,2):
#     print(i)

# i=1
# while i<10:
#     print(i)
#     i+=1

#collection datatypes - list,tuple,dictionaries
#LIST

li = ['Aston Martin','Porsche','Mercedes','BMW','Bentley']
# # print(li)
# # print(li[0:4])
# for i in li:
#     print(i)

#append,insert,pop,remove,del

l2 = ['Rolls Royce','Nissan']
l2[0]='Toyota'
# print(l2)

li.extend(l2) #Concatinates
# print(li)

li.append("Range Rover") #adds to the end of list
# #print(li)

li.insert(7,"Land Rover Defender") #add to particular index
# # print(li)

li.pop() #removes the last item
# #print(li)

li.remove("Bentley") #removes the item using a VALUE
# #print(li)

del(li) #deletes the list
# #print(li)
# var = input("Enter someting: ") #Accepting input from user
# print("User input "+var)

