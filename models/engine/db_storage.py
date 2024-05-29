class DBStorage:
    # existing code...

    def get(self, cls, id):
        """Retrieve one object based on the class and its ID."""
        if cls and id:
            key = "{}.{}".format(cls.__name__, id)
            return self.all(cls).get(key)
        return None

    def count(self, cls=None):
        """Count the number of objects in storage matching the given class.
        If no class is passed, return the count of all objects in storage.
        """
        return len(self.all(cls))

