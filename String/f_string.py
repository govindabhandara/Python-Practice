#Invoce Generation
from datetime import datetime 
customer="sugam"
amount=149.4566
invoice_text= f"""
Invoice for :{customer}
Amount deu: ${amount:,.2f}
Due date: {datetime.now().strftime('%B %d, %Y')} """
print(invoice_text)
