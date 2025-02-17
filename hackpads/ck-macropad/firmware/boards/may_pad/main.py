from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

media = MediaKeys()
layers = Layers()

keyboard.extensions = [media]
keyboard.modules = [layers]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# fmt:off
keyboard.keymap = [
    [
        KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        KC.P7,   KC.P8,   KC.P9,   _______,
        KC.P4,   KC.P5,   KC.P6,   KC.PPLS,
        KC.P1,   KC.P2,   KC.P3,   _______,
        _______, KC.P0, KC.PDOT,   KC.PENT,
        ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
