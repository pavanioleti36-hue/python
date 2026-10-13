class InvalidFileFormatError(Exception): pass
class InvalidDataError(Exception): pass
class FileManager:
    def read_file(self, filename):
        try:
            if not filename.endswith(".txt"):
                raise InvalidFileFormatError("Only .txt files are allowed")
            with open(filename, "r") as file:
                data = file.read()
                if not data.strip():
                    raise InvalidDataError("File is empty")
                print(data)
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Permission denied")
        except (InvalidFileFormatError, InvalidDataError) as e:
            print(e)
manager = FileManager()
manager.read_file("sample.txt")