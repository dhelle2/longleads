from random import *

print("enter desired number of coin flips:")
i = int(raw_input())

heads = 0;
tails = 0;
h_leads = 0;
t_leads = 0;
ties = 0;
no_leader = 0;

for i in range(0,i):
        print("flip number: " + str(i+1))
	r = randint(0,1)
        print("flip: " + str(r))
	if r == 0:
		heads = heads + 1
	if r == 1:
		tails = tails + 1
        if(heads > tails):
			h_leads = h_leads + 1
	if(tails > heads):
			t_leads = t_leads + 1
        if heads == tails:
		ties = ties + 1
	print("heads " + str(heads))
	print("tails " + str(tails))
        print()

print("final heads/tails counts:")
print("heads " + str(heads))
print("tails " + str(tails))
#print("final leads")
print("heads was winning after " + str(h_leads) + " flips")
print("tails was winning after " + str(t_leads) + " flips")
print("and there were " + str(ties) + " ties.")	
