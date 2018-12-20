#!/usr/bin/python
import random
import json

class Monster:

    def __init__(self,name,meta,ac,hp,speed,str,str_mod,dex,dex_mod,con,con_mod,int,int_mod,wis,wis_mod,cha,cha_mod,saves,skills,dmg_vul,dmg_res,dmg_imu,condi_imu,sense,languages,cr,traits,actions,lActions,reActions):
        self.name = name
        self.meta = meta
        self.ac = ac
        self.hp = hp
        self.speed = speed
        self.str = str
        self.str_mod=str_mod
        self.dex=dex
        self.dex_mod=dex_mod
        self.con=con
        self.con_mod=con_mod
        self.int=int
        self.int_mod=int_mod
        self.wis=wis
        self.wis_mod=wis_mod
        self.cha=cha
        self.cha_mod=cha_mod
        self.saves=saves
        self.skills=skills
        self.dmg_vul=dmg_vul
        self.dmg_res=dmg_res
        self.dmg_imu=dmg_imu
        self.condi_imu=condi_imu
        self.sense=sense
        self.lanuages=languages
        self.cr=cr
        self.traits=traits
        self.actions=actions
        self.lActions=lActions
        self.reActions=reActions

    def iniative(self):
        return roll(1,20,self.DEX_mod)

data = open('monsters.json')
search = input("what creature are you looking for?")
book = json.load(data)
#its a LIST of DICTS
query = 0

for i in range(len(book)):
   if book[i]['name'] == search:
        query = i
if query ==0: print('we werent able to find that monster')
else: print(book[query]['name']+' number is '+ str(query))


#index to get each value. will need to find a formula where i enter the


def roll(amount,dice,bonus):
    #the amount is the number of dices your rolling. so for 2d6 its 2
    #the type which dice
    #if there is a bonus. it can be 0

    total = 0
    for i in range(0,amount):
        total+= random.randint(1,dice)
        print(total)
    return total+bonus

def makeMonster(theBook,theQuery):
    creature = Monster(theBook[theQuery]['name'],theBook[theQuery]['meta'],theBook[theQuery]['Armor Class'],theBook[theQuery]['Hit Points'],theBook[theQuery]['Speed'],theBook[theQuery]['STR'],theBook[theQuery]['STR_mod'],theBook[theQuery]['DEX'],theBook[theQuery]['DEX_mod'],theBook[theQuery]['CON'],theBook[theQuery]['CON_mod'],theBook[theQuery]['INT'],theBook[theQuery]['INT_mod'],theBook[theQuery]['WIS'],theBook[theQuery]['WIS_mod'],theBook[theQuery]['CHA'],theBook[theQuery]['CHA_mod'],theBook[theQuery]['Saving Throws'],theBook[theQuery]['Skills'],theBook[theQuery]['Damage Vulnerabilities'],theBook[theQuery]['Damage Resistances'],theBook[theQuery]['Damage Immunities'],theBook[theQuery]['Condition Immunities'],theBook[theQuery]['Senses'],theBook[theQuery]['Languages'],theBook[theQuery]['Challenge'],theBook[theQuery]['Traits'],theBook[theQuery]['Actions'],theBook[theQuery]['Legendary Actions'],theBook[theQuery]['Reactions'])
    return creature

monster = (makeMonster(book,query).meta)

print(roll(2,10,2))





