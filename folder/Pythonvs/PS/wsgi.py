from app import app  # Replace 'your_flask_app_file' with the actual filename of your Flask app

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
