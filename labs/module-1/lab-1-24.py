# Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

age = int(input())
weight = int(input())
heartRate = int(input())
time = int(input())

calories = (((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * time) / 8.368

print("Calories: {:.2f} calories".format(calories))