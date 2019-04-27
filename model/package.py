class Package:

    id = 0

    def __init__(self, data, sender, receiver):
        self.id = Package.id
        Package.id += 1
        self.sender = sender
        self.receiver = receiver


    def __repr__(self):
        return f"ID:{self.id}\nSENDER:{self.sender}\nRECEIVER:{self.receiver}"
        
        
    def __eq__(self, other):
        return self.id == other.id