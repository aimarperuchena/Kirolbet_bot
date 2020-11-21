cont=1
for x in range(0, 200, 16):
    call='xterm  -T BOT_'+str(cont)+' -e python3 new_bot.py '+str(x)+' '+str(x+15)+' & '
    with open('launch2.sh', 'a') as the_file:
        the_file.write(call)
    cont=cont+1
