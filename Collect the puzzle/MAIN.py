# from tkcalendar import DateEntry
# from pathlib import Path
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk, Frame

# import os
# current_directory = os.getcwd()
# relative_path = "All_Assets"


# # OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = os.path.join(current_directory, relative_path)
# # print(ASSETS_PATH)


# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)


# def SignUp(root):
#     window = root
#     canvas = Canvas(
#         window,
#         bg = "#FFFFFF",
#         height = 610,
#         width = 993,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge"
#     )

#     canvas.place(x = 0, y = 0)
#     canvas.create_rectangle(
#         0.0,
#         55.0,
#         172.0,
#         610.0,
#         fill="#474747",
#         outline="")

#     button_image_1 = PhotoImage(
#         file=relative_to_assets("SUbutton_1.png"))
#     button_1 = Button(
#         image=button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: LogIn(root),
#         relief="flat"
#     )
#     button_1.place(
#         x=6.0,
#         y=170.0,
#         width=155.0,
#         height=44.0
#     )

#     button_image_2 = PhotoImage(
#         file=relative_to_assets("SUbutton_2.png"))
#     button_2 = Button(
#         image=button_image_2,
#         borderwidth=0,
#         highlightthickness=0,

#         relief="flat"
#     )
#     button_2.place(
#         x=6.0,
#         y=250.0,
#         width=155.0,
#         height=44.0
#     )

#     button_image_3 = PhotoImage(
#         file=relative_to_assets("SUbutton_3.png"))
#     button_3 = Button(
#         image=button_image_3,
#         borderwidth=0,
#         highlightthickness=0,

#         relief="flat"
#     )
#     button_3.place(
#         x=6.0,
#         y=330.0,
#         width=155.0,
#         height=44.0
#     )

#     button_image_4 = PhotoImage(
#         file=relative_to_assets("SUbutton_4.png"))
#     button_4 = Button(
#         image=button_image_4,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_4 clicked"),
#         relief="flat"
#     )
#     button_4.place(
#         x=6.0,
#         y=410.0,
#         width=155.0,
#         height=44.0
#     )

#     image_image_1 = PhotoImage(
#         file=relative_to_assets("SUimage_1.png"))
#     image_1 = canvas.create_image(
#         582.0,
#         332.0,
#         image=image_image_1
#     )

#     entry_image_1 = PhotoImage(
#         file=relative_to_assets("SUentry_1.png"))
#     entry_bg_1 = canvas.create_image(
#         623.0,
#         134.0,
#         image=entry_image_1
#     )
#     entry_1 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         highlightthickness=0
#     )
#     entry_1.place(
#         x=312.0,
#         y=109.0,
#         width=622.0,
#         height=48.0
#     )

#     entry_image_2 = PhotoImage(
#         file=relative_to_assets("SUentry_2.png"))
#     entry_bg_2 = canvas.create_image(
#         623.0,
#         207.0,
#         image=entry_image_2
#     )
#     entry_2 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         highlightthickness=0
#     )
#     entry_2.place(
#         x=312.0,
#         y=182.0,
#         width=622.0,
#         height=48.0
#     )

#     entry_image_3 = PhotoImage(
#         file=relative_to_assets("SUentry_3.png"))
#     entry_bg_3 = canvas.create_image(
#         523.5,
#         276.0,
#         image=entry_image_3
#     )
#     entry_3 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         show="*",
#         highlightthickness=0
#     )
#     entry_3.place(
#         x=331.0,
#         y=251.0,
#         width=385.0,
#         height=48.0
#     )

#     entry_image_4 = PhotoImage(
#         file=relative_to_assets("SUentry_4.png"))
#     entry_bg_4 = canvas.create_image(
#         628.5,
#         345.0,
#         image=entry_image_4
#     )
#     entry_4 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         show="*",
#         highlightthickness=0
#     )
#     entry_4.place(
#         x=436.0,
#         y=320.0,
#         width=385.0,
#         height=48.0
#     )

