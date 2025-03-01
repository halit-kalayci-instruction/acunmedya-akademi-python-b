# fonksiyonlar-methodlar

#kodun yeniden kullanılabilirliğini artırmak ve bakımını kolaylaştırmak için kullanılır.

price = 100
total_price = price + (price*0.2)
print(total_price)

# fonksiyon tanımlamak
#parametre => fonksiyona çağırılma aşamasında verilen veri.

# default parameter => rate=20 -> rate gönderilirse gönderilen değeri, gönderilmez ise 20'i kullan.
# required parameter, default parameter
# default parameter, required parameter
def calculate_tax(price, rate=20): #void -> dönüş tipi olmayan # return -> dönüş tipi (int,str)
    return price + (price * (rate / 100))

print("***")
price1 = calculate_tax(100) #print
price2 = calculate_tax(200) # toplam fiyatı alıp başka bi değerle (kargo fiyatı) ile topla
price3 = calculate_tax(500)
price4 = calculate_tax(100, 10)
price5 = calculate_tax(1000, 10)

print(price1)
print(price2+50)
print("****")

def sum(*args): # sayilar
    if len(args) <= 0:
        raise ArithmeticError("En az 1 argüman zorunludur") #hata yönetimi
    sonuc = 0
    for sayi in args:
        sonuc += sayi
    return sonuc

print(sum(1,2,3,4,5,6,7,8,9,10))
print(sum(5,10))
print(sum(5))
#print(sum())

# **kwargs -> araştırma ve uygulama

# lamdba fonksiyonlar
# tek satırlık fonksiyonları kısaca tanımlama yöntemi.
topla = lambda a,b: a+b

def topla2(a,b):
    return a+b

selamla = lambda isim: print(f"Merhaba, {isim}")

print(topla(3,5))
selamla("Halit")

# oop, modules, pip -> basic python # 1mart
# python for AI -> Pandas,Numpy,Matplotlib # 1marttan sonraki hafta
# vscode -> jupyter notebook


