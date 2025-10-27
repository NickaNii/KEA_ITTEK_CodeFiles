# Øvelse: Arbejde med klasser og instanser i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.


# Opret en klasse der navngives Scanner
# Lav en konstructor som tager to parametre, ip_from, ip_to og mode
# tjek at mode er en af følgende "stealth, agressive, fast" og ellers sæt den til "default"
class Scanner():
    def __init__(self, ip_from, ip_to, mode):
        self.ip_from = ip_from
        self.ip_to = ip_to
        allowed_modes = ["stealth", "agressive", "fast"]
        if mode in allowed_modes:
            self.mode = mode
        else:
            self.mode = "default"
# lav nu en metode som ikke tager argumenter
# kaldet scan som skal printe en formateret string
# her skal den angive hvilken ip der scannes fra og scannes til
    def scan(self):
        print(f"scanning from {self.ip_from} to {self.ip_to}")

# lav en instals fra klassen og kør scan metoden
scan = Scanner("192.168.1.0", "192.168.1.100", "fast")
scan.scan()

# lav nu en ny klasse kalde PortScanner som nedarver fra klassen Scanner
class PortScanner(Scanner):
    # tilføj en metode kaldet port_scan, som tager to parametre port_start og port_to
    # port_start skal have standardværdien 80
    # port_to skal have standardværdien None
    def port_scan(self, port_start = 80, port_to = None):
        # valider at første argumente er en integer
        # og at 2. argument er integer eller None

        if not isinstance(port_start, int):
            port_start = 80
        
        if not isinstance(port_to, (int, type(None))):
            port_to = None
        # hvis begge tal er angivet så print hvilken port der scannes fra og til

        if port_to != None:
            print(f"Scanning ports from {port_start} to {port_to}")
        # ellers så print kun den port som scannes
        else:
            print(f"Scanning port {port_start}")
        
# Lav en instans af klassen 
ps = PortScanner("0.0.0.0", "255.255.255.255", "stealth")
# kald den port_scan metoden med 2 argumenter, med tallet 22 og tallet 80
ps.port_scan(22, 80)
# Lav en instans af klassen hvor der kun angives 1 argument med tallet 22
ps.port_scan(22)

# kald port_scan metoden med 1. argument hvor der indsættes en string
ps.port_scan("22")