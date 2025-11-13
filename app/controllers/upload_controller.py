import os
import pika, json

from werkzeug.utils import secure_filename

allowed_extensions = {"png","jpg","svg","pdf"}

def is_file_extension_allowed(filename):
    if(filename.rsplit('.', 1)[1].lower() in allowed_extensions):
        return True
    
    return False


def save_file(file):
    if not is_file_extension_allowed(file.filename):
        return None, "File type is not allowed"
    
    filename = secure_filename(file.filename)
    upload_folder = os.path.join("app", "static", "assets")
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path, None


def send_to_queue(filename):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="process_ocr")
    message = json.dumps({"filename": filename})
    channel.basic_publish(exchange='', routing_key='process_ocr', body=message)
    connection.close()