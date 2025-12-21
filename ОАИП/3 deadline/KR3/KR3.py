class FileManager:
    
    def search_file(self, file_system: dict, target_file: str, current_path: str = "") -> str:
        for key, value in file_system.items():
            new_path = f"{current_path}/{key}" if current_path else key
            if isinstance(value, list):
                if target_file in value:
                    return new_path
            elif isinstance(value, dict):
                result = self.search_file(value, target_file, new_path)
                if result:
                    return result
        return ""

    def find_file(self, file_system: dict, target_file: str):
        result = self.search_file(file_system, target_file)
        if result:
            return result
        else:
            return True if result else False

if __name__ == "__main__":
    file_system = {
        "Folder1": {
            "Subfolder1": ["file1.txt", "file2.txt"],
            "Subfolder2": ["file3.txt", "file4.txt"]
        },
        "Folder2": {
            "Subfolder3": {
                "DeepFolder": ["file5.txt", "file6.txt"]
            },
            "file7.txt": []
        }
    }
    
    fm = FileManager()

    test_files = ["file5.txt", "file7.txt", "nonexistent.txt"]
    
    for test_file in test_files:
        result = fm.find_file(file_system, test_file)
        print(f"Поиск файла '{test_file}': {result}")
