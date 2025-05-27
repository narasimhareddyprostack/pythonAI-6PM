ba = bytearray([10,20,30,40])
#index           0  1  2  3
ba[2] =33
print(ba)  #bytearray(b'\n\x14!(')

for ele in ba:
    print(ele)