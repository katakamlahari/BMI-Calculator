import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("600x850")
        self.root.config(bg="#ECF0F1")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Body Mass Index (BMI) Calculator", 
                 font=("Helvetica", 16, "bold"), bg="#ECF0F1", fg="#2C3E50").pack(pady=15)

        # Weight input
        tk.Label(self.root, text="Weight (kg):", font=("Helvetica", 12), bg="#ECF0F1").pack()
        self.weight_entry = tk.Entry(self.root, font=("Helvetica", 12), width=20)
        self.weight_entry.pack(pady=5)

        # Height input (in cm now)
        tk.Label(self.root, text="Height (cm):", font=("Helvetica", 12), bg="#ECF0F1").pack()
        self.height_entry = tk.Entry(self.root, font=("Helvetica", 12), width=20)
        self.height_entry.pack(pady=5)

        # Age input
        tk.Label(self.root, text="Age:", font=("Helvetica", 12), bg="#ECF0F1").pack()
        self.age_entry = tk.Entry(self.root, font=("Helvetica", 12), width=20)
        self.age_entry.pack(pady=5)

        # Gender input
        tk.Label(self.root, text="Gender:", font=("Helvetica", 12), bg="#ECF0F1").pack()
        self.gender_var = tk.StringVar(value="Select")
        self.gender_menu = tk.OptionMenu(self.root, self.gender_var, "Male", "Female", "Other")
        self.gender_menu.config(font=("Helvetica", 12), bg="white", width=17)
        self.gender_menu.pack(pady=5)

        # Buttons
        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi,
                  font=("Helvetica", 12, "bold"), bg="#27AE60", fg="white", width=20).pack(pady=10)
        tk.Button(self.root, text="Reset", command=self.reset_fields,
                  font=("Helvetica", 12, "bold"), bg="#C0392B", fg="white", width=20).pack()

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#ECF0F1", fg="#2C3E50")
        self.result_label.pack(pady=20)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())
            age = int(self.age_entry.get())
            gender = self.gender_var.get()

            if weight <= 0 or height_cm <= 0 or age <= 0 or gender == "Select":
                raise ValueError

            height_m = height_cm / 100  # Convert cm to meters
            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            self.result_label.config(
                text=f"Age: {age} | Gender: {gender}\nBMI: {bmi} ({category})"
            )

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid positive values for all fields.")

    def reset_fields(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_var.set("Select")
        self.result_label.config(text="")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
