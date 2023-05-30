from flask import Flask, redirect  # Remove: import Flask
from flask_cors import CORS
import connexion

DEV_FRONTEND_ORIGIN='http://localhost:5173'
PROD_FRONTEND_ORIGIN='https://travel-vaccine-web.onrender.com'

app = connexion.App(__name__, specification_dir="./")
CORS(app.app)
app.add_api("swagger.yml")


@app.route("/")
def home():
    return redirect('/api/ui')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
