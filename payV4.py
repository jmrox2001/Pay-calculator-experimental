#TODO: Explain how my program should work


# Define tax brackets based on annual income
def calculate_tax_single(weekly_income):
    tax_brackets = {
        11600 : 0.1,
        47150 : .12,
        100525: 0.22,
        191950: 0.24,
        243725: 0.32,
        609350: 0.35,
        float('inf'): 0.37  # Upper bound for highest bracket
    }
    # Determine the tax rate based on the weekly income
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    # If the income exceeds the highest bracket, return the rate for the highest bracket
    return tax_brackets[float('inf')]




def calculate_tax_joint(weekly_income):
    tax_brackets = {
        23200 : 0.1,
        94300 : 0.12,
        201050: 0.22,
        383900: 0.24,
        487450: 0.32,
        731200: 0.35,
        float('inf'): 0.37  
    }
    
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    return tax_brackets[float('inf')]



def calculate_tax_hoh(weekly_income):
    tax_brackets = {
        16550 : 0.1,
        63100 : 0.12,
        100500: 0.22,
        191950: 0.24,
        243700: 0.32,
        609350: 0.35,
        float('inf'): 0.37  
    }
    
    annual_income = weekly_income * 52
    for bracket, rate in sorted(tax_brackets.items()):
        if annual_income <= bracket:
            return rate

    return tax_brackets[float('inf')]


# validates and returnes a input value and asks the user 
# for the value until it's not valid.
# use: valid_input(pormpt, <type>)
# example: valid_input('number> ', int)
#
# arguments: 
#   prompt - the text to show while taking a input.
#   type   - the type of value to accept. can only be 
#            one of [int, str, "yn", "sjh"]. 
# 
# Note: yn stands for yes or no. (y/n)
#       sjh stands for single, joint, hoh (s/j/h)
def valid_input (prompt, typ):
    while True:
        # strip() removes spaces from start and the end of a string.
        user_input = input(prompt).strip().lower()
        if typ==str:
            return user_input

        
        if typ==int:
            try:
                converted_input = int(user_input)
                return converted_input
            except ValueError:
                print('\n-> enter a valid number!\n')
                continue

        
        if typ=="yn":
            if user_input=='y' or user_input=='n':
                return user_input
            
            print("\n-> please enter 'y' for yes and 'n' for no.\n")
            continue


        
        if typ=="sjh":
            if user_input=='s' or user_input=='j' or user_input=='h':
                return user_input
            
            print("\n-> please enter 's' for single, 'j' for joint, 'h' for hoh .\n")
            continue



def main():
    # prompt the user to get hours.
    hours = valid_input('Enter Hours: ', int)

    # prompt the user to enter Rate.
    rate = float(valid_input('Enter Rate: ', int))

    # set the default tax rate.
    tax_rate = 0



    # Calculate overtime.
    if hours > 40:
        regular_pay = rate * 40 # Regular pay for the first 40 hours.
        overtime_pay = (hours - 40) * (rate * 1.5) # Overtime pay for hours over 40.
        total_pay = regular_pay + overtime_pay # Total pay including overtime
    else:
        regular_pay = hours * rate 
        overtime_pay = 0 
        total_pay = regular_pay


    # Ask User if they would like to have taxes adjusted for.
    choice_prompt = 'Would you like to have taxes taken out of your calculated pay? y/n'
    user_choice = valid_input(choice_prompt, 'yn')

    if user_choice=='y':
        choice_prompt2 = 'Enter your filing status single/joint/hoh (s/j/h):'
        filig_status = valid_input(choice_prompt2, 'sjh')
    
        # To escape if else hell, you can try this trick with dictonary
        # since we are gettng s/j/h as a return value from the input.
        tax_rate_funcs = {
            "s": calculate_tax_single,
            "j": calculate_tax_joint,
            "h": calculate_tax_hoh
        }
    
        # this line means get the function for either s/j/h from the 
        # dictonary depending on what user chose.
        # then execute it with regular_pay.
        tax_rate = tax_rate_funcs[filig_status](regular_pay)


    # Calculate the pay before tax
    print(f'Weekly Pay: { regular_pay }')
    print(f'Overtime Pay: { overtime_pay }\n')
    print(f'Total pay before tax: { total_pay }')


    # Calculate the pay after tax
    if tax_rate != 0:
        sub_tax_amount = total_pay * (1 - tax_rate )  # Subtracting the tax amount from total pay
    else:
        sub_tax_amount = total_pay

    print(f'Pay after tax: { sub_tax_amount }')


    # Find and display the user's Owed Tax Amount
    tax = total_pay - sub_tax_amount
    print(f'Taxes Owed: { tax }')



# (if __name__ == "__main__":) this line says if youre directly
# runnig the file with python like 'python payV4.py', then it should 
# run the code inside this block.

# it can be helpful if you want to import any functions from here
# to anothet file. if you do so then it won't run the calculator automatically.
# you can remove this line if you want, and have a while loop only.
# it'll work the same.

if __name__ == "__main__":
    while True:
        main()
        prompt = "Would you like to calculate again? (yes/no): "
        choice = valid_input(prompt, 'yn')
        
        if choice=='n':
            break
