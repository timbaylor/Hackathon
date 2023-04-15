import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

# GLOBAL VARIABLE
DOLLAR_PER_GALLON = 0.009 # www.move.org
AVG_WATER_BILL_PER_MONTH = 45.44 # www.move.org
PEOPLE_PER_HOUSEHOLD = 3.13 # www.census.gov

def calculate_water_usage(user_data):
    water_usage = {
        'shower': user_data['shower_minutes'] * user_data['showers_per_week'] * 2.1,
        'toilet': user_data['toilet_flushes'] * 3,
        'faucet': user_data['faucet_minutes'] * 2,
        'dishwasher': user_data['dishwasher_loads'] * 6,
        'washing_machine': user_data['washing_machine_loads'] * 40,
    }
    return water_usage

def generate_water_saving_tips(water_usage):
    tips = []
    # Add your water-saving tips here based on water_usage
    return tips

def on_calculate():
    user_data = {
        'shower_minutes': int(shower_minutes_var.get()),
        'showers_per_week': int(showers_per_week_var.get()),
        'toilet_flushes': int(toilet_flushes_var.get()),
        'faucet_minutes': int(faucet_minutes_var.get()),
        'dishwasher_loads': int(dishwasher_loads_var.get()),
        'washing_machine_loads': int(washing_machine_loads_var.get()),
    }
    water_usage = calculate_water_usage(user_data)
    tips = generate_water_saving_tips(water_usage)

    result = "Water Usage:\n"
    for k, v in water_usage.items():
        result += f"{k.capitalize()}: {v} gallons\n"

    result += "\nWater Saving Tips:\n"
    for tip in tips:
        result += f"{tip}\n"

    # NEW CALC COST PER WEEK
    dict_sum = sum(water_usage.values())
    cumulative_cost_per_week = dict_sum * DOLLAR_PER_GALLON
    household_cost_per_week = cumulative_cost_per_week * PEOPLE_PER_HOUSEHOLD

    # TEST
    print(water_usage)
    print(dict_sum)
    print(household_cost_per_week)

    # OLD
    messagebox.showinfo("Water Usage Results", result)

# Use ThemedTk instead of tk.Tk
app = ThemedTk(theme="arc")
app.title("Water Usage Calculator")

# Create input fields
shower_minutes_var = tk.StringVar()
showers_per_week_var = tk.StringVar()
toilet_flushes_var = tk.StringVar()
faucet_minutes_var = tk.StringVar()
dishwasher_loads_var = tk.StringVar()
washing_machine_loads_var = tk.StringVar()

inputs = [
    ("Minutes spent in shower daily:", shower_minutes_var),
    ("Showers per week:", showers_per_week_var),
    ("Toilet flushes per day:", toilet_flushes_var),
    ("Minutes spent with faucet on daily:", faucet_minutes_var),
    ("Dishwasher loads per week:", dishwasher_loads_var),
    ("Washing machine loads per week:", washing_machine_loads_var),
]

for i, (label_text, var) in enumerate(inputs):
    label = ttk.Label(app, text=label_text)
    entry = ttk.Entry(app, textvariable=var)
    label.grid(row=i, column=0, padx=10, pady=10)
    entry.grid(row=i, column=1, padx=10, pady=10)

# Use ttk.Button instead of tk.Button
calculate_button = ttk.Button(app, text="Calculate", command=on_calculate)
calculate_button.grid(row=len(inputs), column=0, columnspan=2, pady=10)

app.mainloop()