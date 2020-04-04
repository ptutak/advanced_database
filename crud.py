import sys
import argparse
from pprint import pformat

from pymongo import MongoClient
import schema


def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "operation",
        metavar="OPERATION",
        type=str,
    )

    parser.add_argument(
        "schema",
        metavar="SCHEMA",
        type=str,
    )

    parser.add_argument(
        "value",
        metavar="VALUE",
        type=str,
    )

    return parser.parse_args(args)


class Database:
    _schema = schema.schema

    def __init__(self):
        client = MongoClient()
        self._db = client.advanced_database

    def validate_schema(self, schema_name, value):
        if schema_name not in self._schema:
            raise RuntimeError(f"Schema {schema_name} does not exist")
        if set(self._schema[schema_name]) != set(value.keys()):
            raise RuntimeError(f"Value {pformat(value)} is not valid for schema: {schema_name}")

    def create(self, schema, value):
        pass

    def read(self, schema, value=None):
        pass

    def update(self, schema, value):
        pass

    def delete(self, schema, value=None):
        pass


def main():
    parsed_args = parse_args()
    if parsed_args.operation == "create":
        pass
    elif parsed_args.operation == "read":
        pass
    elif parsed_args.operation == "update":
        pass
    elif parsed_args.operation == "delete":
        pass
    else:
        print("Wrong operation")
        return -1

    return 0


if __name__ == "__main__":
    exit(main())