#     entry_image_5 = PhotoImage(
#         file=relative_to_assets("SUentry_5.png"))
#     entry_bg_5 = canvas.create_image(
#         468.5,
#         418.0,
#         image=entry_image_5
#     )
#     entry_5 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         highlightthickness=0
#     )
#     entry_5.place(
#         x=276.0,
#         y=393.0,
#         width=385.0,
#         height=48.0
#     )

#     canvas.create_text(
#         175.0,
#         112.0,
#         anchor="nw",
#         text="Name",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_text(
#         175.0,
#         189.0,
#         anchor="nw",
#         text="Email",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_text(
#         175.0,
#         258.0,
#         anchor="nw",
#         text="Password",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_text(
#         175.0,
#         327.0,
#         anchor="nw",
#         text="Confirm Password",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_text(
#         176.0,
#         397.0,
#         anchor="nw",
#         text="Phone",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_rectangle(
#         0.0,
#         55.0,
#         172.0,
#         610.0,
#         fill="#474747",
#         outline=""
#     )

#     canvas.create_text(
#         176.0,
#         474.0,
#         anchor="nw",
#         text="Gender",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     gender_combo = ttk.Combobox(canvas, values=["Male", "Female"], state="readonly")
#     gender_combo.place(x=285.0, y=470.0, width=250.0, height=48.0)

#     canvas.create_text(
#         604.0,
#         474.0,
#         anchor="nw",
#         text="Date of Birth",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     date_of_birth_entry = DateEntry(canvas)
#     date_of_birth_entry.place(x=780.0, y=470.0, width=150.0, height=48.0)

#     button_image_5 = PhotoImage(
#         file=relative_to_assets("SUbutton_5.png"))
#     button_5 = Button(
#         image=button_image_5,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_5 clicked"),
#         relief="flat"
#     )
#     button_5.place(
#         x=6.0,
#         y=90.0,
#         width=158.0,
#         height=44.0
#     )

#     button_image_6 = PhotoImage(
#         file=relative_to_assets("SUbutton_6.png"))
#     button_6 = Button(
#         image=button_image_6,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_6 clicked"),
#         relief="flat"
#     )
#     button_6.place(
#         x=390.0,
#         y=544.0,
#         width=214.0,
#         height=48.0
#     )

#     image_image_2 = PhotoImage(
#         file=relative_to_assets("SUimage_2.png"))
#     image_2 = canvas.create_image(
#         496.0,
#         27.0,
#         image=image_image_2
#     )
#     window.resizable(False, False)
#     window.mainloop()


# def LogIn(window):
    

#     canvas = Canvas(
#         window,
#         bg = "#FFFFFF",
#         height = 610,
#         width = 993,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge"
#     )

#     canvas.place(x = 0, y = 0)
#     canvas.create_rectangle(
#         0.0,
#         55.0,
#         172.0,
#         610.0,
#         fill="#474747",
#         outline="")

#     button_image_1 = PhotoImage(
#         file=relative_to_assets("LGbutton_1.png"))
#     button_1 = Button(
#         image=button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_1 clicked"),
#         relief="flat"
#     )
#     button_1.place(
#         x=6.0,
#         y=250.0,
#         width=155.0,
#         height=44.0
#     )

#     button_image_2 = PhotoImage(
#         file=relative_to_assets("LGbutton_2.png"))
#     button_2 = Button(
#         image=button_image_2,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_2 clicked"),
#         relief="flat"
#     )
#     button_2.place(
#         x=6.0,
#         y=330.0,
#         width=155.0,
#         height=44.0
#     )

#     button_image_3 = PhotoImage(
#         file=relative_to_assets("LGbutton_3.png"))
#     button_3 = Button(
#         image=button_image_3,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_3 clicked"),
#         relief="flat"
#     )
#     button_3.place(
#         x=6.0,
#         y=410.0,
#         width=155.0,
#         height=44.0
#     )

