class Scanner:
    def __init__(self, ip_from, ip_to, mode):
        self.ip_from = ip_from
        self.ip_to = ip_to
        allowed_modes = ["stealth", "agressive", "fast"]
        if mode in allowed_modes:
            self.mode = mode
        else:
            self.mode = "default"
            
    def scan(self):
         print(f"scanning from {self.ip_from} to {self.ip_to}")

scan = Scanner("192.168.1.0", "192.168.1.100", "fast")
scan.scan()
