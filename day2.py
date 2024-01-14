#TUPLE - count

tpl = ("ADMIN","TEACHER","STUDENT") #Tuple - similar to list but cannot add, delete or modify the contents - always fixed
# print(type(tpl))
# print(tpl)
# print(tpl[0]) #Accessing the elements of tuple using index number

# print(tpl.count("TEACHER"))

#For modifying tuple : type convert to list -> modify it -> type convert back to tuple
# li = list(tpl)
# print(type(li))

# li.insert(3,"GUEST")
# print(li)

# tpl=tuple(li)
# print(type(tpl))
# print(tpl)

#DICTIONARY -> key:value

df = {'name':['Ashwin'],'course':'BCA','year':2021}

# print(df)
# print(type(df))
# print(df.values()) #print only values
# print(df.keys()) #print only keys
#print(df.items()) #prints the key and values as a tuple inside a list

# print(df['name']) #accessing the values using key
# print(df.get('name')) #accessing the values using get method

# df['name'].append('Tom')
# print(df.get('name'))

# df.update({'year':2023}) #updating an existing item
# print(df)
# df.update({'dur':'3 year'}) #updating and adding and item
# print(df)

# df.pop('dur') #poping the specific item
# print(df)
# df.popitem() #poping the last item
# print(df)

# df.clear() #empty the dictionary
# print(df)
# del df #deleting df
# print(df)