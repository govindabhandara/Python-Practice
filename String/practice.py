from datetime import datetime
customer="sugam bhandari"
amount=345.4566
invoice_format=f"""
customer name:{customer}
amount due:{amount:,.2f}
due date: {datetime.now().strftime('%B %d, %Y')}
"""
print(invoice_format)