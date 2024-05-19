from time import strftime,gmtime
from tkcalendar import DateEntry
from pathlib import Path
import tkinter as tk
from tkinter import messagebox , Canvas, Entry, Button, PhotoImage,ttk, Frame,Scrollbar,Label
import os
import jojo
import ast
import datetime




current_directory = os.getcwd()
relative_path = "All_Assets"


# OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(current_directory, relative_path)
# print(ASSETS_PATH)

ggemail = ""

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(496.0, 27.0, image=self.image_image_1)

        self.image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 395.0, image=self.image_image_2)

        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: self.master.show_sign_up_frame())
        self.button_1.place(x=82.0, y=400.0, width=271.0, height=67.0)

        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, relief="flat" , command=lambda: self.master.show_sign_up_admin_frame())
        self.button_2.place(x=601.0, y=400.0, width=271.0, height=67.0)

        self.image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(505.0, 102.0, image=self.image_image_3)

        self.cairo_city_label = tk.Label(self, text="", font=('Arial', 12), foreground='black')
        self.cairo_city_label.place(x=400, y=160)

        self.london_city_label = tk.Label(self, text="", font=('Arial', 12), foreground='black')
        self.london_city_label.place(x=100, y=160)

        self.abu_dhabi_city_label = tk.Label(self, text="", font=('Arial', 12), foreground='black')
        self.abu_dhabi_city_label.place(x=700, y=160)

        self.cairo_label = tk.Label(self, font=('Arial', 30), foreground='black', background="#E8B4FF")
        self.cairo_label.place(x=400, y=188)

        self.london_label = tk.Label(self, font=('Arial', 30), foreground='black', background="#E8B4FF")
        self.london_label.place(x=100, y=188)

        self.abu_dhabi_label = tk.Label(self, font=('Arial', 30), foreground='black', background="#E8B4FF")
        self.abu_dhabi_label.place(x=700, y=188)

        cairo_city_label = Label(self, text="📌Cairo", font=('Arial', 12), foreground='black')
        cairo_city_label.place(x=400, y=160)

        london_city_label = Label(self, text="📌London", font=('Arial', 12), foreground='black')
        london_city_label.place(x=100, y=160)

        abu_dhabi_city_label = Label(self, text="📌Abu Dhabi", font=('Arial', 12), foreground='black')
        abu_dhabi_city_label.place(x=700, y=160)




        self.time()

    def time(self):
        gmt_time = gmtime()
        cairo_time = (gmt_time.tm_hour + 3) % 24
        cairo_time = cairo_time if cairo_time != 0 else 12
        cairo_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, cairo_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

        london_time = (gmt_time.tm_hour + 1) % 24
        london_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, london_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

        abu_dhabi_time = (gmt_time.tm_hour + 4) % 24
        abu_dhabi_time_str = strftime('%I:%M:%S %p', (1900, 1, 1, abu_dhabi_time, gmt_time.tm_min, gmt_time.tm_sec, 0, 0, 0))

        self.cairo_label.config(text=cairo_time_str)
        self.london_label.config(text=london_time_str)
        self.abu_dhabi_label.config(text=abu_dhabi_time_str)

        self.after(1000, self.time)

class LogInFrameAdmin(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(583.0, 332.0, image=self.image_image_1)

        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png")) #login
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_login_admin_frame() , relief="flat")

        self.entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(623.0, 165.0, image=self.entry_image_1)
        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(564.0, 273.0, image=self.entry_image_2)
        self.entry_2 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))#sign up
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_sign_up_admin_frame(), relief="flat")

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, command= self.log_in , relief="flat")

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.email_text = self.canvas.create_text(222.0, 147.0, anchor="nw", text="Email", fill="#000000", font=("IrishGrover Regular", 30*-1))
        self.password_text = self.canvas.create_text(222.0, 255.0, anchor="nw", text="Password", fill="#000000", font=("IrishGrover Regular", 30*-1))

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=6.0, y=160.0, width=155.0, height=44.0)
        self.entry_1.place(x=314.0, y=140.0, width=622.0, height=48.0)
        self.entry_2.place(x=372.0, y=248.0, width=385.0, height=48.0)
        self.button_2.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_3.place(x=390.0, y=544.0, width=214.0, height=48.0)
    
    def log_in(self):
        global ggemail
        email = self.entry_1.get()
        ggemail = email
        password = self.entry_2.get()
        x = jojo.login("admin",email, password)
        messagebox.showinfo("", x)
        if x == "Login successful!":
          self.master.show_add_trip_frame()
          self.entry_1.delete(0, tk.END)
          self.entry_2.delete(0, tk.END)

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/loginadmin"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)


class SignUpFrameAdmin(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(583.0, 332.0, image=self.image_image_1)

        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png")) #login
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_login_admin_frame(), relief="flat")

        self.entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(623.0, 134.0, image=self.entry_image_1)
        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(623.0, 207.0, image=self.entry_image_2)
        self.entry_2 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_3 = tk.PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(523.5, 276.0, image=self.entry_image_3)
        self.entry_3 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)

        self.entry_image_4 = tk.PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(628.5, 345.0, image=self.entry_image_4)
        self.entry_4 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)

        self.entry_image_5 = tk.PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(468.5, 418.0, image=self.entry_image_5)
        self.entry_5 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))#sign up
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_sign_up_admin_frame(), relief="flat")

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, command= self.sign_up, relief="flat")

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.name_text = self.canvas.create_text(175.0, 112.0, anchor="nw", text="Name", fill="#000000", font=("IrishGrover Regular", 30*-1))
        self.email_text = self.canvas.create_text(175.0, 189.0, anchor="nw", text="Email", fill="#000000", font=("IrishGrover Regular", 30*-1))
        self.password_text = self.canvas.create_text(175.0, 258.0, anchor="nw", text="Password", fill="#000000", font=("IrishGrover Regular", 30*-1))
        self.confirm_password_text = self.canvas.create_text(175.0, 327.0, anchor="nw", text="Confirm Password", fill="#000000", font=("IrishGrover Regular", 30*-1))
        self.phone_text = self.canvas.create_text(176.0, 397.0, anchor="nw", text="Phone", fill="#000000", font=("IrishGrover Regular", 30*-1))

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=6.0, y=160.0, width=155.0, height=44.0)
        self.entry_1.place(x=312.0, y=109.0, width=622.0, height=48.0)
        self.entry_2.place(x=312.0, y=182.0, width=622.0, height=48.0)
        self.entry_3.place(x=331.0, y=251.0, width=385.0, height=48.0)
        self.entry_4.place(x=436.0, y=320.0, width=385.0, height=48.0)
        self.entry_5.place(x=276.0, y=393.0, width=385.0, height=48.0)
        self.button_2.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_3.place(x=390.0, y=544.0, width=214.0, height=48.0)

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/signupadmin"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)
    
    def sign_up(self):
        name = self.entry_1.get()
        email = self.entry_2.get()
        password = self.entry_3.get()
        confirm_password = self.entry_4.get()
        phone = self.entry_5.get()
        x = jojo.signup("admin", email, password, confirm_password, name, phone)
        messagebox.showinfo("", x)
        if x == "Signup successful!":
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_3.delete(0, tk.END)
            self.entry_4.delete(0, tk.END)
            self.entry_5.delete(0, tk.END)
            self.master.show_login_admin_frame()


