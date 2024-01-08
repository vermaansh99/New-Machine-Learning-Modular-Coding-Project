from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def index():
    return 'Hello, World! This is my Flask app.'

# Run the Flask app on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
