import pika, json, pytesseract, time, os, cv2
import numpy as np
from PIL import Image

def connect_to_rabbitmq():
    for i in range(10):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            return connection
        except pika.exceptions.AMQPConnectionError:
            time.sleep(5)

    raise Exception("Couldn't connect to rabbit mq after 10 attempts")

def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode())
        filename = data["filename"]
        print(f"Received OCR task for: {filename}")

        file_path = os.path.join("app", "static", "assets", filename)
        print(f"Looking for file at: {file_path}")

        if not os.path.exists(file_path):
            print("File not found!")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return
        else:
            print("Image found!")

        try:
            img = cv2.imread(file_path)
            grayscaledimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grayscaledimg = cv2.threshold(grayscaledimg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

            text = pytesseract.image_to_string(grayscaledimg, lang="eng")
            print("OCR TEXT OUTPUT:\n", text)
            # text = pytesseract.image_to_string(img)
        except Exception as e:
            print(f"Failed to process image: {e}")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Unexpected error: {e}")

        try:
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except:
            pass

connection = connect_to_rabbitmq()
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='process_ocr')
channel.basic_consume(queue='process_ocr', on_message_callback=callback, auto_ack=True)
print(" [*] Waiting for OCR tasks...")
channel.start_consuming()