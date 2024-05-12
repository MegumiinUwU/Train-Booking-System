


from time import strftime,gmtime
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

import os
current_directory = os.getcwd()
relative_path = "assets/frame0"


# OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(current_directory, relative_path)
# print(ASSETS_PATH)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def time():
    # Get the current time in GMT
    gmt_time = gmtime()

    # Convert to Cairo time (GMT+2)
    cairo_time = (gmt_time.tm_hour + 3) % 24
    # Convert to 12-hour format
    cairo_time = cairo_time if cairo_time != 0 else 12  # Convert 0 to 12
    cairo_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, cairo_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

    # Get London time (GMT)
    london_time = (gmt_time.tm_hour+1) % 24
    london_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, london_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

    # Get Abu Dhabi time (GMT+4)
    abu_dhabi_time = (gmt_time.tm_hour + 4) % 24
    abu_dhabi_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, abu_dhabi_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

    # Update label texts
    cairo_label.config(text=cairo_time_str)
    london_label.config(text=london_time_str)
    abu_dhabi_label.config(text=abu_dhabi_time_str)

    # Call time() function after 1 second
    window.after(1000, time)

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
    395.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("1111111"),
    relief="flat"
)
button_1.place(
    x=82.0,
    y=400.0,
    width=271.0,
    height=67.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("000000"),
    relief="flat"
)
button_2.place(
    x=601.0,
    y=400.0,
    width=271.0,
    height=67.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    505.0,
    102.0,
    image=image_image_3
)


cairo_font = ('Arial', 30)  


# Adding label to display city names
cairo_city_label = Label(window, text="📌Cairo", font=('Arial', 12), foreground='black')
cairo_city_label.place(x=400, y=160)

london_city_label = Label(window, text="📌London", font=('Arial', 12), foreground='black')
london_city_label.place(x=100, y=160)

abu_dhabi_city_label = Label(window, text="📌Abu Dhabi", font=('Arial', 12), foreground='black')
abu_dhabi_city_label.place(x=700, y=160)


# Adding label to display time in Cairo
cairo_label = Label(window, font=cairo_font, foreground='black',background="#E8B4FF")
cairo_label.place(x=400, y=188)  

# Adding label to display time in London
london_label = Label(window, font=cairo_font, foreground='black',background="#E8B4FF")
london_label.place(x=100, y=188)  

# Adding label to display time in Abu Dhabi
abu_dhabi_label = Label(window, font=cairo_font, foreground='black',background="#E8B4FF")
abu_dhabi_label.place(x=700, y=188)  




window.resizable(False, False)
time()
window.mainloop()
