
class Smatrix:
    def __init__(self, matrix = {}):
        self.__matrix= matrix
    def get(self,row,col):
        if 'row,col' in self.__matrix:
            return self.__matrix['row,col']
        else:
            return 0

    def set(self,row,col,value):
        if self.__matrix['row,col'] != 0:
            return self.__matrix['row,col']
        else:
            del self.__matrix['row,col']

    def __repr__(self):
        print(self.__matrix)

    def __add__(self,m1,m2):
        return self.m1+self.m2

    def __sub__(self,m1,m2):
        return self.m1-self.m2
    def __mul__(self,m1,m2):
        return self.m1*self.m2
    m1 = Smatrix()
    m1.set(0,0,2)
    m1.set(0,1,2)
    m2 = Smatrix()
    m2.set(0,0,1)
    m2.set(0,1,4)
    print(m1+m2)
    print(m1-m2)
    print(m1*m2)
