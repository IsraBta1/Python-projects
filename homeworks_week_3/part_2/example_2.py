# Example 2
def main():
    print("This program computes and prints the remaining")
    print("balance for a loan with a fixed and annual percentage")
    print("rate and a fixed number of payments per year")
    print()
    print("Please enter the following five values.")
    
    principal = float(input("Principal amount: "))
    annual_rate = float(input("Annual percentage rate: "))
    years = int(input("Number of the years in the life of the loan: "))
    payments_per_year = int(input("Number of payment per year: "))
    number_paid = int(input("Number od payment already paid: "))
    compute_balance = ()
    balance = compute_balance(principal, annual_rate, years, payments_per_year, number_paid)
    print()
    print(f"Balance remaining: {balance}")


def compute_balance(principal, ar, years, ppy, pdt):
    """Compute and return the balance remaining for a loan."""
    payment = compute_payment(principal, ar, years, ppy, pdt)
    print()
    print(f"compute_balance({principal}, {ar}, {years}, {ppy}, {pdt})")
    rate = ar / ppy
    power = (1 + rate) ** pdt
    # Show variable values for debugging
    print(f"    payment: {payment} rate: {rate} power: {power}")
    balance = principal * power - payment * (power - 1) /rate
    #show
    print(f"    balance: {balance:.2f}")
    return round(balance, 2)

def compute_payment(principal, ar, years, ppy):
    """Compute and return the payment per period for a loan."""
    #show
    print()
    print(f"compute_payment({principal})")
    rate = ar / ppy
    n = years * ppy
    #show
    print(f"    rate: {rate} n: {n}")
    payment = principal * rate / (1 - (1 + rate) ** -n)
    #show
    print(f"    payment: {payment:.2f}")
    return round(payment, 2)
if __name__ == "__main__":
    main()