class AddTrain(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):

        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(582.0, 332.0, image=self.image_image_1)
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_trip_frame() , relief="flat")

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_trip_frame(), relief="flat")

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_train_frame(), relief="flat")

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_train_frame(), relief="flat")

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_ticket_frame(), relief="flat")

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_ticket_frame(), relief="flat")

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(self, image=self.button_image_7, borderwidth=0, highlightthickness=0, command= self.add_train, relief="flat")

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            496.0,
            27.0,
            image=self.image_image_2
        )

      
        

        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.master.show_menu_frame(),
            relief="flat"
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            552.0,
            138.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            459.0,
            210.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.canvas.create_text(
            186.0,
            120.0,
            anchor="nw",
            text="Train Model:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            192.0,
            anchor="nw",
            text="Capacity:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )
    def layout_widgets(self):
        self.canvas.place(x=0, y=0)

        self.button_1.place(x=6.0, y=76.0, width=155.0, height=44.0)
        self.button_2.place(x=6.0, y=148.0, width=155.0, height=44.0)
        self.button_3.place(x=6.0, y=220.0, width=155.0, height=44.0)
        self.button_4.place(x=6.0, y=292.0, width=155.0, height=44.0)
        self.button_5.place(x=6.0, y=364.0, width=155.0, height=44.0)
        self.button_6.place(
            x=6.0,
            y=436.0,
            width=155.0,
            height=44.0
        )

        self.button_7.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.button_8.place(x=6.0, y=508.0, width=155.0, height=44.0)

        self.entry_1.place(x=367.0, y=114.0, width=370.0, height=47.0)
        self.entry_2.place(x=327.0, y=185.0, width=264.0, height=48.0)

    def add_train(self):
        model = self.entry_1.get()
        capacity = self.entry_2.get()
        x = jojo.add_train(model, capacity)
        messagebox.showinfo("", x)
        if x == "Train added successfully!":
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Addtrain"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)

class AddTrip(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    # TO MAKE THE DATA REFRESH FROM DATA BASE (fixed by super awesome youssef)
    def refresh(self):
        self.Start_st['values'] = jojo.get_all_stations()
        self.end_st['values'] = jojo.get_all_stations()
        self.Train_combo['values'] = jojo.get_all_trains()

    def create_widgets(self):
        self.transparent_canvas = Canvas(self, bg="#f0f0f0", height=1080, width=1920, highlightthickness=0)
        self.transparent_canvas.place(x=0, y=0)

        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(582.0, 332.0, image=self.image_image_1)
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_trip_frame() , relief="flat")

        self.image_image_1bf = PhotoImage(file=relative_to_assets("image_1bf.png"))
        self.image_1bf = self.canvas.create_image(582.0,332.0,image=self.image_image_1bf)

        self.image_image_2bf = PhotoImage(file=relative_to_assets("image_2bf.png"))
        self.image_2bf = self.canvas.create_image(496.0,27.0,image=self.image_image_2bf)

        self.button_image_1bf = PhotoImage(file=relative_to_assets("button_1bf.png"))
        self.button_1bf = Button(self.canvas, image=self.button_image_1bf, borderwidth=0, highlightthickness=0, command=self.master.show_profile_frame, relief="flat")
        self.button_1bf.place(x=941.0, y=63.0, width=41.0, height=37.0)

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_trip_frame(), relief="flat")

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_train_frame(), relief="flat")

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_train_frame(), relief="flat")

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_ticket_frame(), relief="flat")

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_ticket_frame(), relief="flat")

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(self, image=self.button_image_7, borderwidth=0, highlightthickness=0, command= self.add_trip, relief="flat")

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = tk.Button(self, image=self.button_image_8, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_menu_frame(), relief="flat")

        self.canvas.create_text(186.0, 120.0, anchor="nw", text="Departure Time:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 192.0, anchor="nw", text="Arrival Time:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 264.0, anchor="nw", text="Start Station:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 333.0, anchor="nw", text="End Station:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 397.0, anchor="nw", text="Train:", fill="#010101", font=("IrishGrover Regular", 30 * -1))

        Meaw = jojo.get_all_trains()
        self.Train_combo = ttk.Combobox(self.canvas, values= Meaw, state="readonly")
        self.Train_combo.place(x=400, y=397.0, width=250.0, height=48.0)

        self.Start_st = ttk.Combobox(self.canvas, values=jojo.get_all_stations(), state="readonly")
        self.Start_st.place(x=400, y=264.0, width=250.0, height=48.0)

        self.end_st = ttk.Combobox(self.canvas, values=jojo.get_all_stations(), state="readonly")
        self.end_st.place(x=400, y=333.0, width=250.0, height=48.0)

        self.departure_date_entry = DateEntry(self.canvas)
        self.departure_date_entry.place(x=420, y=120.0, width=150.0, height=48.0)

        self.arrival_date_entry = DateEntry(self.canvas)
        self.arrival_date_entry.place(x=420, y=192.0, width=150.0, height=48.0)

        self.departure_time_entry = Entry(self.canvas)
        self.departure_time_entry.place(x=600, y=120, width=150, height=40)
        self.departure_time_entry.insert(0, "12:00:00 PM")

        self.arrival_time_entry = Entry(self.canvas)
        self.arrival_time_entry.place(x=600, y=192, width=150, height=40)
        self.arrival_time_entry.insert(0, "12:00:00 PM")

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=6.0, y=76.0, width=155.0, height=44.0)
        self.button_2.place(x=6.0, y=148.0, width=155.0, height=44.0)
        self.button_3.place(x=6.0, y=220.0, width=155.0, height=44.0)
        self.button_4.place(x=6.0, y=292.0, width=155.0, height=44.0)
        self.button_5.place(x=6.0, y=364.0, width=155.0, height=44.0)
        self.button_6.place(x=6.0, y=436.0, width=155.0, height=44.0)
        self.button_7.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.button_8.place(x=6.0, y=508.0, width=155.0, height=44.0)

    def add_trip(self):
        train = self.Train_combo.get()
        start_station = self.Start_st.get()
        end_station = self.end_st.get()
        departure_date = self.departure_date_entry.get()
        arrival_date = self.arrival_date_entry.get()
        departure_time = self.departure_time_entry.get()
        arrival_time = self.arrival_time_entry.get()
        d = ast.literal_eval(train)
        train_id = d['train_id']
        s = ast.literal_eval(start_station)
        start_station_id = s['station_id']
        e = ast.literal_eval(end_station)
        end_station_id = e['station_id']
        dep_time = departure_date + " " + departure_time
        arr_time = arrival_date + " " + arrival_time

        if not all([train, start_station, end_station, departure_date, arrival_date, departure_time, arrival_time]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        x = jojo.add_trip(dep_time, arr_time, train_id, start_station_id, end_station_id)
        messagebox.showinfo("", x)
        if x == "Trip added successfully!":
            self.Train_combo.set('')
            self.Start_st.set('')
            self.end_st.set('')
            self.departure_date_entry.set_date('')
            self.arrival_date_entry.set_date('')
            self.departure_time_entry.delete(0, tk.END)
            self.arrival_time_entry.delete(0, tk.END)


    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Addtrip"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)
    
class AddTicket(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    # TO MAKE THE DATA REFRESH FROM DATA BASE (fixed by super awesome youssef)
    def refresh(self):
        self.Trip_combo_onichan['values'] = jojo.get_all_trips()


    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")

        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(582.0, 332.0, image=self.image_image_1)

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command= self.add_ticket, relief="flat")
        self.button_1.place(x=390.0, y=544.0, width=214.0, height=48.0)

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

       
        self.canvas.create_text(186.0, 155.0, anchor="nw", text="Trip:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        
        self.canvas.create_text(186.0, 285.0, anchor="nw", text="Price:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 213.0, anchor="nw", text="Quantity:", fill="#010101", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(186.0, 343.0, anchor="nw", text="Tier:", fill="#010101", font=("IrishGrover Regular", 30 * -1))

        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_1.place(x=360, y=213.0, width=250.0, height=47.0)


        self.entry_2 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_2.place(x=360, y=285.0, width=250.0, height=47.0)

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_trip_frame(), relief="flat")
        self.button_2.place(x=9.0, y=83.0, width=155.0, height=44.0)

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(self, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_trip_frame(), relief="flat")
        self.button_3.place(x=9.0, y=155.0, width=155.0, height=44.0)

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_train_frame(), relief="flat")
        self.button_4.place(x=9.0, y=227.0, width=155.0, height=44.0)

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_train_frame(), relief="flat")
        self.button_5.place(x=9.0, y=299.0, width=155.0, height=44.0)

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_add_ticket_frame(), relief="flat")
        self.button_6.place(x=9.0, y=371.0, width=155.0, height=44.0)

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(self, image=self.button_image_7, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_edit_ticket_frame(), relief="flat")
        self.button_7.place(x=9.0, y=443.0, width=155.0, height=44.0)

        self.button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = tk.Button(self, image=self.button_image_8, borderwidth=0, highlightthickness=0, command=lambda: self.master.show_menu_frame(), relief="flat")
        self.button_8.place(x=9.0, y=515.0, width=155.0, height=44.0)

        self.Trip_combo_onichan = ttk.Combobox(self.canvas, values=jojo.get_all_trips(), state="readonly")
        self.Trip_combo_onichan.place(x=260, y=155.0, width=250.0, height=47.0)

        self.tier_combo = ttk.Combobox(self, values=["First Class", "Second Class"], font=("Arial", 20))
        self.tier_combo.place(x=322.0, y=343.0, width=250.0, height=47.0)

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)

    def add_ticket(self):
        
        trip = self.Trip_combo_onichan.get()
        trip_dict = {}
        for item in trip.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                trip_dict[key.strip("'")] = value.strip("'")
        trip_id = trip_dict.get('trip_id')
        start_station = trip_dict.get('start_station')
        end_station = trip_dict.get('end_station')
        
     
        price = self.entry_2.get()
        quantity = self.entry_1.get()
        tier = self.tier_combo.get()

        

        if not all([trip, price, quantity, tier]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        x = jojo.add_tickets(quantity, price, tier, start_station, end_station, trip_id)
        
        messagebox.showinfo("", x)
        if x == "Ticket added successfully!":
            self.Trip_combo_onichan.set('')

            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.tier_combo.set('')
    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Addticket"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)

class EditTrip(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    # IAM Awesome
    def refresh(self):
        self.Select_Trip_combo ['values'] = jojo.get_all_trips()
        self.Train_combo['values'] = jojo.get_all_trains()
        self.Start_st['values'] = jojo.get_all_stations()
        self.end_st['values'] = jojo.get_all_stations()


    def create_widgets(self):
        self.transparent_canvas = Canvas(self, bg="#f0f0f0", height=1080, width=1920, highlightthickness=0)
        self.transparent_canvas.place(x=0, y=0)

        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=610,
            width=993,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(582.0, 332.0, image=self.image_image_1)

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_trip_frame(),
            relief="flat"
        )
        #####################################
        self.button_image_1bff = PhotoImage(file=self.relative_to_assets("remove.png"))
        self.button_1bff = Button(self.canvas, image=self.button_image_1bff, borderwidth=0, highlightthickness=0, command=self.deleteTrip, relief="flat")
        self.button_1bff.place(x=650.0, y=544.0, width=141.0, height=44.0)
        #####################################


        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_trip_frame(),
            relief="flat"
        )
        self.canvas.create_rectangle(
            0.0,
            55.0,
            172.0,
            610.0,
            fill="#474747",
            outline="")


        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_train_frame(),
            relief="flat"
        )

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_train_frame(),
            relief="flat"
        )

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_ticket_frame(),
            relief="flat"
        )

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_ticket_frame(),
            relief="flat"
        )

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command= self.edit_trip,
            relief="flat"
        )

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = tk.Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_menu_frame(),
            relief="flat"
        )
        self.canvas.create_text(
            186.0,
            120.0,
            anchor="nw",
            text="New Departure Time:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            69.0,
            anchor="nw",
            text="Select Trip:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            192.0,
            anchor="nw",
            text="New Arrival Time:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            264.0,
            anchor="nw",
            text="New Start Station:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            333.0,
            anchor="nw",
            text="New End Station:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            397.0,
            anchor="nw",
            text="New Train:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )
        
        self.Select_Trip_combo = ttk.Combobox(self, values=jojo.get_all_trips(), state="readonly")
        self.Train_combo = ttk.Combobox(self, values=jojo.get_all_trains(), state="readonly")
        self.Start_st = ttk.Combobox(self, values=jojo.get_all_stations(), state="readonly")
        self.end_st = ttk.Combobox(self, values=jojo.get_all_stations(), state="readonly")
        self.departure_date_entry = DateEntry(self)
        self.arrival_date_entry = DateEntry(self)
        self.departure_time_entry = tk.Entry(self)
        self.arrival_time_entry = tk.Entry(self)
        self.departure_time_entry.insert(0, "12:00:00 PM")
        self.arrival_time_entry.insert(0, "12:00:00 PM")
     
        

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=6.0, y=76.0, width=155.0, height=44.0)
        self.button_2.place(x=6.0, y=148.0, width=155.0, height=44.0)
        self.button_3.place(x=6.0, y=220.0, width=155.0, height=44.0)
        self.button_4.place(x=6.0, y=292.0, width=155.0, height=44.0)
        self.button_5.place(x=6.0, y=364.0, width=155.0, height=44.0)
        self.button_6.place(x=6.0, y=436.0, width=155.0, height=44.0)
        self.button_7.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.button_8.place(x=6.0, y=508.0, width=155.0, height=44.0)

        self.Select_Trip_combo.place(x=380, y=66, width=250.0, height=48.0)
        self.Train_combo.place(x=450, y=397.0, width=250.0, height=48.0)
        self.Start_st.place(x=450, y=264.0, width=250.0, height=48.0)
        self.end_st.place(x=450, y=333.0, width=250.0, height=48.0)
        self.departure_date_entry.place(x=470, y=120.0, width=150.0, height=48.0)
        self.arrival_date_entry.place(x=470, y=192.0, width=150.0, height=48.0)
        self.departure_time_entry.place(x=650, y=120, width=150, height=40)
        self.arrival_time_entry.place(x=650, y=192, width=150, height=40)

    def edit_trip(self):
        
        trip = self.Select_Trip_combo.get()
        trip_dict = {}
        for item in trip.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                trip_dict[key.strip("'")] = value.strip("'")
        trip_id = trip_dict.get('trip_id')
        print(trip_id)
        

  
        new_train = self.Train_combo.get()
        trains = {}
        for item in new_train.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                trains[key.strip("'")] = value.strip("'")
        new_train_id = trains.get('train_id')
        print(new_train_id)

        new_start_station = self.Start_st.get()
        stations = {}
        for item in new_start_station.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                stations[key.strip("'")] = value.strip("'")
        new_start_id = stations.get('station_id')
        print(new_start_id )

        new_end_station = self.end_st.get()
        print(new_end_station)
        stations_e = {}
        for item in new_end_station.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                stations_e[key.strip("'")] = value.strip("'")
        new_end_id = stations_e.get('station_id')
        print(new_end_id)


        new_departure_date = self.departure_date_entry.get()

        new_arrival_date = self.arrival_date_entry.get()
        new_departure_time = self.departure_time_entry.get()
        new_arrival_time = self.arrival_time_entry.get()

        new_arr = new_arrival_date + " " + new_arrival_time
        new_dep = new_departure_date + " " + new_departure_time
        
        t = str(datetime.date.today)
        if new_arr == t + " " + "12:00:00 AM":
            new_arr = None
        if new_dep == t + " " + "12:00:00 AM":
            new_dep = None

        if new_train == "":
            new_train_id = None
        
        if new_start_station == "":
            new_start_id = None
        
        if new_end_station == "":
            new_end_id = None

        print(new_start_id)
        print(new_end_id)
        x = jojo.update_trip(trip_id, new_dep, new_arr,new_train_id , new_start_id, new_end_id)
        messagebox.showinfo("", x)
        self.master.show_edit_trip_frame()
        if x == "Trip edited successfully!":
            self.Select_Trip_combo.set('')
            self.Train_combo.set('')
            self.Start_st.set('')
            self.end_st.set('')
            self.departure_date_entry.set_date('')
            self.arrival_date_entry.set_date('')
            self.departure_time_entry.delete(0, tk.END)
            self.arrival_time_entry.delete(0, tk.END)


    def deleteTrip(self):
            trip = self.Select_Trip_combo.get()
            trip_dict = {}
            for item in trip.strip('{}').split(', '):
                if ':' in item:
                    key, value = item.split(': ')
                    trip_dict[key.strip("'")] = value.strip("'")
            trip_id = trip_dict.get('trip_id')
            if trip_id == None:
                messagebox.showerror("Error", "Please select a trip to delete")
                return
            x = jojo.remove_trip(trip_id)
            messagebox.showinfo("", x)
            self.master.show_edit_trip_frame()
            if x == "Trip deleted successfully!":
                self.Select_Trip_combo.set('')

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Edittrip"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)

