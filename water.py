import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

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
        'name': name_var.get(),
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

    result = f"Water Usage for {user.name}:\n"
    for k, v in water_usage.items():
        result += f"{k.capitalize()}: {v} gallons\n"

    result += "\nWater Saving Tips:\n"
    for tip in tips:
        result += f"{tip}\n"

    messagebox.showinfo("Water Usage Results", result)

def on_profile_select(event):
    user = users[profile_select.current()]
    name_var.set(user.name)
    shower_minutes_var.set(user.shower_minutes)
    showers_per_week_var.set(user.showers_per_week)
    toilet_flushes_var.set(user.toilet_flushes)
    faucet_minutes_var.set(user.faucet_minutes)
    dishwasher_loads_var.set(user.dishwasher_loads)
    washing_machine_loads_var.set(user.washing_machine_loads)

def add_profile():
    # Create a new window to enter the profile information
    profile_window = tk.Toplevel(app)
    profile_window.title("Add Profile")

    # Create input fields for the profile information
    profile_name_var = tk.StringVar()
    profile_name_entry = ttk.Entry(profile_window, textvariable=profile_name_var)
    profile_shower_minutes_var = tk.StringVar()
    profile_shower_minutes_entry = ttk.Entry(profile_window, textvariable=profile_shower_minutes_var)
    profile_showers_per_week_var = tk.StringVar()
    profile_showers_per_week_entry = ttk.Entry(profile_window, textvariable=profile_showers_per_week_var)
    profile_toilet_flushes_var = tk.StringVar()
    profile_toilet_flushes_entry = ttk.Entry(profile_window, textvariable=profile_toilet_flushes_var)
    profile_faucet_minutes_var = tk.StringVar()
    profile_faucet_minutes_entry = ttk.Entry(profile_window, textvariable=profile_faucet_minutes_var)
    profile_dishwasher_loads_var = tk.StringVar()
    profile_dishwasher_loads_entry = ttk.Entry(profile_window, textvariable=profile_dishwasher_loads_var)
    profile_washing_machine_loads_var = tk.StringVar()
    profile_washing_machine_loads_entry = ttk.Entry(profile_window, textvariable=profile_washing_machine_loads_var)

    def add_profile_data():
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

app = ThemedTk(theme="arc")
app.title("Water Usage Calculator")

name_var = tk.StringVar()
shower_minutes_var = tk.StringVar()
showers_per_week_var = tk.StringVar()
toilet_flushes_var = tk.StringVar()
faucet_minutes_var = tk.StringVar()
dishwasher_loads_var = tk.StringVar()
washing_machine_loads_var = tk
washing_machine_loads_var = tk.StringVar()

inputs = [
    ("Name:", name_var),
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

add_profile_button = ttk.Button(app, text="Add Profile", command=add_profile)
add_profile_button.grid(row=len(inputs), column=0, pady=10)

users = []
profile_select = ttk.Combobox(app, values=[user.name for user in users], state="readonly")
profile_select.bind("<<ComboboxSelected>>", on_profile_select)
profile_select.grid(row=len(inputs), column=1, pady=10)

calculate_button = ttk.Button(app, text="Calculate", command=on_calculate)
calculate_button.grid(row=len(inputs)+1, column=0, columnspan=2, pady=10)

app.mainloop()

