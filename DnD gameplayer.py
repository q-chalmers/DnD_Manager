#!/usr/bin/python
import random
import json

class Monster:

    def __init__(self,name,type,ac,HP,speed,STR,STR_mod,DEX,DEX_mod,CON,CON_mod,INT,INT_mod,WIS,WIS_mod,CHA,CHA_mod,saves,dmg_imu,condi_imu,skills,sense,languages,cr,traits,actions,lActions,):
        self.name=name
        self.type=type
        self.ac=ac
        self.HP=HP
        self.speed=speed
        self.STR=STR
        self.STR_mod=STR_mod
        self.DEX=DEX
        self.DEX_mod=DEX_mod
        self.CON=CON
        self.CON_mod=CON_mod
        self.INT=INT
        self.INT_mod=INT_mod
        self.WIS=WIS
        self.WIS_mod=WIS_mod
        self.CHA=CHA
        self.CHA_mod=CHA_mod
        self.saves=saves
        self.dmg_imu=dmg_imu
        self.condi_imu=condi_imu
        self.skills=skills
        self.sense=sense
        self.lanuages=languages
        self.cr=cr
        self.traits=traits
        self.actions=actions
        self.lActions=lActions

    def iniative(self):
        return roll(1,20,self.DEX_mod)

data =open('monsters.json')
search = input("what creature are you looking for?")
book = json.load(data)
#its a LIST of DICTS
query = 0

for i in range(len(book)):
   if(book[i]['name']== search):
        query = i
if(query ==0): print('we werent able to find that monster')
else: print(book[query]['name']+' number is '+ str(query))


#index to get each value. will need to find a formula where i enter the


def roll(amount,dice,bonus):
    #the amount is the number of dices your rolling. so for 2d6 its 2
    #the type which dice
    #if there is a bonus. it can be 0

    total = 0
    for i in range(1,amount):
        total+= random.randint(1,dice)
    return total+bonus

def makeMonster(theBook,theQuery):
    creature = Monster(theBook[theQuery]['name'],theBook[theQuery]['meta'],theBook[theQuery]['Armor Class'],theBook[theQuery]['Hit Points'],theBook[theQuery]['Speed'],theBook[theQuery]['STR'],theBook[theQuery]['STR_mod'],theBook[theQuery]['DEX'],theBook[theQuery]['DEX_mod'],theBook[theQuery]['CON'],theBook[theQuery]['CON_mod'],theBook[theQuery]['INT'],theBook[theQuery]['INT_mod'],theBook[theQuery]['WIS'],theBook[theQuery]['WIS_mod'],theBook[theQuery]['CHA'],theBook[theQuery]['CHA_mod'],theBook[theQuery]['Saving Throws'],theBook[theQuery]['Damage Immunities'],theBook[theQuery]['Condition Immunities'],theBook[theQuery]['Skills'],theBook[theQuery]['Senses'],theBook[theQuery]['Languages'],theBook[theQuery]['Challenge'],theBook[theQuery]['Traits'],theBook[theQuery]['Actions'],theBook[theQuery]['Legendary Actions'])
    return creature

print(makeMonster(book,query))




#may need to do a mass edit of the json file. 
