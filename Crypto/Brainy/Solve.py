import binascii

#SPOILERS AHEAD IF YOU HAVE NOT SOLVED THE FIRST PART


#this script can be used to solve any RSA using chinese remainder algorithm. just replace p, q, dp, dq, c with your values.

p=  #your p value goes here 

q=  #your q value goes here

dp= #your dp value goes here 

dq= #your dq value goes here

c=  #your c value goes here

qinv = (1/q) % p 

m1 = pow(c, dp, p) % p

m2 = pow(c, dq, q) % q


message1 = binascii.unhexlify(format(m1, 'x')).decode()
message2 = binascii.unhexlify(format(m2, 'x')).decode()

print(message1)
print(message2)


#normally both messages would print the same, so you can just cut it short to a single message if you want
