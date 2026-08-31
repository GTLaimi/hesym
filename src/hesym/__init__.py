"""
hesym - HesychiaMidS CLI tool
MIDI parsing and visualization in your terminal
"""

from .core.midi_parser import parse_midi
from .models.note import Note
from .cli import main

__all__ = [
    "parse_midi",
    "Note",
    "main",
]

__version__ = "0.1.0"
