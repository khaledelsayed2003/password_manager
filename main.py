from tkinter import *
from tkinter import messagebox

FONT_NAME = "Courier"
entry_style = {
    "highlightthickness": 1,      
    "highlightbackground": "green", 
    "highlightcolor": "red",      
    "bd": 0,                       
    "font": (FONT_NAME, 10, "bold")
}

# ---------------------------SAVE DATA INTO txt FILE & clear the entry textbox---------------------------------------
def save():
    # get hold of the entry datas.
    website_info = website_entry.get()
    email_info = email_entry.get()
    pass_info = password_entry.get()
    
    # popup message to warn for empty fields.
    if len(website_info) == 0 or len(email_info) == 0 or len(pass_info) == 0:
        warning_message = messagebox.showwarning(title="Oops!....Empty fields!", message="Please don't leave any fields empty!")
    else:
        # popup message to confirm the info.
        is_ok = messagebox.askokcancel(title= website_info, message=(
            f"Please confirm the following details:\n\n"
            f"📧 Email: {email_info}\n"
            f"🔑 Password: {pass_info}\n\n"
            f"Do you want to save this information?"
        ))
    
        if is_ok:
            # save them into txt file.
            with open("password_manager/data.txt", "a") as file:
                file.write(f"{website_info} | {email_info} | {pass_info} \n")
        
            # clear the textbox.
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    
            # restart the cursor focus(reset input fields).
            website_entry.focus()

# ----------------------------UI SETUP-------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file= "password_manager/assets/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(**entry_style)
website_entry.grid(column=1, row=1, sticky="ew", columnspan=2, pady=3)
website_entry.focus()

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry(**entry_style)
email_entry.grid(column=1, row=2, sticky="ew", columnspan=2, pady=3)
email_entry.insert(0, "khaled.elsayed2206@gmail.com")

password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(**entry_style)
password_entry.grid(column=1, row=3, sticky="we", pady=3)

password_gen_button = Button(text="Generate Password", fg="#0000CD", bg="#F0FFFF", font=(FONT_NAME, 10, "bold"))
password_gen_button.grid(column=2, row=3, padx=5)

add_button = Button(text="Add", fg="#006400", bg="#98FB98", command= save, font=(FONT_NAME, 10, "bold"))
add_button.grid(column=1, row=4, sticky="ew", columnspan=2)








































window.mainloop()