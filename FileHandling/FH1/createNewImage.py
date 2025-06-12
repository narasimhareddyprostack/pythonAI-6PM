fp1=open('Python.jpg','rb')

data=fp1.read()

fp2=open('pc.jpg','bw')
fp2.write(data)
print("New Image Created")
fp2.close()
fp1.close()