class EditTrain(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def refresh(self):
        self.Train_combo['values'] = jojo.get_all_trains()

    def create_widgets(self):
        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=610,
            width=993,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            582.0,
            332.0,
            image=self.image_image_1
        )

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.edit_train,
            relief="flat"
        )


        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            496.0,
            27.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            186.0,
            213.0,
            anchor="nw",
            text="New Train Model:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            187.0,
            141.0,
            anchor="nw",
            text="Train:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            285.0,
            anchor="nw",
            text="New Capacity:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            55.0,
            172.0,
            610.0,
            fill="#474747",
            outline="")

        self.entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            617.0,
            231.5,
            image=self.entry_image_1
        )
        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_2 = tk.PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            522.0,
            303.0,
            image=self.entry_image_2
        )
        self.entry_2 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        #####################################
        self.button_image_1bff = PhotoImage(file=self.relative_to_assets("remove.png"))
        self.button_1bff = Button(self.canvas, image=self.button_image_1bff, borderwidth=0, highlightthickness=0, command=self.deleteTrain, relief="flat")
        self.button_1bff.place(x=650.0, y=544.0, width=141.0, height=44.0)
        #####################################

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_trip_frame(),
            relief="flat"
        )

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_trip_frame(),
            relief="flat"
        )

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_train_frame(),
            relief="flat"
        )

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_train_frame(),
            relief="flat"
        )

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_ticket_frame(),
            relief="flat"
        )

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_ticket_frame(),
            relief="flat"
        )

        self.button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = tk.Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_menu_frame(),
            relief="flat"
        )

        self.Train_combo = ttk.Combobox(self, values=jojo.get_all_trains())

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.entry_1.place(x=432.0, y=207.0, width=370.0, height=47.0)
        self.entry_2.place(x=390.0, y=278.0, width=264.0, height=48.0)
        self.button_2.place(x=9.0, y=83.0, width=155.0, height=44.0)
        self.button_3.place(x=9.0, y=155.0, width=155.0, height=44.0)
        self.button_4.place(x=9.0, y=227.0, width=155.0, height=44.0)
        self.button_5.place(x=9.0, y=299.0, width=155.0, height=44.0)
        self.button_6.place(x=9.0, y=371.0, width=155.0, height=44.0)
        self.button_7.place(x=9.0, y=443.0, width=155.0, height=44.0)
        self.button_8.place(x=9.0, y=515.0, width=155.0, height=44.0)
        self.Train_combo.place(x=270, y=141.0, width=250, height=47.0)

    def edit_train(self):
        train = self.Train_combo.get()
        train_dict = {}
        for item in train.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                train_dict[key.strip("'")] = value.strip("'")
        train_id = train_dict.get('train_id')
        new_model = self.entry_1.get()
        new_capacity = self.entry_2.get()

        if new_capacity == "":
            new_capacity = None
        if new_model == "":
            new_model = None

        if(not new_capacity and not new_model):
            messagebox.showerror("Error", "Please fill in at least one field")
            return
        x = jojo.update_train(train_id, new_model, new_capacity)
        messagebox.showinfo("", x)
        if x == "Train details updated successfully!":
            self.Train_combo.set('')
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
    
    def deleteTrain(self):
        train = self.Train_combo.get()
        train_dict = {}
        for item in train.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                train_dict[key.strip("'")] = value.strip("'")
        train_id = train_dict.get('train_id')
        if train_id==None:
            messagebox.showerror("Error", "Please select a train to delete")
            return
        x = jojo.remove_train(train_id)
        messagebox.showinfo("", x)
        self.master.show_edit_train_frame()
        if x == "Train deleted successfully!":
            self.Train_combo.set('')

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Edittrain"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)


