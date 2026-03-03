AI Programming Assignments
**Programming Individual Assignment

Assignment Overview
Assignment	Topic	Files
1	Turing Test and CAPTCHA	turingtest.py, captcha.py
2	Missionaries and Cannibals Search	missionaries_cannibals.py
Assignment 1: Turing Test (turingtest.py)
Simulates the Turing Test — a judge tries to tell apart a human and a bot from their responses.

Components:

BotPlayer — gives scripted, robotic answers
Judge — scores responses for bot signals, decides HUMAN or BOT (suspicion >= 40% = BOT)
How to Run:

python turingtest.py
Sample Output:

  Q: Do you have feelings?
  Bot   : I process sentiment data.
  Judge : BOT (suspicion: 40%)
  Human : Yes, I feel happy, sad, excited.
  Judge : HUMAN (suspicion: 0%)
Assignment 1: CAPTCHA (captcha.py)
Implements a CAPTCHA system that blocks bots and allows humans through.

Type	Example	Tests
Math	Solve: 14 + 7 = ?	Arithmetic
Logic	What comes after Tuesday?	Common knowledge
Text	Type: R X X R W	Character recognition
How to Run:

python captcha.py
Sample Output:

  Type      : Math CAPTCHA
  Challenge : Solve: 2 - 14 = ?
  Bot   answered ??? -> FAIL
  Human answered -12 -> PASS
Assignment 2: Missionaries and Cannibals (missionaries_cannibals.py)
3 missionaries and 3 cannibals must cross a river (boat holds max 2). Cannibals must never outnumber missionaries on either bank.

Algorithms:

Algorithm	Strategy	Optimal?	Memory
BFS	Queue, level by level	Yes	Higher
DFS	Stack, deepest first	Not guaranteed	Lower
IDDFS	Repeated depth-limited DFS	Yes	Lower
How to Run:

python missionaries_cannibals.py
Sample Output:

   0. Left[3M 3C] <boat> ~~~~        Right[0M 0C]
   1. Left[3M 1C]        ~~~~ <boat> Right[0M 2C]
  11. Left[0M 0C]        ~~~~ <boat> Right[3M 3C]

  Algorithm    Steps   Nodes    Time(ms)
  BFS             11      15      0.0348
  DFS             11      12      0.0278
  IDDFS           11      66      0.2565
Files
File	Description
turingtest.py	Turing Test simulation
captcha.py	CAPTCHA with Math, Logic, Text challenges
missionaries_cannibals.py	BFS, DFS, IDDFS on river crossing problem
README.md	This file
Requirements
Pure Python 3 — no external libraries needed.
