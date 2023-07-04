import json
from collections import namedtuple


class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        self.sucess_count = 0
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
            self.sucess_count += 1
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)


some_json = namedtuple("cic", ["foo"])
print(dir(some_json))
