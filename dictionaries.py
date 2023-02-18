notlar={"Deniz":80, "Ege":75, "Gizem":95}
print(notlar["Ege"])
notlar["Mert"]=58
print(notlar)
ogrenciler={"Deniz":{"not":80, "ogrenci_no":703}, "Ege":{"not":75, "ogrenci_no":704}, "Gizem":{"not":95, "ogrenci_no":705}}
print(ogrenciler["Deniz"]["not"])

message="Merhaba, orda mısın?"
s=set(message)
print(s)

for i in range(3):
    print("Iteration: ", i)
    
l=['limon','portakal','elma']
"-".join(l)
print("-".join(l))

squares=[i*i for i in range(1,11)]
print(squares)

odd_squares=[e for e in squares if e %2==1]
print(odd_squares)

x,_=(4,7)
print(x)
adlar=['eda','seda','meda','heda']
for i, e in enumerate(adlar):
    print(i, "indexindeki eleman: ", e)

adlar=['eda','seda','meda','heda']
for i, e in enumerate(adlar, start=1):
    print(i, "indexindeki eleman: ", e)