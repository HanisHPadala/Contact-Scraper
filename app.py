from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_contacts  # Import the scraping function from scraper.py

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route('/scrape', methods=['POST'])
def scrape():
    """
    API endpoint to scrape contacts from a given URL.
    """
    data = request.json
    url = data.get('url')  # Get the URL from the frontend request
    
    if not url:
        return jsonify({"error": "URL is required"}), 400  # Error if URL is missing

    try:
        # Call the scraping function and get results
        emails, phones = scrape_contacts(url)
        
        # Return the results as JSON to the frontend
        return jsonify({
            "emails": list(emails),
            "phones": list(phones)
        })
    except Exception as e:
        # Handle and return any errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
