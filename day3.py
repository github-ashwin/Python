# def login(id,password): #def stands for define, used to define a user-defined function
#     print("***CREDENTIALS***")
#     print("Username: "+id)
#     print("Password: "+password)

# un=str(input("Enter username: "))
# pwd=str(input("Enter password: "))
# login(un,pwd)

#built-in function: print(), range()

# def sum(a,b):
#     return a+b
# # a=sum(3,4)
# # print(a)
# print(sum(3,4))

#positional,keyword,default,variable length

# def course(backend,db="MySQL",*frontend):
#     print("frontend: ",frontend)
#     print("backend; ",backend)
#     print("database: ",db)
# course('python','PostgreSQL','html','css','bootstrap')

#MODULE
# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a+b)

# def mul(a,b):
#     print(a+b)

# def div(a,b):
#     print(a+b)

# a=int(input("Enter a number to be divided :"))
# b=int(input("Enter a number: "))

# try:
#     print(a/b)

# except ZeroDivisionError:
#     print("Division by zero not possible")

# except:
#     print("Unexpected error")

# finally:
#     print("Try Again")

# class Cars:
#     def brands(self): #parameter self for object creation
#         print("Porsche")
#         print("Mclaren")
#         print("Dodge")

# obj = Cars()
# obj.brands()

# temp = Cars()
# Cars.brands(temp) #what happens when we call a function

# class Details: #class, object and attributes
#     def __init__(self,name,department):
#         self.n = name
#         self.d = department
#     def Student(self):
#         print("Name: ",self.n," Department: ",self.d)


# obj = Details("Ashwin","Computer Science")
# obj.Student()
