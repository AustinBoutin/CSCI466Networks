class Ship:
    def __init__(self, pos, ship_type):
        self.positions = pos
        self.ship_type = ship_type

    def check_pos(self, pos):
        #print(str(pos) + ' ' + str(self.positions))
        if pos in self.positions:
            self.positions.remove(pos)
            if len(self.positions) == 0:
                return self.ship_type
            return 1
        return 0
