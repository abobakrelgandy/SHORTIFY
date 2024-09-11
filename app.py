#!/usr/bin/python3
"""
starts a Url Shortener web application
"""
import string
import random
from flask import Flask, request, redirect, jsonify, render_template
from core.db import DBStorage
from core.models import URL
from dotenv import load_dotenv

app = Flask(__name__)

db_storage = DBStorage()
load_dotenv()

@app.route('/', strict_slashes=False)
def index():
    """ rendering home page of project """
    return render_template('index.html')

def generate_short_code(length=2):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return (short_code)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """  shorten a url """
    original_url = request.form.get('original_url')
    
    if not original_url:
        return jsonify({"error": "Original URL is required"}), 400
    
    original_url = original_url.strip()

    if not original_url.startswith(('http://', 'https://')):
        # Prepend https://www. if not present
        original_url = f'https://www.{original_url}'
        
    # Generate a short code
    short_code = generate_short_code()
    
    # Store the URL and short code in the database
    new_url = URL(original_url=original_url, short_code=short_code)
    db_storage.new(new_url)
    db_storage.save()

    short_code = f"s-y-w.vercel.app/{short_code}"
    return jsonify(short_code=short_code)


@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Query the database for the original URL
    # short_code = f"{short_code}"
    short_code = short_code.strip()
    print(short_code)
    
    url_entry = db_storage.get(URL, short_code)
    print(url_entry)
    
    print("Hello !")
    print("\n\n\n\n")
    print(url_entry.original_url)
    if url_entry:
        return redirect(url_entry.original_url)
    else:
        return jsonify({"error": "Short code not found"}), 404
    
    
if __name__ == "__main__":
    app.run()
