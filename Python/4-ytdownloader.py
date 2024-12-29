
import yt_dlp

from tkinter import filedialog
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Youtube Video İndirme Sihirbazı")

def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)    
    
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="İndirilecek klasörü belirtiniz", command=browse_button)
button2.grid(row=0, column=3)    


mainframe = ttk.Frame(root, padding="15 15 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


url = StringVar()
url_entry = ttk.Entry(mainframe, width=40, textvariable=url)
url_entry.grid(column=2, row=1, sticky=(W, E))
    

def download():
    global url
    url = url.get()
    folder = folder_path.get()

    if not url:
        print("Please enter a valid YouTube link.")
        return
    if not folder:
        print("Please specify a download folder.")
        return

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'quiet': False,  # Set to True to hide logs
            'noplaylist': True,  # Disable playlist downloading
            'progress_hooks': [lambda d: print(d)],  # Optionally display download progress
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")



ttk.Button(mainframe, text="İndir", command=download).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

mainloop()