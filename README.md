# Dice Roller

My very first project using a GUI library.
A very basic single die, dice roller. Click the button to roll.

## Required libraries
Dice Roller uses the following libraries:
`random`
`tkinter`
`ttkbootstrap`

### Creating the executable
1) Ensure you have the prerequisite libraries imported.
2) `import os`, `import sys`
3) Access the ```MEIPASS.py``` file. Replace the lines in the original .py file
4) Ensure the .ico file is saved in the root dir
5) Run the following command:
   
``` pyinstaller -w --onefile --icon=dice.ico --add-data=dice.ico:. diceroller.py ```

6) Your executable will be saved under the ```./dist``` dir
   
> [!NOTE]
> Below is a helpful 'what does' on each argument

```-w``` launches program without terminal

```--onefile``` makes a single .exe file

```--icon-key=FILE``` sets the window icon

```--add-data=FILE:LOCATION``` compiles key.ico into program

