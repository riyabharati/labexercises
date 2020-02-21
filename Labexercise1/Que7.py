"""You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph; then run
 the next two at15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?"""

homedistance = 4
busspeed = 25
stoptime= 2
numofstop = 10
journeytime = (busspeed/homedistance)*60+(stoptime*numofstop) #minutes
firstjog = 7
secondjog = 15
lastjog =7
jogtime = (firstjog/homedistance + secondjog/homedistance + lastjog/homedistance)*60 #minutes
if journeytime >jogtime:
    print("jogging will be quicker than the bus")
else:
    print("jogging will be slower than the bus")