s=int(input("enter"))
print(abs(s))

x=-10
abs_x=abs(x)
print(abs_x)

a=10
b=15
print(abs(a-b))

expected=100
measured=98.6
error=abs(measured-expected)
if error:
    print("accepted with in range")

# data science and statistics
data=[2.1,2.9,3.0,2.8]
mean=sum(data)/len(data)
deviation=[abs(x-mean) for x in data]
print(deviation)

# Game Development(physics/Collisions)
player_pops=10
enemy_pops=-4
if abs(player_pops - enemy_pops) < 15:
    print("Enemy nearby")

#Complex Number Magnitude
z= 3 +4j
magnitude =abs(z)
print(magnitude)