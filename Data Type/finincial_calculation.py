# Compound interest calculator
principal = 10000  # int
rate = 0.05        # float
years = 10

amount = principal * (1 + rate) ** years
print(f"Investment will grow to ${amount:,.2f} in {years} years")
    