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
    
    # == +e / +en / +er ==
    
    # lat + en = latten
    (r'^(.*[^aeiou][aeiou])([bdfgklmnprst]) \^ (e|en|er)$', r'\1\2\2\3'),
    # laat + en = laten
    (r'^(.*)aa([bdfgklmnprst]) \^ (e|en|er)$', r'\1a\2\3'),
    (r'^(.*)ee([bdfgklmnprst]) \^ (e|en|er)$', r'\1e\2\3'),
    (r'^(.*)oo([bdfgklmnprst]) \^ (e|en|er)$', r'\1o\2\3'),
    (r'^(.*)uu([bdfgklmnprst]) \^ (e|en|er)$', r'\1u\2\3'),
    
    # == diminutive ending +je ==
    # (rules taken from http://www.dutchgrammar.com/nl/?n=NounsAndArticles.16)
    
    # short or long vowel -> +tje
    (r'^(.*[^aeiou])?(a|o|u) \^ je$', r'\1\2\2tje'),
    (r'^(.*[^aeiou])?i \^ je$', r'\1ietje'),
    (r'^(.*[^aeiou])?y \^ je$', r"\1y'tje"),
    (r'^(.*)(a|e|i|o|u|ij|uw) \^ je$', r'\1\2tje'),
    # long vowel + r/l/n -> +tje
    (r'^(.*)(aa|ee|ie|oo|uu|aai|ai|au|ee|ei|eu|ie|ij|oe|ou|ui)([rln]) \^ je$', r'\1\2\3tje'),
    # unstressed er/el/en/or -> +tje
    # we can't distinguish stressed / unstressed, so do this for every word with at least five letters
    (r'^(.*..[^aeiou])(er|el|en|or) \^ je$', r'\1\2tje'),
    
    # long vowel + m -> +pje
    (r'^(.*)(aa|ee|ie|oo|uu|aai|ai|au|ee|ei|eu|ie|ij|oe|ou|ui)m \^ je$', r'\1\2mpje'),
    # lm/rm -> +pje
    (r'^(.*)(l|r)m \^ je$', r'\1\2mpje'),
    # unstressed em/um -> +pje
    # we can't distinguish stressed / unstressed, so do this for every word with at least five letters
    (r'^(.*..[^aeiou])(em|um) \^ je$', r'\1\2pje'),
    
    # unstressed ing -> +kje
    # we can't distinguish stressed / unstressed, so do this for every word with at least six letters
    (r'^(.*..[^aeiou])ing \^ je$', r'\1inkje'),
    
    # short vowel + r/l/n/m/ng -> +etje
    (r'^(.*[^aeiou])?(a|e|i|o|u)(r|l|n|m) \^ je$', r'\1\2\3\3etje'),
    (r'^(.*[^aeiou])?(a|e|i|o|u)ng \^ je$', r'\1\2ngetje'),
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
