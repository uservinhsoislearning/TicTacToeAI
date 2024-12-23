# TicTacToeAI - A Tic-Tac-Toe solver using AI algorithms

This repository is my project for the course IT3160E(Introduction to Artificial Intelligence).

Here are my algorithms:

- MiniMax algorithm

- AlphaBeta algorithm

- Monte Carlo Tree Search algorithm

This project runs on Python 3.10.6, and the GUI was done in the pygame library.

### Requirements

To run this, you need to download Python 3.10.6. You can download Python 3.10.6 using this [link](https://www.python.org/downloads/release/python-3106/). It can also run on later releases of Python (e.g. 3.11), however, it is recommended to run on this version. 

After that, you have to run this command to download the necessary libraries:
```
pip install -r requirement.txt
```

### How to play

Run this command:
```
python main.py
```

If this does not work, download VSCode and run it in VSCode. Remember to download the libraries above.

Firstly, there will be a popup window that looks like this:

![image](https://github.com/user-attachments/assets/178c14b8-9cb4-4ac4-a427-c3c8edba3ef7)

Click on one of the algorithms then wait for 1 second. Then the main game will go up and you can play Tic-Tac-Toe! You will always go first (as O) and the computer goes after (as X)

The colors display the state of the game. If the game ends in a win for you, the lines are colored green. If the game ends in a loss for you, the lines are colored in red. If the game ends in a draw, the lines are covered in blue. For example,

Lose:

![image](https://github.com/user-attachments/assets/b2735205-7213-45ed-88bd-39a8f034dce7)

Draw:

![image](https://github.com/user-attachments/assets/4f97cf2c-e6cd-4020-90b3-7f620cee8da5)

Win:

![image](https://github.com/user-attachments/assets/5b42eaf3-5007-4491-9f82-304930b7f88b)

While the game is running, you can press R to restart the game and click on the red X to exit the game.

## References
[Tic-Tac-Toe game and MiniMax algorithm](https://www.youtube.com/watch?v=LbTu0rwikwg&t=1946s)

[MCTS implementation](https://github.com/hayoung-kim/mcts-tic-tac-toe)

[What is the UCT (based on UCB1) algorithm?](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
