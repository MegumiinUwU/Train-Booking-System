



from pathlib import Path

from tkcalendar import DateEntry
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk


import os
current_directory = os.getcwd()
relative_path = "build/assets/frame0"



ASSETS_PATH = os.path.join(current_directory, relative_path)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("993x610")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 610,
    width = 993,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    496.0,
    27.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    496.0,
    332.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    454.0,
    102.0,
    image=entry_image_1
)
entry_1 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_1.place(
    x=143.0,
    y=77.0,
    width=622.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    454.0,
    175.0,
    image=entry_image_2
)
entry_2 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_2.place(
    x=143.0,
    y=150.0,
    width=622.0,
    height=48.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    354.5,
    244.0,
    image=entry_image_3
)
entry_3 = Entry( bd=0, bg="#FFFCFC", fg="#000716", show="*", font=("Arial", 20), highlightthickness=0)
entry_3.place(
    x=162.0,
    y=219.0,
    width=385.0,
    height=48.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    459.5,
    313.0,
    image=entry_image_4
)
entry_4 = Entry( bd=0, bg="#FFFCFC", show="*", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_4.place(
    x=267.0,
    y=288.0,
    width=385.0,
    height=48.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    299.5,
    386.0,
    image=entry_image_5
)
entry_5 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_5.place(
    x=107.0,
    y=361.0,
    width=385.0,
    height=48.0
)

canvas.create_text(
    6.0,
    80.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    6.0,
    157.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    6.0,
    226.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    6.0,
    295.0,
    anchor="nw",
    text="Confirm Password",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    7.0,
    365.0,
    anchor="nw",
    text="Phone",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    7.0,
    442.0,
    anchor="nw",
    text="Gender",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    435.0,
    442.0,
    anchor="nw",
    text="Date of Birth",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=396.0,
    y=555.0,
    width=214.0,
    height=48.0
)

gender_combo = ttk.Combobox( values=["Male", "Female"], state="readonly")
gender_combo.place(x=120, y=442, width=300, height=48)

date_entry = DateEntry( width=300, bg="#FFFCFC", fg="#000716", highlightthickness=0)
date_entry.place(x=605, y=435, width=300, height=48)

window.resizable(False, False)
window.mainloop()
