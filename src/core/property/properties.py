from src.core.util.tools import log_init
from src.main import Main

LOG = log_init(Main.log_file)


class Properties:
    def __init__(self, filename):
        self.filename = filename
        self.properties = {}

    def get(self, key: str) -> str:
        return self.properties[key.strip().upper()] if key.strip().upper() in self.properties else None

    def get_int(self, key: str) -> int:
        try:
            return int(self.get(key))
        except TypeError:
            return 0

    def read(self):
        with open(self.filename, 'r') as f_properties:
            all_properties = f_properties.readlines()
            for prop in all_properties:
                if prop.startswith('#'):
                    continue
                parts = prop.split('=', 1)
                if len(parts) != 2:
                    continue
                key = parts[0].strip().upper()
                value = parts[1].strip()
                self.properties[key] = value
            LOG.info('Successfully read {} properties from {}'.format(len(self.properties), self.filename))

        return self
