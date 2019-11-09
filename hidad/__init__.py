#!/usr/bin/env


def replydad(message, channel):
    if message.lower().replace('\'', '').startswith('im '):
        if "'" in message:
            response = 'Hi, ' + message[3:] + ', I\'m Dad!'
        else:
            response = 'Hi, ' + message[2:] + ', I\'m Dad!'
        return response
    else:
        return False
