notlar = [78,89,65,90]
print(notlar[1])
print(notlar[1:3])
notlar[1]  +=5
print(notlar[1])
print(len(notlar))
'''notlar.append(25)
print(notlar)'''
notlar.extend([1,2,3])
print(notlar)
notlar.insert(0,100)
print(notlar)
notlar.remove(100)
print(notlar.pop(1))
print(notlar)
print(notlar.count(2))
print(notlar.index(1))
l2=notlar.reverse()
print(l2)
l3=sorted(notlar)
print(l3)

konum=(10,34 )