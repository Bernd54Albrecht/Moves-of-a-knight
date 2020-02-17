# Moves-of-a-knight
2 little games with pawns and a knight

Game 1 (Moves_of_a_knight.py): Select a number of pawns between 1 and 63. Take the knight to capture the pawns, which do not move in this game. No feedback on minimum number of moves is provided.

Mod (Moves_of_a_knight_mod.py): Like game 1, however max number of pawns is 9 due to the high amount of calculations and index problems.
At the end, your moves are compared with the shortest path (which is calculated in a parallel thread).
If you uncomment the print statements at the end  you can obtain the (first possible) shortest path.

Game 2 (Moves_of_a_knight_8pawns.py): One knight and opposing 8 pawns are correctly distributed on the chess board. Pawns move forward and can capture the knight on a diagonal field in front. Knight must prevent a pawn becoming a queen.

Remarks on logic and maths:
I started with the study of Dijkstra's algorithm, which provides the shortest path from a start node to an end node.
Then went on with Floyd–Warshall algorithm iot visit all nodes. However, this method  is not necessary.
The Travelling salesman problem does not apply, because it returns to the starting node, when all nodes are visited.
I ended up with a Matrix of all possible moves of one knight on a chess board, and the permutations of the moves to visit all pawns. Due to the number of permutations = faculty(n)  the numer of pawns is limited to 9 in Game 1 mod.
