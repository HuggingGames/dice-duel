"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

def new_game():return {'score':0,'cpu':0,'round':0,'done':False},"5 tur zar düellosu. 'at' yaz."
def play(s,action):
    if s['done']:return reply(s,'Yeni oyun başlat.')
    if action.strip().lower()!='at':return reply(s,"Zar atmak için 'at' yaz.")
    a=random.randint(1,6);b=random.randint(1,6);s['score']+=int(a>b);s['cpu']+=int(b>a);s['round']+=1
    msg=f"🎲 Sen {a} · bilgisayar {b} | {s['score']}-{s['cpu']} | Tur {s['round']}/5"
    return finish(s,msg) if s['round']==5 else reply(s,msg)
