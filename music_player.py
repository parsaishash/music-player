import os
import numpy as np
import time
#import pickle
import pygame
import tkinter as tk
from tkinter import filedialog, Text, ttk
from tkinter import*
from PIL import Image, ImageTk
from PIL import*
#from scipy.ndimage.measurements import label
#from scipy.misc import toimage
#import matplotlib.image as mg
from functools import partial
from mutagen.mp3 import MP3
#import sys
#from io import BytesIO
from mutagen.id3 import ID3
pygame.mixer.init()


############            root           #############
root=tk.Tk()

container = ttk.Frame(root)
canvas = tk.Canvas(container, height=350, width=640)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
###############            images           ################
imgstop=ImageTk.PhotoImage(Image.open('/home/parsa/icons/pa.png'))
imgplay=ImageTk.PhotoImage(Image.open('/home/parsa/icons/p2.png'))
imgnext=ImageTk.PhotoImage(Image.open('/home/parsa/icons/next.png'))
imgback=ImageTk.PhotoImage(Image.open('/home/parsa/icons/back.png'))
imgpl=ImageTk.PhotoImage(Image.open('/home/parsa/icons/pl.png'))
imgpla=ImageTk.PhotoImage(Image.open('/home/parsa/icons/pla.png'))
imgplus=ImageTk.PhotoImage(Image.open('/home/parsa/icons/plus.png'))
imgfol=ImageTk.PhotoImage(Image.open('/home/parsa/icons/fol.png'))
imgsl=ImageTk.PhotoImage(Image.open('/home/parsa/icons/select.png'))
imgit=ImageTk.PhotoImage(Image.open('/home/parsa/icons/itunes.png'))
imgsn=ImageTk.PhotoImage(Image.open('/home/parsa/icons/skip_next.png'))
imgsb=ImageTk.PhotoImage(Image.open('/home/parsa/icons/skip_back.png'))
#imgitb=ImageTk.PhotoImage(Image.open('/home/parsa/icons/itb.png'))
imgrp=ImageTk.PhotoImage(Image.open('/home/parsa/icons/rp.png'))
imgitm=ImageTk.PhotoImage(Image.open('/home/parsa/icons/itm.png').resize((40,40), Image.ANTIALIAS))
imgitm2=ImageTk.PhotoImage(Image.open('/home/parsa/icons/itm.png').resize((200,200), Image.ANTIALIAS))
imgitb=ImageTk.PhotoImage(Image.open('/home/parsa/icons/itb.png').resize((150,150), Image.ANTIALIAS))
imgpm=ImageTk.PhotoImage(Image.open('/home/parsa/icons/pm.png').resize((40,40), Image.ANTIALIAS))

on=Image.open('/home/parsa/icons/toggleon.png').resize((40,40), Image.ANTIALIAS)
imn=Image.open('/home/parsa/icons/togglein.png').resize((40,40), Image.ANTIALIAS)
off=Image.open('/home/parsa/icons/toggleoff.png').resize((40,40), Image.ANTIALIAS)


imgon=ImageTk.PhotoImage(on)
imgimn=ImageTk.PhotoImage(imn)
imgoff=ImageTk.PhotoImage(off)
'''

tags=ID3('Wannabe.mp3')

if (tags.get("APIC:"))!=None:
    print("lllllll")
    
    im=ImageTk.PhotoImage(Image.open(BytesIO(tags.get("APIC:").data)).resize((40,40), Image.ANTIALIAS))
    Button(root,image=im,bg="cyan2").pack()
'''
####################################################################################################


######################## var #########################
everysongs=[]
songs_shuffle=[]
playlistsong=[]
button = list()
i2=0
c2=0
c=0
i=0  #thats important int!
time=0
ij=0
ss=0
bimage=[]
bimageb=[]
sample_rate=0
a1=0
bc=0
tt=0
st=""
bigimagedict={}
minimagedict={}