#     image_image_1 = PhotoImage(
#         file=relative_to_assets("LGimage_1.png"))
#     image_1 = canvas.create_image(
#         582.0,
#         332.0,
#         image=image_image_1
#     )

#     entry_image_1 = PhotoImage(
#         file=relative_to_assets("LGentry_1.png"))
#     entry_bg_1 = canvas.create_image(
#         615.0,
#         153.0,
#         image=entry_image_1
#     )
#     entry_1 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         font=("Arial", 20),
#         highlightthickness=0
#     )
#     entry_1.place(
#         x=304.0,
#         y=128.0,
#         width=622.0,
#         height=48.0
#     )

#     entry_image_2 = PhotoImage(
#         file=relative_to_assets("LGentry_2.png"))
#     entry_bg_2 = canvas.create_image(
#         561.5,
#         261.0,
#         image=entry_image_2
#     )
#     entry_2 = Entry(
#         bd=0,
#         bg="#FFFCFC",
#         fg="#000716",
#         highlightthickness=0,
#         font=("Arial", 20),
#         show="*"
#     )
#     entry_2.place(
#         x=369.0,
#         y=236.0,
#         width=385.0,
#         height=48.0
#     )

#     canvas.create_text(
#         218.0,
#         134.0,
#         anchor="nw",
#         text="Email",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     canvas.create_text(
#         218.0,
#         243.0,
#         anchor="nw",
#         text="Password",
#         fill="#000000",
#         font=("IrishGrover Regular", 30 * -1)
#     )

#     button_image_4 = PhotoImage(
#         file=relative_to_assets("LGbutton_4.png"))
#     button_4 = Button(
#         image=button_image_4,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_4 clicked"),
#         relief="flat"
#     )
#     button_4.place(
#         x=389.0,
#         y=410.0,
#         width=214.0,
#         height=48.0
#     )

#     image_image_2 = PhotoImage(
#         file=relative_to_assets("LGimage_2.png"))
#     image_2 = canvas.create_image(
#         496.0,
#         27.0,
#         image=image_image_2
#     )

#     button_image_5 = PhotoImage(
#         file=relative_to_assets("LGbutton_5.png"))
#     button_5 = Button(
#         image=button_image_5,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_5 clicked"),
#         relief="flat"
#     )
#     button_5.place(
#         x=6.0,
#         y=90.0,
#         width=158.0,
#         height=44.0
#     )

#     button_image_6 = PhotoImage(
#         file=relative_to_assets("LGbutton_6.png"))
#     button_6 = Button(
#         image=button_image_6,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_6 clicked"),
#         relief="flat"
#     )
#     button_6.place(
#         x=6.0,
#         y=170.0,
#         width=155.0,
#         height=44.0
#     )
#     window.resizable(False, False)
#     window.mainloop()
    
    


# root = Tk()
# root.geometry("993x610")
# root.configure(bg = "#FFFFFF")
# SignUp(root)

from tkcalendar import DateEntry
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk, Frame,Scrollbar,Label
import os
current_directory = os.getcwd()
relative_path = "All_Assets"


# OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(current_directory, relative_path)
# print(ASSETS_PATH)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("993x610")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

        self.sign_up_frame = SignUpFrame(self)
        self.login_frame = LogInFrame(self)
        self.inventory_frame = Inventory(self)
        self.BookTrip_frame = BookTrip(self)

        self.sign_up_frame.pack(fill="both", expand=True)

    def show_sign_up_frame(self):
        self.inventory_frame.pack_forget()
        self.login_frame.pack_forget()
        self.BookTrip_frame.pack_forget()
        self.sign_up_frame.pack(fill="both", expand=True)

    def show_login_frame(self):
        self.inventory_frame.pack_forget()
        self.sign_up_frame.pack_forget()
        self.BookTrip_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)


    def show_inventory_frame(self):
        self.sign_up_frame.pack_forget()
        self.login_frame.pack_forget()
        self.BookTrip_frame.pack_forget()
        self.inventory_frame.pack(fill="both", expand=True)
    
    def show_BookTrip_frame(self):
        self.sign_up_frame.pack_forget()
        self.login_frame.pack_forget()
        self.inventory_frame.pack_forget()
        self.BookTrip_frame.pack(fill="both", expand=True)


class SignUpFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.button_image_1 = PhotoImage(file=relative_to_assets("SUbutton_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat" , command=self.master.show_login_frame)
        self.button_image_2 = PhotoImage(file=relative_to_assets("SUbutton_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, relief="flat", command=self.master.show_BookTrip_frame)
        self.button_image_3 = PhotoImage(file=relative_to_assets("SUbutton_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_inventory_frame)
        self.button_image_4 = PhotoImage(file=relative_to_assets("SUbutton_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat")
        self.image_image_1 = PhotoImage(file=relative_to_assets("SUimage_1.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("SUentry_1.png"))
        self.entry_1 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_image_2 = PhotoImage(file=relative_to_assets("SUentry_2.png"))
        self.entry_2 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_image_3 = PhotoImage(file=relative_to_assets("SUentry_3.png"))
        self.entry_3 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)
        self.entry_image_4 = PhotoImage(file=relative_to_assets("SUentry_4.png"))
        self.entry_4 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)
        self.entry_image_5 = PhotoImage(file=relative_to_assets("SUentry_5.png"))
        self.entry_5 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.gender_combo = ttk.Combobox(self, values=["Male", "Female"], state="readonly")
        self.date_of_birth_entry = DateEntry(self)
        self.button_image_5 = PhotoImage(file=relative_to_assets("SUbutton_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat" , command=self.master.show_sign_up_frame)
        self.button_image_6 = PhotoImage(file=relative_to_assets("SUbutton_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, relief="flat")
        self.image_image_2 = PhotoImage(file=relative_to_assets("SUimage_2.png"))

    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.button_1.place(x=6.0, y=170.0, width=155.0, height=44.0)
        self.button_2.place(x=6.0, y=250.0, width=155.0, height=44.0)
        self.button_3.place(x=6.0, y=330.0, width=155.0, height=44.0)
        self.button_4.place(x=6.0, y=410.0, width=155.0, height=44.0)
        self.canvas.create_image(582.0, 332.0, image=self.image_image_1)
        self.canvas.create_image(623.0, 134.0, image=self.entry_image_1)
        self.entry_1.place(x=312.0, y=109.0, width=622.0, height=48.0)
        self.canvas.create_image(623.0, 207.0, image=self.entry_image_2)
        self.entry_2.place(x=312.0, y=182.0, width=622.0, height=48.0)
        self.canvas.create_image(523.5, 276.0, image=self.entry_image_3)
        self.entry_3.place(x=331.0, y=251.0, width=385.0, height=48.0)
        self.canvas.create_image(628.5, 345.0, image=self.entry_image_4)
        self.entry_4.place(x=436.0, y=320.0, width=385.0, height=48.0)
        self.canvas.create_image(468.5, 418.0, image=self.entry_image_5)
        self.entry_5.place(x=276.0, y=393.0, width=385.0, height=48.0)
        self.canvas.create_text(175.0, 112.0, anchor="nw", text="Name", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(175.0, 189.0, anchor="nw", text="Email", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(175.0, 258.0, anchor="nw", text="Password", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(175.0, 327.0, anchor="nw", text="Confirm Password", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(176.0, 397.0, anchor="nw", text="Phone", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        #Edited the Gender (youssef)
        self.canvas.create_text(
            176.0,
            474.0,
            anchor="nw",
            text="Gender",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )
        gender_combo = ttk.Combobox(self.canvas, values=["Male", "Female"], state="readonly")
        gender_combo.place(x=285.0, y=470.0, width=250.0, height=48.0)
        self.canvas.create_text(604.0, 474.0, anchor="nw", text="Date of Birth", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.date_of_birth_entry.place(x=780.0, y=470.0, width=150.0, height=48.0)
        self.button_5.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_6.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.canvas.create_image(496.0, 27.0, image=self.image_image_2)


class LogInFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.button_image_1 = PhotoImage(file=relative_to_assets("LGbutton_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat", command=self.master.show_BookTrip_frame)
        self.button_image_2 = PhotoImage(file=relative_to_assets("LGbutton_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_inventory_frame)
        self.button_image_3 = PhotoImage(file=relative_to_assets("LGbutton_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, relief="flat")
        self.image_image_1 = PhotoImage(file=relative_to_assets("LGimage_1.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("LGentry_1.png"))
        self.entry_1 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_image_2 = PhotoImage(file=relative_to_assets("LGentry_2.png"))
        self.entry_2 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)
        self.button_image_4 = PhotoImage(file=relative_to_assets("LGbutton_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat")

        self.image_image_2 = PhotoImage(file=relative_to_assets("LGimage_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_5 = PhotoImage(file=relative_to_assets("LGbutton_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.master.show_sign_up_frame, relief="flat")

        self.button_image_6 = PhotoImage(file=relative_to_assets("LGbutton_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.master.show_login_frame, relief="flat")


    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.button_1.place(x=6.0, y=250.0, width=155.0, height=44.0)
        self.button_2.place(x=6.0, y=330.0, width=155.0, height=44.0)
        self.button_3.place(x=6.0, y=410.0, width=155.0, height=44.0)
        self.canvas.create_image(582.0, 332.0, image=self.image_image_1)
        self.canvas.create_image(615.0, 153.0, image=self.entry_image_1)
        self.entry_1.place(x=304.0, y=128.0, width=622.0, height=48.0)
        self.canvas.create_image(561.5, 261.0, image=self.entry_image_2)
        self.entry_2.place(x=369.0, y=236.0, width=385.0, height=48.0)
        self.canvas.create_text(218.0, 134.0, anchor="nw", text="Email", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(218.0, 243.0, anchor="nw", text="Password", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        self.button_4.place(x=389.0, y=410.0, width=214.0, height=48.0)
        self.button_5.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_6.place(x=6.0, y=170.0, width=155.0, height=44.0)


class Inventory(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")


        self.button_image_1 = PhotoImage(file=relative_to_assets("Ibutton_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat")


        self.button_image_2 = PhotoImage(file=relative_to_assets("Ibutton_2.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, relief="flat", command=self.master.show_sign_up_frame)


        self.button_image_3 = PhotoImage(file=relative_to_assets("Ibutton_3.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_login_frame)


        self.image_image_1 = PhotoImage(file=relative_to_assets("Iimage_1.png"))

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        

        self.button_image_4 = PhotoImage(file=relative_to_assets("Ibutton_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_BookTrip_frame)

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_5 = PhotoImage(file=relative_to_assets("Ibutton_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat")



        self.transparent_canvas = Canvas(
        self,
        bg="white",  # Adjust as needed
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
        self.scrollbar = Scrollbar(self.transparent_canvas, orient="vertical", command=self.transparent_canvas.yview)
        self.transparent_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame = Frame(self.transparent_canvas, bg="white")


    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.button_1.place(
        x=6.0,
        y=410.0,
        width=155.0,
        height=44.0
    )
        self.button_2.place(
        x=6.0,
        y=90.0,
        width=158.0,
        height=44.0
    )
        self.button_3.place(
        x=6.0,
        y=170.0,
        width=155.0,
        height=44.0
    )
        self.canvas.create_image(
        496.0,
        27.0,
        image=self.image_image_1
        )
        self.canvas.create_image(
            594.0,
            347.0,
            image=self.image_image_2
        )


        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        self.button_4.place(
        x=6.0,
        y=250.0,
        width=155.0,
        height=44.0
    )
        self.button_5.place(
        x=6.0,
        y=330.0,
        width=155.0,
        height=44.0
    )
        
        trips = [
        {"Trip": "112", "From": "Cairo", "To": "Giza", "Price": 50, "Available": 89},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "0000", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 7500},
        
        ]
        self.transparent_canvas.place(x=277, y=101, width=500, height=500)
        self.scrollbar.pack(side="right", fill="y")
        self.transparent_canvas.create_window((0, 0), window=self.frame, anchor="nw")
        for i, trip in enumerate(trips):
            trip_info = f"Trip: {trip['Trip']} From: {trip['From']} To: {trip['To']} Price: {trip['Price']} Available: {trip['Available']}"
            Label(self.frame, text=trip_info).pack(anchor="w", pady=5)  # Add padding between tickets
            buy_button = Button(self.frame, text="Refund Ticket", command=lambda trip=trip: print('A7A'))
            buy_button.pack(anchor="w", pady=5)  # Add padding between tickets
        # buy_button.place(x=300)  # Place the "Buy" button at x=430
        self.frame.update_idletasks()
        self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))



class BookTrip(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")


        self.button_image_1 = PhotoImage(file=relative_to_assets("BKbutton_2.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat")


        self.button_image_2 = PhotoImage(file=relative_to_assets("BKbutton_3.png"))
        self.button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, relief="flat", command=self.master.show_sign_up_frame)


        self.button_image_3 = PhotoImage(file=relative_to_assets("BKbutton_4.png"))
        self.button_3 = Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_login_frame)


        self.image_image_1 = PhotoImage(file=relative_to_assets("Iimage_1.png"))

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        

        self.button_image_4 = PhotoImage(file=relative_to_assets("BKbutton_5.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat")

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_5 = PhotoImage(file=relative_to_assets("BKbutton_1.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_inventory_frame)



        self.transparent_canvas = Canvas(
        self,
        bg="white",  # Adjust as needed
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
        self.scrollbar = Scrollbar(self.transparent_canvas, orient="vertical", command=self.transparent_canvas.yview)
        self.transparent_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame = Frame(self.transparent_canvas, bg="white")


    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.button_1.place(
        x=6.0,
        y=410.0,
        width=155.0,
        height=44.0
    )
        self.button_2.place(
        x=6.0,
        y=90.0,
        width=158.0,
        height=44.0
    )
        self.button_3.place(
        x=6.0,
        y=170.0,
        width=155.0,
        height=44.0
    )
        self.canvas.create_image(
        496.0,
        27.0,
        image=self.image_image_1
        )
        self.canvas.create_image(
            594.0,
            347.0,
            image=self.image_image_2
        )


        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        self.button_4.place(
        x=6.0,
        y=250.0,
        width=155.0,
        height=44.0
    )
        self.button_5.place(
        x=6.0,
        y=330.0,
        width=155.0,
        height=44.0
    )
        
        trips = [
        {"Trip": "112", "From": "Cairo", "To": "Giza", "Price": 50, "Available": 89},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "113", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 75},
        {"Trip": "0000", "From": "Giza", "To": "Alexandria", "Price": 60, "Available": 7500},
        
        ]
        self.transparent_canvas.place(x=277, y=101, width=500, height=500)
        self.scrollbar.pack(side="right", fill="y")
        self.transparent_canvas.create_window((0, 0), window=self.frame, anchor="nw")
        for i, trip in enumerate(trips):
            trip_info = f"Trip: {trip['Trip']} From: {trip['From']} To: {trip['To']} Price: {trip['Price']} Available: {trip['Available']}"
            Label(self.frame, text=trip_info).pack(anchor="w", pady=5)  # Add padding between tickets
            buy_button = Button(self.frame, text="Buy Ticket", command=lambda trip=trip: print('A'))
            buy_button.pack(anchor="w", pady=5)  # Add padding between tickets
        # buy_button.place(x=300)  # Place the "Buy" button at x=430
        self.frame.update_idletasks()
        self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))




if __name__ == "__main__":
    app = Application()
    app.mainloop()




