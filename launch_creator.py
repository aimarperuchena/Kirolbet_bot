cont=1
for x in range(1, 4000, 300):
    call='xterm  -T BOT_'+str(cont)+' -e python3 bot_params.py '+str(x)+' '+str(x+100)+' & '
    print('xterm  -T BOT_'+str(cont)+' -e python3 bot_params.py '+str(x)+' '+str(x+100)+' & ')
    with open('launch2.sh', 'a') as the_file:
        the_file.write(call)
    cont=cont+1
