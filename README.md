# Contact Scraper

**Contact Scraper** is a Python-based tool that helps extract contact information such as email addresses and phone numbers from websites. It offers a modern web interface and a powerful backend API to simplify the process of data collection for research, marketing, or personal projects.

---

## Features

- **Web Scraping**: Extracts emails and phone numbers from any publicly accessible webpage.
- **Regex-Based Parsing**: Uses precise patterns for accurate contact extraction.
- **API Integration**: Provides a backend Flask API for easy integration with other systems.
- **User-Friendly UI**: Includes a responsive, animated frontend for smooth user experience.
- **Error Handling**: Validates inputs and provides feedback for inaccessible URLs or scraping errors.

---

## How It Works

1. **Frontend**:
   - Users enter a website URL via the web interface.
   - The form validates the URL and sends it to the backend for processing.

2. **Backend**:
   - The Flask API receives the URL and uses the `scraper.py` module to fetch the webpage.
   - Contact information is extracted using regex patterns for emails and phone numbers.

3. **Output**:
   - Results are displayed on the web interface.
   - Optionally, users can save the contacts to a file for offline use.

---
