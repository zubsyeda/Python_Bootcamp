from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=str(km))

window = Tk()
window.title("Miles to Kilometer Converer")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

km_result = Label(text="0")
km_result.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=2, row=3)








window.mainloop()