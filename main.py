print("Hello World")

# değişkenler
name = "Halit" #string, str
print(name)
# python=> type-safe olmayan bir dildir.
age = 25 # integer,int
print(age)
print(type(age))
age = "abc"
print(age)
#
print(type(age))

# operatörler
# matematiksel (aritmetik) operatörler
rate = 49.56 #float,double

print(1+1)
print(5-2)
print(25/5) # bölme işlemi
print(5*5)
print(30//5) # tam bölme işlemi (aşağıya yuvarlar)
print(36 % 5) # mod alma operatörü
print(5**3) # üssü almak

a = 'Abc'
b = "Abc"
#
# atama operatörleri
a = "abc"
number = 5
print(number)

number += 5 # number = number + 5
number -= 2
print(number)
number /= 4 #float
number *= 10
print(number)
#


#karşılaştırma operatörleri

is_valid = True #bool,boolean
print(1==1)
print(1!=1)
print(10 > 5)
print(10 >= 10)
#


# mantıksal operatörler, => and,or,not
# and => iki tarafında true olması dışındaki tüm durumları false yapar
print("mantıksal operatörler -")
print( 1==1 and 1==2 ) # true & false => false
print( 1==1 and 10>5 ) # true & true => true
print( 1!=1 and 5>10 ) # false & false => false

print( 1==1 or 5 > 10 ) #  true | false -> true
print( 1!=1 or 5 > 10 ) # false | false -> false


print( ( 1==1 and 2>5 ) or 6>6 and (10 > 5 or 5 == 5)  )

print(not 1==1)
print(1!=1)
#

students = ["Salih","Bayram","Muhammet","Ahmed", 1, True, 50.5]
print(students)
students.append("Fatma")
print(students)
students.pop()
print(students)

# indexing
print(students[0])
#print(students[50]) # hata aldı ve kapandı
print("Merhaba")
#

# reference type vs value type
print("**** 22.02.2025 *****")
a=1
b=a
b += 10
print(a)
print(b)

list1 = ["Ahmet","Azra","Emine"]
list2 = list1

list2.append("Fatma")

print(list1)
print(list2)

# reference-value type
#immutable-mutable

# döngüler - iterasyon (iteration)
for i in range(5): #indentation,indent #for X adet satırla çalışabilir
    print(i)
    print("Merhaba")
print("For bitti")

print("****")
for i in range(5,10):
    print(i)

for i in range(5,50,2):
    print(i)

# { }

print("****")

#dongüyü kırmak => manual bitirmek
for i in range(0, 100):
    if i == 50:
        break #bu iterasyonda bu satırdan aşağısını çalıştırmadan döngüyü bitir.
    print(i)
print("***")
for i in range(0,100):
    if i == 50:
        continue # bu iterasyonda bu satırdan aşağısını çalıştırmadan sonraki iterasyona geç
    print(i)
# iteration,index
for student in list1:
    if student == "Emine":
        continue
    print(student)

# while
# koşullarla çalışır
# sonsuz döngü tehlikesi


i=5
while i<=10:
    i += 1
    if i == 6:
        continue
    print(i)

    
#while True: #infinite loop
    #print("While...")


# şart-koşul blokları
age=18
# kural1=> tek çıktı!!
# kural2=> yukarıdan aşağıya ilk doğru koşul
if age >= 18:
    print("Giriş yapabilirsiniz")
elif age == 18:
    print("Ay kontrolü yapılıyor...")
else:
    print("Giriş yapamazsınız..")

#

#

