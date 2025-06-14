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

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/word-analysis-tool.git
cd word-analysis-tool
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter your word list in the text area (one word per line)
2. Select a feature to analyze from the dropdown menu
3. Click "Analyze" to see the results
4. The results will show:
   - The parameter used
   - Number of words remaining after filtering
   - Percentage of words filtered out

## Deployment

This application can be deployed on GitHub Pages or any other web hosting service that supports Python/Flask applications.

## License

MIT License 