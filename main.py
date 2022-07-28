from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.configure(bg='#e8f0fe')
root.title('YouTube video downloader')

Label(root, text='YouTube Video Downloader', font='Modern 20 bold', bg='#ddcff0').pack()

link = StringVar()

Label(root, text='Paste Link Here:', font='Modern 15 bold', bg='#ad80ea').place(x=180, y=60)
link_enter = Entry(root, width=55, textvariable=link).place(x=30, y=95)


def Downloader():
    path = '/home/olga/Загрузки'
    url = YouTube(str(link.get()))
    video = url.streams.filter(adaptive=True).first()
    video.download(path)
    Label(root, text='DOWNLOADED', font='Modern 15', bg='#87c34c').place(x=195, y=200)


Button(root, text='DWONLOAD', font='arial 15 bold', bg='#6823b7', padx=2, command=Downloader).place(x=210, y=150)

root.mainloop()
