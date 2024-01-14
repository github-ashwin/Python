def greeting(name,age=20,color="black"):
    print("Hello "+name+". You are "+str(age)+" years old")
    print("We heard that you like the color "+color+".")
    print("You will be "+str(age+1)+" years on next birthday.")


name=input("Enter name: ")
name=name.capitalize()
age=int(input("Enter age: "))
color=input("Enter color: ")
color=color.lower()
greeting(name,age,color)
