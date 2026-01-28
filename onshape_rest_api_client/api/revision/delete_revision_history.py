from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_revision_history_response_default import DeleteRevisionHistoryResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cid: str,
    pnum: str,
    et: str,
    *,
    ignore_linked_documents: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ignoreLinkedDocuments"] = ignore_linked_documents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/revisions/companies/{cid}/partnumber/{pnum}/elementType/{et}".format(
            cid=quote(str(cid), safe=""),
            pnum=quote(str(pnum), safe=""),
            et=quote(str(et), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteRevisionHistoryResponseDefault:
    response_default = DeleteRevisionHistoryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteRevisionHistoryResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cid: str,
    pnum: str,
    et: str,
    *,
    client: AuthenticatedClient,
    ignore_linked_documents: bool | Unset = False,
) -> Response[DeleteRevisionHistoryResponseDefault]:
    """Delete all revisions for a part number.

     Only company admins can call this API. All documents that contain or use the part number must be
    deleted first. This operation cannot be undone.

    Args:
        cid (str):
        pnum (str):
        et (str):
        ignore_linked_documents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRevisionHistoryResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        et=et,
        ignore_linked_documents=ignore_linked_documents,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cid: str,
    pnum: str,
    et: str,
    *,
    client: AuthenticatedClient,
    ignore_linked_documents: bool | Unset = False,
) -> DeleteRevisionHistoryResponseDefault | None:
    """Delete all revisions for a part number.

     Only company admins can call this API. All documents that contain or use the part number must be
    deleted first. This operation cannot be undone.

    Args:
        cid (str):
        pnum (str):
        et (str):
        ignore_linked_documents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRevisionHistoryResponseDefault
    """

    return sync_detailed(
        cid=cid,
        pnum=pnum,
        et=et,
        client=client,
        ignore_linked_documents=ignore_linked_documents,
    ).parsed


async def asyncio_detailed(
    cid: str,
    pnum: str,
    et: str,
    *,
    client: AuthenticatedClient,
    ignore_linked_documents: bool | Unset = False,
) -> Response[DeleteRevisionHistoryResponseDefault]:
    """Delete all revisions for a part number.

     Only company admins can call this API. All documents that contain or use the part number must be
    deleted first. This operation cannot be undone.

    Args:
        cid (str):
        pnum (str):
        et (str):
        ignore_linked_documents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRevisionHistoryResponseDefault]
    """

    kwargs = _get_kwargs(
        cid=cid,
        pnum=pnum,
        et=et,
        ignore_linked_documents=ignore_linked_documents,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cid: str,
    pnum: str,
    et: str,
    *,
    client: AuthenticatedClient,
    ignore_linked_documents: bool | Unset = False,
) -> DeleteRevisionHistoryResponseDefault | None:
    """Delete all revisions for a part number.

     Only company admins can call this API. All documents that contain or use the part number must be
    deleted first. This operation cannot be undone.

    Args:
        cid (str):
        pnum (str):
        et (str):
        ignore_linked_documents (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRevisionHistoryResponseDefault
    """

    return (
        await asyncio_detailed(
            cid=cid,
            pnum=pnum,
            et=et,
            client=client,
            ignore_linked_documents=ignore_linked_documents,
        )
    ).parsed
