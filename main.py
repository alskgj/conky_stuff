import textwrap

import praw
import sys

from Api import ConkyWriter
from random import choice
import argparse

# choose subreddit
parser = argparse.ArgumentParser()
parser.add_argument("subreddit")
sub = parser.parse_args().subreddit
reddit = praw.Reddit("Dimdalf reddit")
submissions = list(reddit.get_subreddit(sub).get_hot())

# choose a color
my_little_colors = ['aquamarine', 'chartreuse', 'chocolate', 'deepskyblue', 'firebrick', 'darkorange']
color = choice(my_little_colors)
my_little_colors = my_little_colors.remove(color)

# setup writter
Writer = ConkyWriter()

# constants
BREAK_LENGTH = 40

submission = ""
for submission in submissions:
    if not submission.stickied:
        break


quote = submission.title

quotes = textwrap.wrap(quote, BREAK_LENGTH)

quotes.insert(0, sub.capitalize()+":")
for color_index, line in enumerate(quotes):
    Writer.voffset(8).offset(16).color(color+str(color_index+1)).write(line).newline()
