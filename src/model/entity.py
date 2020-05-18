class Entity:
    def __init__(self, entity_id: str = None):
        self.uuid = entity_id

    def __str__(self):
        return "{:36}".format(self.uuid)
