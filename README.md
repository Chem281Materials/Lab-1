# 💻 CHEM 281 Lab: Text Editors, IDE's, & Development

## 🧪 Goal

The goal of this lab is to:

1. Familiarize yourself with **text editors and IDE's**.
2. Learn how to use **basic VIM commands**. 
3. Practice using **VIM** to fix bugs in a puzzle game.

---

## 🗂️ Provided

- A `docker` file to set up the dev environment.
- A complete terminal based puzzle game with 2 bugs in `app.py`.

---

## 💻 Setup
```bash
./docker_build.sh # You may need to chmod +x
./docker_run.sh # You may need to chmod +x
python3 app.py
```

You should be able to view the puzzle game!
```
root@be16e2180eab:/repo# python3 app.py
8-Puzzle Game
Use WASD to move tiles, q to quit.

+---+---+---+
| 5 | 2 | 8 |
+---+---+---+
| 7 | 4 | 1 |
+---+---+---+
|   | 3 | 6 |
+---+---+---+
Move (w/a/s/d):
```

## ✅ Tasks

### Find and fix bugs
This is a simple puzzle game where you type w/a/s/d to move the missing tile. It is following typical action movement in video games where w is for up, s is for down, a is left and d is right. The goal is to arrange the tiles in the following formation:
```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+
🎉 Puzzle solved!
```
If you are successful, the game should print `🎉 Puzzle solved!`, and then exit giving you back control of the terminal.

There are 2 bugs hidden amongst the game code which you need to solve using the `VIM` text editor. The first bug is that currently there are no boundary conditions for the game. This means that you can wrap around from top to bottom and left to right like a rubik's cube. This makes the game much easier and is not the current functionality, fix it so that there are boundary conditions and moves that try to `wrap` around are illegal and should print a statement when they are attempted. The second bug is less obvious but while you're playing around with the game you should run into it eventually.

Fix both bugs to create a fully functioning terminal based game!

### Extra time
Look into the docker file and the bash scripts to get a sense of how the environment is set up and how environment variables are being passed around.
