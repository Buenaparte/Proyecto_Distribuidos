quijote = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"

listica = quijote.split(",")
listica_ascii = []
listica_midi = []

for i in listica:
    ascii_lista = [ord(c) for c in i]
    valor_ascii = sum(ascii_lista)
    listica_ascii.append(valor_ascii)

min_valor = min(listica_ascii)
max_valor = max(listica_ascii)

for i in listica_ascii:
    valor_midi = ((i-min_valor)/(max_valor-min_valor))*127
    listica_midi.append(int(valor_midi))

print(listica) 
print("\n")
print(listica_ascii)
print("\n")
print(listica_midi)