class password_authentication:
    def login(self):
        print("login with password authentication")
class otp_authentication:
    def login(self):
        print("login with OTP authentication")
class pin_authentication:
    def login(self):
        print("login with PIN authentication")
def assign_login(employee):
    employee.login()
password_auth = password_authentication()
otp_auth = otp_authentication()
pin_auth = pin_authentication()
assign_login(password_auth)
assign_login(otp_auth)
assign_login(pin_auth)