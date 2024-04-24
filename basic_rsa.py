import math


def find_coprime(phi):
    e = 11  # Common choice for e in RSA for efficiency reasons
    while e < phi:
        if math.gcd(e, phi) == 1:
            return e
        e += 2  # Increment by 2 to ensure e stays odd; no even number can be coprime with phi(n) if phi(n) is even
    return None  # If no coprime number is found within the loop, though very unlikely for typical values of phi

def find_d(e, phi):
    return pow(e, -1, phi)

# Set p and q

p = 29

q = 13

# Calculate m

n = p * q
print ("n = ", n)

# Calculate m
m = (p-1)*(q-1)

# Find coprime to m
e = find_coprime(m)
print ("e = ", e)


d = find_d(e, m)
print ("d = ", d, ". This is the private key")


# Let's encrypt
M1 = "This is now an optimized version of the code.... try it out!!!"
res = []
for each in M1:
    res.append(ord(each)**e%n)
print ("Let's encrypt ", M1)

#c = M1**e%n # Keep for ref
print (''.join(str(res)).replace(', ',''))

#M2 = c**d%n # Keep for ref

#Decrypt sample
dec = []
for each in res:
    dec.append(chr(each**d%n))

print (''.join(dec))