##################################################
for file in os.walk("/home/parsa/Music"):
        for f in file:
            for f2 in f:
                if f2.endswith(".mp3"):
                    print("__________________________________________________________")
                    print(f2)
                    f2=str(f2)
                    if f2[:-4]!="":
                        s="/home/parsa/Music/"+f2
                        everysongs.append(s)
                        if ID3:
                            tags=ID3(s)
                            if (tags.get("APIC:"))!=None:
                                print(".........image add")
                                im=ImageTk.PhotoImage(Image.open(BytesIO(tags.get("APIC:").data)).resize((40,40), Image.ANTIALIAS))
                                im2=ImageTk.PhotoImage(Image.open(BytesIO(tags.get("APIC:").data)).resize((150,150), Image.ANTIALIAS))
                            else:
                                im=imgitm
                                im2=imgitb

                            bigimagedict[s]=im2
                            minimagedict[s]=im
                            bimage.append(im)
                            bimageb.append(im2)



songs2=[]
songsfile=open("songs.txt","r+")
for line in songsfile:
        songs2.append(line[:-1])




###############################################################################################################


def ti():
    global tt,c
    if c%2==1:
        tt=tt+1
    root.after(1000,ti)

v2 = StringVar()
Label(root, textvariable=v2).place(x=138,y=373)
v2.set("00:00")

v3 = StringVar()
Label(root, textvariable=v3).place(x=480,y=373)
v3.set("00:00")

v5 = StringVar()
Label(root, textvariable=v5).pack()
v5.set("     ")

v4 = StringVar()
Label(root, textvariable=v4).place(x=0,y=148)
v4.set("None")



#imf=tk.Label(root, image=imgitb).place(x=570,y=352)


def klik(n):
    global i, c
    i=n
    c=0
    playsong()





def s(son):
    global st,button,bimage, songs
    button=[]
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    d=tk.Label(scrollable_frame,text="                     ",font=("Courier", 10),compound="left").grid(column=0)  
    d2=tk.Label(scrollable_frame,text="name",font=("Courier", 10),compound="left").place(x=230,y=0)
    d3=tk.Label(scrollable_frame,text="time",font=("Courier", 10),compound="left").place(x=600,y=0)
    for i in range(0,len(son)):
        song=str(son[i])
        ss2=MP3(song)
        time22=float(ss2.info.length)
        mn22=int(time22/60)
        sc22=int(time22-(mn22*60))
        if sc22<10:
            lt22=str(mn22)+":0"+str(sc22)
        else:
            lt22=str(mn22)+":"+str(sc22)
        
        st=(song.split('/')[-1][:-4])
        if len(st)>15:
            st=st[:15]+"..."
        st=st+(46-len(st))*" "+lt22
        songs=son
        button.append(tk.Button(scrollable_frame,bg="gray93",image=minimagedict[song],text=st,font=("Courier", 10),compound="left",bd='0', command=partial(klik, i)))
        button[-1].grid(column=1,sticky="nw")

s(everysongs)

def playsong():
    global c,sample_rate,tt,a1,button,bc
    global i,ss,time,l,bimageb
    if i>=(len(songs)):
        i=i-len(songs)
    if c!=0:
        if c%2==1:
            pygame.mixer_music.pause()
            playsong1.config(text='play',image=imgplay)
            c=c+1
        else:
            pygame.mixer_music.unpause()
            playsong1.config(text='pause',image=imgstop)
            c=c+1
    else:
        pygame.mixer.quit()
        sample_rate=MP3(songs[i%(len(songs))]).info.sample_rate
        pygame.mixer.init(sample_rate)
        pygame.mixer_music.load(songs[i%(len(songs))])
        ss=MP3(str(songs[i%(len(songs))]))
        time=float(ss.info.length)
        mn2=int(time/60)
        sc2=int(time-(mn2*60))
        if sc2<10:
            lt2=str(mn2)+":0"+str(sc2)
            v3.set(str(lt2))
        else:
            lt2=str(mn2)+":"+str(sc2)
            v3.set(str(lt2))
        

        s=songs[i%(len(songs))]
        st=(s.split('/')[-1][:-4])
        if len(st)>20:
            st=st[:20]+"..."
        v4.set(st)
        #notif="notify-send deMusic "+(song.split('/')[-1][:-4])+" -i "+"/home/parsa/icons/mu.png"
        #os.system(notif)
        button[bc].config(bg="gray95")
        button[i].config(bg="cyan2")
        bc=i
        ibc.config(image=bigimagedict[songs[i]])
        i=i+1
        print("songs: ",i)
        pygame.mixer_music.play()
        playsong1.config(text='pause',image=imgstop)
        pygame.mixer_music.queue(songs[i%(len(songs))])
        c=c+1
        tt=0
    if a1==0:
        a1=a1+1
        ti()
        que()

