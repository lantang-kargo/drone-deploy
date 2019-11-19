import os
import requests

def main():
    webhook_url = os.environ.get('PLUGIN_WEBHOOK_URL')
    s3_bucket = os.environ.get('PLUGIN_S3_BUCKET')

    text = 'The APK in ' + str(s3_bucket) + ' has been updated.'
    if 'PLUGIN_WEBHOOK_TEXT' in os.environ:
        text = str(os.environ.get('PLUGIN_WEBHOOK_TEXT'))
    
    data = '{ "text": "' + text + '" }'
    r = requests.post(url = webhook_url, data = data)
    print(r.text)

main()