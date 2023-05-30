#!/usr/bin/python3
from datetime import datetime
import json
import random

lower = "acdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
char = "&()_ç=#@{}/\[]"
all = lower + upper + num + char
length = 16
password = "".join(random.sample(all, length))
line_len = 1
try:
	with open("password.txt", "r") as f:
		lines = f.readlines()
	line_len += len(lines)
except FileNotFoundError:
	line_len = 1
current = datetime.now()
formated_date = current.strftime("%d/%m/%Y at %H:%M:%S")
with open("password.txt", "a") as f:
	f.write(str(line_len))
	f.write(" password: ")
	f.write(password)
	f.write(" Created at ")
	f.write(formated_date)
	f.write("\n")
print(f"{line_len}- Password: {password} created at {formated_date}")
