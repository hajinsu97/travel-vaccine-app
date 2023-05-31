from dotenv import load_dotenv
from flask import redirect
from flask_cors import CORS
import connexion
import os

app = connexion.App(__name__, specification_dir="./")

# Load environment variables from .env file
load_dotenv()
cors_origin = os.environ.get("TRAVEL_VACCINE_APP_WEB_URL")
if cors_origin:
    CORS(app.app, origins=cors_origin)

app.add_api("swagger.yml")


@app.route("/")
def home():
    return redirect("/api/ui")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
