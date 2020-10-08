# -*- coding: utf-8 -*-

SAMPLE_THRESHOLD = 20
SKIP_THRESHOLD = 20000
target_languages = ['zho', 'spa', 'eng', 'hin', 'ara']
indexes = []

with open("languages.txt", "w") as output:
    with open("y_train.txt", "r") as inp:
        for index, lng in enumerate(inp):
            if lng[:-1] in target_languages and index > SKIP_THRESHOLD:
                indexes.append(index)
                output.write(lng)
                if len(indexes) > SAMPLE_THRESHOLD - 1:
                    break

with open("texts.txt", "w", encoding="utf8") as output:
    with open("x_train.txt", "r", encoding="utf8") as inp:
        for index, text in enumerate(inp):
            if index in indexes:
                output.write(text)
