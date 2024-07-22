# Expense Tracker

# Initialize an empty list to store expenses
expenses = []

# Function to add an expense
def add_expense(date, category, amount):
    expenses.append({
        'date': date,
        'category': category,
        'amount': amount
    })
add_expense(date, category, amount)


# Function to remove an expense by index
def remove_expense(index):
    if 0 <= index < len(expenses):
        del expenses[index]
        return True
    else:
        return False
remove_expense(index)

# Function to calculate daily, weekly, and monthly totals
def calculate_totals():
    daily_total = []
    weekly_total = []
    monthly_total = []
    
    for expense in expenses:
        date = expense['date']
        amount = expense['amount']
        
        # Daily total
        if date in daily_total:
            daily_total[date] += amount
            print("daily total+ ", daily_total[date])
            
        else:
            daily_total[date] = amount

        
        # Weekly total (assuming week starts on Monday)
        week_key = date.strftime('%Y-%W')
        if week_key in weekly_total:
            weekly_total[week_key] += amount
        else:
            weekly_total[week_key] = amount
    
        
        # Monthly total
        month_key = date.strftime('%Y-%m')
        if month_key in monthly_total:
            monthly_total[month_key] += amount
        else:
            monthly_total[month_key] = amount
calculate_totals()
# Function to generate a report
def generate_report():
    report = ""
    for expense in expenses:
        report += f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']}\n"
    return report
generate_report()
print('report',generate_report())

# Function to highlight days or categories with high spending
def highlight_high_spending(threshold):
    high_spending_days = []
    high_spending_categories = {}
    
    for expense in expenses:
        date = expense['date']
        category = expense['category']
        amount = expense['amount']
        
        # Check for high spending days
        if amount > threshold:
            high_spending_days.append(date)
        
        # Check for high spending categories
        if category in high_spending_categories:
            high_spending_categories[category] += amount
        else:
            high_spending_categories[category] = amount
    
    return high_spending_days, high_spending_categories
highlight_high_spending(threshold)



    

