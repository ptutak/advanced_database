import sys
import argparse
from pprint import pformat
from copy import deepcopy

from pymongo import MongoClient
from bson.objectid import ObjectId
import schema


def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "operation", metavar="OPERATION", type=str,
    )

    parser.add_argument(
        "schema", metavar="SCHEMA", type=str,
    )

    parser.add_argument(
        "value", metavar="VALUE", type=str,
    )

    return parser.parse_args(args)


class Database:
    def __init__(self, version="1"):
        client = MongoClient()
        self._db = client.advanced_database
        for schema_version in schema.schema:
            if schema_version["_version"] == version:
                self._schema = schema_version
        self._create_indices()

    def _create_indices(self):
        for schema_name, index in self._schema["_indices"].items():
            getattr(self._db, schema_name).create_index(index)

    def validate_schema(self, schema_name, value):
        if schema_name not in self._schema:
            raise RuntimeError(f"Schema {schema_name} does not exist")
        if not set(self._schema[schema_name]) >= set(value.keys()):
            raise RuntimeError(
                f"Value {pformat(value)} is not valid for schema: {schema_name}"
            )

    def update_id(self, document):
        new_document = deepcopy(document)
        for key, value in document.items():
            if key.endswith("_id"):
                new_document[key] = ObjectId(value)
        return new_document

    def create(self, schema, value):
        return getattr(self._db, schema).insert_one(value).inserted_id

    def read(self, schema, value=None):
        return list(getattr(self._db, schema).find(value))

    def update(self, schema, value):
        query = {"_id": value["_id"]}
        del value["_id"]
        value = {"$set": value}
        result = getattr(self._db, schema).update_one(query, value)
        return (result.matched_count, result.modified_count)

    def delete(self, schema, value=None):
        return getattr(self._db, schema).delete_many(value).deleted_count

    def perform_operation(self, operation, schema, value):
        value = eval(value)
        self.validate_schema(schema, value)
        new_value = self.update_id(value)
        return getattr(self, operation)(schema, new_value)

    def __getattr__(self, attribute):
        return getattr(self._db, attribute)


def main():
    parsed_args = parse_args()
    if parsed_args.operation not in {"create", "read", "update", "delete"}:
        print("Wrong operation")
        return -1
    schema_version = parsed_args.schema.split(":")
    schema_name = schema_version[0]
    if len(schema_version) == 2:
        schema_version = schema_version[1]
    else:
        schema_version = "1"

    db = Database(schema_version)
    result = db.perform_operation(
        parsed_args.operation, schema_name, parsed_args.value
    )
    print(pformat(result))
    return 0


if __name__ == "__main__":
    exit(main())
