class BigBell:
    def __init__(self):
        self.ring = 'ding'

    def sound(self):
        print(self.ring)
        if self.ring == 'ding':
            self.ring = 'dong'
        else:
            self.ring = 'ding'

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
