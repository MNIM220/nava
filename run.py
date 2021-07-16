from config import DevConfig
from factory import create_app

# Create a Flask app.
app = create_app(DevConfig)

if __name__ == '__main__':
    # Start the Flask app.
    app.run(
        port=8000,
        use_reloader=False
    )
