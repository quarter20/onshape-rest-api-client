import json
import sys

# Provides custom updates to the Onshape schema to fix mismatches between Onshape schema and actual data.

path = sys.argv[1]

with open(path) as f:
    data = json.load(f)

# Change "propertyIdToEvalInfo" type to allow null
propertyIdToEvalInfo = {
    "anyOf": [
        {
        "type": "object"
        },
        {
        "type": "null"
        }
    ]
}
data["components"]["schemas"]["BTAssemblyItemMetadataInfo"]["properties"]["propertyIdToEvalInfo"] = propertyIdToEvalInfo


with open(path, "w") as f:
    json.dump(data, f, indent=2)
