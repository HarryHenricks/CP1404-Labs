
from programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1992)
languages = [ruby, python, visual_basic]

ruby.is_dynamic()

ruby.__str__()

print("The dynamically typed languages are:")


for language in languages:

    if language.typing == "Dynamic":
        print(language.name)