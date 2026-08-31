# core/midi_parser.py
import mido
from models.note import Note

def parse_midi(file_path: str):
    mid = mido.MidiFile(file_path)
    notes = []
    active_notes = {}
    cur_tick = 0
    bpm = 120.0
    ticks_per_beat = mid.ticks_per_beat
    time_sig = "4/4"

    for track in mid.tracks:
        for msg in track:
            cur_tick += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = cur_tick
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    notes.append(Note(msg.note, active_notes[msg.note], cur_tick - active_notes[msg.note], msg.velocity))
                    del active_notes[msg.note]
            elif msg.type == 'set_tempo':
                bpm = mido.tempo2bpm(msg.tempo)
            elif msg.type == 'time_signature':
                time_sig = f"{msg.numerator}/{msg.denominator}"
    
    return notes, cur_tick, bpm, ticks_per_beat, time_sig
