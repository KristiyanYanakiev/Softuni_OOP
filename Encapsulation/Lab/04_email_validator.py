from typing import List


class EmailValidator:

    def __init__(self, min_length: int, mails: List[str], domains: List[str]) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, email) -> bool:
        name = email.split("@")[0]
        mail = email.split("@")[1].split(".")[0]
        domain = email.split("@")[1].split(".")[1]

        return all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)])


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))