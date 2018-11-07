import requests

requests.packages.urllib3.disable_warnings()


def get_html(website):
    html = requests.get(website)
    list_html = html.content.split(',')
    text = ''
    for item in list_html:
        text += item + ',\n'
    return text
