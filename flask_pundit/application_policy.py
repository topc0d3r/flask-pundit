class ApplicationPolicy:
    def __init__(self, user, record):
        self.user = user
        self.record = record
    class Scope:
        def resolve(self):
            pass
