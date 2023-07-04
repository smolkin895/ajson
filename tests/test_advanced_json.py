from collections import namedtuple

from advanced_json.extended_decoder import ExtendedDecoder

decoder = ExtendedDecoder()


def test_object_hook():
    some_json = namedtuple("cic", ["foo"])
    setattr(some_json, "__extended_json_type__", "dict")
    obj = decoder.object_hook(some_json)
    assert some_json is obj
