#  2

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

# Inheritance  (IS-A relationship)
class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredCSVLogger(CSVLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


'''
with open(r"D:\PYTHON\OOP\sample.log") as f:
    consl_logg = ConsoleLogger()
    for line in f:
        consl_logg.log(line)
    

'''


'''
with open(r"D:\PYTHON\OOP\sample.log") as f:
    con_logger = FilteredConsoleLogger("WARNING")
    for line in f:
        con_logger.log(line)
    
'''



'''
with open(r"D:\PYTHON\OOP\sample.log") as f:
    with open(r"D:\PYTHON\OOP\events10.csv", "w") as fw:
        filter_text = FilteredTextFileLogger("INFO", fw)
        for line in f:
            filter_text.log(line)
'''

with open(r"D:\PYTHON\OOP\sample.log") as f:
    with open(r"D:\PYTHON\OOP\events10.csv", "w") as fw:
        filter_csv = FilteredCSVLogger("INFO", fw)
        for line in f:
            filter_csv.log(line)
        
    

         
        
            

