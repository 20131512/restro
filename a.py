import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant App")

        self.menu = {
            "Fries": 2, "Lunch": 2, "Burger": 3, "Pizza": 4, "Cheese Burger": 2.5, "Drinks": 1,
        }
        self.rate = 94.64
        frame = ttk.Frame(root)
        frame.pack(pady=20)

        ttk.Label(
            frame,
            text="Restaurant Order",
            font=("Arial", 18, "bold"),
        ).grid(columnspan=2, pady=10)

        self.entries = {}
        for i, (item, price) in enumerate(self.menu.items()):
            ttk.Label(frame, text=f"{item} (${price})").grid(row=i + 1, column=0)
            e = ttk.Entry(frame, width=5)
            e.grid(row=i + 1, column=1)
            self.entries[item] = e
            self.currency = tk.StringVar(value="USD")
        ttk.Combobox(frame, textvariable=self.currency, values=["USD", "INR"], width=10, state="readonly").grid(columnspan=2, pady=5)

        ttk.Button(frame, text="Place Order", command=self.place_order).grid(columnspan=2, pady=10)

    def place_order(self):
        total = 0
        currency = self.currency.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.rate if currency == "INR" else 1

        summary = "Order Summary:\n"
        for item, entry in self.entries.items():
            qty = entry.get()
            if qty.isdigit() and int(qty) > 0:
                price = self.menu[item] * rate
                cost = int(qty) * price
                total += cost
                summary += f"{item}: {qty} x {symbol}{price} = {symbol}{cost}\n"

        if total:
            summary += f"\nTotal: {symbol}{total}"
            messagebox.showinfo("Order", summary)
        else:
            messagebox.showerror("Error", "Order at least one item")

root = tk.Tk()
root.geometry("400x400")
RestaurantApp(root)
root.mainloop()
