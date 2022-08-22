from tkinter import *
from tkinter import ttk

# Create a variable to store the account balance
savings_balance = 0


# Create a function that will update the balance.
def update_balance():
    global savings_balance
    deposit_amount = amount.get()
    savings_balance += deposit_amount
    total_balance = savings_balance
    account_details.set("Savings: ${:.2f}\nTotal Balance: ${:.2f}".format(savings_balance, total_balance))
    amount.set("")


# Creating a function to create the account
def account_creation():
    exit(create_account())


# Creating a function to display the Create account screen
def create_account():
    root = Tk()
    root.title("Create account")
    create_account = True

    # Instructions
    instruction_label = ttk.Label(root, text="Enter a title for the account, and a starting value, then press submit")
    instruction_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Creating the title for the account
    account_title = ttk.Label(root, text="Account Title:")
    account_title.grid(row=1, column=0)

    account_title_entry = ttk.Entry(root, textvariable=account_title)
    account_title_entry.grid(row=1, column=1, padx=10, pady=3)

    # Making the button that will create the account
    create_button = ttk.Button(root, text="Create", command=account_creation)
    create_button.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

    return


root = Tk()
root.title("Finance Manager")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(root, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()
account_details.set("Savings: $0 \nTotal balance: $0")

# Create the details label and pack it into the GUI
details_label = ttk.Label(root, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label for the account combobox
account_label = ttk.Label(root, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
account_names = ["Savings", "Phone", "Holiday"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(root, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3)

# Create a label for the action Combobox
action_label = ttk.Label(root, text="Action: ")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(root, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3)

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

account_creation_button = ttk.Button(root, text="New account", command=create_account)
account_creation_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the mainloop
root.mainloop()
