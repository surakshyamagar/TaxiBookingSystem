from tkinter import *
from PIL import Image, ImageTk
import tkinter as ttk
from tkinter import ttk, messagebox

class Dashboard:
        
# from tkinter import Tk, Frame, Label

# class TaxiBookingSystem:
#     def __init__(self):
#         self.window = Tk()
#         self.initialize_window()
#         self.create_header()

#     def initialize_window(self):
#         self.window.title('Taxi Booking System')
#         self.window.geometry("1366x768")
#         self.window.state('zoomed')

#     def create_header(self):
#         header_frame = Frame(self.window, bg='#009df4')
#         header_frame.place(x=300, y=15, width=910, height=50)

#         header_label = Label(header_frame, text='Your Header Text', bg='#009df4', font=('Arial', 12, 'bold'))
#         header_label.pack(expand=True, fill='both')

    def __init__(self, window):
        self.window = window
        self.window.title('Taxi Booking System')
        self.window.geometry("1366x768")
        self.window.state('zoomed')

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=15, width=910, height=50)

        # Correcting the assignment of font attributes
        # self.header.configure(bg="skyblue")
        

        # Add a label for the system name in the header
        system_name_label = Label(self.header, text='Taxi Booking System', font=("", 22, "bold"), bg='#009df4', fg='white')
        system_name_label.place(x=300, y=5)

        # self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=15, width=905, height=120)

        self.logout_text = Button(self.window, text='LOG OUT', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='white', cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=1110, y=27)

        self.Dashboard_text = Button(self.window, text='Dashboard', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='white', cursor='hand2', activebackground='#32cf8e')
        self.Dashboard_text.place(x=300, y=26)

        self.image_frame()
        self.customer_info_frame()

    def image_frame(self):
        self.window.configure(bg="white")

        image_path1 = r"C:\Users\renum\OneDrive\Desktop\r.jpg"
        background_image1 = Image.open(image_path1)
        background_image1 = background_image1.resize((260, 260))

        circular_image1= Image.new('RGBA', (267, 245), (0, 0, 0, 0))
        circular_image1.paste(background_image1, (10, 10))

        circular_photo1 = ImageTk.PhotoImage(circular_image1)

        background_label1 = Label(self.window, image=circular_photo1, background='white')
        background_label1.image = circular_photo1
        background_label1.place(x=29, y=2)

        # Second Image
        image_path2 = r"C:\Users\renum\OneDrive\Desktop\phone.jpeg"  # Add the path to your second image
        background_image2 = Image.open(image_path2)
        background_image2 = background_image2.resize((900, 700))

        circular_image2 = Image.new('RGBA', (8000, 7094), (0, 0, 0, 0))
        circular_image2.paste(background_image2, (10, 10))

        circular_photo2 = ImageTk.PhotoImage(circular_image2)

        background_label2 = Label(self.window, image=circular_photo2, background='white')
        background_label2.image = circular_photo2
        background_label2.place(x=293, y=60)  # Adjust the x-coordinate as needed

   


    def customer_info_frame(self): 
        # Create a new frame for driver information
        customer_info_frame = Frame(self.window)
        customer_info_frame.place(x=42, y=250, width=257, height=522)

        self.customer_Home = Button(customer_info_frame, text="Home", font=("Arial", 14), bg="black", fg="white")
        self.customer_Home.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.customer_Home.place(x=45, y=55)

        self.customer_make_booking = Button(customer_info_frame, text="make booking", font=("Arial", 14), bg="black", fg="white")
        self.customer_make_booking.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.customer_make_booking.place(x=45, y=120)

        self.customer_manage_profile = Button(customer_info_frame, text="manage profile", font=("Arial", 14), bg="black", fg="white")
        self.customer_manage_profile.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.customer_manage_profile.place(x=45, y=175)

         # Insert your image path here
        self.image_path = r"C:\Users\renum\OneDrive\Desktop\logbl.jpg"
        self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image = image.resize((36, 36))
        photo = ImageTk.PhotoImage(image)

        self.image_label = ttk.Label(self.window, image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.place(x=42, y=424)

         
        # Insert your image path here
        self.image_path4 = r"C:\Users\renum\OneDrive\Desktop\home.jpg"
        self.display_image4()

        self.display_image4()

    def display_image4(self):
        image4 = Image.open(self.image_path4)
        image4 = image4.resize((36, 36))
        photo = ImageTk.PhotoImage(image4)

        self.image4_label = ttk.Label(self.window, image=photo)
        self.image4_label.image = photo  # Keep a reference to avoid garbage collection
        self.image4_label.place(x=42, y=305)


    # def booking(self):
    #     self.bodyframe = Frame(self.window, bg='yellow')
    #     self.bodyframe.place(x=205, y=130, width=1200, height=1300)

    #     self.heading = Label(self.bodyframe, text=' BOOK HERE', bg='lightblue', font=('', 13, 'bold'), bd=1)
    #     self.heading.place(x=100, y=50)

    #     label_username = Label(self.window, text="Username:", font=("Courier New", 15, "bold"), fg='Black')
    #     label_username.place(x=300, y=200)
    #     self.entry_username = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
    #     self.entry_username.place(x=600, y=200)

    #     label_Booking_id = Label(self.window, text="Booking id:", font=("Courier New", 15, "bold"), fg='Black')
    #     label_Booking_id.place(x=300, y=250)
    #     self.entry_Booking_id = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
    #     self.entry_Booking_id.place(x=600, y=250)

    #     label_pickup_address = Label(self.window, text="Pickup Address:", font=("Courier New", 15, "bold"), fg='Black')
    #     label_pickup_address.place(x=300, y=300)
    #     self.entry_pickup_address = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
    #     self.entry_pickup_address.place(x=600, y=300)

    #     label_dropoff_address = Label(self.window, text="Dropoff Address:", font=("Courier New", 15, "bold"), fg='Black')
    #     label_dropoff_address.place(x=300, y=350)
    #     self.entry_dropoff_address = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
    #     self.entry_dropoff_address.place(x=600, y=350)

    #     label_pickup_time_and_date = Label(self.window, text="Pickup Time/Date:", font=("Courier New", 15, "bold"), fg='Black')
    #     label_pickup_time_and_date.place(x=300, y=400)
    #     self.entry_pickup_time_and_date = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
    #     self.entry_pickup_time_and_date.place(x=600, y=400)

    #     self.book_text = Button(self.window, text='BOOK', bg='lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command=self.make_booking)
    #     self.book_text.place(x=300, y=450)

    # def make_booking(self):
    #     # Placeholder for the actual booking logic
    #     print("Booking in progress...")


if __name__ == "__main__":
    window = Tk()
    dashboard = Dashboard(window)
    window.mainloop()
    

