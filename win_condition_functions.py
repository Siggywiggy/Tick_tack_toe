
class Player():

    player_moves_list = [] #Saving every move a player makes (and is possible to play at that moment) to a list of played moves 

def check_winning(self):
    
    def check_win_rows(self):
        
        for row_num in range(0,3): #row = 0, row = 1, row = 2
            # Adding all player moves with 0 index = row to a list
            row_container = [1 for player_move in player_moves_list if player_move[0] == row_num]
            # Checking if player has made 3 moves in one row and returning True if so - player won
            if sum(row_container) == 3:
                return True   
            else:
                continue
    
    def check_win_columns(self):

        for column_num in range(0,3): #column = 0, column = 1, column = 2
            # Adding all player moves with 1 index = column to a list
            column_container = [1 for player_move in player_moves_list if player_move[1] == column_num]
            # Checking if player has made 3 moves in one column and returning True if so - player won
            if sum(column_container) == 3:
                return True   
            else:
                continue
    
    def check_digonal(self):

        # Adding a "1" to a list if a player move had equal x and y "coordinates" - moves 1:1, 2:2, 3:3
        diagonal_container = [1 for player_move in player_moves_list if player_move[0] == player_move[1]]

        if sum(diagonal_container) == 3:
            return True 
        else:
            return False
    
    def check_opposite_diagonal(self):
        #if moves are 0:2, 1,1 and 2,0 - opposite diagonal, then x + y + 1 = 3 so filtering these moves matching this condition out to a container 
        opposite_diagonal_container = [1 for player_move in player_move_list if player_move[0] + player_move[1] + 1 == 3]

        if sum(opposite_diagonal_container) == 3:
            return True
        else:
            return False
        

    

    
