from math import sqrt, floor

def inverse_mod(value,mod,limit):
    #computes the inverse mod through the method of linear combinations
    #finds multiples of both value and mod until limit
    for alpha in range(0, limit):
        for beta in range(0, limit):
            if (alpha*value - beta*mod == 1): return alpha
    print("couldn't find inverse with limit = " + str(limit))
    return 0

def is_prime(value):
    #returns true if value is prime, returns false if not
    #uses sieve of eratosthenes

    checked_primes = []
    for n in range(2,value):
        #print("Checked: " + str(checked_primes))
        #first check if it is a multiple of the checked primes
        checked = False
        for prime in checked_primes:
            if n%prime == 0:
                checked = True
                break
        if checked == True:
            checked = False
            continue
        else:
            if value%n == 0: 
                return False
            else:
                checked_primes.append(n)
    return True


def find_d(publicKey,limit):
    #bruteforce cracks a public key
    #publicKey is a tuple of (e,n)
    #limit is the largest value you should text for primes
    e = publicKey[0]
    n = publicKey[1]
    d = 1

    #we have to guess two primes p & q that their produc is equal to n
    p = 0
    q = 0

    foundPrimes = False
    for i in range(0,limit):
        for j in range(0,limit):
            #first make sure p and q are prime
            if (is_prime(p) and is_prime(q)):
                if p*q == n:
                    foundPrimes = True
                    break #found p & q. exit the loop
            q += 1
        if foundPrimes == True: break
        else:
            p += 1
            q = 0
    
    if foundPrimes == True: #found our primes. we can compute d
        print('p: ' + str(p) + ' q: ' + str(q))
        totient_n = (p-1)*(q-1)
        try:
            d = inverse_mod(e,totient_n,limit) #d is equal to the inverse of e mod totient_q
        except:
            d = 1

    else:
        print('p and q could not be found. d is set to 1')

    return d

def decrypt(value,privateKey):
    #privateKey is a tuple of (d,n)
    d = privateKey[0]
    n = privateKey[1]
    return (value**d)%n

def encrypt(value,publicKey):
    #publicKey is a tuple of (e,n)
    e = publicKey[0]
    n = publicKey[1]
    return (value**e)%n