total = 0

print("|     💰 EXPENSE TRACKER 💰          |")
print("📝 Start entering your expenses below.")
print("👉 Type 'done' when you have finished.\n")

while True:
    expense = input("💵 Enter expense (or type 'done'): ")

    if expense.lower() == "done":
        break

    try:
        total += float(expense)
        print(f"✅ Current Total: 💰 {total}\n")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")

print("📊SUMMARY")
print(f"💸 Total Expenses: 💰 {total}")
print("🎉 Thank you for using Expense Tracker!")
print("👋 Have a wonderful day!")