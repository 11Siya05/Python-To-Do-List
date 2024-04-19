from tkinter import *

def calculate(initial_amount, monthly_contri, interest_rate):
    initial_investment = initial_amount
    interest = interest_rate / 12 / 100
    gained_monthly = []

    for month in range(1, 9):
        gained_interest = initial_investment * interest
        initial_investment += monthly_contri
        gained_monthly.append(gained_interest)

    for month, gained in enumerate(gained_monthly, start=1):
        month_label = globals()[f"month{month}"]  # Get the label dynamically
        month_label.config(text=f'Month {month} you will have R{gained:.2f}')

def submit_values():
    initial_amount = investment_var.get()
    monthly_contri = monthly_var.get()
    interest_rate = rate_var.get()
    calculate(initial_amount, monthly_contri, interest_rate) 

root = Tk()
root.title('Interest Calculator')
root.geometry('400x500')

investment_var = DoubleVar()
monthly_var = DoubleVar()
rate_var = DoubleVar()

wlc = Label(root, text='Welcome', font=("Helvetica", 16)).pack()
prompt1 = Label(root, text='Enter your initial investment amount:', font=("Helvetica", 16)).pack()
initial1 = Entry(root, textvariable=investment_var, font=("Helvetica", 16)).pack()

prompt2 = Label(root, text='Enter your monthly deposit:', font=("Helvetica", 16)).pack()
initial2 = Entry(root, textvariable=monthly_var, font=("Helvetica", 16)).pack()

prompt3 = Label(root, text='Enter your interest percentage:', font=("Helvetica", 16)).pack()
initial3 = Entry(root, textvariable=rate_var, font=("Helvetica", 16)).pack()

for month in range(1, 9):
    globals()[f"month{month}"] = Label(root, text=' ', font=("Helvetica", 16))
    globals()[f"month{month}"].pack()

submit = Button(root, text='SUBMIT', font=("Helvetica", 16), command=submit_values).pack(pady=5)
root.mainloop()
