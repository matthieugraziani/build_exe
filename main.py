import tkinter as tk
from tkinter import messagebox
import webbrowser
from updater import check_for_updates

root = tk.Tk()
root.title("Mon Application")

upd = check_for_updates()
if upd.get("available"):
    if messagebox.askyesno("Mise à jour disponible",
                           f"Version {upd['version']} disponible. Télécharger ?"):
        url = upd.get("download_url")
        if isinstance(url, str) and url:
            webbrowser.open(url)

label = tk.Label(root, text="Application exemple")
label.pack(padx=20, pady=20)

root.mainloop()
