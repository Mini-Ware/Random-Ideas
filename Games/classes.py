from random import randint

class Board():
    checker = True
    arr = [["#","#","#"],["#","#","#"],["#","#","#"]]
    def set_square(self, position, type):
        if self.__class__.arr[int(position[1])][int(position[0])] == "#":
            self.__class__.arr[int(position[1])][int(position[0])] = type
            self.__class__.checker = False
        else:
            self.__class__.checker = True
    def set_checker(self, value):
        self.__class__.checker = value
    def get_checker(self):
        return self.__class__.checker
    def check_game_over(self):
        pass
    def __str__(self):
        current = ""
        for i in self.__class__.arr:
            for j in i:
                current += j
            current += "\n"
        return current

class Player():
    position = "00"
    def __init__(self, type):
        self.type = type
    def select_square(self, Board):
        Board.set_square(self.__class__.position[0],self.__class__.position[1], self.type)

class Human(Player):
    def __init__(self, type="X"):
        super().__init__(type)
    def select_square(self):
        return input("Give a position (XY), between 0-2: ")
    def __str__(self):
        return self.type

class Com(Player):
    def __init__(self, type="O"):
        super().__init__(type)
    def select_square(self):
        return str(randint(0,2))*2
    def __str__(self):
        return self.type
