from tkinter import *

root=Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

meaning=Label(root,text="Enter the Word",font=30)
textbox=Entry(root,font=30)
meaning.pack(side=LEFT, padx=(30,10),pady=(10,30))
textbox.pack(side=RIGHT,padx=(10,30),pady=(10,30))

button1= Button(bottomFrame,text="Meaning",fg="red")
button2= Button(bottomFrame,text="Antonym",fg="red")
button3= Button(bottomFrame,text="Synonym",fg="red")

button1.pack(side=LEFT,padx=(20,10),pady=(20,10))
button2.pack(side=LEFT,padx=(20,10),pady=(20,10))
button3.pack(side=LEFT,padx=(20,10),pady=(20,10))

root.mainloop()

