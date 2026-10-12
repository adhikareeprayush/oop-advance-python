class Father:
    def gardening(self):
        print("I enjoy gardening")


class Mother:
    def cooking(self):
        print("I enjoy cooking")


# child gets methods from both Father and Mother
class Child(Father, Mother):
    def sports(self):
        print("I enjoy playing soccer")


c = Child()
c.gardening()
c.cooking()
c.sports()
