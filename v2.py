import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

app = ThemedTk(theme='equilux')

# GLOBAL VARIABLE
DOLLAR_PER_GALLON = 0.009 # www.move.org
AVG_WATER_BILL_PER_MONTH = 45.44 # www.move.org
PEOPLE_PER_HOUSEHOLD = 3.13 # www.census.gov

class User:
    def __init__(self, name, shower_minutes, showers_per_week, toilet_flushes, faucet_minutes, dishwasher_loads, washing_machine_loads):
        self.name = name
        self.shower_minutes = shower_minutes
        self.showers_per_week = showers_per_week
        self.toilet_flushes = toilet_flushes
        self.faucet_minutes = faucet_minutes
        self.dishwasher_loads = dishwasher_loads
        self.washing_machine_loads = washing_machine_loads

    def calculate_water_usage(self):
        water_usage = {
            'shower': self.shower_minutes * self.showers_per_week * 2.1,
            'toilet': self.toilet_flushes * 3,
            'faucet': self.faucet_minutes * 2,
            'dishwasher': self.dishwasher_loads * 6,
            'washing_machine': self.washing_machine_loads * 40,
        }
        return water_usage

    def generate_water_saving_tips(self, water_usage):
        tips = []
        # Add your water-saving tips here based on water_usage
        return tips

def on_calculate():
    user_data = {
        'name': profile_select.get(),
        'shower_minutes': int(shower_minutes_var.get()),
        'showers_per_week': int(showers_per_week_var.get()),
        'toilet_flushes': int(toilet_flushes_var.get()),
        'faucet_minutes': int(faucet_minutes_var.get()),
        'dishwasher_loads': int(dishwasher_loads_var.get()),
        'washing_machine_loads': int(washing_machine_loads_var.get()),
    }
    user = User(**user_data)
    users.append(user)

    water_usage = user.calculate_water_usage()
    tips = user.generate_water_saving_tips(water_usage)

    result = f"Water Usage:\n"
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
    print(household_cost_per_week) # *** USE THIS FOR GRAPH ***

    messagebox.showinfo("Water Usage Results", result)

def on_profile_select(event):
    user = users[profile_select.current()]
    shower_minutes_var.set(user.shower_minutes)
    showers_per_week_var.set(user.showers_per_week)
    toilet_flushes_var.set(user.toilet_flushes)
    faucet_minutes_var.set(user.faucet_minutes)
    dishwasher_loads_var.set(user.dishwasher_loads)
    washing_machine_loads_var.set(user.washing_machine_loads)

