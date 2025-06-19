import requests,json
fp=open('beauty.json','w')

#Extract Data

data=requests.get('https://dummyjson.com/products')
product_data=data.json()
print(type(product_data))  #<class,dict>
products=product_data['products']
print(type(products))      #<class,list>
print(len(products))

#Transform
beauty_products=[]

for product in products:
    if product['category'] =='beauty':
        beauty_products.append(product)
print(len(beauty_products))


#Load
json.dump(beauty_products,fp)

print("New file Created!")

fp.close()