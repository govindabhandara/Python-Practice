# Walrus operator
if (data := fetch_health_data()) and data['can_exercise']:
    print(f"Recommended exercise: {data['recommendation']}")