class Package:

    package_id = 0

    def __init__(self, data, sender, receiver):
        self.id = package_id
        package_id += 1
        self.sender = sender
        self.receiver = receiver