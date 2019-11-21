import os
import requests

def main():
    webhook_url = os.environ.get('PLUGIN_WEBHOOK_URL')
    s3_bucket = os.environ.get('PLUGIN_S3_BUCKET')
    build_status = os.environ.get('DRONE_BUILD_STATUS')

    theme_color = 'fc0303'
    if build_status == 'success':
        theme_color = '24fc03'

    repo_name = os.environ.get('DRONE_REPO')
    repo_link = os.environ.get('DRONE_REPO_LINK')

    status = 'FAIL'
    if build_status == 'success':
        status = 'SUCCESS'
    
    build_link = os.environ.get('DRONE_BUILD_LINK')
    commit_sha = os.environ.get('DRONE_COMMIT')
    commit_link = os.environ.get('DRONE_COMMIT_LINK')
    additional_info = '-'
    if 'PLUGIN_WEBHOOK_TEXT' in os.environ:
        additional_info = os.environ.get('PLUGIN_WEBHOOK_TEXT')

    text = '{"@type": "MessageCard","@context": "http://schema.org/extensions","themeColor": "' + theme_color + '","summary": "Drone Pipelines","sections": [{"activityTitle": "A Drone Pipeline has been finished!","activitySubtitle": "For [' + repo_name + '](' + repo_link + ')","activityImage": "https://raw.githubusercontent.com/drone/brand/master/logos/png/dark/drone-logo-png-dark-512.png","facts": [{"name": "Status","value": "[' + status + '](' + build_link + ')"}, {"name": "Commit SHA","value": "[' + commit_sha + '](' + commit_link + ')"}, {"name": "Additional Info","value": "' + additional_info + '"}],"markdown": true}]}'

    data = text
    r = requests.post(url = webhook_url, data = data)
    print(r.text)

main()

