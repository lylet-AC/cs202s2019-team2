class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.assigned = False

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_assigned(self):
        self.assigned = True

    def get_assigned(self):
        return self.assigned
