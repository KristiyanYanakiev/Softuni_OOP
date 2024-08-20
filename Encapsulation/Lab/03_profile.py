class Profile:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) in range(5, 16):
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")
    
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_case_presented = len([c for c in value if c.isupper()]) > 0
        is_digit_present = len([c for c in value if c.isdigit()]) > 0

        if not all([is_length_valid, is_upper_case_presented, is_digit_present]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)