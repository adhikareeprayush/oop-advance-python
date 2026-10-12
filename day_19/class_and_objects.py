# a person with a name and an occupation
class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    # prints what the person does depending on occupation
    def do_work(self):
        if self.occupation == "tennis player":
            print(f"{self.name} plays tennis!")
        elif self.occupation == "actor":
            print(f"{self.name} shoots movies!")
        else:
            print(f"{self.name} works as a {self.occupation}")

    # just says hello
    def speaks(self):
        print(f"{self.name} says hello!")



tom = Human("Prayush", "software developer")
tom.do_work()
tom.speaks()

maria = Human("Ram", "tennis player")
maria.do_work()
maria.speaks()
