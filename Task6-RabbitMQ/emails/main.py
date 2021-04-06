import os

import pika
from flask import Flask, jsonify

app = Flask(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ["BROKER_HOST"]))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


def send_email(ch, method, properties, body) -> None:
    email = body.decode()
    print("Email has been sent!")
    print("Email address: " + str(email))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=send_email)
channel.start_consuming()


@app.route("/", methods=["GET"])
def home() -> str:
    return jsonify(info="Emails working")


def main() -> None:
    app.run(port=5000, debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
