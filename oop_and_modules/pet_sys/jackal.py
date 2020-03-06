from dog import Dog

class Jackal(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)