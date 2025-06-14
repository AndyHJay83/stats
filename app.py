from flask import Flask, render_template, request, jsonify
import itertools
from collections import Counter, defaultdict

app = Flask(__name__)

# === FEATURE LOGIC ===
def filter_length(words, length):
    return [w for w in words if len(w) == length]

def filter_abcde(words, yes_letters):
    return [w for w in words if all(l in w for l in yes_letters)]

def filter_not_in(words, not_letters):
    return [w for w in words if all(l not in w for l in not_letters)]

def filter_most_frequent(words, letter):
    def most_freq(w):
        c = Counter(w)
        return max(c, key=lambda k: (c[k], k))
    return [w for w in words if most_freq(w) == letter]

def filter_least_frequent(words, letter):
    def least_freq(w):
        c = Counter(w)
        return min(c, key=lambda k: (c[k], k))
    return [w for w in words if least_freq(w) == letter]

def filter_o_question(words):
    return [w for w in words if 'o' in w]

def filter_curved_pos(words, pos):
    curved = set('ceos')
    return [w for w in words if len(w) > pos and w[pos] in curved]

def filter_eee(words):
    return [w for w in words if w.count('e') == 3]

def filter_eeefirst(words):
    return [w for w in words if w.startswith('eee')]

def filter_cons_together(words):
    vowels = set('aeiou')
    return [w for w in words if any(w[i] not in vowels and w[i+1] not in vowels for i in range(len(w)-1))]

def filter_colour3(words):
    colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'black', 'white', 'pink', 'grey']
    return [w for w in words if any(col in w for col in colours) and len(w) == 3]

# === FEATURE DEFINITIONS ===
FEATURES = {
    "LENGTH": {
        "params": lambda words: sorted(set(len(w) for w in words)),
        "filter": filter_length,
        "desc": "Filter by word length"
    },
    "ABCDE": {
        "params": lambda words: [combo for n in range(1, 6) for combo in itertools.combinations('abcde', n)],
        "filter": filter_abcde,
        "desc": "Filter by presence of A, B, C, D, E (all YES)"
    },
    "NOT IN": {
        "params": lambda words: [combo for n in range(1, 4) for combo in itertools.combinations('abcde', n)],
        "filter": filter_not_in,
        "desc": "Remove words containing any of the specified letters"
    },
    "MOST FREQUENT": {
        "params": lambda words: sorted(set(''.join(words))),
        "filter": filter_most_frequent,
        "desc": "Keep words where the most frequent letter is X"
    },
    "LEAST FREQUENT": {
        "params": lambda words: sorted(set(''.join(words))),
        "filter": filter_least_frequent,
        "desc": "Keep words where the least frequent letter is X"
    },
    "O?": {
        "params": lambda words: [None],
        "filter": lambda words, _: filter_o_question(words),
        "desc": "Keep words containing 'o'"
    },
    "CURVED POS.": {
        "params": lambda words: list(range(max(len(w) for w in words))),
        "filter": filter_curved_pos,
        "desc": "Keep words with a curved letter (c,e,o,s) at position N"
    },
    "EEE?": {
        "params": lambda words: [None],
        "filter": lambda words, _: filter_eee(words),
        "desc": "Keep words with exactly three 'e's"
    },
    "EEEFIRST": {
        "params": lambda words: [None],
        "filter": lambda words, _: filter_eeefirst(words),
        "desc": "Keep words starting with 'eee'"
    },
    "CONS. TOGETHER": {
        "params": lambda words: [None],
        "filter": lambda words, _: filter_cons_together(words),
        "desc": "Keep words with two consonants together"
    },
    "COLOUR3": {
        "params": lambda words: [None],
        "filter": lambda words, _: filter_colour3(words),
        "desc": "Keep 3-letter words containing a colour"
    }
}

def load_wordlist(path):
    with open(path, encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

def analyze_feature(words, feature_name):
    feature = FEATURES[feature_name]
    params = feature["params"](words)
    results = []
    for p in params:
        filtered = feature["filter"](words, p) if p is not None else feature["filter"](words, p)
        pct = 100 * (1 - len(filtered)/len(words)) if words else 0
        results.append((p, len(filtered), pct))
    results.sort(key=lambda x: x[2], reverse=True)
    return results

def format_param(p):
    if p is None:
        return "-"
    if isinstance(p, (list, tuple)):
        return "".join(p)
    return str(p)

@app.route('/')
def index():
    return render_template('index.html', features=FEATURES)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    feature_name = data.get('feature')
    wordlist = data.get('wordlist', '').split('\n')
    wordlist = [w.strip().lower() for w in wordlist if w.strip()]
    
    if not wordlist:
        return jsonify({'error': 'No words provided'}), 400
    
    results = analyze_feature(wordlist, feature_name)
    formatted_results = [
        {
            'param': format_param(p),
            'words_left': n,
            'percent_filtered': f"{pct:.1f}%"
        }
        for p, n, pct in results
    ]
    
    return jsonify({
        'results': formatted_results,
        'total_words': len(wordlist)
    })

if __name__ == '__main__':
    app.run(debug=True) 