# file_1=open("file_example.py","wb+") #File creation
# file_1=open("file_example.py","w")
# file_1.write("print('file operation example')")
# file_1.close()

with open("file_example.py","r") as f:  #with
    f1=f.read()
    print(f1)

# from docx2pdf import convert #(example from pip)

# convert("D:\AcademIQ\Documentation\LMS-abstract.docx")
