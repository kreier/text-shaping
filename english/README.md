# Modifier letter prime U+02B9 like in Me·thuʹse·lah

Visual studio posts a warning when using the character ʹ in a python file, but no warning in an `.md` file. The warning in python reads

> The character U+02b9 "ʹ" could be confused with the ASCII character U+0060 "`", which is more common in source code.

Using reportlab and fpdf2 this character gets completely ignored. fpdf2 prints a warning that this character is not included in the selected font - and I have not found any font that includes it. But using it with Microsoft Word creates a readable PDF that has this character in it's place. So which character is included there to be part of the pdf?
