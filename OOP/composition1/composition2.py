
#   1

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

class CSVLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        words = message.split()
        from csv import writer
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()

# with open("./data/sample.log") as f:
#     c = ConsoleLogger()
#     for line in f:
#         c.log(line.strip())

# with open("./data/sample.log") as f:
#     with open("events.csv", "w") as fw:
#         text_logger = TextFileLogger(fw)
#         for line in f:
#             text_logger.log(line)
    
with open(r"D:\PYTHON\OOP\sample.log") as f:
    with open(r"D:\PYTHON\OOP\events8.csv", "w") as fww:
        csv_logger = CSVLogger(fww)
        for line in f:
            csv_logger.log(line)
