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
    string_or_object_type = {
        "anyOf": [
            {
            "type": "object"
            },
            {
            "type": "string"
            }
        ]
    }
    print('* Change "BTAssemblyItemMetadataInfo.propertyIdToEvalInfo" type to allow null')
    data["components"]["schemas"]["BTAssemblyItemMetadataInfo"]["properties"]["propertyIdToEvalInfo"] = nullable_object_type

    print('* Change "BTMetadataPropertyInfo.defaultValue" type to allow null')
    data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["defaultValue"] = nullable_object_type

    print('* Change "BTMetadataPropertyInfo.enumValues" type to allow null')
    data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["enumValues"]["nullable"] = True

    print('* Change "BTMetadataPropertyInfo.value" type to allow object or string')
    data["components"]["schemas"]["BTMetadataPropertyInfo"]["properties"]["value"] = string_or_object_type

    print('* Change "BTMetadataPropertyValidatorInfo.maxDate" and "BTMetadataPropertyValidatorInfo.minDate" type to allow null')
    data["components"]["schemas"]["BTMetadataPropertyValidatorInfo"]["properties"]["maxDate"]["nullable"] = True
    data["components"]["schemas"]["BTMetadataPropertyValidatorInfo"]["properties"]["minDate"]["nullable"] = True

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    update_json(sys.argv[1])
