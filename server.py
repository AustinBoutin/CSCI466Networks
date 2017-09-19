import sys
import socket
from bottle import post, request, error, HTTPError
from tkinter import *
from fleet import Fleet
from client import Client

class Server:

    def get_tile_color(self, tile):
        return{
            'C' : "#FF9232",
            'B' : "#FFEC23",
            'R' : "#91FF23",
            'S' : "#22F9C4",
            'D' : '#2226F9'
            }.get(tile, "#FFF")

    def color_op_board(self, x, y, code):
        global op_buttons
        if code == 0:
            op_buttons[x][y].config(bg = "#777")
        else:
            op_buttons[x][y].config(bg = "#f00")
        

    @post('/')
    def handle_salvo():

        try:
            x = int(request.forms.get('x'))
            y = int(request.forms.get('y'))

        except TypeError:
            print ('404')
            return HTTPError(404, reason='Not Found.')

        if x > 9 or x < 0 or y > 9 or y < 0:
            print ('400')
            return HTTPError(400, reason='Bad Request.')       

        #If shot has already been guessed
        if not op_board[x][y] == -1:
            print ('410')
            return HTTPError(410, reason='Gone.')
        
        print(str(x) + ", " + str(y))

        #Change 'fleet' to check opponents board instead
        return_code = fleet.check_pos((x,y))
        op_board[x][y] = return_code
        #Perform action based on return code
        self.color_op_board(y,x,return_code)
        
        print(str(return_code))

        if str(return_code) in 'CBRSD':
            return 'hit=1&sink={}'.format(return_code)
        else:
            return 'hit={}'.format(return_code)
            
            

    def __init__(self, master):

        sys.argv = [sys.argv[0], 10000, 'board.txt']

        port = sys.argv[1]
        board_file = sys.argv[2]
        

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #server_address = ('localhost', port)
        
        #print >>sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(('127.0.0.1', port))

        sock.listen(1)

        
        print(socket.gethostname() + ' ' + str(port))
        #client = Client('localhost', port, 4, 3)

        #Stuck Here
        conn, addr = sock.accept()
        data = conn.recv(1024)
        print(data)
        
        
        print('There')
        
        
        global fleet
        fleet = Fleet(board_file)
        fleet.print_fleet()

        frame = Frame(master)
        frame.pack()

        player_grid = Frame(frame)
        player_grid.grid(row=0, column=0, padx = 25, pady = 25)

        for y in range(0, 10):
            subframe = Frame(player_grid)
            subframe.grid(row=y)
            for x in range(0, 10):
                button_color = self.get_tile_color(fleet.board[y][x])
                self.button = Button(subframe, height = 1, width = 2, bg=button_color, state=DISABLED)
                self.button.grid(row=y, column=x)

        opponent_grid = Frame(frame)
        opponent_grid.grid(row=0, column=1, padx=25, pady=25)

        global op_board
        op_board = []
        global op_buttons
        op_buttons = []
        
        for y in range(0, 10):
            subframe = Frame(opponent_grid)
            subframe.grid(row=y)
            board_row = []
            op_button_row =[]
            for x in range(0, 10):
                self.button = Button(subframe, width = 2, height = 1, bg="#fff", state=DISABLED)
                self.button.grid(row=y, column=x)
                board_row.append(-1)
                op_button_row.append(self.button)
            op_board.append(board_row)
            op_buttons.append(op_button_row)
            
        input_frame = Frame(frame)
        input_frame.grid(row = 1, column = 0, columnspan = 2)
        
        l = Label(input_frame, text="X:")
        l.grid(row=0, column=0)

        x_entry = Entry(input_frame)
        x_entry.grid(row=0, column=1, pady=5)

        l = Label(input_frame, text="Y:")
        l.grid(row=1, column=0)

        y_entry = Entry(input_frame)
        y_entry.grid(row=1, column=1)

        fire_button = Button(input_frame, text="FIRE!", command= lambda: self.fire(x_entry, y_entry))
        fire_button.grid(row=3, column=1, pady=5)

root = Tk()

app = Server(root)

root.mainloop()
root.destroy
