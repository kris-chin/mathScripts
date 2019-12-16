import rsa

for x in range(0,21):
    print("x: " + str(x) + " is_prime: " + str(rsa.is_prime(x)))
