import customtkinter as ctk
import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image


class LoginScreen:
    def __init__(self):
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')


        self.root = ctk.CTk()
        self.root.geometry('450x550+430+90')
        self.root.title('Login')
        self.root.resizable(False, False)

        # Imported images
        bg_image = ImageTk.PhotoImage(Image.open('assets/pattern.png'))

        # Text fonts
        self.font1 = Font(family='@Batang', size=22, weight='bold', slant='roman', underline=False)
        self.font2 = Font(family='@KaiTi', size=8, weight='bold')
        self.font3 = Font(family='@KaiTi', size=8, weight='bold', underline=True, slant='italic')

        # Background image setup
        self.bg_label = ctk.CTkLabel(self.root, image=bg_image)
        self.bg_label.pack()

        # Frame setup
        self.frame = ctk.CTkFrame(self.bg_label, width=320, height=360, corner_radius=20)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Log into Label
        self.login_label = tk.Label(self.root, text='Login', font=self.font1, bg='#2b2b2b', fg='white')
        self.login_label.place(x=180, y=105)

        # User entry
        self.user_entry = ctk.CTkEntry(self.root, width=220, placeholder_text='Username')
        self.user_entry.place(x=112, y=175)

        # Password entry
        self.password_entry = ctk.CTkEntry(self.root, width=220, placeholder_text='Password')
        self.password_entry.place(x=112, y=230)

        # Show password checkbox

        self.checkbox = ctk.CTkCheckBox(self.root, bg_color='#38343c', text='',border_width=1, width=2,
                                        height=2, checkbox_width=18, checkbox_height=18, command=self.show_password)
        self.checkbox.place(x=305, y=235)
        self.password_entry.configure(show='*')

    def show_password(self):
        value = self.checkbox.get()
        if value:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')

    def run(self):
        self.root.mainloop()

app = LoginScreen()
app.run()
