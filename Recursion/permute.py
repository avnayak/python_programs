#!/usr/bin/env python

def perm(n, i):
    if i == len(n) - 1:
        print n
	#print "v"
    else:
        for j in range(i, len(n)):
	    print i
	    print j
            n[i], n[j] = n[j], n[i]
            perm(n, i + 1)	
            #n[i], n[j] = n[j], n[i] # swap back, for the next loop
        
perm([1, 2,3,4], 0)