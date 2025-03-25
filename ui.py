import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import aithink as ait


def ai():
    user=chatin.get()
    mugiko=ait.generate_response(user)
    outchat.configure(text=mugiko)

switch_voice="false"

def voice():
    outchat.configure(text="ขณะนี้ ระบบคำสั่งด้วยเสียงยังไม่สามารถใช้งานได้")
    pass
    if switch_voice=="false":
        switch_voice="true"
        ait.listen()
    elif switch_voice=="true":
        pass


screen=ttk.Window(title="Mugiko",size=(500,400))
#screen.resizable(width=False, height=False)
screen.resizable(width=False, height=True)
screen.position_center()

outchat = ttk.Label(text="สวัสดีค่ะมีอะไรให้ช่วยไหมคะ", wraplength=300)
chatin=ttk.Entry()
chatin.focus()
sendbox=ttk.Button(text="Send",command=ai)
voicebox=ttk.Button(text="Voice",command=voice)

outchat.grid(row=1,column=1,padx=100,pady=100,columnspan=5)
chatin.grid(row=5,column=1,columnspan=4,padx=1)
sendbox.grid(row=5,column=5,padx=1)
voicebox.grid(row=5,column=6,padx=1)

screen.mainloop()
