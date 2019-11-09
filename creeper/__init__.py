#!/usr/bin/env python3

from fuzzywuzzy import fuzz

# keep the bot from using offensive/nsfw posts/words
lyrics = open('creeper/lyrics.txt', 'r').read()


def processlyric(string):
    for i in ',\'.\n\r':
        string = string.replace(i, ' ').lower()
    string = string.replace('  ', ' ')
    string = string.replace('  ', ' ')
    return string


lyrics = processlyric(lyrics)
lyrics = lyrics.split(' ')

creeperchannels = {}


def creeper(message, channel):
    global creeperchannels
    if not channel in creeperchannels.keys():
        if not 'creeper' in processlyric(message):
            return False
        else:
            creeperchannels[channel] = 0
    returner = False

    creeperindex = creeperchannels[channel]

    islyric = False
    for i in processlyric(message).split(' '):
        if int(fuzz.ratio(i, lyrics[creeperindex])) > 85:
            creeperindex += 1
            islyric = True
        else:
            print('real lyric is ', lyrics[creeperindex])
            if not creeperindex == 0:
                creeperindex = 0
                returner = 'You fukd up '
                islyric = False
            break
    if islyric:
        response = lyrics[creeperindex] + ' ' + \
            lyrics[creeperindex + 1] + ' ' + lyrics[creeperindex + 2]
        creeperindex += 3
        returner = response

    creeperchannels[channel] = creeperindex
    return returner
