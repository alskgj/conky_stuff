from Api import ConkyWriter

import re
from os.path import expanduser
from itertools import cycle
from textwrap import wrap


path = expanduser("~/Desktop/todo")

# setup writter
Writer = ConkyWriter()

my_little_colors = ['aquamarine', 'chartreuse', 'chocolate', 'deepskyblue', 'firebrick', 'darkorange']
colorwheel = cycle(my_little_colors)
topic = re.compile(r"\[(.*?)\]")

with open(path, "r") as fo:
    data = fo.read()

last = ""
color = next(colorwheel)
for line in data.split("\n"):
    if line:
        # only get new color if new topic
        current_topic = re.findall(topic, line)

        if not last or current_topic[0] != last:
            color = next(colorwheel)

        last = current_topic[0]

        for sub_line in wrap(line, width=30):
            Writer.voffset(8).offset(16).color(color).write(sub_line+" ").newline()
        print("$hr")