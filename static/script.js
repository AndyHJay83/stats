function showLoading() {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = '<div class="loading"></div>';
}

function showError(message) {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = `
        <div class="alert alert-danger" role="alert">
            ${message}
        </div>
    `;
}

function displayResults(data) {
    const resultsContainer = document.getElementById('results-container');
    const { results, total_words } = data;

    if (results.length === 0) {
        resultsContainer.innerHTML = '<div class="text-center text-muted">No results found</div>';
        return;
    }

    let html = `
        <div class="mb-3">
            <strong>Total words analyzed:</strong> ${total_words}
        </div>
        <table class="results-table">
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Words Left</th>
                    <th>% Filtered</th>
                </tr>
            </thead>
            <tbody>
    `;

    results.forEach(result => {
        html += `
            <tr>
                <td>${result.param}</td>
                <td>${result.words_left}</td>
                <td>${result.percent_filtered}</td>
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
    `;

    resultsContainer.innerHTML = html;
}

async function analyzeWords() {
    const wordlist = document.getElementById('wordlist').value;
    const feature = document.getElementById('feature').value;

    if (!wordlist.trim()) {
        showError('Please enter some words to analyze');
        return;
    }

    showLoading();

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                wordlist,
                feature
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'An error occurred');
        }

        displayResults(data);
    } catch (error) {
        showError(error.message);
    }
} 