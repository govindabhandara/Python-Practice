# Structural pattern matching 
workout_intensity = "high"

match workout_intensity:
    case "low":
        reps, sets = 15, 3
    case "medium":
        reps, sets = 12, 4
    case "high":
        reps, sets = 8, 5
    case _:
        reps, sets = 10, 3

print(f"Do {sets} sets of {reps} reps")