class ConsoleLogger:
    def log(self, message):
        print(message)
class TextFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()
with open("")
