from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_diff_json_response_2725 import BTDiffJsonResponse2725
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    json_difference_format: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params["versionId"] = version_id

    params["microversionId"] = microversion_id

    params["linkDocumentId"] = link_document_id

    params["jsonDifferenceFormat"] = json_difference_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/compare".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTDiffJsonResponse2725:
    response_default = BTDiffJsonResponse2725.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTDiffJsonResponse2725]:
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
    eid: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    json_difference_format: str | Unset = UNSET,
) -> Response[BTDiffJsonResponse2725]:
    """Compare app element JSON trees between workspaces/versions/microversions in a document.

     Specify the source workspace/version/microversion in the URL and specify the target
    workspace/version/microversion in the query parameters.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        link_document_id (str | Unset):
        json_difference_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDiffJsonResponse2725]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        link_document_id=link_document_id,
        json_difference_format=json_difference_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    json_difference_format: str | Unset = UNSET,
) -> BTDiffJsonResponse2725 | None:
    """Compare app element JSON trees between workspaces/versions/microversions in a document.

     Specify the source workspace/version/microversion in the URL and specify the target
    workspace/version/microversion in the query parameters.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        link_document_id (str | Unset):
        json_difference_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDiffJsonResponse2725
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        link_document_id=link_document_id,
        json_difference_format=json_difference_format,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    json_difference_format: str | Unset = UNSET,
) -> Response[BTDiffJsonResponse2725]:
    """Compare app element JSON trees between workspaces/versions/microversions in a document.

     Specify the source workspace/version/microversion in the URL and specify the target
    workspace/version/microversion in the query parameters.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        link_document_id (str | Unset):
        json_difference_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTDiffJsonResponse2725]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        workspace_id=workspace_id,
        version_id=version_id,
        microversion_id=microversion_id,
        link_document_id=link_document_id,
        json_difference_format=json_difference_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str | Unset = UNSET,
    version_id: str | Unset = UNSET,
    microversion_id: str | Unset = UNSET,
    link_document_id: str | Unset = UNSET,
    json_difference_format: str | Unset = UNSET,
) -> BTDiffJsonResponse2725 | None:
    """Compare app element JSON trees between workspaces/versions/microversions in a document.

     Specify the source workspace/version/microversion in the URL and specify the target
    workspace/version/microversion in the query parameters.

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        workspace_id (str | Unset):
        version_id (str | Unset):
        microversion_id (str | Unset):
        link_document_id (str | Unset):
        json_difference_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTDiffJsonResponse2725
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            workspace_id=workspace_id,
            version_id=version_id,
            microversion_id=microversion_id,
            link_document_id=link_document_id,
            json_difference_format=json_difference_format,
        )
    ).parsed
