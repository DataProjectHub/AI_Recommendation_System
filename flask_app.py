from flask import Flask, request, jsonify
from svd_model import model, get_recommendations, movies

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = int(request.args.get("user_id"))
    recommendations = get_recommendations(user_id, model, movies)
    return jsonify({"User ID": user_id, "Recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
