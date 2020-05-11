import os
import sys
from flask import Flask, request, Response
from pymessenger.bot import Bot


app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAPYHYawtZAABAPnFbRbK0rpRjBOprOPuacXqmnKnfjVuu5LdZA1702a9gECy8hsqXL68t6Yl7yzoBW7pE6FM7u3GxfzZAsNbj2Xp8MMaX8ITqhiKxZBQWoH6fclZCrhsvqmzOIxJja2vzKmzNcdjZCaUfSZAEAQkYRVKnXvKmqXAZDZD"
VALIDATION_TOKEN = "hello"


# class EchoBot(Bot):

#     def handle_message(self, messaging_event):
#         sender_id = messaging_event['sender_id']['id']
#         text = messaging_event['message']['text']
#         self.send_text_message(sender_id, text)


# chat_bot = EchoBot(VALIDATION_TOKEN, PAGE_ACCESS_TOKEN)

bot = Bot(PAGE_ACCESS_TOKEN)

# @app.route("/", methods=["GET", "POST"])
# def handle():
#     if request.method == 'GET':
#         verify_token = request.args.get('hub.verify_token')

#         if verify_token == VALIDATION_TOKEN:
#             return Response(request.args.get('hub.challenge'), 200)

#         else:
#             return Response("Hello World", 403)
#     # POST request
#     else:
#         chat_bot.process_message(request.json)
#         return Response("", 200)


@app.route("/", methods=['GET'])
def verify():
    # webhook verification

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return ["Verification token mismatch"], 403

        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    log(data)

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                # IDs
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"]

                if messaging_event.get("message"):
                    if "text" in messaging_event["message"]:
                        messaging_text = messaging_event["message"]["text"]

                    else:
                        messaging_text = "no text"

                    # ECHO
                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":

    app.run(port=8080, debug=True)
