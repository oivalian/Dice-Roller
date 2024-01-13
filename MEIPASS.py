def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# window|root
root = ttk.Window(themename='darkly')
iconPath = resource_path('dice.ico')
root.iconbitmap(iconPath)
window.title('Dice Roller')
window.geometry("350x400")
window.maxsize(350, 400)
window.minsize(350, 400)


'''
replace lines 11-17 in diceroller.py with the above code

run command:
pyinstaller -w --onefile --icon=dice.ico --add-data=dice.ico:. diceroller.py
'''