def add_profile():
    global profile_window
    # Create a new window to enter the profile information
    profile_window = tk.Toplevel(app)
    profile_window.title("Add Profile")

    # Create input fields for the profile information
    global profile_name_var, profile_shower_minutes_var, profile_showers_per_week_var, profile_toilet_flushes_var, profile_faucet_minutes_var, profile_dishwasher_loads_var, profile_washing_machine_loads_var
    profile_name_var = tk.StringVar()
    profile_shower_minutes_var = tk.StringVar()
    profile_showers_per_week_var = tk.StringVar()
    profile_toilet_flushes_var = tk.StringVar()
    profile_faucet_minutes_var = tk.StringVar()
    profile_dishwasher_loads_var = tk.StringVar()
    profile_washing_machine_loads_var = tk.StringVar()
    profile_name_entry = ttk.Entry(profile_window, textvariable=profile_name_var)
    profile_shower_minutes_entry = ttk.Entry(profile_window, textvariable=profile_shower_minutes_var)
    profile_showers_per_week_entry = ttk.Entry(profile_window, textvariable=profile_showers_per_week_var)
    profile_toilet_flushes_entry = ttk.Entry(profile_window, textvariable=profile_toilet_flushes_var)
    profile_faucet_minutes_entry = ttk.Entry(profile_window, textvariable=profile_faucet_minutes_var)
    profile_dishwasher_loads_entry = ttk.Entry(profile_window, textvariable=profile_dishwasher_loads_var)
    profile_washing_machine_loads_entry = ttk.Entry(profile_window, textvariable=profile_washing_machine_loads_var)

    ttk.Label(profile_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
    profile_name_entry.grid(row=0, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Minutes spent in shower daily:").grid(row=1, column=0, padx=10, pady=10)
    profile_shower_minutes_entry.grid(row=1, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Showers per week:").grid(row=2, column=0, padx=10, pady=10)
    profile_showers_per_week_entry.grid(row=2, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Toilet flushes per day:").grid(row=3, column=0, padx=10, pady=10)
    profile_toilet_flushes_entry.grid(row=3, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Minutes spent with faucet on daily:").grid(row=4, column=0, padx=10, pady=10)
    profile_faucet_minutes_entry.grid(row=4, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Dishwasher loads per week:").grid(row=5, column=0, padx=10, pady=10)
    profile_dishwasher_loads_entry.grid(row=5, column=1, padx=10, pady=10)
    ttk.Label(profile_window, text="Washing machine loads per week:").grid(row=6, column=0, padx=10, pady=10)
    profile_washing_machine_loads_entry.grid(row=6, column=1, padx=10, pady=10)
    ttk.Button(profile_window, text="Save Profile", command=add_profile_data).grid(row=7, column=0, columnspan=2, pady=10)

def add_profile_data():
    global profile_name_var, profile_shower_minutes_var, profile_showers_per_week_var, profile_toilet_flushes_var, profile_faucet_minutes_var, profile_dishwasher_loads_var, profile_washing_machine_loads_var
    profile_data = {
        'name': profile_name_var.get(),
        'shower_minutes': int(profile_shower_minutes_var.get()),
        'showers_per_week': int(profile_showers_per_week_var.get()),
        'toilet_flushes': int(profile_toilet_flushes_var.get()),
        'faucet_minutes': int(profile_faucet_minutes_var.get()),
        'dishwasher_loads': int(profile_dishwasher_loads_var.get()),
        'washing_machine_loads': int(profile_washing_machine_loads_var.get()),
    }
    user = User(**profile_data)
    users.append(user)
    profile_select['values'] = [user.name for user in users]
    profile_select.current(len(users)-1)
    profile_window.destroy()

def delete_profile():
    index = profile_select.current()
    del users[index]
    profile_select['values'] = [user.name for user in users]
    if len(users) > 0:
        profile_select.current(0)
    else:
        shower_minutes_var.set('')
        showers_per_week_var.set('')
        toilet_flushes_var.set('')
        faucet_minutes_var.set('')
        dishwasher_loads_var.set('')
        washing_machine_loads_var.set('')
    calculate_button.grid(row=len(inputs)+1, column=0, pady=10)

inputs = ['Minutes spent in shower daily:', 'Showers per week:', 'Toilet flushes per day:', 'Minutes spent with faucet on daily:', 'Dishwasher loads per week:', 'Washing machine loads per week:']

for i, text in enumerate(inputs):
    ttk.Label(app, text=text).grid(row=i, column=0, padx=10, pady=10)

shower_minutes_var = tk.StringVar()
shower_minutes_entry = ttk.Entry(app, textvariable=shower_minutes_var)
shower_minutes_entry.grid(row=0, column=1, padx=10, pady=10)

showers_per_week_var = tk.StringVar()
showers_per_week_entry = ttk.Entry(app, textvariable=showers_per_week_var)
showers_per_week_entry.grid(row=1, column=1, padx=10, pady=10)

toilet_flushes_var = tk.StringVar()
toilet_flushes_entry = ttk.Entry(app, textvariable=toilet_flushes_var)
toilet_flushes_entry.grid(row=2, column=1, padx=10, pady=10)

faucet_minutes_var = tk.StringVar()
faucet_minutes_entry = ttk.Entry(app, textvariable=faucet_minutes_var)
faucet_minutes_entry.grid(row=3, column=1, padx=10, pady=10)

dishwasher_loads_var = tk.StringVar()
dishwasher_loads_entry = ttk.Entry(app, textvariable=dishwasher_loads_var)
dishwasher_loads_entry.grid(row=4, column=1, padx=10, pady=10)

washing_machine_loads_var = tk.StringVar()
washing_machine_loads_entry = ttk.Entry(app, textvariable=washing_machine_loads_var)
washing_machine_loads_entry.grid(row=5, column=1, padx=10, pady=10)

calculate_button = ttk.Button(app, text="Calculate", command=on_calculate)
calculate_button.grid(row=len(inputs)+1, column=0, pady=10)

users = []
profile_select = ttk.Combobox(app, state='readonly')
profile_select.grid(row=6, column=1, padx=10, pady=10)
profile_select.bind('<<ComboboxSelected>>', on_profile_select)

add_profile_button = ttk.Button(app, text="Add Profile", command=add_profile)
add_profile_button.grid(row=len(inputs)+1, column=1, pady=10)

delete_profile_button = ttk.Button(app, text="Delete Profile", command=delete_profile)
delete_profile_button.grid(row=len(inputs)+1, column=2, pady=10)

graph_button = ttk.Button(app, text="Graph")
graph_button.grid(row=len(inputs)+1, column=3, pady=10)

app.mainloop()


