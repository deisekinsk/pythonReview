#!/usr/bin/python3

name = input("What's your name?")
parseName = name.title()

birthYear = input("What's your birth year. (Example:1988)")
parseBirthYear = 2022 - (int(birthYear))

print(f'Hello {parseName}! Your age today are {parseBirthYear}.')