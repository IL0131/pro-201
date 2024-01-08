from tkinter import *
window=Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')
def calculate_interest():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)


    result_label.destroy()
    message=Label(result_frame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=55) 
    message.place(x=20,y=40) 
    message.pack()


principle_label=Label(window, text="Enter Principle ($)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principle_label.place(x=20, y=140)

principle_entry=Entry(window, text="", bd=2, width=15)
principle_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter Rate (%)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=163)

rate_entry = Entry(window, text="", bd = 2, width = 15)
rate_entry.place(x=150, y=165)

time_label=Label(window, text="Enter Time (Yrs)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button = Button(window, text="calculate", fg = "black", bg = "cyan", bd = 4, command = calculate_interest)
calculate_button.place(x = 20 , y = 250)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()