import os
import tkinter as tk
from tkinter import messagebox as msgb

EmuPath = "C:/Users/asus/AppData/Local/Citra/nightly-mingw/citra-qt.exe"
_3dsFile = "./JSAB.3dsx"

def main():
    global code, root
    curDir = os.path.abspath('.')
    print(curDir)

    code = os.system("make") #Compile

    root = tk.Tk()
    root.withdraw()
    if(code != 0):
        input()
        exit(-1)
    else:
        succes()

def fail():
    msgb.showerror("Error",
    f"""
    Make Compilation FAILED !
    you can try to debug it via the console.
    
    Error code : {code}.""")
def succes():
    #root.after(timeout, root.destroy)
    Ask = msgb.askokcancel('Info', "Launching Citra ?", master=root)
    if not Ask:
        msgb.showwarning(root,"User stopped launch")
        exit()
    print("Opening Citra")
    os.system(EmuPath + " " + _3dsFile)

if __name__ == "__main__":
    main()