def find():
    filename1=filedialog.askopenfilename(initialdir="/home/parsa",title="Select File")
    playlistsong.append(filename1)
    print(filename1)
    for song in songs:
        label=tk.Label(root2,text=song,bg="gray")
        label.pack()
##########################################################play list########################################################################################
def playlist_f():
    print("ddd")
    root2=tk.Tk()
    container2 = ttk.Frame(root2)
    canvas2 = tk.Canvas(container2, height=200, width=260,bg="purple1")
    scrollbar2 = ttk.Scrollbar(container2, orient="vertical", command=canvas2.yview)
    scrollable_frame2 = ttk.Frame(canvas2)
    scrollable_frame2.bind(
        "<Configure>",
        lambda e: canvas2.configure(
            scrollregion=canvas2.bbox("all")
        )
    )

    canvas2.create_window((0, 0), window=scrollable_frame2, anchor="nw")
    canvas2.configure(yscrollcommand=scrollbar2.set)
    container2.pack()
    canvas2.pack(side="left", fill="both", expand=True)
    scrollbar2.pack(side="right", fill="y")
    #######################################################
    playlistsong=[]
    songs2=[]
    button2=list()
    i2=0
    c2=0
    


    for file in os.walk("/home/parsa/Music"):
            for f in file:
                for f2 in f:
                    if f2.endswith(".mp3"):
                        print(f2)
                        f2=str(f2)
                        if f2[:-4]!="":
                            s="/home/parsa/Music/"+f2
                            songs2.append(s)
    def klik2(n):
       print(n)
       button2[n].configure(bg='orange red')
       playlistsong.append(songs2[n])
       print(playlistsong)
    def s2():
        for widget in scrollable_frame2.winfo_children():
            widget.destroy()
        for i in range(0,len(songs2)):
            song=str(songs2[i])
            button2.append(tk.Button(scrollable_frame2,bg="lawn green",text =(song.split('/')[-1][:-4])+(80-len(song[18:-4]))*" ",font=("Courier", 10),compound="left", command=partial(klik2, i)))
            button2[-1].grid(column=0,sticky="nw")

    root2.after(1,s2)
    ##########################################
    
    sl2=tk.Button(root2, text="done", command=quit).pack(side="right")
    name=tk.Label(root2,text='name:').pack(side='left')
    e=tk.Entry(root2).pack(side='left')
    root2.mainloop()
################################################################play list###############################################################################################
'''def song():
    global songs
    filename=filedialog.askopenfilename(initialdir="/home",title="Select File")
    if filename!=():
        if filename not in songs:
            print(filename)
            songs.append(filename)
    
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for i in range(0,len(songs)):
        song=str(songs[i])
        
        button.append(tk.Button(scrollable_frame,bg="cyan2",image=imgitm,text =(song.split('/')[-1][:-4])+(80-len(song[18:-4]))*" ",font=("Courier", 10),compound="left", command=partial(klik, i)))
        button[-1].grid(column=0,sticky="nw")'''
####################
def previous():
    global c,tt
    global i
    c=0
    if tt>10:
        i=i-1
        playsong()
    else:
        i=i-2
        playsong()
####################
def nextf():
    global i
    global c
    c=0
    playsong()
####################
def sn():
    global tt
    tt=tt+15
    pygame.mixer_music.set_pos(tt)
#####################
def sb():
    global tt
    if (tt-15)>0:
        tt=tt-15
        pygame.mixer_music.set_pos(tt)
    else:
        tt=0
        pygame.mixer_music.set_pos(tt)
#####################
def rp():
    global ij
    if ij==0:
        print("replay is on")
        ij=1
    else:
        print("replay is off")
        ij=0
    


