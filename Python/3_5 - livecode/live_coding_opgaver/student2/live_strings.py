# i denne opgave skal du eksaminere din medstuderende med en live-coding opgave.
# Spørg til spørgmsålene i nedenstående kommentarer. Du må IKKE hjælpe med løsningen som
# står nedenunder, men du skal forklare hvad de skal lave og se om de kan komme frem til løsningen selv.

# opret en string variabel med de første 5 bogstaver i alfabetet i lowercase
letters = "abcde"

# omdan denne string til upper case og gem i en ny variabel
upper_case_letters = letters.upper()

# udprint variablen med uppercase
print(upper_case_letters)

# lav en docstring med 3 linjers tekst og gem indholdet i en variabel
some_text = """hello, world!
computers are nice
and software is cool!"""

# lav en operation hvor hvert ord fra variablen lægges i en liste og print den
print(some_text.split())

# prøv nu at lægge hver linje fra sætningen i en liste og print resultatet
print(some_text.split("\n"))

# prøv nu at udskifte alle forkomster af bogsteavet "e" så det erstattes med bogstavet "a"
# print dernæst resultatet
print(some_text.replace("e", "a"))
# lav en variabel der gemmer brugerinput med et et navn i en variabel
name = input("input name:\n>")

# lav et loop der printer hver karakter fra navnet ud for sig
for char in name:
    print(char)

# lav et nyt loop hvor du printer unicode ascii decimal værdien for hver karakter
for char in name:
    print(ord(char))

# prøv nu at lave en tom string variabel og så ryk hver karakter 
rotated_name = ""
for char in name:
    print(ord(char))
    rotated_name += chr(ord(char) + 1)

print(rotated_name)

