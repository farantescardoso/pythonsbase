#!/usr/bin/env python
"""
Hello World multi languages

Dependendo da lingua configurado no ambiente 
o programa exibe a mesnagem do ambiente

execuçao:

python hello.py
./hello.py


"""

__version__ ="0.0.1"
__author__="Filipe"
__lisence__="Unlicense"


import os

current_language = "en_US" os.getenv("LANG", "en_US")[:5]
msg = "Hello World"


if current_language == "pt_BR":
    msg ="Ola Mundo"
elif current_language == "it_IT":
    msg ="Ciao Mundo"
elif current_language == "es_SP"
    msg = "Habla"

print('filipe'.upper())
print(56 + 7)
print(56 - 6)
print(msg)
