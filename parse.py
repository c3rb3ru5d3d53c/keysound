#!/usr/bin/env python

# Parse Config from MechVibes

import json
import soundfile as sfo
from soundfile import SoundFile
from pprint import pprint

keymap = {
  1: 'Esc',
  59: 'F1',
  60: 'F2',
  61: 'F3',
  62: 'F4',
  63: 'F5',
  64: 'F6',
  65: 'F7',
  66: 'F8',
  67: 'F9',
  68: 'F10',
  87: 'F11',
  88: 'F12',
  91: 'F13',
  92: 'F14',
  93: 'F15',
  41: '`',
  2: '1',
  3: '2',
  4: '3',
  5: '4',
  6: '5',
  7: '6',
  8: '7',
  9: '8',
  10: '9',
  11: '0',
  12: '-',
  13: '=',
  14: 'Backspace',
  15: 'Tab',
  58: 'CapsLock',
  30: 'A',
  48: 'B',
  46: 'C',
  32: 'D',
  18: 'E',
  33: 'F',
  34: 'G',
  35: 'H',
  23: 'I',
  36: 'J',
  37: 'K',
  38: 'L',
  50: 'M',
  49: 'N',
  24: 'O',
  25: 'P',
  16: 'Q',
  19: 'R',
  31: 'S',
  20: 'T',
  22: 'U',
  47: 'V',
  17: 'W',
  45: 'X',
  21: 'Y',
  44: 'Z',
  26: '[',
  27: ']',
  43: 'backslash',
  39: ';',
  40: "'",
  28: 'Enter',
  51: ',',
  52: '.',
  53: '/',
  57: 'Space',
  3639: 'PrtSc',
  70: 'ScrLk',
  3653: 'Pause',
  3666: 'Ins',
  3667: 'Del',
  3655: 'Home',
  3663: 'End',
  3657: 'PgUp',
  3665: 'PgDn',
  57416: '↑',
  57419: '←',
  57421: '→',
  57424: '↓',
  42: 'Shift',
  54: 'Shift',
  29: 'Ctrl',
  3613: 'Ctrl',
  56: 'Alt',
  3640: 'Alt',
  3675: 'Meta',
  3676: 'Meta',
  3677: 'Menu',
  69: 'NumLock',
  3637: '/',
  55: '*',
  74: '-',
  3597: '=',
  78: '+',
  3612: 'Enter',
  83: '.',
  79: '1',
  80: '2',
  81: '3',
  75: '4',
  76: '5',
  77: '6',
  71: '7',
  72: '8',
  73: '9',
  82: '0',
}

cfg = json.loads(open('/home/c3rb3ru5/Tools/mechvibes/src/audio/cherrymx-red-abs/config.json', 'rb').read())

def write_key(input: str, offset: int, duration: int, output: str):
    sf = SoundFile(input)
    sf.seek(int((offset / 1000) * sf.samplerate))
    data = sf.read(int((duration/1000) * sf.samplerate))
    sfo.write(output, data, sf.samplerate)
    sf.close()

for k, v in cfg['defines'].items():
    write_key(
        input='/home/c3rb3ru5/Tools/mechvibes/src/audio/cherrymx-red-abs/sound.ogg',
        offset=v[0],
        duration=v[1],
        output=f'output/{k}.ogg'
    )

# for k, v in keymap.items():
#     print(f'"{v.lower()}": "{k}.wav",')

# with SoundFile('mechvibes/src/audio/cherrymx-red-abs/out.wav', 'r+') as sf:
#     data, sr = sf.read()
#     sf.seek(2464 * sr / 1000)

# sf.write('dump.wav', data, sr)

#pprint(keymap)
