#!/usr/bin/env bash
set -euo pipefail

echo "-------------------------------------------"
echo "Updating onshape_rest_api_client (Mac only)"
pushd /tmp
pipx install --force openapi-python-client --include-deps
curl -H "Accept: application/json" https://cad.onshape.com/api/openapi -o onshape_openapi.json
popd
python3 update_json.py /tmp/onshape_openapi.json
pushd /tmp
openapi-python-client generate --path onshape_openapi.json --overwrite
echo "Changelog info:"
jq ".servers[0].url, .info.version" onshape_openapi.json
openapi-python-client --version
popd
[ -d /tmp/onshape-rest-api-client/onshape_rest_api_client ] || { echo "generation failed: /tmp/onshape-rest-api-client/onshape_rest_api_client not found"; exit 1; }
trash onshape_rest_api_client
mv /tmp/onshape-rest-api-client/onshape_rest_api_client .
echo "-------------------------------------------"
echo "Now"
echo "1. add release details to CHANGELOG.md (doublecheck first column for duplicates!)"
echo ""
echo "|$(jq -r '.info.version | sub("\\.[^.]*$"; ".0")' /tmp/onshape_openapi.json)|$(date '+%B %-d, %Y')|$(jq -r '.servers[0].url | split("/") | last' /tmp/onshape_openapi.json)|$(openapi-python-client --version | awk '{print $NF}')|"
echo "
echo "2. update pyproject.toml [project] version"
echo "3. if server url has changed, update README.md"
echo "4. commit to github"
echo "5. poetry build"
echo "6. poetry publish"

