# Basic KMK code for the WannaBe Engineering 3x3 macropad
# To customize your keymap, and all other possibilities visit https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md
# Big thanks to the team at KMK for providing their code to the public

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

kb = KMKKeyboard()
xxxxx = KC.NO

kb.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
kb.modules = [encoder_handler]
encoder_handler.pins = ((board.GP4, board.GP3, None, True),)

kb.col_pins = (board.GP13, board.GP12, board.GP1)
kb.row_pins = (board.GP2, board.GP11, board.GP10, board.GP9)
kb.diode_orientation = DiodeOrientation.COL2ROW

kb.keymap = [
    [xxxxx, xxxxx, KC.MUTE,
     KC.N1, KC.N2, KC.N3,
     KC.N4, KC.N5, KC.N6,
     KC.N7, KC.N8, KC.N9
     ]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, xxxxx),)
]


if __name__ == '__main__':
    kb.go()