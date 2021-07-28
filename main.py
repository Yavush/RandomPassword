import random
passlen = int(input("Şifrenizin uzunluğunu girin : "))
s = "abcçdefgğhıijklmnoöprsştuüvyzwxABCÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZWX1234567890"
p = "".join(random.sample(s,passlen))
print(p)