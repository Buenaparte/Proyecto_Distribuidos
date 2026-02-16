import mido
from mido import Message, open_output

def enviar_midi(nota):
    # puerto MIDI de salida
    # ahorita esta para abrir un puerto random pero se puede cambiar por el nombre del puerto que se quiera usar
    with open_output('puerto_midi') as puerto:
        mensaje = Message('note_on', note=nota, velocity=64, duracion=0.3)
        puerto.send(mensaje)
        
        mido.sleep(1)

        mensaje = Message('note_off', note=nota, velocity=64, duracion=0.3)
        puerto.send(mensaje)