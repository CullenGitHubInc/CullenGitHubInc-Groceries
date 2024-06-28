def get_coupon_amount():
    coupon_amount = float(input("Enter the coupon amount as a decimal (e.g., 0.10 for 10%): "))
    
    if coupon_amount > 1.0 or coupon_amount <= 0:
        coupon_amount = 0.10
    return coupon_amount
def get_weekly_grocery_bills():
    weekly_bills = []
    
    for i in range(1, 5):
        bill = float(input(f"Enter the grocery bill for week {i}: "))
        weekly_bills.append(bill)
    return weekly_bills
def calculate_totals(weekly_bills, coupon_amount):
    monthly_total_without_coupon = sum(weekly_bills)
    weekly_average_without_coupon = monthly_total_without_coupon / 4
    discount = monthly_total_without_coupon * coupon_amount
    monthly_total_with_coupon = monthly_total_without_coupon - discount
    weekly_average_with_coupon = monthly_total_with_coupon / 4
    
    return (monthly_total_without_coupon, weekly_average_without_coupon,
            monthly_total_with_coupon, weekly_average_with_coupon)
def display_results(monthly_total_without_coupon, weekly_average_without_coupon,
                    monthly_total_with_coupon, weekly_average_with_coupon):
    print(f"Monthly total without coupon: ${monthly_total_without_coupon:.2f}")
    print(f"Weekly average without coupon: ${weekly_average_without_coupon:.2f}")
    print(f"Monthly total with coupon: ${monthly_total_with_coupon:.2f}")
    print(f"Weekly average with coupon: ${weekly_average_with_coupon:.2f}")
def main():
    coupon_amount = get_coupon_amount()
    weekly_bills = get_weekly_grocery_bills()
        
    (monthly_total_without_coupon, weekly_average_without_coupon,
     monthly_total_with_coupon, weekly_average_with_coupon) = calculate_totals(weekly_bills, coupon_amount)
        
    display_results(monthly_total_without_coupon, weekly_average_without_coupon,
                    monthly_total_with_coupon, weekly_average_with_coupon)
if __name__ == "__main__":
    main()
