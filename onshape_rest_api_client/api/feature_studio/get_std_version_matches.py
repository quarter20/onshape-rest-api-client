from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_feature_studio_std_version_matches_info import BTFeatureStudioStdVersionMatchesInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    *,
    include_versions: list[str] | Unset = UNSET,
    exclude_versions: list[str] | Unset = UNSET,
    feature_studio_name_wildcard_filter: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_versions: list[str] | Unset = UNSET
    if not isinstance(include_versions, Unset):
        json_include_versions = include_versions

    params["includeVersions"] = json_include_versions

    json_exclude_versions: list[str] | Unset = UNSET
    if not isinstance(exclude_versions, Unset):
        json_exclude_versions = exclude_versions

    params["excludeVersions"] = json_exclude_versions

    params["featureStudioNameWildcardFilter"] = feature_studio_name_wildcard_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/featurestudios/d/{did}/{wvm}/{wvmid}/stdversionmatches".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTFeatureStudioStdVersionMatchesInfo:
    response_default = BTFeatureStudioStdVersionMatchesInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTFeatureStudioStdVersionMatchesInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    include_versions: list[str] | Unset = UNSET,
    exclude_versions: list[str] | Unset = UNSET,
    feature_studio_name_wildcard_filter: str | Unset = UNSET,
) -> Response[BTFeatureStudioStdVersionMatchesInfo]:
    """Find the standard library versions imported by the Feature Studios of a document.

     Reports every `onshape/std` import whose version is selected by the `includeVersions` and
    `excludeVersions` filters, one entry per Feature Studio. A filter term is a version (e.g., `2830`),
    a specific point release (e.g., `2830.1`), or a range with either end optionally omitted (e.g.,
    `2600-2700`, `2900-`, `-1800`). Terms may be repeated or given as a comma separated list. An empty
    `includeVersions` matches every version.
    If there are too many matches to report, the result is truncated and 'resultsTruncated' is true;
    narrow the filters to see the rest.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        include_versions (list[str] | Unset):
        exclude_versions (list[str] | Unset):
        feature_studio_name_wildcard_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureStudioStdVersionMatchesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        include_versions=include_versions,
        exclude_versions=exclude_versions,
        feature_studio_name_wildcard_filter=feature_studio_name_wildcard_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    include_versions: list[str] | Unset = UNSET,
    exclude_versions: list[str] | Unset = UNSET,
    feature_studio_name_wildcard_filter: str | Unset = UNSET,
) -> BTFeatureStudioStdVersionMatchesInfo | None:
    """Find the standard library versions imported by the Feature Studios of a document.

     Reports every `onshape/std` import whose version is selected by the `includeVersions` and
    `excludeVersions` filters, one entry per Feature Studio. A filter term is a version (e.g., `2830`),
    a specific point release (e.g., `2830.1`), or a range with either end optionally omitted (e.g.,
    `2600-2700`, `2900-`, `-1800`). Terms may be repeated or given as a comma separated list. An empty
    `includeVersions` matches every version.
    If there are too many matches to report, the result is truncated and 'resultsTruncated' is true;
    narrow the filters to see the rest.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        include_versions (list[str] | Unset):
        exclude_versions (list[str] | Unset):
        feature_studio_name_wildcard_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureStudioStdVersionMatchesInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        client=client,
        include_versions=include_versions,
        exclude_versions=exclude_versions,
        feature_studio_name_wildcard_filter=feature_studio_name_wildcard_filter,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    include_versions: list[str] | Unset = UNSET,
    exclude_versions: list[str] | Unset = UNSET,
    feature_studio_name_wildcard_filter: str | Unset = UNSET,
) -> Response[BTFeatureStudioStdVersionMatchesInfo]:
    """Find the standard library versions imported by the Feature Studios of a document.

     Reports every `onshape/std` import whose version is selected by the `includeVersions` and
    `excludeVersions` filters, one entry per Feature Studio. A filter term is a version (e.g., `2830`),
    a specific point release (e.g., `2830.1`), or a range with either end optionally omitted (e.g.,
    `2600-2700`, `2900-`, `-1800`). Terms may be repeated or given as a comma separated list. An empty
    `includeVersions` matches every version.
    If there are too many matches to report, the result is truncated and 'resultsTruncated' is true;
    narrow the filters to see the rest.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        include_versions (list[str] | Unset):
        exclude_versions (list[str] | Unset):
        feature_studio_name_wildcard_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureStudioStdVersionMatchesInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        include_versions=include_versions,
        exclude_versions=exclude_versions,
        feature_studio_name_wildcard_filter=feature_studio_name_wildcard_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    *,
    client: AuthenticatedClient,
    include_versions: list[str] | Unset = UNSET,
    exclude_versions: list[str] | Unset = UNSET,
    feature_studio_name_wildcard_filter: str | Unset = UNSET,
) -> BTFeatureStudioStdVersionMatchesInfo | None:
    """Find the standard library versions imported by the Feature Studios of a document.

     Reports every `onshape/std` import whose version is selected by the `includeVersions` and
    `excludeVersions` filters, one entry per Feature Studio. A filter term is a version (e.g., `2830`),
    a specific point release (e.g., `2830.1`), or a range with either end optionally omitted (e.g.,
    `2600-2700`, `2900-`, `-1800`). Terms may be repeated or given as a comma separated list. An empty
    `includeVersions` matches every version.
    If there are too many matches to report, the result is truncated and 'resultsTruncated' is true;
    narrow the filters to see the rest.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        include_versions (list[str] | Unset):
        exclude_versions (list[str] | Unset):
        feature_studio_name_wildcard_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureStudioStdVersionMatchesInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            client=client,
            include_versions=include_versions,
            exclude_versions=exclude_versions,
            feature_studio_name_wildcard_filter=feature_studio_name_wildcard_filter,
        )
    ).parsed
