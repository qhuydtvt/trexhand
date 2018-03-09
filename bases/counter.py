class Counter:
    def __init__(self, count_max):
        self.count_max = count_max
        self.count = 0

    def run(self):
        if self.count >= self.count_max:
            return True
        else:
            self.count += 1
            return False

    def reset(self):
        self.count = 0
