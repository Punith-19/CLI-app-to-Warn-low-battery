import tkinter as tk
import threading
from tkinter import Tk, messagebox

class warning:
    @staticmethod
    def lowbattery(percent):
        # Run the GUI in a separate thread
        gui_thread = threading.Thread(target=warning._show_window, args=(percent,))
        gui_thread.daemon = True
        gui_thread.start()
    
    @staticmethod
    def _show_window(percent):
        root = Tk()
        icon_image = tk.PhotoImage(file="icon.png")
        root.withdraw()
        root.attributes('-topmost', True)
        messagebox.showwarning("Warning", f"Low Battery {percent}%")
        root.mainloop()