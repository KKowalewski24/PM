import os

import pika
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> str:
    return jsonify(info="Users working")


# def create_user() -> str:
#     message = "sample_email"
#
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters(host=os.environ["BROKER_HOST"]))
#     channel = connection.channel()
#     channel.queue_declare(queue='task_queue', durable=True)
#     channel.basic_publish(
#         exchange='',
#         routing_key='task_queue',
#         body=message,
#         properties=pika.BasicProperties(delivery_mode=2))
#     connection.close()


def main() -> None:
    app.run(port=5001, debug=True)


if __name__ == "__main__":
    main()
