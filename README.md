# Moves-of-a-knight
2 little games with pawns and a knight

Game 1 (Moves_of_a_knight.py): Select a number of pawns between 1 and 63. Take the knight to capture the pawns, which do not move in this game. No feedback on minimum number of moves is provided.

Mod (Moves_of_a_knight_mod.py): Like game 1, however max number of pawns is 9 due to the high amount of calculations and index problems.
At the end, your moves are compared with the shortest path (which is calculated in a parallel thread).
If you uncomment the print statements at the end  you can obtain the (first possible) shortest path.

Game 2 (Moves_of_a_knight_8pawns.py): One knight and opposing 8 pawns are correctly distributed on the chess board. Pawns move forward and can capture the knight on a diagonal field in front. Knight must prevent a pawn becoming a queen.
