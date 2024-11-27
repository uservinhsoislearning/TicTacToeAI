import tkinter as tk 
import sys
  
def selection():  
   selection = "You selected the option " + str(radio.get())  
   label.config(text = selection)
   top.quit()
  
top = tk.Tk()  
top.geometry("300x150")  
radio = tk.IntVar()  
lbl = tk.Label(text = "Favourite programming language:")  
lbl.pack()  
R1 = tk.Radiobutton(top, text="C", variable=radio, value=1,  
                  command=selection)  
R1.pack( anchor = tk.W )  
  
R2 = tk.Radiobutton(top, text="C++", variable=radio, value=2,  
                  command=selection)  
R2.pack( anchor = tk.W )  
  
R3 = tk.Radiobutton(top, text="Java", variable=radio, value=3,  
                  command=selection)  
R3.pack( anchor = tk.W)  

label = tk.Label(top)  
label.pack()  
top.mainloop()

print(f"You chose: {radio.get()}")