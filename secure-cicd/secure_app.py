"""
Secure Flask application with fixed vulnerabilities
This demonstrates proper security practices
"""
from flask import Flask, request, render_template_string, escape
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    return "Secure App - Best Practices Applied"

@app.route('/search')
def search():
    # Fixed: Properly escape user input to prevent XSS
    query = request.args.get('q', '')
    safe_query = escape(query)
    template = f"<h1>Search Results for: {safe_query}</h1>"
    return render_template_string(template)

@app.route('/config', methods=['POST'])
def load_config():
    # Fixed: Use safe YAML loading to prevent deserialization attacks
    config_data = request.data
    config = yaml.safe_load(config_data)  # Safe YAML loading
    return str(config)

if __name__ == '__main__':
    # Fixed: Disable debug mode in production
    app.run(debug=False)
