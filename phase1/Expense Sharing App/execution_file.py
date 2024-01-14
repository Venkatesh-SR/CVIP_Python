import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk 
from doctest import master
 # Import themed Tkinter module

class ExpenseTracker:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, user_name):
        if user_name not in self.users:
            self.users[user_name] = 0
            return f"User '{user_name}' added successfully."
        else:
            return f"{user_name} already exists."

    def add_expense(self, payer, amount, participants):
        if payer not in self.users:
            return f"{payer} does not exist. Please add the user first."

        total_participants = len(participants)
        if total_participants == 0:
            return "No participants in the expense. Please add participants."

        individual_share = amount / total_participants

        # Update payer's balance
        self.users[payer] += amount

        # Update participants' balances
        for participant in participants:
            if participant not in self.users:
                return f"{participant} does not exist. Please add the user first."
            self.users[participant] -= individual_share

        self.expenses.append({
            'payer': payer,
            'amount': amount,
            'participants': participants
        })

        return "Expense added successfully."

    def show_balances(self):
        return "\n".join([f"{user}: {balance}" for user, balance in self.users.items()])

    def show_expenses(self):
        return "\n".join([f"Payer: {expense['payer']}, Amount: {expense['amount']}, Participants: {expense['participants']}" for expense in self.expenses])
    
    

class ExpenseTrackerApp:
    def __init__(self, master):
        self.tracker = ExpenseTracker()
        # GUI setup
        self.master = master
        master.title("Expense Sharing App")

        # Choose a different theme - 'clam', 'alt', 'default', 'classic', etc.
        style = ttk.Style()
        style.theme_use('classic')
        # Create a custom style for themed widgets
        style.configure("TButton", padding=7, relief="flat", background="pink", foreground="black")  # Change button style

        self.label = ttk.Label(master, text="Expense Tracker Menu", style="TLabel")
        self.label.pack(pady=8)

        self.add_user_button = ttk.Button(master, text="Add User", command=self.add_user)
        self.add_user_button.pack()

        self.add_expense_button = ttk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.show_balances_button = ttk.Button(master, text="Show Balances", command=self.show_balances)
        self.show_balances_button.pack()

        self.show_expenses_button = ttk.Button(master, text="Show Expenses", command=self.show_expenses)
        self.show_expenses_button.pack()
        self.exit_button = ttk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

        self.details_text = tk.Text(master, height=10, width=50, wrap="word", background="#ECF0F1", foreground="#2C3E50")
        self.details_text.pack(pady=10)

        # Additional widgets for displaying details
        self.user_details_label = ttk.Label(master, text="User Details:", foreground="black")
        self.user_details_label.pack()

        self.expense_details_label = ttk.Label(master, text="Expense Details:", foreground="black")
        self.expense_details_label.pack()

    def add_user(self):
        user_name = simpledialog.askstring("Add User", "Enter user name:")
        if user_name:
            result = self.tracker.add_user(user_name)
            messagebox.showinfo("Result", result)
            self.print_to_console(result)

    def add_expense(self):
        payer = simpledialog.askstring("Add Expense", "Enter the payer's name:")
        amount = simpledialog.askfloat("Add Expense", "Enter the expense amount:")
        participants_str = simpledialog.askstring("Add Expense", "Enter participants' names (comma-separated):")
        participants = participants_str.split(',') if participants_str else []
        result = self.tracker.add_expense(payer, amount, participants)
        messagebox.showinfo("Result", result)
        self.print_to_console(result)

    def show_balances(self):
        balances = self.tracker.show_balances()
        self.details_text.delete(1.0, tk.END)  # Clear previous content
        self.details_text.insert(tk.END, "User Balances:\n" + balances)

        # Display user details
        self.user_details_label.config(text="User Details:\n" + balances)
        self.print_to_console("User Balances:\n" + balances)

    def show_expenses(self):
        expenses = self.tracker.show_expenses()
        self.details_text.delete(1.0, tk.END)  # Clear previous content
        self.details_text.insert(tk.END, "Expense Details:\n" + expenses)

        # Display expense details
        self.expense_details_label.config(text="Expense Details:\n" + expenses)
        self.print_to_console("Expense Details:\n" + expenses)

    def print_to_console(self, message):
        print(message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()