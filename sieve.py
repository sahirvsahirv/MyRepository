
#Try another with while loops

##maxnum = int(input('Enter the number you want to print primes till: '))
###Creata an array of maxnum zeroes
###to avoid index out of range
##sieve = [0]*(maxnum+1)
##primes = [2]
###print(sieve)
##
###2 is a prime - set to one and 1 is neither even nor prime so set to 1
##sieve[0] = 1
##sieve[1] = 0
##
##
###Outer loop - loop through each number in the range
###Inner loop - loop through multiples of i, post i
###Condition  - Only loop when i is not already a multiple
##for i in range(1, maxnum+1):
##    #Corner condition for primes of 2
##    if(i == 1):
##        #multiples of 2 so start with 4, the next multiple
##        #since 2 is marked
##        #already and go with multiple of i+1 that is 2
##        for multiples in range((i+1)*2, maxnum+1, i+1):
##            sieve[multiples-1]=1
##        #if i is 1, for multiples of 2. If it is done go to 3
##        continue
##    #if in the beginning itself you know i==4 is a multiple, skip
##    #Saves time
##    if(sieve[i] == 1):
##            continue
##    #start with the next immediate multiple - for 3 start with 6
##    for multiples in range((i+1)*2, maxnum+1, i+1):
##        #If already a mult5iple - skip
##        #6 is already a multiple of 2, now it can
##        #be a multiple of 3 too
##        if(sieve[i] == 1):
##            continue
##        sieve[multiples-1]=1
##    #print(sieve)    
##    
##for i in range(2,maxnum):
##    #sieve[0] is for 1 and sieve[1] is for 2
##    if(sieve[i]==0):
##        #print(i+1)
##        primes.append(i+1)
##
##print(primes)

#Time for timing the code
#sys for exiting, when imported from a module
import time
import sys
#without comments
primes = [2]

def sieve(maxnum):
    sieve = [0]*(maxnum+1)
    
    sieve[0] = 1
    sieve[1] = 0
    
    for i in range(1, maxnum+1):
        if(sieve[i] == 1):
                continue
        for multiples in range((i+1)*2, maxnum+1, i+1):
            if((sieve[i] == 1) and (i!=1)):
                continue
            sieve[multiples-1]=1
    

    for i in range(2,maxnum):
        if(sieve[i]==0):
            primes.append(i+1)


#If not imported and run from the command line
if __name__ == '__main__':
    maxnum = int(input('Enter the number you want to print primes till: '))
    start = time.time()
    sieve(maxnum)
    print('time taken = {}'.format(time.time() - start))
    print(primes)
#__name__ == module name
else:
    sys.exit("not for importing")
