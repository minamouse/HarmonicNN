from music21 import *
import os


def list_files(path):

    files = []
    for p in os.listdir(path):
        if p.split('.')[-1] == 'mid':
            files.append

