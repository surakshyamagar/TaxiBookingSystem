import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from PIL import Image, ImageTk



        
class Registraion():

    def __init__(self, root):
        
        self.root = root
        self.root.title("Registration")
        self.root.geometry("500x600+400+100")

        self.connection = sqlite3.connect("crud.db")
        self.connection.commit()

        self.conn = sqlite3.connect("crud.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              firstname TEXT, lastname TEXT, address TEXT, Gender TEXT, mobile INTEGER, email TEXT, password TEXT)''')
        self.conn.commit()


        

        # # Create a frame for the entire registration page
        self.registration_frame_container = tk.Frame(self.root, bg="lightblue")
        self.registration_frame_container.pack(expand=True, fill="both")

        # Create a frame for registration inside the container frame
        self.registration_frame = tk.Frame(self.registration_frame_container, padx=20, pady=20)
        self.registration_frame.place(x=20, y=40, width=700, height=530)

        
        self.header_label = tk.Label(self.root, text="Sign In", font=("Times", 24, "bold"))
        self.header_label.place(x=200, y=57)


        self.First_name = tk.Label(self.root, text="First name", font=("Times",15))
        self.First_name.place(x=30, y=126)

        self.First_name_entry = tk.Entry(self.root, font=("Times",15))
        self.First_name_entry.place(x=150, y=125)

        self.Last_name = tk.Label(self.root, text=" Last name", font=("Times",15))
        self.Last_name.place(x=30, y=165)

        self.Last_name_entry = tk.Entry(self.root, font=("Times",15))
        self.Last_name_entry.place(x=150, y=165)

        self.Address = tk.Label(self.root, text="Address", font=("Times",15))
        self.Address.place(x=30, y=205)
        
        self.Address_entry = tk.Entry(self.root, font=("Times",15))
        self.Address_entry.place(x=150, y=206)



        self.Gender = tk.Label(self.root, text="Gender", font=("Times",15))
        self.Gender.place(x=30, y=244)

        self.Gender_var = tk.StringVar()
        self.Gender_var.set("Male")  # Set default value to Male

        self.Gender_male = tk.Radiobutton(self.root, text="Male", variable=self.Gender_var, value="Male", font=("Times", 15))
        self.Gender_male.place(x=150, y=244)

        self.Gender_female = tk.Radiobutton(self.root, text="Female", variable=self.Gender_var, value="Female", font=("Times", 15))
        self.Gender_female.place(x=250, y=244)

        self.Gender_other = tk.Radiobutton(self.root, text="Other", variable=self.Gender_var, value="Other", font=("Times", 15))
        self.Gender_other.place(x=350, y=244)



        self.Mobile = tk.Label(self.root, text="Mobile.no", font=("Times",15))
        self.Mobile.place(x=30, y=285)

        self.Mobile_entry = tk.Entry(self.root, font=("Times",15))
        self.Mobile_entry.place(x=150, y=285)

        self.Email = tk.Label(self.root, text="Email", font=("Times",15))
        self.Email.place(x=30, y=330)

        self.Email_entry = tk.Entry(self.root, font=("Times",15))
        self.Email_entry.place(x=150, y=330)

        self.Password = tk.Label(self.root, text="Password", font=("Times",15))
        self.Password.place(x=30, y=370)

        self.Password_entry = tk.Entry(self.root, font=("Times",15), show="*")
        self.Password_entry.place(x=150, y=370)

        self.Register_btn = tk.Button(self.root,command=self.create_record, text="Register",font=("Times",15), bg="lightgreen")
        self.Register_btn.place(x=130, y=460)

        self.back_btn = tk.Button(self.root, text="Back", font=("Times",15), bg="lightgreen")
        self.back_btn.place(x=280, y=460)

        # Insert your image path here
        self.image_path = r"C:\Users\renum\OneDrive\Desktop\750.jpg"
        self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image = image.resize((300, 526))
        photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.root, image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.place(x=460, y=40)


    def create_record(self):
        First_name = self.First_name_entry.get()
        Last_name = self.Last_name_entry.get()
        Address = self.Address_entry.get()
        Gender = self.Gender_var.get()
        Mobile = self.Mobile_entry.get()
        Email = self.Email_entry.get()
        Password= self.Password_entry.get()
            
        
        if First_name and Last_name and Address and Gender and Mobile and Email and Password:
            self.cursor.execute('''INSERT INTO users (firstname, lastname, address, Gender, mobile, email, password) VALUES (?,?,?,?,?,?,?)''', (First_name, Last_name, Address, Gender, Mobile, Email, Password))
            self.conn.commit()
            messagebox.showinfo("Success", "Record created successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")



          

if __name__ == "__main__":
    root = tk.Tk()
    Registraion(root)
    root.mainloop()

