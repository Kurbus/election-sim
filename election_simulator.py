#your mom lol
#defining since python has a fit if i dont
can1=0
can0=0
#import random because the United States Electoral College might as well be random
import random as r 
for i in range(50):
 st = r.randint(0,1)
 if st==1: can1=can1+1
 elif st==0: can0=can0+1
if can1>can0: print("candidiate 1 won")
elif can1<can0: print("candidate 2 won")
