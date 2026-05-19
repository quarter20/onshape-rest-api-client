import json
import sys

# Provides custom updates to the Onshape schema to fix mismatches between Onshape schema and actual data.

def add_type_schema(node: dict, type_name: str):
    """Replaces type in schema to allow nullable value, for use with .  Do not user for v"""

    return {
        "anyOf": [
            node,
            {
            "type": type_name
            }
        ]
    }

def add_null_to_type(node: dict):
    add_type_schema(node, "null")

def add_str_to_type(node: dict):
    add_type_schema(node, "string")

def add_nullable(node: dict):
    node["nullable"] = True

def update_json(path: str) -> None:
    with open(path) as f:
        data = json.load(f)

    print("Applying schema modifications.....")

    print('* Change "BTAssemblyItemMetadataInfo.propertyIdToEvalInfo" type to allow null')
    print(data["components"]["schemas"]["BTAssemblyItemMetadataInfo"]["properties"]["propertyIdToEvalInfo"])
    add_null_to_type(data["components"]["schemas"]["BTAssemblyItemMetadataInfo"]["properties"]["propertyIdToEvalInfo"])

    print('* Change "BTMetadataPropertyInfo.defaultValue" type to allow null')
    add_null_to_type(data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["defaultValue"])

    print('* Change "BTMetadataPropertyInfo.enumValues" type to allow null')
    add_nullable(data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["enumValues"])
    
    print('* Change "BTMetadataPropertyInfo.uiHints" type to allow null')
    add_null_to_type(data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["uiHints"])

    print('* Change "BTMetadataPropertyInfo.value" type to allow object or string')
    add_str_to_type(data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["value"])

    print('* Change "BTMetadataPropertyValidatorInfo.maxDate" and "BTMetadataPropertyValidatorInfo.minDate" type to allow null')
    add_nullable(data["components"]["schemas"]["BTMetadataPropertyValidatorInfo"]["properties"]["maxDate"])
    add_nullable(data["components"]["schemas"]["BTMetadataPropertyValidatorInfo"]["properties"]["minDate"])

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    update_json(sys.argv[1])
