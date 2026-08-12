from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.btb_file_upload import BTBFileUpload
from ...models.update_library_response_default import UpdateLibraryResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    *,
    body: BTBFileUpload | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/materials/libraries/d/{did}/w/{wid}/e/{eid}/csv".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateLibraryResponseDefault:
    response_default = UpdateLibraryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateLibraryResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBFileUpload | Unset = UNSET,
) -> Response[UpdateLibraryResponseDefault]:
    """Updates an existing material library

     Update a material in an Onshape Material Library from a csv file. Changes made replace the existing
    library.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTBFileUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateLibraryResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBFileUpload | Unset = UNSET,
) -> UpdateLibraryResponseDefault | None:
    """Updates an existing material library

     Update a material in an Onshape Material Library from a csv file. Changes made replace the existing
    library.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTBFileUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateLibraryResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBFileUpload | Unset = UNSET,
) -> Response[UpdateLibraryResponseDefault]:
    """Updates an existing material library

     Update a material in an Onshape Material Library from a csv file. Changes made replace the existing
    library.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTBFileUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateLibraryResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTBFileUpload | Unset = UNSET,
) -> UpdateLibraryResponseDefault | None:
    """Updates an existing material library

     Update a material in an Onshape Material Library from a csv file. Changes made replace the existing
    library.

    Args:
        did (str):
        wid (str):
        eid (str):
        body (BTBFileUpload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateLibraryResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            client=client,
            body=body,
        )
    ).parsed
