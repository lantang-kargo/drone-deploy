import os
import requests

def main():
    webhook_url = os.environ.get('PLUGIN_WEBHOOK_URL')
    s3_bucket = os.environ.get('PLUGIN_S3_BUCKET')
    data = '{ "text": "The APK in ' + str(s3_bucket) + ' has been updated." }'
    r = requests.post(url = webhook_url, data = data)
    print(r.text)

main()