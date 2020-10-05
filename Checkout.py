# -*- coding: utf-8 -*-

from Detect import Detector

if __name__=='__main__':
    successes = 0
    tries = 0
    detector = Detector()
    expected_languages = []
    with open("languages.txt", "r") as inp:
        for lng in inp:
            expected_languages.append(detector.label_to_str[lng[:-1]])
    with open("texts.txt", "r", encoding="utf8") as inp:
        for index, txt in enumerate(inp):
            tries += 1
            lng = detector.get_language(txt)
            if lng == expected_languages[index]:
                successes += 1
            else:
                print(f"Misdetect: {lng} instead of {expected_languages[index]}")
    print(f'Performed full run over {tries} sentences, got {successes} correct ({round(100 * successes / tries, 1)}%)')
