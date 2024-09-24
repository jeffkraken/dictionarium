import requests
from bs4 import BeautifulSoup
import re

def extract_from_document(file_path):
    """Extracts words from a text document."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text.lower())
            unique_words = sorted(set(words))
            return unique_words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def extract_from_website(url):
    """Extracts words from a website's content."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            words = re.findall(r'\b\w+\b', text.lower())
            unique_words = sorted(set(words))
            return unique_words
        else:
            print(f"Error: Unable to access the website. Status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error: An error occurred while accessing the website: {e}")
        return []

def save_to_file(word_list, output_file):
    """Saves the word list to a text file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word in word_list:
                file.write(f"{word}\n")
        print(f"Word list saved to {output_file}")
    except IOError as e:
        print(f"Error: Could not write to file {output_file}: {e}")

def main():
    print("Custom Dictionary Generator for Password Testing")
    print("1. Extract from a text document")
    print("2. Extract from a website")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == '1':
        file_path = input("Enter the path to the document: ").strip()
        words = extract_from_document(file_path)
        if words:
            print(f"Extracted {len(words)} unique words from the document.")
            output_file = input("Enter the output file name (e.g., wordlist.txt): ").strip()
            save_to_file(words, output_file)

    elif choice == '2':
        url = input("Enter the website URL: ").strip()
        words = extract_from_website(url)
        if words:
            print(f"Extracted {len(words)} unique words from the website.")
            output_file = input("Enter the output file name (e.g., wordlist.txt): ").strip()
            save_to_file(words, output_file)

    else:
        print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    main()
