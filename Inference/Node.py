from netzob.all import 8

class Node:
    def __init__(self,m_id,sequence):
        self.id = m_id
        self.sequence = sequence
        self.lo = 0
    
    def get_next(self):
        return self.sequence[self.lo + 1]

    def go_next(self):
        self.lo = self.lo + 1

    

