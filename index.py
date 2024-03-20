import tkinter as tk
from tkinter import ttk

# Function to collect user input and display it
def submit_form():
    # Collect user input from entry fields
    user_info = {
        'first_name': entry_first_name.get(),
        'last_name': entry_last_name.get(),
        'email': entry_email.get(),
        'concentration': entry_concentration.get()
    }
    # Display user information
    display_user_info(user_info)

# Function to display user information in a text box
def display_user_info(user_info):
    # Clear the text box
    result_text.delete('1.0', tk.END)
    # Insert user information into the text box
    result_text.insert(tk.END, "Name: {} {}\n".format(user_info['first_name'], user_info['last_name']))
    result_text.insert(tk.END, "Email: {}\n".format(user_info['email']))
    result_text.insert(tk.END, "Concentration: {}\n".format(user_info['concentration']))

# Function to handle the "Exit" menu item
def exit_program():
    root.quit()

# Create the main GUI window
root = tk.Tk()
root.title("Python Lab Activity 1")  # Set window title

# Create a style object
style = ttk.Style(root)
style.theme_use('clam')  # Use a basic theme for consistency

# Configure style for entry fields
style.configure('TEntry', font=('Helvetica', 12))

# Create a frame for the header
header_frame = ttk.Frame(root)
header_frame.pack(fill='x')

# Create a header label
header_label = ttk.Label(header_frame, text="Python Lab Activity 1", font=('Helvetica', 16, 'bold'))
header_label.pack(side='left', padx=10, pady=10)

# Create a frame for the menu bar
menu_frame = ttk.Frame(root)
menu_frame.pack(fill='y', side='left')

# Create a menu bar
menu_bar = tk.Menu(menu_frame)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=menu_file)
menu_bar.add_command(label="Help") # Dummy help item
root.config(menu=menu_bar)

# Create a frame for the form
form_frame = ttk.Frame(root)
form_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Create labels and entry fields for the form
label_first_name = ttk.Label(form_frame, text="First Name:")
label_last_name = ttk.Label(form_frame, text="Last Name:")
label_email = ttk.Label(form_frame, text="Email:")
label_concentration = ttk.Label(form_frame, text="Concentration:")

entry_first_name = ttk.Entry(form_frame)  # Entry field for first name
entry_last_name = ttk.Entry(form_frame)   # Entry field for last name
entry_email = ttk.Entry(form_frame)       # Entry field for email
entry_concentration = ttk.Entry(form_frame)  # Entry field for concentration

# Create a submit button
submit_button = ttk.Button(form_frame, text="Submit", command=submit_form)

# Arrange widgets in the form frame using grid layout
label_first_name.grid(row=0, column=0, sticky='e', padx=5, pady=5)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)
label_last_name.grid(row=1, column=0, sticky='e', padx=5, pady=5)
entry_last_name.grid(row=1, column=1, padx=5, pady=5)
label_email.grid(row=2, column=0, sticky='e', padx=5, pady=5)
entry_email.grid(row=2, column=1, padx=5, pady=5)
label_concentration.grid(row=3, column=0, sticky='e', padx=5, pady=5)
entry_concentration.grid(row=3, column=1, padx=5, pady=5)
submit_button.grid(row=4, columnspan=2, padx=5, pady=10, sticky='we')

# Create a frame for the footer
footer_frame = ttk.Frame(root)
footer_frame.pack(fill='x', side='bottom')

# Create a footer label
footer_label = ttk.Label(footer_frame, text="Thank you for using this program! - Castro", font=('Helvetica', 12))
footer_label.pack(side='left', padx=10, pady=10)

# Create a frame for the result text
result_frame = ttk.Frame(root)
result_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Create a text box to display the result
result_text = tk.Text(result_frame, wrap='word', font=('Helvetica', 12))
result_text.pack(fill='both', expand=True)

# Start the GUI event loop
root.mainloop()
