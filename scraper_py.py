# -*- coding: utf-8 -*-
"""Scraper.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A_l4oLgcTTq4-w4tXHdYACSVrfm_hRd7
"""

import re
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def scrape_contacts(url):
    """
    Scrapes email addresses and phone numbers from the given URL.
    """
    try:
        print(f"Scraping {url}...")
        # Fetch webpage content without SSL verification
        response = requests.get(url, timeout=20, verify=False)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Regex to find email addresses
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        emails = re.findall(email_pattern, soup.text)

        # Improved regex to find phone numbers (handles various formats)
        phone_pattern = r'(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})'
        phones = re.findall(phone_pattern, soup.text)

        # Join the parts of the phone numbers and preserve their original formatting
        formatted_phones = set(
            [''.join(phone).strip() for phone in phones if ''.join(phone).strip()]
        )

        return set(emails), formatted_phones
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return set(), set()

def save_to_file(data, filename="contacts.txt"):
    """
    Saves the scraped email addresses and phone numbers to a file.
    """
    try:
        with open(filename, 'w') as file:
            if data["emails"]:
                file.write("Emails:\n")
                file.writelines(email + '\n' for email in data["emails"])
            if data["phones"]:
                file.write("\nPhone Numbers:\n")
                file.writelines(phone + '\n' for phone in data["phones"])
        print(f"Contacts saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    """
    Main function to run the contact scraper.
    """
    print("Welcome to Contact Scraper!")
    url = input("Enter the website URL: ").strip()
    emails, phones = scrape_contacts(url)

    if emails or phones:
        print("\nFound Contacts:")
        if emails:
            print(f"\nFound {len(emails)} email(s):")
            for email in emails:
                print(email)
        if phones:
            print(f"\nFound {len(phones)} phone number(s):")
            for phone in phones:
                print(phone)

        save_option = input("\nWould you like to save the contacts to a file? (y/n): ").strip().lower()
        if save_option == 'y':
            save_to_file({"emails": emails, "phones": phones})
    else:
        print("No contacts found or the site is inaccessible.")

if __name__ == "__main__":
    main()