class UserDAO:
    def __init__(self):
        U1 = [122, 'Ricardo Casares', '7879999999','email1@upr.edu', 'db10rocks']
        U2 = [74, 'Diego', '7879999998','email2@upr.edu', 'db10sucks']
        U3 = [2, 'Victor', '7879999997','email3@upr.edu', 'db10meh']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)

    def getAllUsers(self):
        # P1 = [122, 'Bolt', 0.5, 'blue']
        # P2 = [74, 'Wire', 1.5, 'silver']
        # P3 = [849, 'wood', 5, 'brow']
        # result = []
        # result.append(P1)
        # result.append(P2)
        # result.append(P3)
        return self.data

    def getPartById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getSuppliersByPartId(self, id):
        if id == 74:
            return [['123', 'Home Depot']]
        elif id == 122:
            T = []
            T.append(['123', 'Home Depot'])
            T.append(['456', 'National'])
            return T
        else:
            return []

    def searchByColor(self, color):
        result = []
        for r in self.data:
            if color == r[3]:
                result.append(r)
        return result
