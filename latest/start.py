import os
cont=1
for x in range(0, 200, 16):
    command='python3 new_bot.py '+str(x)+' '+str(x+15)
    os.system(command)
    
    cont=cont+1