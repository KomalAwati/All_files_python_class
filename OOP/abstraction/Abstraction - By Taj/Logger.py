from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        raise Exception

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

class TextFileLogger(Logger):
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()

class Spam(Logger):
    def demo(self):
        return "hello world"

f1 = "This is an ERROR message"
c1 = ConsoleLogger()
# c1.log("ERROR")
s1 = Spam()
print(s1.demo())


