input_file = "C:\\Users\\janke\\Desktop\\template.txt"


f = open(input_file, 'r')
wczyt = f.read()
wczyt = wczyt.split()

print(wczyt)
