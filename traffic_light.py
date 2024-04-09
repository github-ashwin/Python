from tkinter import *


traffic_light = Tk()
traffic_light.title("Traffic Signal Simulation")
traffic_light.geometry("1280x720")  # window dimension
traffic_light.resizable(False, False)


my_canvas = Canvas(traffic_light, width=1200, height=700, bg='white') #canvas dimension
my_canvas.pack()


my_canvas.create_rectangle(50, 550, 1150, 650, fill="gray", outline="") #north(top)
my_canvas.create_oval(550, 570, 600, 620, fill="red", outline="")
my_canvas.create_oval(620, 570, 670, 620, fill="yellow", outline="")
my_canvas.create_oval(690, 570, 740, 620, fill="green", outline="")


my_canvas.create_rectangle(50, 50, 1150, 150, fill="gray", outline="") #south(bottom)
my_canvas.create_oval(550, 70, 600, 120, fill="red", outline="")
my_canvas.create_oval(620, 70, 670, 120, fill="yellow", outline="")
my_canvas.create_oval(690, 70, 740, 120, fill="green", outline="")


my_canvas.create_rectangle(1050, 150, 1150, 550, fill="gray", outline="") #east(right)
my_canvas.create_oval(1070, 230, 1120, 280, fill="red", outline="")
my_canvas.create_oval(1070, 300, 1120, 350, fill="yellow", outline="")
my_canvas.create_oval(1070, 370, 1120, 420, fill="green", outline="")


my_canvas.create_rectangle(50, 150, 150, 550, fill="gray", outline="") #west(left)
my_canvas.create_oval(70, 230, 120, 280, fill="red", outline="")
my_canvas.create_oval(70, 300, 120, 350, fill="yellow", outline="")
my_canvas.create_oval(70, 370, 120, 420, fill="green", outline="")

traffic_light.mainloop()