class EditTicket(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def refresh(self):
        self.Trip_combo_onichan['values'] = jojo.get_all_trips()


    def create_widgets(self):
        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=610,
            width=993,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_rectangle(
            0.0,
            55.0,
            172.0,
            610.0,
            fill="#474747",
            outline=""
        )

        self.image_image_1 = tk.PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            582.0,
            332.0,
            image=self.image_image_1
        )
        #####################################
        self.button_image_1bff = PhotoImage(file=self.relative_to_assets("remove.png"))
        self.button_1bff = Button(self.canvas, image=self.button_image_1bff, borderwidth=0, highlightthickness=0, command=self.deleteTicket, relief="flat")
        self.button_1bff.place(x=650.0, y=544.0, width=141.0, height=44.0)
        #####################################

        self.button_image_1 = tk.PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.edit_ticket,
            relief="flat"
        )

        self.image_image_2 = tk.PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            496.0,
            27.0,
            image=self.image_image_2
        )


        self.canvas.create_text(
            186.0,
            155.0,
            anchor="nw",
            text="Trip:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )


        self.canvas.create_text(
            186.0,
            406.0,
            anchor="nw",
            text="Price:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            186.0,
            343.0,
            anchor="nw",
            text="Tier:",
            fill="#010101",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            394.0,
            430.5,
            image=self.entry_image_1
        )
        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.button_image_2 = tk.PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = tk.Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_trip_frame(),
            relief="flat"
        )

        self.button_image_3 = tk.PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = tk.Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_trip_frame(),
            relief="flat"
        )

        self.button_image_4 = tk.PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = tk.Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_train_frame(),
            relief="flat"
        )

        self.button_image_5 = tk.PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = tk.Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_train_frame(),
            relief="flat"
        )

        self.button_image_6 = tk.PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = tk.Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_add_ticket_frame(),
            relief="flat"
        )

        self.button_image_7 = tk.PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = tk.Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_edit_ticket_frame(),
            relief="flat"
        )

        self.button_image_8 = tk.PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = tk.Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.master.show_menu_frame(),
            relief="flat"
        )

        self.Trip_combo_onichan = ttk.Combobox(self, values=jojo.get_all_trips(), font=("Arial", 20))

        self.tier_combo = ttk.Combobox(self, values=["First Class", "Second Class"], font=("Arial", 20))

    def edit_ticket(self):
        trip = self.Trip_combo_onichan.get()
        trip_dict = {}
        for item in trip.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                trip_dict[key.strip("'")] = value.strip("'")
        trip_id = trip_dict.get('trip_id')
   
        price = self.entry_1.get()
        tier = self.tier_combo.get()


        if price == "":
            price = None
        
        if tier == "":
            tier = None

        
        if (not price and not tier):
            messagebox.showerror("Error", "Please fill in at least one field")
            return
        
        x = jojo.update_ticket(trip_id, price, tier)
        messagebox.showinfo("", x)
        if x == "Ticket edited successfully!":
            self.Trip_combo_onichan.set('')
            self.entry_1.delete(0, tk.END)
            self.tier_combo.set('')
        
    def deleteTicket(self):
        trip = self.Trip_combo_onichan.get()
        trip_dict = {}
        for item in trip.strip('{}').split(', '):
            if ':' in item:
                key, value = item.split(': ')
                trip_dict[key.strip("'")] = value.strip("'")
        trip_id = trip_dict.get('trip_id')
        teir = trip_dict.get('tier')

        
        
        if ( trip_id==None):
            messagebox.showerror("Error", "Please enter trip id to delete tickets")
            return
    
        x = jojo.remove_ticket(trip_id , teir)

        messagebox.showinfo("", x)
        self.master.show_edit_ticket_frame()
        if x == "Ticket deleted successfully!":
            self.Trip_combo_onichan.set('')

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.button_1.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.button_2.place(x=9.0, y=83.0, width=155.0, height=44.0)
        self.button_3.place(x=9.0, y=155.0, width=155.0, height=44.0)
        self.button_4.place(x=9.0, y=227.0, width=155.0, height=44.0)
        self.button_5.place(x=9.0, y=299.0, width=155.0, height=44.0)
        self.button_6.place(x=9.0, y=371.0, width=155.0, height=44.0)
        self.button_7.place(x=9.0, y=443.0, width=155.0, height=44.0)
        self.button_8.place(x=9.0, y=515.0, width=155.0, height=44.0)
        self.entry_1.place(x=269.0, y=406.0, width=250.0, height=47.0)
        self.Trip_combo_onichan.place(x=260, y=155.0, width=250.0, height=47.0)
        self.tier_combo.place(x=322.0, y=343.0, width=250.0, height=47.0)

    def relative_to_assets(self, path: str) -> Path:
        current_directory = os.getcwd()
        relative_path = "All_Assets/Editticket"
        ASSETS_PATH = os.path.join(current_directory, relative_path)
        return ASSETS_PATH / Path(path)

