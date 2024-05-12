
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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    583.0,
    332.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    55.0,
    172.0,
    610.0,
    fill="#474747",
    outline="")

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
    y=160.0,
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
    y=90.0,
    width=158.0,
    height=44.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    496.0,
    27.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    625.0,
    165.0,
    image=entry_image_1
)
entry_1 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
entry_1.place(
    x=314.0,
    y=140.0,
    width=622.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    564.5,
    273.0,
    image=entry_image_2
)
entry_2 = Entry( bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)

entry_2.place(
    x=372.0,
    y=248.0,
    width=385.0,
    height=48.0
)

canvas.create_text(
    222.0,
    147.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
)

canvas.create_text(
    222.0,
    255.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("IrishGrover Regular", 30 * -1)
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
    x=458.0,
    y=529.0,
    width=214.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
