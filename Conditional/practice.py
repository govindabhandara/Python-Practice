work_intensity ="high"
match work_intensity:
    case "low":
        reps, sets = 15, 3
    case "medium":
        reps, sets = 16, 3
    case "high":
        reps, sets = 19, 4
    case _:
        reps, sets = 10, 3

print(f"Do {sets} sets of {reps} reps")