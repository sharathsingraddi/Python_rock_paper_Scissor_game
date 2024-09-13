import random
comp=random.randint(0,2)
user=int(input("please select 0 for rock,1 for paper,2 for scissor"))
def check(user,comp):
    if comp==user:
        return 0
    if (comp==1 and user==0):
        return -1
    elif(comp==2 and user==1):
        return -1
    elif(comp==0 and user==2):
        return -1
    return 1

print(comp)
score=check(comp,user)
if(score==0):
    print('its a draw')
elif(score==-1):
    print('comp won game')
else:
    print('you won the game')