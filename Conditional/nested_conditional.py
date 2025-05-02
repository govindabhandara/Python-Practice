# Nested conditional classification
def classify_number(num):
    if num > 0:
        if num % 2 == 0:
            if num % 3 == 0:
                return "Positive even multiple of 3"
            else:
                return "Positive even not multiple of 3"
        else:
            if num % 3 == 0:
                return "Positive odd multiple of 3"
            else:
                return "Positive odd not multiple of 3"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    