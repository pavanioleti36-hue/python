from abc import ABC, abstractmethod
class authentication(ABC):
    @abstractmethod
    def login(self):
        pass
class password(authentication):
    def login(self):
        print("Login using password")
class otp(authentication):
    def login(self):
        print("Login using OTP")
class biometric(authentication):
    def login(self):
        print("Login using Biometric")  
pas= password()
ot = otp()
bio = biometric()
pas.login()
ot.login()
bio.login()