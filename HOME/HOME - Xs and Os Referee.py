##Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
##
##But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
##
##x-o-referee
##
##A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
##
##Input: A game result as a list of strings (unicode).
##
##Output: "X", "O" or "D" as a string.
##
##Example:
##
##checkio([
##    "X.O",
##    "XX.",
##    "XOO"]) == "X"
##checkio([
##    "OO.",
##    "XOX",
##    "XOX"]) == "O"
##checkio([
##    "OOX",
##    "XXO",
##    "OXX"]) == "D"
##
##How it is used: The concepts in this task will help you when iterating data types. They can also be used in game algorithms, allowing you to know how to check results.

def checkline(line):
    if "X" in line and not "O" in line and not "." in line:
        return "X"
    elif "O" in line and not "X" in line and not "." in line:
        return "O"
    else:
        return "D"
    
def checkio(game_result):
    for line in game_result:
        if checkline(line) != "D":
            return checkline(line)
    diag1 = ""
    diag2 = ""
    for i in range(len(game_result)):
        col = ""
        for j in range(len(game_result)):
            col += game_result[j][i]
            if i == j:
                diag1 += game_result[j][i]
            if j == 0 and i+1 == len(game_result) or j == len(game_result) // 2 and i == len(game_result) // 2 or i == 0 and j+1 == len(game_result):
                diag2 += game_result[j][i]
        if checkline(col) != "D":
            return checkline(col)
    if len(diag1) == len(game_result) and checkline(diag1) != "D":
        return checkline(diag1)
    if len(diag2) == len(game_result) and checkline(diag2) != "D":
        return checkline(diag2)         
    return "D"
            
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

