# models/note.py
"""MIDI 音符数据模型"""


class Note:
    """MIDI 音符对象

    Attributes:
        pitch: 音高 (0-127)
        start_tick: 起始 tick
        duration: 持续时间 (tick 数)
        velocity: 力度 (0-127)
        pitch_name: 音名，如 "C4" (自动计算)
    """

    def __init__(self, pitch: int, start_tick: int, duration: int, velocity: int):
        self.pitch = pitch
        self.start_tick = start_tick
        self.duration = duration
        self.velocity = velocity
        self.pitch_name = self._midi_to_name(pitch)

    def _midi_to_name(self, midi_note: int) -> str:
        """将 MIDI 音高编号转换为音名，如 60 -> C4"""
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        return f"{notes[midi_note % 12]}{(midi_note // 12) - 1}"

    def __repr__(self) -> str:
        return f"Note(pitch={self.pitch}, name={self.pitch_name}, start={self.start_tick}, dur={self.duration}, vel={self.velocity})"
