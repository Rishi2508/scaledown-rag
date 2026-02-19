from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from rag_service import answer_query, build_index
from zip_handler import extract_zip

app = Flask(__name__)
CORS(app)

# ---------------------------
# Serve Frontend
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# Upload ZIP & Build Index
# ---------------------------
@app.route("/upload", methods=["POST"])
def upload():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        print("Extracting ZIP...")
        project_path = extract_zip(file)

        print("Building index...")
        build_index(project_path)

        print("Index built successfully.")

        return jsonify({"message": "Project indexed successfully!"})

    except Exception as e:
        print("Upload error:", str(e))
        return jsonify({"error": str(e)}), 500


# ---------------------------
# Ask Question
# ---------------------------
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "No question provided"}), 400

        question = data["question"]

        print("Answering question:", question)

        result = answer_query(question)

        return jsonify(result)

    except Exception as e:
        print("Ask error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
