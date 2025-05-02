# Conditional list comprehensions
exercises = ["Running", "Swimming", "Weight Lifting", "Yoga"]
cardio_exercises = [ex for ex in exercises if ex in ["Running", "Swimming"]]
print(cardio_exercises)

