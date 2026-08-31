#!/usr/bin/env python3
"""命令行入口 - MIDI 解析与可视化 CLI"""

import argparse
import json
import sys
import os

# 使用相对导入（包内导入）
from .core.midi_parser import parse_midi


def main():
    parser = argparse.ArgumentParser(
        description="hesym: MIDI file parser and visualizer - extract notes, stats, and more"
    )
    parser.add_argument("file", help="要解析的 MIDI 文件路径")
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出原始数据")
    parser.add_argument("--stats", action="store_true", help="显示统计信息（总音符数、时长等）")
    parser.add_argument("--limit", type=int, default=20, help="显示前 N 个音符 (默认 20)")
    parser.add_argument("--fix-vel", type=int, default=0, help="将力度为0的音符修正为指定值 (例如 100)")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"❌ 错误: 文件 '{args.file}' 不存在", file=sys.stderr)
        sys.exit(1)

    try:
        notes, total_ticks, bpm, ticks_per_beat, time_sig = parse_midi(args.file)
    except Exception as e:
        print(f"❌ 解析 MIDI 失败: {e}", file=sys.stderr)
        sys.exit(1)

    # ---- 力度修复 ----
    if args.fix_vel > 0:
        for note in notes:
            if note.velocity == 0:
                note.velocity = args.fix_vel

    # ---- 输出逻辑 ----
    if args.json:
        data = {
            "format": "hesym_core",
            "ticks_per_beat": ticks_per_beat,
            "bpm": bpm,
            "time_signature": time_sig,
            "total_ticks": total_ticks,
            "note_count": len(notes),
            "notes": [
                {
                    "pitch": n.pitch,
                    "name": n.pitch_name,
                    "start_tick": n.start_tick,
                    "duration_ticks": n.duration,
                    "velocity": n.velocity
                } for n in notes
            ]
        }
        print(json.dumps(data, indent=2))
    elif args.stats:
        total_sec = total_ticks / ((bpm / 60.0) * ticks_per_beat)
        pitches = [n.pitch for n in notes]
        print(f"📊 MIDI 统计报告")
        print(f"   🎵 音符总数: {len(notes)}")
        print(f"   ⏱️  总时长: {total_ticks} ticks ≈ {total_sec:.2f} 秒")
        print(f"   🎚️  BPM: {bpm:.1f}")
        print(f"   📏  PPQ (每拍Tick数): {ticks_per_beat}")
        print(f"   🎼 拍号: {time_sig}")
        if pitches:
            print(f"   🎹 音域: {min(pitches)} -> {max(pitches)}")
        if args.fix_vel > 0:
            print(f"   🔧 已将所有力度 0 修正为 {args.fix_vel}")
    else:
        # 默认表格显示
        print(f"\n🎵 解析成功！共读取 {len(notes)} 个音符 (显示前 {min(args.limit, len(notes))} 个):\n")
        print(f"{'Note':<6} {'Pitch':<5} {'Start':<10} {'Dur':<8} {'Vel'}")
        print("-" * 40)
        for n in notes[:args.limit]:
            print(f"{n.pitch_name:<6} {n.pitch:<5} {n.start_tick:<10} {n.duration:<8} {n.velocity}")
        if len(notes) > args.limit:
            print(f"... (以及其余 {len(notes) - args.limit} 个音符)")

if __name__ == "__main__":
    main()
