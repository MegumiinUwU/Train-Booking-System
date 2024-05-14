

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import os
current_directory = os.getcwd()

relative_path = "assets/frame0"


# OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(current_directory, relative_path)
# print(ASSETS_PATH)


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
canvas.create_rectangle(
    0.0,
    55.0,
    172.0,
    610.0,
    fill="#474747",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    582.0,
    332.0,
    image=image_image_1
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
    x=6.0,
    y=76.0,
    width=155.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=6.0,
    y=148.0,
    width=155.0,
    height=44.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=6.0,
    y=220.0,
    width=155.0,
    height=44.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=6.0,
    y=292.0,
    width=155.0,
    height=44.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=390.0,
    y=544.0,
    width=214.0,
    height=48.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    496.0,
    27.0,
    image=image_image_2
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=6.0,
    y=364.0,
    width=155.0,
    height=44.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=6.0,
    y=436.0,
    width=155.0,
    height=44.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=390.0,
    y=544.0,
    width=214.0,
    height=48.0
)


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=6.0,
    y=508.0,
    width=155.0,
    height=44.0
)


canvas.create_text(
    186.0,
    120.0,
    anchor="nw",
    text="Train Model:",
    fill="#010101",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    186.0,
    192.0,
    anchor="nw",
    text="Capacity:",
    fill="#010101",
    font=("IrishGrover Regular", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    552.0,
    138.5,
    image=entry_image_1
)
entry_1 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_1.place(
    x=367.0,
    y=114.0,
    width=370.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    459.0,
    210.0,
    image=entry_image_2
)
entry_2 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_2.place(
    x=327.0,
    y=185.0,
    width=264.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
