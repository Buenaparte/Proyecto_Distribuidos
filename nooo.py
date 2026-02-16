#para que funcione deben copiar el text del quijote ced en la carpeta del proyecto

import mido
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo, second2tick
from puerto_midi import enviar_midi

# medios para crear una archivo midi ademas de elementos basicos para que suene este archivo
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('key_signature', key='Dm'))
track.append(MetaMessage('set_tempo', tempo=bpm2tempo(127)))
track.append(MetaMessage('time_signature', numerator=6, denominator=8))
track.append(Message('program_change', program=12, time=10))

def Quijote():
    # listas para almacenar los valores ascii y midi
    listica = []
    listica_ascii = []
    listica_midi = []

  # lectura del archivo de texto y conversion a ascii y suma de los valores ascii para cada linea, luego normalizacion de estos valores a un rango de 0 a 127 para convertirlos en notas midi
    with open('Don Quijote de la Mancha - Miguel de Cervantes Saavedra Adap Trapiello (arreglado 2).txt', 'r', encoding='utf-8') as archivo:
     for i in archivo:
         listica = i.split(".")
         print(listica)
         for j in listica:
             ascii_lista = [ord(c) for c in j ]
             valor_ascii = sum(ascii_lista)
             listica_ascii.append(valor_ascii)

    min_valor = min(listica_ascii)
    max_valor = max(listica_ascii)

 # conversion de los valores ascii a midi utilizando la formula de normalizacion 
    for i in listica_ascii:
        valor_midi = ((i-min_valor)/(max_valor-min_valor))*127
        listica_midi.append(int(valor_midi))

        # en tiempo real se envia la nota midi utilizando la funcion enviar_midi del puerto_midi.py
        enviar_midi(int(valor_midi))

 # creacion de las notas midi utilizando la lista de valores midi antes normalizados
    for i in listica_midi:
        track.append(Message('note_on', channel=2, note=1, velocity=i, time=1))
        track.append(Message('note_off', channel=2, note=1, velocity=i, time=2))

 #guardado del archivo midi
    mid.save('Quijote.mid')

Quijote()
