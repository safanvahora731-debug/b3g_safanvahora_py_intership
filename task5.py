height_cm = "175"
weight_kg = "68.5"

height_num = float(height_cm)
weight_num = float(weight_kg)
height_m = height_num / 100
bmi = weight_num / (height_m * height_m)
print(f"Height: {height_m} meters")
print(f"Weight: {weight_num} kg")
print(f"Calculated BMI: {bmi:.2f}")