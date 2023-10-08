import requests
import schedule
import time


def send_message():
    # where we posting data
    resp = requests.post('https://textbelt.com/text', {
        'phone': '8572597369',
        'message': "GOOD MORNING , PAIN IS TEMPORARY , Do not give up and go the extra mile study extra hard today ~ Trust in God",
        'key': 'textbelt'
    })

    print(resp.json())


schedule.every().day.at('06:30').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
