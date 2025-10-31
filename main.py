from tkinter import *

FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file= "password_manager/assets/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="ew", columnspan=2)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry()
email_entry.grid(column=1, row=2, sticky="ew", columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="we")

password_gen_button = Button(text="Generate Password", fg="#0000CD", bg="#F0FFFF", font=(FONT_NAME, 10, "bold"))
password_gen_button.grid(column=2, row=3, padx=5)

add_button = Button(text="Add", fg="#006400", bg="#98FB98", font=(FONT_NAME, 10, "bold"))
add_button.grid(column=1, row=4, sticky="ew", columnspan=2)








































window.mainloop()