import os 
from google.cloud import storage  
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"
##os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"
bucket_name =os.environ.get('BUCKET')

from flask import Flask, render_template 

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"
    return message

"""Uploads a file to the bucket."""
# The ID of your GCS bucket
##bucket_name = "bk_lrbd_taller_001" 

# The path to your file to upload
source_file_name = "helloGCS"
# The ID of your GCS object
destination_blob_name = "hello_gcs.csv"

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

print(
    "File {} uploaded to {}.".format(
        source_file_name, destination_blob_name
    )
)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

