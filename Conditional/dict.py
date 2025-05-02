day=str(input("enter day"))
workout = {
    "monday":"legs and Triceps",
    "tuesday":"hand and leg",
    "wednesday":"running"
}
workout_plan=workout.get(day,"yoga and rest")
print(f"today's day is {workout_plan}")