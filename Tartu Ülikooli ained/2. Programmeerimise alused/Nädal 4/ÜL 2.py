from tkinter import *

raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam, width=1000, height=800) #raami suurus

tahvel.create_polygon(500, 620,
                      640, 390,
                      360, 390,
                      fill="red",
                      outline="black")

tahvel.create_polygon(500, 600,
                      620, 400,
                      380, 400,
                      fill="white",
                      outline="black")


# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()