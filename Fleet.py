import os
from ship import Ship

class Fleet:
    def __init__(self, path):
        self.ships = {}
        self.board = []
        
        file_path = os.path.join(path)
        f = open(file_path, 'r')
        lines = f.readlines();
        
        for y, line in enumerate(lines):
            row = []
            for x, char in enumerate(line):
                if char in 'CBRSD':
                    location = (x,y);
                    if self.ships.get(char) is None:
                        self.ships[char] = Ship([location],char)
                    else:
                        self.ships[char].positions.append(location)
                    #print(str(self.ships[char].positions))
                row.append(char)
            self.board.append(row)
        f.close()


    def check_pos(self, pos):
        for ship in self.ships:
            return_code = self.ships[ship].check_pos(pos)
            if not return_code == 0:
                return return_code

        return 0

    def print_fleet(self):
        for ship in self.ships:
            print(str(self.ships[ship].positions) + ' ' + str(self.ships[ship].ship_type))
            
