from config import STUDENT_DATA

allowance = STUDENT_DATA["monthly_allowance"]

total_expenses = (
    STUDENT_DATA["food"]
    + STUDENT_DATA["travel"]
    + STUDENT_DATA["study_materials"]
    + STUDENT_DATA["other"]
)

balance = allowance - total_expenses

print("Student Monthly Expense Report")
print("-------------------------------")
print("Monthly Allowance: ₹", allowance)
print("Total Expenses: ₹", total_expenses)
print("Remaining Balance: ₹", balance)

if balance >= 1000:
    print("Status: Within budget")
else:
    print("Status: Review spending")