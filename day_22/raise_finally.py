# custom exception that keeps the error message
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User Defined Exception:", self.msg)


# opens the file and raises Accident on purpose so except and finally both run
def process_file(file_name):
    try:
        f = open(file_name, "r")
        print("File opened successfully")
        raise Accident("Crash due to unexpected data format!")
    except Accident as e:
        e.print_exception()
    finally:
        print("Finally block executed: Resource cleanup")


process_file("sample_notes.txt")
