k = open('kitters.jpg','rb').read()
c = open('cattos.jpg','rb').read()

flag = ""

for a, b in zip(k,c):
	if a != b:
		flag += b

print flag