class LogInFrameUser(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()
        

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.button_image_1 = PhotoImage(file=relative_to_assets("LGbutton_1.png"))
        self.button_image_2 = PhotoImage(file=relative_to_assets("LGbutton_2.png"))
        self.image_image_1 = PhotoImage(file=relative_to_assets("LGimage_1.png"))
        self.entry_image_1 = PhotoImage(file=relative_to_assets("LGentry_1.png"))

        self.entry_1 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_2 = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), show="*", highlightthickness=0)


        self.button_image_4 = PhotoImage(file=relative_to_assets("LGbutton_4.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0,command=self.log_in  ,relief="flat")

        self.image_image_2 = PhotoImage(file=relative_to_assets("LGimage_2.png"))
        self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_5 = PhotoImage(file=relative_to_assets("LGbutton_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.master.show_sign_up_frame, relief="flat")

        self.button_image_6 = PhotoImage(file=relative_to_assets("LGbutton_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.master.show_login_frame, relief="flat")


    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_image(582.0, 332.0, image=self.image_image_1)
        self.canvas.create_image(615.0, 153.0, image=self.entry_image_1)
        self.entry_1.place(x=304.0, y=128.0, width=622.0, height=48.0)
        self.entry_2.place(x=369.0, y=236.0, width=385.0, height=48.0)
        self.canvas.create_text(218.0, 134.0, anchor="nw", text="Email", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_text(218.0, 243.0, anchor="nw", text="Password", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.canvas.create_rectangle(0.0, 55.0, 172.0, 610.0, fill="#474747", outline="")
        self.button_4.place(x=389.0, y=410.0, width=214.0, height=48.0)
        self.button_5.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_6.place(x=6.0, y=170.0, width=155.0, height=44.0)
    
    def log_in(self):
        global ggemail
        email = self.entry_1.get()
        ggemail = email
        password = self.entry_2.get()
        x = jojo.login("passenger",email, password)
        messagebox.showinfo("", x)
        if x == "Login successful!":
          self.master.show_inventory_frame()
          self.entry_1.delete(0, tk.END)
          self.entry_2.delete(0, tk.END)
        

class SignUpFrameUser(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")
        self.button_image_1 = PhotoImage(file=relative_to_assets("SUbutton_1.png"))
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, relief="flat" , command=self.master.show_login_frame)
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
        self.date_of_birth_entry = Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0) 
        self.button_image_5 = PhotoImage(file=relative_to_assets("SUbutton_5.png"))
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat" , command=self.master.show_sign_up_frame)
        self.button_image_6 = PhotoImage(file=relative_to_assets("SUbutton_6.png"))
        self.button_6 = Button(self, image=self.button_image_6, borderwidth=0, highlightthickness=0, relief="flat" , command=self.sign_up)
        self.image_image_2 = PhotoImage(file=relative_to_assets("SUimage_2.png"))

    def layout_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.button_1.place(x=6.0, y=170.0, width=155.0, height=44.0)
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
        self.canvas.create_text(604.0, 474.0, anchor="nw", text="Age", fill="#000000", font=("IrishGrover Regular", 30 * -1))
        self.date_of_birth_entry.place(x=780.0, y=470.0, width=150.0, height=48.0)
        self.button_5.place(x=6.0, y=90.0, width=158.0, height=44.0)
        self.button_6.place(x=390.0, y=544.0, width=214.0, height=48.0)
        self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

    def sign_up(self):
        name = self.entry_1.get()
        email = self.entry_2.get()
        password = self.entry_3.get()
        confirm_password = self.entry_4.get()
        phone = self.entry_5.get()
        age = self.date_of_birth_entry.get()
        
        gender = self.gender_combo.get()
        x = jojo.signup("passenger", email, password, confirm_password, name, phone , age, gender)
        messagebox.showinfo("", x)
        if x == "Signup successful!":
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_3.delete(0, tk.END)
            self.entry_4.delete(0, tk.END)
            self.entry_5.delete(0, tk.END)
            self.date_of_birth_entry.delete(0, tk.END)
            self.master.show_login_frame()


class Inventory(tk.Frame):
    def __init__(self, master, email=None):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def refresh(self):
        self.reload_inventory_frame()

    def create_widgets(self):
        # self.transparent_canvas = Canvas(self, bg="#f0f0f0", height=1080, width=1920, highlightthickness=0)
        # self.transparent_canvas.place(x=0, y=0)

        
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")


        self.button_image_1 = PhotoImage(file=relative_to_assets("Ibutton_1.png")) #out
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.master.show_menu_frame  ,relief="flat")


        self.image_image_1 = PhotoImage(file=relative_to_assets("Iimage_1.png"))

        # self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        

        self.button_image_4 = PhotoImage(file=relative_to_assets("Ibutton_4.png"))#trip
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat",command=self.master.show_BookTrip_frame)

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        # self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        # self.image_image_1bf = PhotoImage(file=relative_to_assets("image_1bf.png"))
        # self.image_1bf = self.canvas.create_image(582.0,332.0,image=self.image_image_1bf)

        self.image_image_2bf = PhotoImage(file=relative_to_assets("image_2bf.png"))
        self.image_2bf = self.canvas.create_image(496.0,27.0,image=self.image_image_2bf)

        self.button_image_1bf = PhotoImage(file=relative_to_assets("button_1bf.png"))
        self.button_1bf = Button(self.canvas, image=self.button_image_1bf, borderwidth=0, highlightthickness=0, command=self.master.show_profile_frame, relief="flat")
        self.button_1bf.place(x=941.0, y=63.0, width=41.0, height=37.0)
        
        self.button_image_5 = PhotoImage(file=relative_to_assets("Ibutton_5.png"))#inventory
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

        self.button_1.place(x=6.0, y=410.0, width=155.0, height=44.0)
   
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

        self.button_4.place(x=6.0, y=250.0, width=155.0, height=44.0)

        self.button_5.place(x=6.0, y=90.0, width=158.0, height=44.0)
        
        trips = jojo.get_all_users_tickets(ggemail)

        for trip_detail in trips:
            trip_string = ""
            for key, value in trip_detail.items():
                trip_string += f"{key}: {value}\n"
            Label(self.frame, text=trip_string).pack(anchor="w", pady=5)
            buy_button = Button(self.frame, text="Refund Ticket", command=lambda td=trip_detail: self.refund_and_update(td))
            buy_button.pack(anchor="w", pady=5)

        self.transparent_canvas.place(x=277, y=101, width=500, height=500)
        self.scrollbar.pack(side="right", fill="y")
        self.transparent_canvas.create_window((0, 0), window=self.frame, anchor="nw")
        print(trips)
        print(ggemail)
     

        # buy_button.place(x=300)  # Place the "Buy" button at x=430
        self.frame.update_idletasks()
        self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))
        # self.refresh()

    def reload_inventory_frame(self):
        # Clear the current content of the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Get updated trips data
        trips = jojo.get_all_users_tickets(ggemail)
        print(trips)
        print(ggemail)

        # Add updated trip details to the frame
        for trip_detail in trips:
            trip_string = ""
            for key, value in trip_detail.items():
                trip_string += f"{key}: {value}\n"
            Label(self.frame, text=trip_string).pack(anchor="w", pady=5)
            buy_button = Button(self.frame, text="Refund Ticket", command=lambda td=trip_detail: self.refund_and_update(td))
            buy_button.pack(anchor="w", pady=5)

        # Update scrollbar and canvas size
        self.frame.update_idletasks()
        self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))

    def refund_and_update(self, trip_detail):
        jojo.remove_purchase2(trip_detail.get('ticket_id', ''), ggemail)
        self.reload_inventory_frame()




class BookTrip(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def refresh(self):
        # Clear existing widgets in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Fetch the updated trips
        trips = jojo.get_all_trips()

        for trip_detail in trips:
            trip_id = trip_detail['trip_id']
            trip_string = ""
            for key, value in trip_detail.items():
                if key == 'tier' and value is None:
                    value = "Default"
                trip_string += f"{key}: {value}\n"
            Label(self.frame, text=trip_string).pack(anchor="w", pady=5)

            seat_label = Label(self.frame, text="Seat Number:")
            seat_label.pack(anchor="w", pady=5)

            seat_entry = Entry(self.frame)
            seat_entry.pack(anchor="w", pady=5)

            buy_button = Button(self.frame, text="Buy Ticket", command=lambda ti=trip_id, se=seat_entry: self.buy_ticket(ti, se))
            buy_button.pack(anchor="w", pady=5)
        
        self.frame.update_idletasks()
        self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))


    def create_widgets(self):
        global ggemail
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=610, width=993, bd=0, highlightthickness=0, relief="ridge")

        self.button_image_1 = PhotoImage(file=relative_to_assets("BKbutton_2.png")) #out
        self.button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0,command=self.master.show_menu_frame ,relief="flat")

        self.image_image_1 = PhotoImage(file=relative_to_assets("Iimage_1.png"))

        # self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))

        self.button_image_4 = PhotoImage(file=relative_to_assets("BKbutton_5.png"))
        self.button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, relief="flat")

        self.image_image_2 = PhotoImage(file=relative_to_assets("Iimage_2.png"))
        # self.image_2 = self.canvas.create_image(496.0, 27.0, image=self.image_image_2)

        self.button_image_5 = PhotoImage(file=relative_to_assets("BKbutton_1.png")) #inventory
        self.button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: self.master.show_inventory_frame())

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
        self.button_1.place(x=6.0, y=410.0, width=155.0, height=44.0)
        self.button_4.place(x=6.0, y= 250.0, width=158.0, height=44.0)
        self.button_5.place(x=6.0, y=90.0, width=155.0, height=44.0)
    
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

        trips = jojo.get_all_trips()

        self.transparent_canvas.place(x=277, y=101, width=500, height=500)
        self.scrollbar.pack(side="right", fill="y")
        self.transparent_canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        # for trip_detail in trips:
        #     trip_id = trip_detail['trip_id']
        #     trip_string = ""
        #     for key, value in trip_detail.items():
        #         if key == 'tier':
        #             if value == None:
        #               value = "Default"
        #         trip_string += f"{key}: {value}\n"
        #     Label(self.frame, text=trip_string).pack(anchor="w", pady=5)
        #     # Create entry for seat number input
        #     # Label for seat number
        #     seat_label = Label(self.frame, text="Seat Number:")
        #     seat_label.pack(anchor="w", pady=5)

        #     # Entry field for seat number
        #     seat_entry = Entry(self.frame)
        #     seat_entry.pack(anchor="w", pady=5)
        #     # Create button to buy ticket with lambda function to pass trip_id and seat_number
        #     buy_button = Button(self.frame, text="Buy Ticket", command=lambda ti=trip_id, seat_entry=seat_entry: self.buy_ticket(ti, seat_entry))
        #     buy_button.pack(anchor="w", pady=5)
            
        # self.frame.update_idletasks()
        # self.transparent_canvas.config(scrollregion=self.transparent_canvas.bbox("all"))
        self.refresh()
    def buy_ticket(self, trip_id, se):
        # Retrieve seat number input from entry widget
        seat_number = se.get()
        if not seat_number:
            messagebox.showerror("", "Please enter a seat number.")
            return
        print(trip_id)
        print(seat_number)
        print(ggemail)
        # Call the add_purchase2 function with trip_id, ggemail, and seat_number
        x = jojo.add_purchase2(trip_id, ggemail, seat_number)
        # make notification that the ticket has been bought
        messagebox.showinfo("", x)



