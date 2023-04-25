# Get input from the user
loan_amount = float(input("Loan Amount: "))
num_years = int(input("Number of Years: "))
interest_rate = float(input("Interest Rate (%): "))

# Convert interest rate to monthly rate
monthly_rate = interest_rate / 1200

# Calculate monthly payment
num_months = num_years * 12
monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** (-num_months))

# Calculate total payment
total_payment = monthly_payment * num_months

# Print results
print("Monthly Payment: {:.2f}".format(monthly_payment))
print("Total Payment: {:.2f}".format(total_payment))