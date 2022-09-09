# Win_Every_Tetris_Game

Python script which allows to gather the best next move from a given Tetris picture.

# OpenCV

Before suggesting the next best move, the 'mode_test.jpg' image must be processed. This is done by a succession of image processing such as: wrapping the tetris grid into a new model, extrapolate every cells and finally thanks to the model (weights.h5) the script is able to convert every bin into a corrisponding ['X', 'O', ''] understandable by the tetris algorithm.

# Tetris Algorithm

The next best move is based on the number of current 'X' or 'O'. If the number 'X' > 'O' then the algorithm suggests the next best 'O' move, otherwise the next best 'X' move. The best move is found thanks a min-max algorithm which prune the tree and return the best result in a very fast time. Other solution can be explored but the min-max solution is by far the most simple and efficient solution.

# Libraries
<ul>
<li>cv2</li>
<li>numpy</li>
<li>matplotlib</li>
<li>operator</li>
<li>os</li>
<li>tensorflow</li>
</ul>