class Profile(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        user_data = self.get_user_data()
        
        if user_data:
            type , email, name, phone, age , gender = user_data
        else:
            typr , email, name, phone, age , gender = "", "", "", "", "" , ""

        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=610,
            width=993,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1p.png"))
        self.image_1 = self.canvas.create_image(
            496.0,
            27.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2p.png"))
        self.image_2 = self.canvas.create_image(
            496.0,
            332.0,
            image=self.image_image_2
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1p.png"))
        self.entry_bg_1 = self.canvas.create_image(
            454.0,
            102.0,
            image=self.entry_image_1
        )
        self.entry_1 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_1.insert(0, name)

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2p.png"))
        self.entry_bg_2 = self.canvas.create_image(
            454.0,
            175.0,
            image=self.entry_image_2
        )
        self.entry_2 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_2.insert(0, email)

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3p.png"))
        self.entry_bg_3 = self.canvas.create_image(
            354.5,
            244.0,
            image=self.entry_image_3
        )
        self.entry_3 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", show="*", font=("Arial", 20), highlightthickness=0)
        
        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4p.png"))
        self.entry_bg_4 = self.canvas.create_image(
            459.5,
            313.0,
            image=self.entry_image_4
        )
        self.entry_4 = tk.Entry(self, bd=0, bg="#FFFCFC", show="*", fg="#000716", font=("Arial", 20), highlightthickness=0)

        self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_5p.png"))
        self.entry_bg_5 = self.canvas.create_image(
            299.5,
            386.0,
            image=self.entry_image_5
        )
        self.entry_5 = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        self.entry_5.insert(0, phone)

        self.canvas.create_text(
            6.0,
            80.0,
            anchor="nw",
            text="Name",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            6.0,
            157.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            6.0,
            226.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            6.0,
            295.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            7.0,
            365.0,
            anchor="nw",
            text="Phone",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            7.0,
            442.0,
            anchor="nw",
            text="Gender",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.canvas.create_text(
            435.0,
            442.0,
            anchor="nw",
            text="Age",
            fill="#000000",
            font=("IrishGrover Regular", 30 * -1)
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1p.png"))
        self.button_1 = tk.Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = self.update_user_data,
            relief="flat"
        )

        self.gender_combo = ttk.Combobox(self, values=["Male", "Female"], state="readonly" , font=("Arial", 20))
        if gender!= None :
            self.gender_combo.set(gender)
        self.age = tk.Entry(self, bd=0, bg="#FFFCFC", fg="#000716", font=("Arial", 20), highlightthickness=0)
        if age!= None:
            self.age.insert(0, age)

    def layout_widgets(self):
        self.canvas.place(x=0, y=0)
        self.entry_1.place(x=143.0, y=77.0, width=622.0, height=48.0)
        self.entry_2.place(x=143.0, y=150.0, width=622.0, height=48.0)
        self.entry_3.place(x=162.0, y=219.0, width=385.0, height=48.0)
        self.entry_4.place(x=267.0, y=288.0, width=385.0, height=48.0)
        self.entry_5.place(x=107.0, y=361.0, width=385.0, height=48.0)
        self.button_1.place(x=396.0, y=555.0, width=214.0, height=48.0)
        self.gender_combo.place(x=120, y=442, width=300, height=48)
        self.age.place(x=605, y=435, width=300, height=48)

    def get_user_data(self):
        result = jojo.get_user_by_email(ggemail)
        if result:
            type , email, name, phone, age, gender = result
            return type , email, name, phone, age , gender
        else:
            
            return None
        
    def update_user_data(self):
        name = self.entry_1.get()
        email = self.entry_2.get()
        password = self.entry_3.get()
        confirm_password = self.entry_4.get()
        phone = self.entry_5.get()
        age = self.age.get()
        gender = self.gender_combo.get()
        res = self.get_user_data()
        type = res[0]
        if type == 'admin':
            x =jojo.edit_user_details(type ,ggemail, email, password, confirm_password, name, phone , None , None)
        else:
            x =jojo.edit_user_details(type ,ggemail, email, password, confirm_password, name, phone , age , gender)
        messagebox.showinfo("", x)
        if type == 'admin':
            self.master.show_add_trip_frame()
        else:
            self.master.show_inventory_frame()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("993x610")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
                
        
        self.profile_frame = Profile(self)
        self.add_train_frame = AddTrain(self)
        self.inventory_frame = Inventory(self)
        self.BookTrip_frame = BookTrip(self)
        self.add_ticket_frame = AddTicket(self)
        self.add_trip_frame = AddTrip(self)
        self.edit_trip_frame = EditTrip(self)
        self.edit_train_frame = EditTrain(self)
        self.edit_ticket_frame = EditTicket(self)
        self.login_frame = LogInFrameUser(self)
        self.login_admin_frame = LogInFrameAdmin(self)
        self.sign_up_frame = SignUpFrameUser(self)
        self.sign_up_admin_frame = SignUpFrameAdmin(self)
        self.menu_frame = Menu(self)
        
        self.hide_all_frames()
       # self.add_train_frame.pack(fill="both", expand=True)
        self.menu_frame.pack(fill="both" , expand = True)

        
    def show_profile_frame(self):
        self.hide_all_frames()
        self.profile_frame.get_user_data() 
        self.profile_frame.create_widgets()
        self.profile_frame.layout_widgets()
        self.profile_frame.pack(fill="both", expand=True)
    
    def show_sign_up_frame(self):
        self.hide_all_frames()
        self.sign_up_frame.pack(fill="both", expand=True)

    def show_login_frame(self):
        self.hide_all_frames()
        self.login_frame.pack(fill="both", expand=True)

    def show_inventory_frame(self):
        self.hide_all_frames()
        self.inventory_frame.refresh()
        self.inventory_frame.pack(fill="both", expand=True)

    def show_BookTrip_frame(self):
        self.hide_all_frames()
        self.BookTrip_frame.refresh()
        self.BookTrip_frame.pack(fill="both", expand=True)

    def show_sign_up_admin_frame(self):
        self.hide_all_frames()
        self.sign_up_admin_frame.pack(fill="both", expand=True)

    def show_login_admin_frame(self):
        self.hide_all_frames()
        self.login_admin_frame.pack(fill="both", expand=True)

    def show_add_trip_frame(self):
        self.hide_all_frames()
        self.add_trip_frame.refresh()
        self.add_trip_frame.pack(fill="both", expand=True)

    def show_add_train_frame(self):
        self.hide_all_frames()
        self.add_train_frame.pack(fill="both", expand=True)

    def show_add_ticket_frame(self):
        self.hide_all_frames()
        self.add_ticket_frame.refresh()
        self.add_ticket_frame.pack(fill="both", expand=True)

    def show_edit_trip_frame(self):
        self.hide_all_frames()
        self.edit_trip_frame.refresh()
        self.edit_trip_frame.create_widgets()
        self.edit_trip_frame.layout_widgets()
        self.edit_trip_frame.pack(fill="both", expand=True)

    def show_edit_train_frame(self):
        self.hide_all_frames()
        self.edit_train_frame.refresh()
        self.edit_train_frame.create_widgets()
        self.edit_train_frame.layout_widgets()
        self.edit_train_frame.pack(fill="both", expand=True)

    def show_edit_ticket_frame(self):
        self.hide_all_frames()
        self.edit_ticket_frame.refresh()
        self.edit_ticket_frame.create_widgets()
        self.edit_ticket_frame.layout_widgets()
        self.edit_ticket_frame.pack(fill="both", expand=True)

    def show_menu_frame(self):
        self.hide_all_frames()
        self.menu_frame.pack(fill="both", expand=True)

    def hide_all_frames(self):
        for frame in [self.menu_frame, self.sign_up_frame, self.login_frame, self.inventory_frame, self.BookTrip_frame, self.profile_frame , self.sign_up_admin_frame, self.login_admin_frame, self.add_train_frame, self.add_ticket_frame, self.edit_trip_frame, self.edit_train_frame, self.edit_ticket_frame, self.add_trip_frame]:
            frame.pack_forget()




if __name__ == "__main__":
    app = Application()
    app.mainloop()





