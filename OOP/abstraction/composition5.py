
#   4


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

# Composition  (Has-A relationship)
class FilteredLogger:
    def __init__(self, pattern, logger_type):
        self.pattern = pattern
        self.logger_type = logger_type
    
    #polymorphic behaviour or it is also called as Duck Typing
    def log(self, message):
        if self.pattern in message:
            self.logger_type.log(message)


# with open("./data/test.txt") as f:
#     console_logger = ConsoleLogger()
#     _logger = FilteredLogger('This', console_logger)
#     for line in f:
#         _logger.log(line)

# with open('./data/sample.log') as f:
#     with open("./data/events.csv", "w") as fw:
#         text_logger = TextFileLogger(fw)
#         logger = FilteredLogger("INFO", text_logger)
#         for line in f:
#             logger.log(line)

with open('./data/sample.log') as f:
    with open('./data/events2.csv', 'w') as fw:
        csv_logger = CSVLogger(fw)
        logger_ = FilteredLogger('WARNING', csv_logger)
        for line in f:
            logger_.log(line)

