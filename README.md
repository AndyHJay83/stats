# Word Analysis Tool

A web-based tool for analyzing word lists using various filtering features. This tool helps you understand how different word patterns and characteristics affect your word list.

## Features

- Filter words by length
- Filter by presence of specific letters (A, B, C, D, E)
- Remove words containing specific letters
- Find words with most/least frequent letters
- Filter words containing 'o'
- Find words with curved letters at specific positions
- Find words with exactly three 'e's
- Find words starting with 'eee'
- Find words with consecutive consonants
- Find 3-letter words containing color names

## Usage

1. Visit [https://andyhjay83.github.io/stats/](https://andyhjay83.github.io/stats/)
2. Enter your word list in the text area (one word per line)
3. Select a feature to analyze from the dropdown menu
4. Click "Analyze" to see the results
5. The results will show:
   - The parameter used
   - Number of words remaining after filtering
   - Percentage of words filtered out

## How It Works

This is a client-side application that runs entirely in your browser. No data is sent to any server - all processing happens locally on your device.

## Development

To modify or enhance the application:

1. Clone this repository:
```bash
git clone https://github.com/andyhjay83/stats.git
cd stats
```

2. Make your changes to `index.html`
3. Test locally by opening `index.html` in your browser
4. Commit and push your changes to GitHub

## License

MIT License 