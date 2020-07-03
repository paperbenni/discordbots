#!/usr/bin/env
import random

def replyuwu(message, channel):
    responses = ["UwU", "UwU", "WuW", "YwY", "WwW", "uWu", "UwU", "uwu", "<UwU>", "OwO", "<OwO>"]

    if "uwu" in message.lower():
        response = random.choice(responses)
        return response
    else:
        return False
