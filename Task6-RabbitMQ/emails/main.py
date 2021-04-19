import os
import time

import pika

sleepTime = 20
print(' [*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ["BROKER_HOST"]))
channel = connection.channel()
channel.queue_declare(queue='email_queue', durable=True)


def send_email(ch, method, properties, body):
    email = body.decode()
    print("Email has been sent!")
    print("Email address: " + str(email))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=send_email)
channel.start_consuming()
