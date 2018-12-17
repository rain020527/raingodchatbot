import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAEQCBkh4w4BAAvPCAp79LlGDn1PARgeKCjzGV2NqZA3EfniEyefCrSfSsSXyZCB5KZAVxZAU4aoYSMKmtgGJvamAOtnZALq845uCGdCKiZC7aQGRylgGlY2Skf9LiRvIKmQB5XF6eNwXkcye70XI4Bul9QunW6ZBoSlOHqtVkaUAmNmiwpMeCJ"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
