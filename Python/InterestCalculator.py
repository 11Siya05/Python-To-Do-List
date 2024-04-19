print('Welcome To Our Interest Calculator')
intial_amount=float(input('Enter your initial investment amount: '))
monthly_deposit=float(input('Enter your monthly deposit: '))
interest_rate=float(input('Enter the interest rate percentage: '))

def calculate(x,y,z):
    initial_investment=x
    monthly_contr=y
    interest=z/12/100
    gained_interest=0
    
    for b in range(8):
        gained_interest=(initial_investment)*interest
        
        print(f'Month {b+1} you will have R{gained_interest:.2f}')
        initial_investment=initial_investment+monthly_contr
    print(initial_investment)   
calculate(intial_amount,monthly_deposit,interest_rate)