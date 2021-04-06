from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return jsonify("Emails working")


def main() -> None:
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    main()
