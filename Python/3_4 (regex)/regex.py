import re

"""
Regex øvelser

alle funktioner skal returnere True eller False
        # returner True hvis string er valid
        # returner False hvis IKKE string er valid

        Anvend re.search() medmindre andet er beskrevet

        prøv at følge best practice ift. kriterier for kodekvalitet

        Prøv først på egen hånd (uden AI) at løse opgaverne - kig i materialet og læs artikler på nettet
"""

def validate_firstletter_capital(firstname):
    # brug regex til at teste om 
    # at FØRSTE bogstav i en string er et stort bogstav
        # returner True hvis der er et stort bogstav
        # returner False hvis der IKKE er et stort bogstav
    ...


def validate_contains_numbers(pswd):
    # brug regex til at teste om 
    # at en string indeholde et tal
        # returner True hvis der er et tal
        # returner False hvis der IKKE er et tal
    ...

def validate_contains_capital_letters(pswd):
    # brug regex til at teste om 
    # at der er store bogstaver i en string
        # returner True hvis det er stort
        # returner False hvis det IKKE er stort bogstav
    ...

def validate_contains_lowercase_letters(pswd):
    # brug regex til at teste om 
    # at der er små bogstaver i en string
        # returner True hvis det er små bogstaver
        # returner False hvis det IKKE er små bogstaver
    ...

def validate_contains_ascii_printable_chars_non_letter_and_numbers(pswd):
    # brug regex til at validere at der indgår mindst
    # ét ud af alle de printbare ascii karakterer som 
    # ikke er bogstaver eller tal
    # se https://www.ascii-code.com/
    ...

def validate_contains_extented_ascii(pswd):
    # brug regex til at validere at der indgår mindst
    # ét ud af alle de udvidet ascii karakterer
    # se https://www.ascii-code.com/
    ...

def validate_minimum_16_and_max_256_characters(pswd):
    # brug regular expression til at validere password indeholder
    # mindst 16 karakterer og max 256 karakterer
    ...

def validate_password(pswd):
    # brug regular expression til at validere password
    # mindst 16 karakterer og max 256 karakterer
    # skal indeholde mindst et af hver af følgende:
    #   - tal
    #   - store bogstaver
    #   - små bogstaver
    #   - alle printbare ASCII tegn
    #   - udvidet ASCII tegn
    ...
    
def validate_ipv4_address(ip):
    # brug regular expression til at validere korrekt IP version 4 addresse
    # en valid ipv4 adresse er x.x.x.x hvor x er et tal mellem 0 og 255
    ...

def validate_phone_number(phone_number):
    # brug regular expression til at validere 
    # et gyldigt dansk telefonnummer
    # (landekode +45 og 0045 behøves ikke men kan indgå som bonusopgave)
    ...

def validate_phone_numbers_ends_with_0011(phone_number):
    # brug regular expression til at validere 
    # et gyldigt dansk telefonnummer ender på 0011
    ...

def validate_starts_with_letters(email):
    # brug regular expression til at validere 
    # at en string starter med bogstaver (store og små)
    # og at den IKKE starter med tal
    ...

def validate_ends_with_letters(email):
    # brug regular expression til at validere 
    # at en string ender med bogstaver(store og små)
    # og at den IKKE slutter med tal
    ...

def validate_contains_at(email):
    # brug regular expression til at validere 
    # at en string indeholder et snabel-a @  
    # der skal komme andre ascii tegn før @ og efter @
    ...



# https://en.wikipedia.org/wiki/Email_address
# Lav tests til følgende addresser
valid_email_addresses = [r"simple@example.com",
r"very.common@example.com",
r"FirstName.LastName@EasierReading.org", 
r"x@example.com", 
r"long.email-address-with-hyphens@and.subdomains.example.com",
r"user.name+tag+sorting@example.com", 
r"name/surname@example.com",
r"example@s.example", 
r"mailhost!username@example.org", 
r"user%example.com@example.org", 
r"user-@example.org"]


invalid_email_addresses = [r"abc.example.com", 
r"a@b@c@example.com", 
r'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
r'just"not"right@example.com', 
r'this is"not\allowed@example.com', 
r'this\ still\"not\\allowed@example.com',
r"i.like.underscores@but_they_are_not_allowed_in_this_part"]

def validate_email(email):
    # brug regular expression til at validere email addresse
    # bemærk at dette er en opgave som er svær at løse med 100% success
    # MEN man kan lave noget relativt simpelt regex som fungere fint til
    # de fleste email addresser!
    # Start simpelt og byg videre på regex!
    # Se # https://en.wikipedia.org/wiki/Email_address
    # lav tests med email-addresserne fra wikipedia
    # og prøv at følge standarden RFC 5322 så godt som muligt.
    ...

def validate_ends_with_hospital_domain(domain):
    # brug regex til at sørge for at en string ender med korrekt domæne:
    # .hospital
    ... 

def validate_hospital_email(email):
    # brug regex til at sørge for at en valid email addresse ender med korrekt domæne:
    # .hospital
    ...

mixed_emails = """​

nerd99@google.com,

guru99@hotmail.com,

secretary@yahoomail.com,

someuser@hosp.ital,

doctor_pepper@doctor.hospital,

random_pation@patient.hospital,

"""

def find_all_hospital_emails(emails):
    # anvend re.findall() til at finde alle 
    # email adresser i mixed_emails stringen.
    # returner listen med matches
    # sørg for at pytest testen hånderer dette korrekt
    # test at følgende returneres: ['@doctor.hospital', '@patient.hospital']
    ...
