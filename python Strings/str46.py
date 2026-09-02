fname= input("enter first name:-").strip()
lname= input("enter last name:-").strip()
username= fname + "." + lname
print(username)

#invoice msg
customer = "Ravi Kumar"
amount = 12500.50
invoice_number = 125
message = (
f"Invoice #{invoice_number:04d}\n"
f"Customer: {customer}\n"
f"Amount: ₹{amount:.2f}"
)
print(message)

#attendance
student = "Ravi Kumar"
status = "Present"
record = f"{student.upper()} - {status.upper()}"
print(record)