import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os

"""The world we have created is a product of our thinking. — Albert Einstein"""

"""first we are loading the data from the file, and taking the data in order, planet name, distance, mass
then we are returning it as planet_data so we can call it in the main, and calculations"""

#loading the planets.txt file
def load_planet_data(file_path):
    file_path = 'in/planets.txt'
    planet_data = {}
    with open(file_path, 'r') as file:
        while True:
            planet_name = file.readline().strip()
            if not planet_name:
                break
            mass = float(file.readline().strip())
            distance = float(file.readline().strip())
            planet_data[planet_name] = (mass, distance)
    return planet_data

"""using the tkinter funtion, we are going to put the input into the box, and asssign value to the names"""

def vehicle(planet_data):
    #initalizing new window
    root = tk.Tk()
    root.withdraw()#hiding window for the input

#asking for inputs now, using askstring to grab user input
    vehicle_name = simpledialog.askstring("Vehicle Input", "Enter your ship's name:")
    if vehicle_name is None: return

    vehicle_weight, vehicle_velocity = validation()
    if vehicle_weight is None or vehicle_velocity is None:
        return

#planet input
    planets = list(planet_data.keys())
    planet_choice = simpledialog.askstring("Destination Planet", "Enter your destination planet:")

    if planet_choice is None or planet_choice.strip().capitalize() not in planets:#using same strip and capitalize as before so i can input lowercase planet data for ease of use
        messagebox.showerror("Error", "Invalid planet, please enter a valid name.")
        return
    return {
        "name": vehicle_name,"weight": vehicle_weight,"velocity": vehicle_velocity,"destination_planet": planet_choice.strip().capitalize()}

"""validation was tricky, but i got it mostly. """

#input validation, using the same if statments as before, just nested in the while
def validation():
    while True:
        vehicle_weight = simpledialog.askfloat("Vehicle Input", "Enter your ship's weight in kg:")
        if vehicle_weight is None: return None, None
        if 0 <= vehicle_weight <= 1000000:
            break
        else:
            messagebox.showerror("Error", "Weight must be between 0 and 1,000,000 kg!")

    while True:
        vehicle_velocity = simpledialog.askfloat("Vehicle Input", "Enter your ship's velocity in km/hr:")
        if vehicle_velocity is None: return None, None
        if 0 <= vehicle_velocity <= 1080000000:
            break
        else:
            messagebox.showerror("Error", "Velocity must be between 0 and 1,080,000,000 km/hr!")
    return vehicle_weight, vehicle_velocity

#calculations and printing outputs
def calculate(vehicle_details, planet_name, planet_data):
    try:
        planet_name = vehicle_details["destination_planet"]
        mass, distance = planet_data[planet_name]
        travel_time_hours = distance / vehicle_details["velocity"]
        travel_time_days = travel_time_hours / 24
        travel_time_years = travel_time_days / 365

        vehicle_velocity_mph = vehicle_details["velocity"] * 0.621371
        weight_on_planet = vehicle_details["weight"] * mass
        weight_on_planet_lbs = weight_on_planet * 2.20462
        weight_on_earth_lbs = vehicle_details["weight"] * 2.20462


        results = "\n"
        results += f"The weight of your ship, {vehicle_details['name']}, on Earth is: {vehicle_details['weight']:.2f} kg or {weight_on_earth_lbs:.2f} lbs.\n"
        results += f"The weight of {vehicle_details['name']} on {planet_name} is: {weight_on_planet:.2f} kg or {weight_on_planet_lbs:.2f} lbs.\n"
        results += "\n"
        results += f"If you max out your ship going {vehicle_details['velocity']:.2f} km/hr ({vehicle_velocity_mph:.2f} mph),\n"
        results += f"you will get to {planet_name} in {travel_time_years:.2f} years, {travel_time_days:.2f} days, and {travel_time_hours:.2f} hours.\n"
        results += "\n"
        results += "Thank you for using the Interstellar Space Calculator! Listen to some good music on your way there!\n"
        
        
        print(results) #printing the variable results to the console
        
        messagebox.showinfo("Here are your results!", results)
        
        save_to_file(results) #here i am printing them to the file, which i will define in the next chunk after this
    
    except KeyError:
        print(f"{planet_name} not found Please be sure its in the list!") #error handling for the planet name input, if its not in the csv file, it wont work


"""here, we are writing the results to a file, using tthe random funtion. I tried to do this as straight forward as i can, and hard coded the output file. """

def save_to_file(results):
    random_number = random.randint(1, 100)
    dir_name = 'out/'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    filename = f"interstellar_calculator_{random_number}.txt"
    file_path = f"out/{filename}"
    
    with open(file_path, 'w') as file:
        file.write(results)
    print(f"This has been saved to {file_path}")


#the main program
def main():
    file_path = 'in/planets.txt'
    planet_data = load_planet_data(file_path)

    while True:
        vehicle_details = vehicle(planet_data)
        if vehicle_details is None:
            messagebox.showwarning("Invalid, please try again!")#error handling for the vehicle detail input

        planet_name = vehicle_details["destination_planet"]
        #run calculations
        calculate(vehicle_details, planet_name, planet_data)

        #repeat program in a message box
        repeat = messagebox.askyesno("repeat", "Would yuou like to run this program again?")
        if not repeat:
            messagebox.showinfo("","Thank you for using the Interstellar Space Calculator!")
            break

#closing the main funtion out, allowing the program to run fully. 
 
if __name__ == "__main__":
    main()
"""last project of this semester, kind of sad about it"""