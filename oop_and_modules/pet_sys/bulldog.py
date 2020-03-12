from dog import Dog

class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)