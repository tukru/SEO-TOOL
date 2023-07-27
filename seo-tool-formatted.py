import requests
from bs4 import BeautifulSoup
import sys
import re
import collections
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import argparse
import concurrent.futures

def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def analyze_seo_tags(soup):
    seo_relevant_tags = ['title', 'meta', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'img']
    tag_data = {}
    for tag in seo_relevant_tags:
        tag_data[tag] = soup.find_all(tag)
    return tag_data

def analyze_keyword_usage(soup, keyword):
    if keyword:
        text = soup.get_text()
        keyword_count = len(re.findall(keyword, text, re.IGNORECASE))
        keyword_density = keyword_count / len(text.split())
        return keyword_count, keyword_density
    else:
        return 0, 0

def analyze_links(soup):
    internal_links = []
    external_links = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('/'):
            internal_links.append(url)
        elif url.startswith('http'):
            external_links.append(url)
    return internal_links, external_links

def check_links(links):
    broken_links = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(check_link, link): link for link in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                is_broken = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
            else:
                if is_broken:
                    broken_links.append(url)
    return broken_links

def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code != 200
    except requests.exceptions.RequestException:
        return True

def analyze_word_frequencies(soup):
    text = soup.get_text()
    words = re.findall(r'\w+', text.lower())
    word_counts = collections.Counter(words)
    return word_counts.most_common()

def print_seo_tags(tag_data):
    print("\nSEO Relevant Tags:")
    for tag, elements in tag_data.items():
        print(f"{tag}: {len(elements)}")

def print_keyword_analysis(keyword_count, keyword_density):
    print(f"\nKeyword Analysis:")
    print(f"Keyword count: {keyword_count}")
    print(f"Keyword density: {keyword_density:.2%}")

def print_links_analysis(internal_links, external_links, broken_links):
    print(f"\nLinks Analysis:")
    print(f"Internal links: {len(internal_links)}")
    print(f"External links: {len(external_links)}")
    print(f"Broken links: {len(broken_links)}")

def print_word_frequencies(word_frequencies):
    print("\nWord Frequencies:")
    for word, count in word_frequencies[:10]:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description='SEO Analyzer')
    parser.add_argument('url', help='The URL to analyze')
    parser.add_argument('-k', '--keyword', help='The keyword to analyze')
    args = parser.parse_args()

    soup = fetch_webpage(args.url)
    if soup is None:
        return

    tag_data = analyze_seo_tags(soup)
    keyword_count, keyword_density = analyze_keyword_usage(soup, args.keyword)
    internal_links, external_links = analyze_links(soup)
    broken_links = check_links(internal_links + external_links)
    word_frequencies = analyze_word_frequencies(soup)

    print_seo_tags(tag_data)
    print_keyword_analysis(keyword_count, keyword_density)
    print_links_analysis(internal_links, external_links, broken_links)
    print_word_frequencies(word_frequencies)

if __name__ == "__main__":
    main()
