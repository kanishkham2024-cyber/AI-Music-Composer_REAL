<<<<<<< HEAD
import pretty_midi
import random

def generate_music(genre='classical', mood='happy', tempo=120):
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)

    start = 0
    for i in range(10):
        note_number = random.randint(60, 72)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start+0.5)
        piano.notes.append(note)
        start += 0.5

    midi.instruments.append(piano)

    output_path = 'output.mid'
    midi.write(output_path)
    return output_path
=======
import pretty_midi
import random

def generate_music(genre='classical', mood='happy', tempo=120):
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)

    start = 0
    for i in range(10):
        note_number = random.randint(60, 72)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start+0.5)
        piano.notes.append(note)
        start += 0.5

    midi.instruments.append(piano)

    output_path = 'output.mid'
    midi.write(output_path)
    return output_path
>>>>>>> deed5f4ef2e9571dcc2a7a6fd0bcb21cdc297718
