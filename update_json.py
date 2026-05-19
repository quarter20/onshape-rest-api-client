import json
import sys

# Provides custom updates to the Onshape schema to fix mismatches between Onshape schema and actual data.


def update_json(path: str) -> None:
    with open(path) as f:
        data = json.load(f)

    print("Applying schema modifications.....")
    nullable_object_type = {
        "anyOf": [
            {
            "type": "object"
            },
            {
            "type": "null"
            }
        ]
    }
    print('* Change "BTAssemblyItemMetadataInfo.propertyIdToEvalInfo" type to allow null')
    data["components"]["schemas"]["BTAssemblyItemMetadataInfo"]["properties"]["propertyIdToEvalInfo"] = nullable_object_type

    print('* Change "BTMetadataPropertyInfo.defaultValue" type to allow null')
    data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["defaultValue"] = nullable_object_type
    
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    update_json(sys.argv[1])
