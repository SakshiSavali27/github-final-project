def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate (%), and time (years)."""
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time period (years): "))

    interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + interest

    print(f"Simple Interest: {interest}")
    print(f"Total Amount: {total_amount}")
