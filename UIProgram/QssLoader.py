class QSSLoader:
    @staticmethod
    def read_qss_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading QSS file: {e}")
            return ""
