# import requests

# def get_exchange_rate(base_currency, target_currency):
#     url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
import requests
import tkinter as tk
from tkinter import ttk, messagebox

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        messagebox.showerror("Error", "Error fetching exchange rates")
        return None
    
    data = response.json()
    rates = data.get("rates", {})
    return rates.get(target_currency, None)

def convert_currency():
    base_currency = base_currency_var.get().upper()
    target_currency = target_currency_var.get().upper()
    
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return
    
    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate is None:
        messagebox.showerror("Error", "Invalid currency or unable to fetch exchange rate.")
        return
    
    converted_amount = amount * rate
    result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

def main():
    global amount_entry, base_currency_var, target_currency_var, result_label
    
    root = tk.Tk()
    root.title("Currency Converter")
    
    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=5)
    base_currency_var = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD"])
    base_currency_var.grid(row=1, column=1, padx=10, pady=5)
    base_currency_var.set("USD")
    
    tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=5)
    target_currency_var = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD"])
    target_currency_var.grid(row=2, column=1, padx=10, pady=5)
    target_currency_var.set("INR")
    
    convert_button = tk.Button(root, text="Convert", command=convert_currency)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()