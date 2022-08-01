
#   3

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

class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# using Multiple Inheritance
class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)

class FilteredTextFileLogger(FilteredLogger, TextFileLogger):
    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        TextFileLogger.__init__(self, file_object)

class FilteredCSVLogger(FilteredLogger, CSVLogger):
    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        CSVLogger.__init__(self, file_object)

# with open("./data/test.txt") as f:
#     console_logger = ConsoleLogger()
#     filter_console = FilteredConsoleLogger('Here')
#     for line in f:
#         filter_console.log(line)

# with open("./data/sample.log") as f:
#     with open("./data/events.csv", "w") as fw:
#         filter_text_file = FilteredTextFileLogger("INFO", fw)
#         for line in f:
#             filter_text_file.log(line)


with open(r"D:\PYTHON\OOP\sample.log") as f:
    with open(r"D:\PYTHON\OOP\events8.csv", "w") as fw:
        filter_csv = FilteredCSVLogger("WARNING", fw)
        for line in f:
            filter_csv.log(line)

