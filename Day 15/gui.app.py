# GUI - Graphical User Interface

#Libraries
# #############
# 1. Tkinter
# 2. pyQT
# 3. Turtle


import tkinter as ttk

app = ttk.Tk()
app.title('My App')
app.geometry('600x400')
ttk.Label(app, text = 'A simple Text Label').place(x = 50 , y = 50)
ttk.Label(app, text='heloo').place(x=20,y=30)
app.mainloop()