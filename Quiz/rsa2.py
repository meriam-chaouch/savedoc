from Crypto.Util.number import *
n=631371953793368771804570727896887140714495090919073481680274581226742748040342637
e=65537
c=421345306292040663864066688931456845278496274597031632020995583473619804626233684
p=1461849912200000206276283741896701133693
q=431899300006243611356963607089521499045809
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
