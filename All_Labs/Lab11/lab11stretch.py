class measure:
    def __init__(self,feet,inches):
        self.feet = feet
        if inches > 12:
            self.inches = 0
            self.feet+=1

    def __str__(self):
        if self.inches == 0:
            return str(self.feet+ "'")
        elif self.inches == 0 and self.feet == 0:
            return str(self.feet+ '"')

        else:
            return str(self.feet + "'" + self.inches + '"')
