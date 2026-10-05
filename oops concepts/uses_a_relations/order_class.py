class EmailService:
    def send_email(self, email, message):
        print("Email sent to:", email)
        print("Message:", message)


class Order:
    def __init__(self, order_id, email):
        self.order_id = order_id
        self.email = email

    def send_confirmation(self, email_service):
        message = "Order " + str(self.order_id) + " confirmed."
        email_service.send_email(self.email, message)


order = Order(101, "student@example.com")
email_service = EmailService()

order.send_confirmation(email_service)