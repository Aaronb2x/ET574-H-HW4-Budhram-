# ET574-H-HW4-Budhram-
Name: Aaron Budhram : QCC ID: 24814218

AI usage documentation:
AI Tool: Claude

Purpose: I used Claude to walk me through building the project step by step: the Die class, DiceGame class, play_round, the main() menu, and the git/commit workflow. It also helped me debug my code and brainstorm. Claude gave me the code for the die and dice game classes, main(), 3 tests, and I pasted them in and ran them, and fixed the bugs in the code and any mistakes I have made myself.

Prompts:
"Walk me through building it step by step"
"Do I run it in the terminal of main.py?"
I sent screenshots of my code and terminal and asked what was wrong
"Triple check that screenshot, make sure it's all good"
"Did I do it right?"
"explain the code"

Evaluation and Modifications: I read and tested all AI-suggested code before committing. When I pasted code, my typing dropped some underscores, and I fixed these after checking for myself, I changed init to __init__, name == "main" to __name__ == "__main__", and maxside to max_side.
I also fixed a wrongly indented roll method. I changed Die so it accepts both sides (used by the starter tests) and max_side (used in the assignment). I added a .gitignore to remove __pycache__. I ran the tests and the game to make sure everything works.

## B.Test Case Modifications
The starter file had 3 test cases, (die roll bounds, outcome evaluation, play_round structure). I added 3 more:
test_evaluate_roll_boundaries: checks 6 and 8 give "Roll Again" and 2 and 12 give "Lose", to catch off-by-one mistakes.
test_play_round_total_matches_dice: runs 50 rounds and checks total equals die1 + die2 and the result matches evaluate_roll(total).
test_custom_sided_die: checks Die(max_side=20) has 20 sides and rolls stay between 1 and 20.


## C. Reflection on AI Use
1. How was AI used?- Claude gave me the code in small steps and helped me debug typos from screenshots.

2. Which test suggestions were adopted, modified, or rejected?- I adopted all 3 suggested tests. I fixed mistakes in spelling in them (for _, max_side, a test name).

3. What modifications were made and why? I fixed the underscore and indentation bugs so the code would run, and made Die accept sides so the starter tests pass.

4. How were results verified? I ran python -m unittest test_dicegame -v (10 tests pass) and played the game with python main.py.

5. What did I learn? Unit tests catch bugs fast (like the __init__ problem), and AI code has to be read and looked over then tested, not just paste, another thing I have noticed is, small typos can break the program, even something very small like a capital letter.

