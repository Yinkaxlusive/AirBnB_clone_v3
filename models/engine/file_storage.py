class FileStorage:
    # existing code...

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    cls_name = value['__class__']
                    cls = classes[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

