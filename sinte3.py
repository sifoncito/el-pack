import pygame as pg
import time

def play_sound(letter):
    global clk
    f = "{}.mp3".format(letter)
    pg.mixer.music.load(f)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clk.tick(30)


pg.mixer.init()
pg.mixer.music.set_volume(1.0)

clk = pg.time.Clock()

text = input("Text: ")
for l in text:
    print(l)
    l = l.lower()
    if l in "abcdefghijklmnñopqrstuvwxyz":
        play_sound(l)
    else:
        time.sleep(1)
