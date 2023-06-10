import tkinter as tk
from random import randint
import time
import requests
import json

window = tk.Tk()
window.title("Chatbot")
window.configure(bg="#006400")
text_box = tk.Text(window, height=15, width=70, bg="#ECECEC", fg="#000000", font=("Arial", 14))
text_box.pack(pady=10)


def handle_user_input():
    chatbot()

entry = tk.Entry(window, width=50, font=("Arial", 12))
entry.pack()

button = tk.Button(window, text="Send", command=handle_user_input, bg="#000000", fg="#800000", font=("Arial", 12, "bold"))
button.pack(pady=10)

def chatbot():
    user_input = entry.get().lower()

    db = {
        'greetings': {
            'triggers': ['hi', 'hey', 'hello', 'heyya', 'heyya', 'sup', 'wassup', 'yo', 'ello'],
            'responses': ['Hello there!', 'Hi!', 'Hey!', 'What\'s up?', 'Sup!'],
        },
        'bye': {
            'triggers': ['bye', 'cya', 'gtg', 'ttyl', 'i gtg', 'gtg bye'],
            'responses': ['See you later!', 'Bye!', 'Cya later!'],
        },
        'thankyou': {
            'triggers': ['ty', 'tysm', 'thanks', 'thank you'],
            'responses': ['No problem!', 'You\'re welcome!', 'Welcome!'],
        },
        'good': {
            'triggers': ['good', 'great', 'nice', 'noice', 'cool'],
            'responses': ['Awesome!', 'Great!'],
        },
        'ok': {
            'triggers': ['ok', 'okay', 'aight', 'ight', 'k', 'kk', 'alright'],
            'responses': ['Are you sure?', 'Ok.', 'Okay.'],
        },
        'yes': {
            'triggers': ['yes', 'yeah', 'ye', 'yea', 'yep', 'ya'],
            'responses': ['Fine.', 'Ok.'],
        },
        'no': {
            'triggers': ['no', 'nope', 'nah', 'na'],
            'responses': ['Why not?', 'Okay.'],
        },
        'bored': {
            'triggers': ['i\'m bored', 'im bored', 'i am bored'],
            'responses': ['Say goodbye to your boredom and chat with me!', 'Why are you bored?'],
        },
        'noyou': {
            'triggers': ['no u', 'no you'],
            'responses': ['no u', 'no you'],
        },
        'stutterwords': {
            'triggers': ["uh", "uhm", "uh-", "uhm-", "uhh"],
            'responses': ["Hm?", "?", "What?"],
        },
        'lol': {
            'triggers': ['lol', 'lmao', 'haha', 'hahaha', 'hehe', 'xd'],
            'responses': ['Haha!', 'Funny, right?', 'xD'],
        }
    }

    if user_input in db['greetings']['triggers']:
        send_bot_message(random(db['greetings']['responses']))

    elif user_input in db['bye']['triggers']:
        send_bot_message(random(db['bye']['responses']))

    elif user_input == 'tell me a joke':
        data = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = json.loads(data.text)
        send_bot_message(f'{joke["setup"]}\n         {joke["punchline"]}')

    else:
        send_bot_message("I'm not sure I understand.")

    entry.delete(0, tk.END)

def send_bot_message(message):
    text_box.insert(tk.END, f'Chatbot: {message}\n')
    text_box.see(tk.END)
    time.sleep(0.2)

def random(array):
    array_length = len(array)
    rand = randint(0, array_length - 1)
    return array[rand]

send_bot_message("Hi! I'm Joker Chatbot. What's your name?")
send_bot_message("I can have conversations with you. Just type your messages below and hit Send!")

window.mainloop()
