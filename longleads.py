from random import *


i = int(raw_input())

heads = 0;
tails = 0;
h_leads = 0;
t_leads = 0;

for i in range(0,i):
	r = randint(0,1)
        print(r)
	if r == 0:
		heads = heads + 1
 		if(heads >= tails):
			h_leads = h_leads + 1
	else:
		tails = tails + 1
		if(tails >= heads):
			t_leads = t_leads + 1
	print(heads)
	print(tails)

print("final leads")
print(h_leads)
print(t_leads)
	
