from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class ISender(ABC):
    def __init__(self, sender_text):
        self.sender_text = sender_text

    @abstractmethod
    def format_sender(self) -> str:
        pass


class IReceiver(ABC):

    def __init__(self, receiver_text):
        self.receiver_text = receiver_text

    @abstractmethod
    def format_receiver(self) -> str:
        pass


class ImProtocolReceiver(IReceiver):

    def format_receiver(self) -> str:
        return ''.join(["I'm ", self.receiver_text])


class AnotherHypotheticalProtocol(IReceiver):

    def format_receiver(self) -> str:
        return ''.join(["I'm another hypothetical protocol ", self.receiver_text])


class ImProtocolSender(ISender):

    def format_sender(self) -> str:
        return ''.join(["I'm ", self.sender_text])


class ExampleProtocolSender(ISender):

    def format_sender(self) -> str:
        return ''.join(["Example: ", self.sender_text])


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self):
        return '\n'.join(['<HTML>', self.text, '</HTML>'])

class SomeExampleContentType(IContent):

    def format(self) -> str:
        return '\n'.join(['<SomeExampleContentType>', self.text, '</SomeExampleContentType>'])



class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, some_sender: ISender):
        self.__sender = some_sender.format_sender()

    def set_receiver(self, some_receiver: IReceiver):
        self.__receiver = some_receiver.format_receiver()

    def set_content(self, some_content: IContent):
        self.__content = some_content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email()
sender = ImProtocolSender('gmail')
receiver = ImProtocolReceiver('james')
content = HTML("Hello, there!")
email.set_content(content)
email.set_sender(sender)
email.set_receiver(receiver)


email2 = Email()

sender2 = ExampleProtocolSender('gmail')
receiver2 = AnotherHypotheticalProtocol('james')
content2 = SomeExampleContentType("here is the example content")

email2.set_sender(sender2)
email2.set_receiver(receiver2)
email2.set_content(content2)

print(email)
print()
print()
print(email2)