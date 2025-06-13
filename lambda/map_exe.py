# a=10
# add= lambda a,b:a+b
# print(add)

# a=lambda a,b:a*b
# print(a(3,4))

# x=lambda a,b:a/b
# print(x(10,5))

# product_prices=[98,198,298,398,498]
# for product in range(len(product_prices)):
#     product_prices[product]+=1
# print(product_prices)

# enames=['rahul','sonia','priya']
# new_ename=[]
# for ename in enames:
#     new_ename.append(ename.upper())
# print(new_ename)

# product_prices=[98,198,298,398,498]
# new_prices=[]
# for price in product_prices:
#     new_prices.append(price+1)
# print(new_prices)

# product_prices=[98,198,298,398,498]
# product_prices=list(map(lambda x:x+1,product_prices))
# print(product_prices)

# product_prices=[98,198,298,398,498]
# new_price=[]
# def add_prices(price):
#     return price+1
# for price in product_prices:
#     new_price.append(add_prices(price))
# print(new_price)

# numbers=[1,2,3,4,5,6,7]
# Squared=list(map(lambda x:x**2,numbers))
# print(Squared)

# #Convert String into Uppercase
# words=['apple','banana','cauli']
# print(list(map(lambda x :x.upper(),words)))

# #Add Constant number
# numbers=[10,20,30,40]
# print(list(map(lambda x: x+10,numbers)))

# #Using multiple Iterable
# list1=[1,2,3]
# list2=[10,20,30]
# print(list(map(lambda x,y:x+y,list1,list2)))

# #string length
# words=['cat','dog','revanth']
# print(list(map(lambda x:len(x),words)))

# #conditional transformation
# num=[1,2,3,4,5,6,7,8,9]
# result=list(map(lambda x:x*2 if x%2==0 else x,num))
# print(result)

#Nested Data Transformation
nested_list=[['apple','ant'],['banana','ball'],['cherry']]
result=list(map(lambda sublist: [s[0] for s in sublist],nested_list))
print(result)