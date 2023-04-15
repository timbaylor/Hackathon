import tkinter as tk
import matplotlib.pyplot as plt
import random
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk
from matplotlib.widgets import Button

app = ThemedTk(theme="arc")

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
        tips = ["Never use your toilet as a waste basket.",
                "Do not use water to defrost frozen foods, thaw in the refrigerator overnight.",
                "When using a hose, control the flow with an automatic shut-off nozzle.",
                "TURN OFF THE TAP", "Turn off the water while brushing your teeth"
                ]
        
        i = random.randint(0,4)
        
        return tips[i]

def on_calculate():
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
        result += f"{tip}"
    dict_sum = sum(water_usage.values())
    cumlulative_cost = dict_sum * .009
    household_cost = cumlulative_cost * 3.13

    messagebox.showinfo("Water Usage Results", result)
    return dict_sum, household_cost

def on_profile_select(event):
    user = users[profile_select.current()]
    name_var.set(user.name)

def add_profile():
    global profile_window
    profile_window = tk.Toplevel(app)
    profile_window.title("Add Profile")

    global profile_name_var
    profile_name_var = tk.StringVar()
    profile_name_entry = ttk.Entry(profile_window, textvariable=profile_name_var)

    ttk.Label(profile_window, text="Profile Name:").grid(row=0, column=0, padx=10, pady=10)
    profile_name_entry.grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(profile_window, text="Save Profile", command=add_profile_data).grid(row=1, column=0, columnspan=2, pady=10)

def add_profile_data():
    profile_data = {
        'name': profile_name_var.get(),
    }
    user = User(**profile_data)
    users.append(user)
    profile_select['values'] = [user.name for user in users]
    profile_select.current(len(users) - 1)
    profile_window.destroy()
    open_water_usage_inputs_window()

def create_graph(users):
    x = [user.name for user in users]
    y = [user.calculate_water_usage()['dishwasher'] * .009 * 3.13 for user in users]
   
    plt.bar(x, y,width=0.1)
    plt.title('Household Cost of Water')
    plt.xlabel('Member')
    plt.ylabel('Total Cost of Water ($)')

    ax_add = plt.axes([0.58,0.05,0.15,0.07])
    ax_delete = plt.axes([0.75,0.05,0.15,0.07])

    button_add = Button(ax_add, 'add', color = 'yellow', hovercolor= 'blue')
    button_delete = Button(ax_delete, 'delete', color = 'yellow', hovercolor= 'blue')

    for i, v in enumerate(y):
        plt.text(i, v, f"${v:.2f}", ha='center', va='bottom')




    plt.show()

def create_graph(user):
    water_usage = user.calculate_water_usage()
    dict_sum, household_cost = sum(water_usage.values()), sum(water_usage.values()) * 0.009 * 3.13

    plt.bar(user.name, household_cost,width=0.1)
    plt.title('Household Cost of Water')
    plt.xlabel('Member')
    plt.ylabel('Total Cost of Water ($)')

    #ax_add = plt.axes([0.58,0.05,0.15,0.07])
    #ax_delete = plt.axes([0.75,0.05,0.15,0.07])

    #button_add = Button(ax_add, 'add', color = 'yellow', hovercolor= 'blue')
    #button_delete = Button(ax_delete, 'delete', color = 'yellow', hovercolor= 'blue')

def show_graph():
    if len(users) == 0:
        messagebox.showerror("Error", "No profiles to view.")
        return

    user = users[profile_select.current()]
    create_graph(user)

    plt.show()

def create_combined_graph(users):
    x = [user.name for user in users]
    y = [user.calculate_water_usage()['dishwasher'] * .009 * 3.13 for user in users]
   
    plt.bar(x, y, width=0.1)
    plt.title('Household Cost of Water')
    plt.xlabel('Member')
    plt.ylabel('Total Cost of Water ($)')

    for i, v in enumerate(y):
        plt.text(i, v, f"${v:.2f}", ha='center', va='bottom')

    plt.show()
def compare_selected_profiles(profile_checkboxes):
    selected_users = []
    for user, checkbox_var in profile_checkboxes:
        if checkbox_var.get() == 1:
            selected_users.append(user)

    create_combined_graph(selected_users)
    compare_profiles_window.destroy()


def delete_profile():
    index = profile_select.current()
    del users[index]
    profile_select['values'] =  [user.name for user in users]
    if len(users) > 0:
        profile_select.current(0)
    else:
        name_var.set('')
def view_profile():
    if len(users) == 0:
        messagebox.showerror("Error", "No profiles to view.")
        return

    user = users[profile_select.current()]
    water_usage = user.calculate_water_usage()

    result = f"Water Usage:\n"
    for k, v in water_usage.items():
        result += f"{k.capitalize()}: {v} gallons\n"

    messagebox.showinfo("Profile Water Usage", result)
    



def open_compare_profiles_window():
    global compare_profiles_window
    compare_profiles_window = tk.Toplevel(app)
    compare_profiles_window.title("Compare Profiles")

    profiles_frame = ttk.LabelFrame(compare_profiles_window, text="Select Profiles to Compare")
    profiles_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    profile_checkboxes = []
    for i, user in enumerate(users):
        checkbox_var = tk.IntVar()
        profile_checkbox = ttk.Checkbutton(profiles_frame, text=user.name, variable=checkbox_var)
        profile_checkbox.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        profile_checkboxes.append((user, checkbox_var))

    compare_button = ttk.Button(profiles_frame, text="Compare", command=lambda: compare_selected_profiles(profile_checkboxes))
    compare_button.grid(row=len(users) + 1, column=0, pady=10)




def open_water_usage_inputs_window():
    global water_usage_inputs_window
    water_usage_inputs_window = tk.Toplevel(app)
    water_usage_inputs_window.title("Water Usage Inputs")

    inputs_frame = ttk.LabelFrame(water_usage_inputs_window, text="Water Usage Inputs")
    inputs_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    inputs = ['Minutes spent in shower daily:', 'Showers per week:', 'Toilet flushes per day:',
              'Minutes spent with faucet on daily:', 'Dishwasher loads per week:', 'Washing machine loads per week:']

    for i, text in enumerate(inputs):
        ttk.Label(inputs_frame, text=text).grid(row=i, column=0, padx=10, pady=10)

    global shower_minutes_var, showers_per_week_var, toilet_flushes_var, faucet_minutes_var, dishwasher_loads_var, washing_machine_loads_var

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


users = []

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

view_profile_button = ttk.Button(profile_frame, text="View Profile", command=view_profile)
view_profile_button.grid(row=7, column=1, pady=10)

graph_button = ttk.Button(profile_frame, text="Graph", command=show_graph)
graph_button.grid(row=8, column=1, pady=10)


compare_button = ttk.Button(profile_frame, text="Compare", command=open_compare_profiles_window)

compare_button.grid(row=9, column=1, pady=10)
app.mainloop()