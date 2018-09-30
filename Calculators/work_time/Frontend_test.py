from tkinter import *

root = Tk()

pay_now = Label(root, text="Palk praegu")
future_percent = Label(root, text="Soovitud tööaeg (%)")
pay_input = Entry(root)
percent_input = Entry(root)

pay_now.grid(row=0)
future_percent.grid(row=1)

pay_input.grid(row=0, column=1)
percent_input.grid(row=1, column=1)


root.mainloop()
