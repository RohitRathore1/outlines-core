import json
import re

from outlines_core.fsm.json_schema import (  # noqa: F401
    BOOLEAN,
    DATE,
    DATE_TIME,
    EMAIL,
    INTEGER,
    NULL,
    NUMBER,
    STRING,
    STRING_INNER,
    TIME,
    URI,
    UUID,
    WHITESPACE,
    build_regex_from_schema,
)
from pydantic import BaseModel


def test_build_regex_from_json_schema():
    class FooBar(BaseModel):
        foo: int
        bar: str

    schema = json.dumps(FooBar.model_json_schema())

    regex = build_regex_from_schema(schema)
    expected = """{"foo" : 4 ,"bar":"baz    baz baz bar"}"""
    assert re.fullmatch(regex, expected)

    # any whitespace pattern can be used
    regex = build_regex_from_schema(schema, r"[\n ]*")
    expected = """{     "foo"   :   4, \n\n\n   "bar": "baz    baz baz bar"\n\n}"""
    assert re.fullmatch(regex, expected)


def test_types_presence():
    assert BOOLEAN
    assert DATE
    assert DATE_TIME
    assert EMAIL
    assert INTEGER
    assert NULL
    assert NUMBER
    assert STRING
    assert STRING_INNER
    assert TIME
    assert URI
    assert UUID
    assert WHITESPACE
