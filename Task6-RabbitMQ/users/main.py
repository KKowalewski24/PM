import os

import pika
from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> str:
    return jsonify(info="Users working")


@app.route("/create", methods=["POST"])
def create_user():
    request_data = request.get_json()
    message = request_data["email"]

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=os.environ["BROKER_HOST"]))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2))
    connection.close()

    return Response(status=201)


def main() -> None:
    app.run(port=5001, debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
