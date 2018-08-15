from plover.system import english_stenotype

KEYS = (
    'S-', 'C-', 'P-', 'T-', 'H-', '+-', 'M-', 'F-', 'R-', 'N-', 'L-', 'Y-',
    'O-', 'E-', '-A', '-U',
    'I',
    '-^', '-N', '-L', '-C', '-M', '-F', '-R', '-P', '-T', '-+', '-S', '-H'
)

IMPLICIT_HYPHEN_KEYS = ('O-', 'E-', '-A', '-U', 'I')

SUFFIX_KEYS = ('-R','-T','-S','-H',)

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'ULFTS'

ORTHOGRAPHY_RULES = [
    	# == +n ==      
		# EN: rad + n = raden
		(r'^(.*[bcdfghjklmnpqrstvwxz]) \^ n$', r'\1en'),
       
	# == +ns ==
		(r'^(.*[cdfghijklmnpqrstvwxz]) \^ ns$', r'\1ens'),
	
	# The following strokes are useful when folded suffixes
	# don't follow the expected behaviour. Maybe they are
	# problematic in some situations? Experience will tell...

	# == +H när -a ==
		(r'^(.*)a \^ a$', r'\1e'),

	# == +H när -e ==
		(r'^(.*)e \^ a$', r'\1a'),

	# == +R när -er ==
		(r'^(.*)er \^ er$', r'\1ar'),

	# == +R när -ar ==
		(r'^(.*)ar \^ er$', r'\1er'),

	# Possibly want to do something with -r -> -er and -t -> -et too??
	# Problem is, these don't seem to abide by rules to the same extent.	

	# Possibly something to avoid triple-consonants when applying certain
	# suffixes? For instance, fall + ler -> falller -> faller. AFAIK, this
	# only occurs when choosing the wrong suffix stroke, but protecting
	# against misstrokes in such a systematic way could be a good way of
	# doing things.
]

ORTHOGRAPHY_RULES_ALIASES = {

}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-': 'a',
        'C-': 'q',
        'P-': '2',
        'T-': 'w',
        'H-': 's',
        '+-': ('m', 'z', 'x', 'c'),
        'M-': '3',
        'F-': 'e',
        'R-': 'd',
        'N-': '4',
        'L-': 'r',
        'Y-': 'f',
        'O-': 'g',
        'E-': 'v',
        '-A': 'h',
        '-U': 'n',
        'I': 'b',
        '-^': (',', '.', '/'),
        '-N': '8',
        '-L': 'u',
        '-C': 'j',
        '-M': '9',
        '-F': 'i',
        '-R': 'k',
        '-P': '0',
        '-T': 'o',
        '-+': 'l',
        '-S': ';',
        '-H': 'p',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('1', '5', '6', '7', 't', 'y', '[', ']', '-', '=', '\'', '\\'),
    },
    'Palantype': {
        'S-': 'S-',
        'C-': 'C-',
        'P-': 'P-',
        'T-': 'T-',
        'H-': 'H-',
        '+-': ('+1-', '+2-'),
        'M-': 'M-',
        'F-': 'F-',
        'R-': 'R-',
        'N-': 'N-',
        'L-': 'L-',
        'Y-': 'Y-',
        'O-': 'O-',
        'E-': 'E-',
        '-A': '-A',
        '-U': '-U',
        'I': 'I',
        '-^': ('-^1', '-^2'),
        '-N': '-N',
        '-L': '-L',
        '-C': '-C',
        '-M': '-M',
        '-F': '-F',
        '-R': '-R',
        '-P': '-P',
        '-T': '-T',
        '-+': '-+',
        '-S': '-S',
        '-H': '-H',
    },
    'Gemini PR': {  # Neutrino Group makes their own Palantype system
        # In Eclipse this is called "Palantype B"
        'S-': 'S2-',
        'C-': 'S1-',
        'P-': '#3',
        'T-': 'T-',
        'H-': 'K-',
        '+-': ('Fn', '#4', 'res2'),
        'M-': 'A-',
        'F-': 'P-',
        'R-': 'W-',
        'N-': '#5',
        'L-': 'H-',
        'Y-': 'R-',
        'O-': 'O-',
        'E-': '*2',
        '-A': '-E',
        '-U': '#C',
        'I': '*1',
        '-^': ('-B', '-D'),
        '-N': '-R',
        '-L': '-F',
        '-C': '#8',
        '-M': '-U',
        '-F': '-P',
        '-R': '#9',
        '-P': '-G',
        '-T': '-L',
        '-+': '#A',
        '-S': '#B',
        '-H': '-T',
        'no-op': ('pwr', 'res1', '#1', '#2', '#6', '*3', '*4', '-S', '#7', '-Z'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_palantype_swedish:dictionaries'
DEFAULT_DICTIONARIES = (
    'sample_swedish.json',
    'user.json'
)
