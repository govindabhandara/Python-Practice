total_purchase=150
discount=0.1 if total_purchase>100 else 0
final_price=total_purchase*(1-discount)
print(f"Final price :${final_price:.2f}")