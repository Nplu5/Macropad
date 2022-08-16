# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_macropad import keycodes as Keycode # REQUIRED if using Keycode.* values

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'PowerToys', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x300000, 'ESC', [Keycode.ESCAPE]),
        (0x300030, 'Colorpicker', [Keycode.WINDOWS, 'C']),
        (0x000000, '', []),
        # 2nd row ----------
        (0x000000, '', []),
        (0x073010, 'Autostart', [Keycode.LEFT_ALT, Keycode.SPACE]),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x303017, 'Zones', [Keycode.WINDOWS, 'Ö']),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x172030, 'Shortcuts', [Keycode.WINDOWS, Keycode.SHIFT, '\'']),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ],
    'logo': './logos/Windows.bmp'
}
