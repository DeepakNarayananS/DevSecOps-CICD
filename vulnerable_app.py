"""
Vulnerable Flask application for SCA demonstration
This app intentionally uses vulnerable dependencies
"""
from flask import Flask, request, render_template_string
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    return "Vulnerable App - DO NOT USE IN PRODUCTION"

@app.route('/search')
def search():
    # Vulnerable to XSS through Jinja2
    query = request.args.get('q', '')
    template = f"<h1>Search Results for: {query}</h1>"
    return render_template_string(template)

@app.route('/config', methods=['POST'])
def load_config():
    # Vulnerable to YAML deserialization attack
    config_data = request.data
    config = yaml.load(config_data)  # Unsafe YAML loading
    return str(config)

if __name__ == '__main__':
    app.run(debug=True)
