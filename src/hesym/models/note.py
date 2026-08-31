# models/note.py
class Note:
    def __init__(self, pitch: int, start_tick: int, duration: int, velocity: int):
        self.pitch = pitch
        self.start_tick = start_tick
        self.duration = duration
        self.velocity = velocity
        self.pitch_name = self._midi_to_name(pitch)

    def _midi_to_name(self, midi_note: int) -> str:
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        return f"{notes[midi_note % 12]}{(midi_note // 12) - 1}"
