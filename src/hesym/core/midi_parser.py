# core/midi_parser.py
"""MIDI 文件解析核心模块

依赖: mido (pip install mido)
"""

import mido
from ..models.note import Note  # 改用相对导入


def parse_midi(file_path: str):
    """
    解析 MIDI 文件，返回音符列表和元数据

    Args:
        file_path: MIDI 文件路径

    Returns:
        tuple: (notes, total_ticks, bpm, ticks_per_beat, time_sig)
            - notes: Note 对象列表
            - total_ticks: 总 tick 数
            - bpm: 速度 (Beats Per Minute)
            - ticks_per_beat: 每拍 tick 数 (PPQ)
            - time_sig: 拍号字符串，如 "4/4"

    Raises:
        FileNotFoundError: 文件不存在时
        ValueError: 解析失败时
    """
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
                    notes.append(Note(
                        pitch=msg.note,
                        start_tick=active_notes[msg.note],
                        duration=cur_tick - active_notes[msg.note],
                        velocity=msg.velocity
                    ))
                    del active_notes[msg.note]
            elif msg.type == 'set_tempo':
                bpm = mido.tempo2bpm(msg.tempo)
            elif msg.type == 'time_signature':
                time_sig = f"{msg.numerator}/{msg.denominator}"

    return notes, cur_tick, bpm, ticks_per_beat, time_sig
