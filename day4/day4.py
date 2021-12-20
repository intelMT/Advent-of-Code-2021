import numpy as np

example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

BOARD_SIZE = 5

class Board:
    def __init__(self, data: str, size: int=BOARD_SIZE):
        self.x = size
        self.y = size
        self.map = self.parse(data)

    
    def parse(self, data: str) -> list:
        values = [{int(num): 0} for line in data.split('\n')
                    for num in line.split()]
        return np.reshape( values, (self.x, self.y))
        
    def check(self) -> bool:
        for i in range(BOARD_SIZE):
            count_Row = np.sum(val for items in self.map[i,:]
                            for val in items.values())
            count_Col = np.sum(val for items in self.map[:,i]
                            for val in items.values())
            # print(count_Row)
            if np.any([count_Row==BOARD_SIZE, count_Col==BOARD_SIZE]):
                return True
        return False
    
    def zero_sum(self)-> int:
        return np.sum(key for line in self.map
                       for pair in line
                       for key in pair.keys() if 0 in pair.values())


def preprocess(data : str) -> list:
    line = data.split('\n\n')[0]
    winning_nums = [int(x) for x in line.split(",")]

    boards = [Board(board) for board in data.split('\n\n')[1:]]

    return [winning_nums, boards]

        
def find_winner_score(lucky_numbers: list, boards: list, want_to_win:bool =True):
    
    win_count = [{key:0} for key in range(len(boards))] # Set all elements to OFF(=0)
    if want_to_win:
        target =1
    else:
        target = len(boards)

    for lucky_num in lucky_numbers:
        for k, board in enumerate(boards):
            for i, line in enumerate(board.map):
                for j, pair in enumerate(line):
                    if pair.get(lucky_num) != None:
                        board.map[i,j] = {lucky_num: 1} #Set the winning num to ON(=1)
                        if board.check():
                            win_count[k]= {k: 1}
                            win_sum = np.sum(x for item in win_count 
                                            for x in item.values())
                            if  win_sum == target:
                                total = board.zero_sum()
                                return lucky_num * total
    
    return None

assert find_winner_score(*preprocess(example)) == 4512
assert find_winner_score(*preprocess(example), False) == 1924

if __name__ == '__main__':
    with open('d4.txt') as f:
        content = f.read()

    print(find_winner_score(*preprocess(content)))
    print(find_winner_score(*preprocess(content), False))