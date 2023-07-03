x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6 

# kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir
a = int(input("sayı giriniz: "))
b = int(input("sayı giriniz: "))

print((a * b) - (z + y + x))

# y nin x e kalansız bölümü nedir
y //= x

print(y)

# x, y, z toplamının mod 3 ü nedir
f = (x+y+z)
f %=3 

print(f) 

# y nin x. kuvveti nedir
y **= x

print(y)

# x, *y, z = numbers işlemine göre z nin küpü kaçtır
x, *y, z = numbers 
z **= 3 

print(z)

# x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır 
x, *y, z = numbers 
g = y[0] + y[1] + y[2]

print(g)
