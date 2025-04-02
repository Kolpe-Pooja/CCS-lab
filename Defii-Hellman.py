p=int(input("Enter the prime number::"))

q=int(input("Enter the primitive root::"))

XA=int(input("Enter the private key of sender(A)::"))
XB=int(input("Enter the private key of Receiver(B)::"))

print("private key of sender(A)::",XA)
print("private key of receiver(B)::",XB)

#Calculate the public ey of A and B
YA=int(pow(q,XA,p))  #Public key of A
YB=int(pow(q,XB,p))  #Public key of A
print("public key of sender(A)::",YA)
print("public key of receiver(B)::",YB)

#Calculate the SHARED SECRET Key of A and B
KA=int(pow(YB,XA,p))
KB=int(pow(YA,XB,p))
print("Secret key of sender(A)::",KA)
print("Secret key of receiver(B)::",KB)

