# SEO-TOOL
![SEO Analyzer](https://img.shields.io/badge/SEO-Analyzer-blue)
![Author](https://img.shields.io/badge/Author-TUKRU-green)

# SEO Analyzer

This is a Python script for analyzing the SEO of a webpage. It fetches a webpage, analyzes the HTML tags that are relevant to SEO, counts the frequency of each word in the text of the webpage, and analyzes the links on the webpage.

## Features

- **Fetching and Analyzing HTML Tags**: The tool fetches a webpage and analyzes the HTML tags that are relevant to SEO, such as the title tag, meta tags, heading tags (h1, h2, etc.), anchor tags (a), and image tags (img).
- **Keyword Analysis**: If a keyword is provided, the tool counts the number of times the keyword appears in the text of the webpage and calculates the keyword density.
- **Link Analysis**: The tool analyzes the links on the webpage, counting the number of internal links (links to the same domain), external links (links to other domains), and broken links (links that return a non-200 HTTP status code). It uses concurrent processing to speed up the link checking process.
- **Word Frequency Analysis**: The tool counts the frequency of each word in the text of the webpage, which can help identify the main topics of the webpage.
- **Improved Error Handling**: The script includes robust error handling to deal with issues like timeouts, non-responsive links, and other potential errors that could occur during the analysis.
- **Code Refactoring**: The main function has been refactored into smaller, more manageable functions to improve readability and maintainability of the code.

## Usage

You can run the script from the command line with the following command:

```bash
python3 seo_analyzer.py -k [keyword] [url]

Automated SEO tool for the cool kids.
SEO Analyzer

SEO Analyzer is a Python-based tool that fetches a webpage and performs an SEO analysis on it. The results of the analysis are printed to the console.
Features

    Fetches and parses the HTML content of a webpage.
    Analyzes SEO-relevant HTML tags and their attributes.
    Performs a detailed keyword analysis, including keyword count and density.
    Analyzes the links on the webpage, categorizing them into internal and external links, and checks for broken links.
    Counts the frequency of each word in the text of the webpage.
    Supports parallel processing to speed up the link checking process.
    Includes robust error handling to deal with issues like timeouts and non-responsive links.

Installation

    Clone this repository to your local machine.

    Navigate to the directory containing the repository.

    Install the required Python packages using pip:

    pip install -r requirements.txt

Usage

Run the script from the command line with the URL of the webpage you want to analyze as an argument:

php

python seo-analyzer.py <url> [-k <keyword>]

The -k or --keyword option allows you to specify a keyword for the keyword analysis.

The results of the analysis will be printed to the console.
Contributing

Contributions are welcome! Please feel free to submit a pull request.
License

This project is licensed under the MIT License.
