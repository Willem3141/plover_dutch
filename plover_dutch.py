KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '5-', '0-', '-E', '-U', '*')

SUFFIX_KEYS = ('-S', '-Z')

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '0-',
    '-F': '-6',
    '-P': '-7',
    '-L': '-8',
    '-T': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
    # == +en ==
    # lat + en = latten
    (r'^(.*[^aeiou][aeiou])([bdfgklmnprst]) \^ en$', r'\1\2\2en'),
    # laat + en = laten
    (r'^(.*)aa([bdfgklmnprst]) \^ en$', r'\1a\2en'),
    (r'^(.*)ee([bdfgklmnprst]) \^ en$', r'\1e\2en'),
    (r'^(.*)oo([bdfgklmnprst]) \^ en$', r'\1o\2en'),
    (r'^(.*)uu([bdfgklmnprst]) \^ en$', r'\1u\2en'),
]

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-F'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-L'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
    },
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : ('S1-', 'S2-'),
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'W-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-F'        : '-F',
        '-R'        : '-R',
        '-P'        : '-P',
        '-B'        : '-B',
        '-L'        : '-L',
        '-G'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-Z'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
}

DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ()
