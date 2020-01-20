class Bug:
    def __init__(self,position = 0):
        self.position = position
        self.direction ='+1'

    def move(self):
        if self.direction == '+1':
            self.position+=1
        else:
            if self.position - 1 > 0:
                self.position-=1

    def turn(self):

        if self.direction == '+1':

            self.direction = '-1'

        else:
            self.direction = '+1'

    def display(self):
        if self.direction == '+1':
            print('.'*self.position, '>')
        else:
            print('.'*self.position, '<')
def main():
    bug = Bug(10)
    looper = 0
    while looper < 13:

        bug.move()
        bug.turn()
        bug.display()
        looper+=1
