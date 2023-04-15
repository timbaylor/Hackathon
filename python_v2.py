import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

app = ThemedTk(theme="equilux")


class User:
    def __init__(self, name, shower_minutes=None, showers_per_week=None, toilet_flushes=None, faucet_minutes=None,
                 dishwasher_loads=None, washing_machine_loads=None):
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
    if not users:
        messagebox.showerror("Error", "No profile selected.")
        return

    selected_user = users[profile_select.current()]
    selected_user.shower_minutes = int(shower_minutes_var.get())
    selected_user.showers_per_week = int(showers_per_week_var.get())
    selected_user.toilet_flushes = int(toilet_flushes_var.get())
    selected_user.faucet_minutes = int(faucet_minutes_var.get())
    selected_user.dishwasher_loads = int(dishwasher_loads_var.get())
    selected_user.washing_machine_loads = int(washing_machine_loads_var.get())

    water_usage = selected_user.calculate_water_usage()
    tips = selected_user.generate_water_saving_tips(water_usage)

    result = f"Water Usage:\n"
    for k, v in water_usage.items():
        result += f"{k.capitalize()}: {v} gallons\n"

    result += "\nWater Saving Tips:\n"
    for tip in tips:
        result += f"{tip}\n"

    messagebox.showinfo("Water Usage Results", result)


def on_profile_select(event):
    user = users[profile_select.current()]
    name_var.set(user.name)


def add_profile():
    global profile_window
    # Create a new window to enter the profile information
    profile_window = tk.Toplevel(app)
    profile_window.title("Add Profile")

    # Create input fields for the profile information
    global profile_name_var
    profile_name_var = tk.StringVar()
    profile_name_entry = ttk.Entry(profile_window, textvariable=profile_name_var)

    ttk.Label(profile_window, text="Profile Name:").grid(row=0, column=0, padx=10, pady=10)
    profile_name_entry.grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(profile_window, text="Save Profile", command=add_profile_data).grid(row=1, column=0, columnspan=2,
                                                                                   pady=10)


def add_profile_data():
    profile_data = {
        'name': profile_name_var.get(),
    }
    user = User(**profile_data)
    users.append(user)
    profile_select['values'] = [user.name for user in users]    
    profile_select.current(len(users) - 1)
    profile_window.destroy()


def delete_profile():
    index = profile_select.current()
    del users[index]
    profile_select['values'] = [user.name for user in users]
    if len(users) > 0:
        profile_select.current(0)
    else:
        name_var.set('')


users = []

# Profile management section
profile_frame = ttk.LabelFrame(app, text="Profile Management")
profile_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

name_var = tk.StringVar()
name_label = ttk.Label(profile_frame, textvariable=name_var)
name_label.grid(row=0, column=1, padx=10, pady=10)

profile_select = ttk.Combobox(profile_frame, state='readonly')
profile_select.grid(row=1, column=1, padx=10, pady=10)
profile_select.bind('<<ComboboxSelected>>', on_profile_select)

add_profile_button = ttk.Button(profile_frame, text="Add Profile", command=add_profile)
add_profile_button.grid(row=2, column=1, pady=10)

delete_profile_button = ttk.Button(profile_frame, text="Delete Profile", command=delete_profile)
delete_profile_button.grid(row=3, column=1, pady=10)

# Water usage input section
inputs_frame = ttk.LabelFrame(app, text="Water Usage Inputs")
inputs_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

inputs = ['Minutes spent in shower daily:', 'Showers per week:', 'Toilet flushes per day:', 'Minutes spent with faucet on daily:', 'Dishwasher loads per week:', 'Washing machine loads per week:']

for i, text in enumerate(inputs):
    ttk.Label(inputs_frame, text=text).grid(row=i, column=0, padx=10, pady=10)

shower_minutes_var = tk.StringVar()
shower_minutes_entry = ttk.Entry(inputs_frame, textvariable=shower_minutes_var)
shower_minutes_entry.grid(row=0, column=1, padx=10, pady=10)

showers_per_week_var = tk.StringVar()
showers_per_week_entry = ttk.Entry(inputs_frame, textvariable=showers_per_week_var)
showers_per_week_entry.grid(row=1, column=1, padx=10, pady=10)

toilet_flushes_var = tk.StringVar()
toilet_flushes_entry = ttk.Entry(inputs_frame, textvariable=toilet_flushes_var)
toilet_flushes_entry.grid(row=2, column=1, padx=10, pady=10)

faucet_minutes_var = tk.StringVar()
faucet_minutes_entry = ttk.Entry(inputs_frame, textvariable=faucet_minutes_var)
faucet_minutes_entry.grid(row=3, column=1, padx=10, pady=10)

dishwasher_loads_var = tk.StringVar()
dishwasher_loads_entry = ttk.Entry(inputs_frame, textvariable=dishwasher_loads_var)
dishwasher_loads_entry.grid(row=4, column=1, padx=10, pady=10)

washing_machine_loads_var = tk.StringVar()
washing_machine_loads_entry = ttk.Entry(inputs_frame, textvariable=washing_machine_loads_var)
washing_machine_loads_entry.grid(row=5, column=1, padx=10, pady=10)

calculate_button = ttk.Button(inputs_frame, text="Calculate", command=on_calculate)
calculate_button.grid(row=len(inputs) + 1, column=0, pady=10)

app.mainloop()
