from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_modify_info import BTAppElementModifyInfo
from ...models.upload_blob_subelement_body import UploadBlobSubelementBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    body: UploadBlobSubelementBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/appelements/d/{did}/w/{wid}/e/{eid}/blob/{bid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            bid=quote(str(bid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementModifyInfo:
    response_default = BTAppElementModifyInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementModifyInfo]:
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
    bid: str,
    *,
    client: AuthenticatedClient,
    body: UploadBlobSubelementBody | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    r"""Create a new blob subelement from an uploaded file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        body (UploadBlobSubelementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
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
    bid: str,
    *,
    client: AuthenticatedClient,
    body: UploadBlobSubelementBody | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    r"""Create a new blob subelement from an uploaded file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        body (UploadBlobSubelementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    body: UploadBlobSubelementBody | Unset = UNSET,
) -> Response[BTAppElementModifyInfo]:
    r"""Create a new blob subelement from an uploaded file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        body (UploadBlobSubelementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementModifyInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        bid=bid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    bid: str,
    *,
    client: AuthenticatedClient,
    body: UploadBlobSubelementBody | Unset = UNSET,
) -> BTAppElementModifyInfo | None:
    r"""Create a new blob subelement from an uploaded file.

     Request body parameters are multipart fields, so you must use `\"Content-Type\":\"multipart/form-
    data\"` in the request header.

    Args:
        did (str):
        wid (str):
        eid (str):
        bid (str):
        body (UploadBlobSubelementBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementModifyInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            bid=bid,
            client=client,
            body=body,
        )
    ).parsed