#####################
def pc(event):
    global time, tt
    tt=((event.x)*time)/300
    pygame.mixer_music.set_pos(tt)
    v['value']=(tt*100)/time
    mn=int(tt/60)
    sc=tt-(mn*60)
    if sc<10:
        lt=str(mn)+":0"+str(int(sc))
        v2.set(str(lt))
    else:
        lt=str(mn)+":"+str(int(sc))
        v2.set(str(lt))


def que():
    global i, c,t2,time,tt,ij
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        c=0
        tt=0
        if ij==1:
            i-=1
        print(i)
        playsong()
        v['value']=0
    else:
        ########## progresbar cionfiguring!!
        if c%2==1:
            v['value']=(tt*100)/time
            mn=int(tt/60)
            sc=tt-(mn*60)
            if sc<10:
                lt=str(mn)+":0"+str(int(sc))
                v2.set(str(lt))
            else:
                lt=str(mn)+":"+str(int(sc))
                v2.set(str(lt))
            
    root.after(1000,que)
############################################################


v=ttk.Progressbar(root, orient = HORIZONTAL,length = 300) 
v.pack()
v.bind('<Button-1>',pc)
v.bind('<B1-Motion>',pc)
def cch22(event):
        root.config(cursor="target")
v.bind('<Enter>',cch22)

def cursorchange(event):
        root.config(cursor="arrow")
v.bind('<Leave>',cursorchange)




ibc=tk.Label(root,image=imgitb,compound="t")
ibc.place(x=-1,y=-1)

ibc2=tk.Label(root,text="_____________________")
ibc2.place(x=0,y=165)

playsong1=tk.Button(root, text="play",image=imgplay, padx=0,pady=0,fg="white",bd='0', command=lambda: playsong())
playsong1.pack()

nextkey=tk.Button(root, text=">",image=imgnext, padx=10,pady=5,fg="white",bd='0',command=nextf).place(x=353,y=400)
previouskey=tk.Button(root, text="<",image=imgback, padx=10,pady=5,fg="white",bd='0',command=previous).place(x=267,y=400)

#snkey=tk.Button(root, text=">",image=imgsn,command=sn,bd='0',fg="white").place(x=407,y=400)
#sbkey=tk.Button(root, text="<",image=imgsb,command=sb,bd='0',fg="white").place(x=212,y=400)
plba=0
def plb():
        global plba, bc, i, c, tt
        i=0
        bc=0
        if plba%2 == 0:
                s(songs2)
                plb.config(text="  every songs")
        else:
                s(everysongs)
                plb.config(text="    play list ")
        c=0
        tt=0
        playsong()
        
        plba+=1

plb=tk.Button(root,text="    play list",image=imgpla,compound="left",command=plb)
plb.place(x=0,y=200)
######### events
def e1(event):
    playsong()
root.bind('<space>',e1)

def e2(event):
    nextf()
root.bind('<Right>',e2)

def e3(event):
    previous()
root.bind('<Left>',e3)
#########################################################################

lon=tk.Label(root,image=imgoff)
lon.place(x=600,y=370)
aon=1
def ca():
      global aon
      rp()
      
      if aon%2 == 0:
          cab.config(image=imgoff)
      else:
          cab.config(image=imgon)
      aon += 1


cab=tk.Button(root,image=imgoff,bd='-5',command=ca)
cab.place(x=600,y=370)

def f(event):
    print(event)

scrollable_frame.bind('<Button-1>',f)
#rpb=Button(root,image=imgrp,command=rp,bg='gray').place(x=500,y=400)

#file.add_command(label='add song',command=song,image=imgsl,compound="left")
#file.add_cascade(menu=playlist,label='playlist',image=imgpl,compound="left")
'''
pla.add_command(label='play lists',image=imgpla,compound="left")
pla.add_command(label='new playlist',command=playlist_f,image=imgplus,compound="left")

playlist.add_command(label='play lists',image=imgpla,compound="left")
playlist.add_command(label='new playlist',command=playlist_f,image=imgplus,compound="left")'''
#####################################################

root.resizable(0, 0) 
root.title('music player')
root.iconphoto(False, tk.PhotoImage(file='/home/parsa/icons/mu.png'))

root.mainloop()