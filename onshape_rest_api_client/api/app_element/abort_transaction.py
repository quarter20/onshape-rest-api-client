from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.abort_transaction_response_default import AbortTransactionResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wid: str,
    eid: str,
    tid: str,
    *,
    return_error: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["returnError"] = return_error

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/appelements/d/{did}/w/{wid}/e/{eid}/transactions/{tid}".format(
            did=quote(str(did), safe=""),
            wid=quote(str(wid), safe=""),
            eid=quote(str(eid), safe=""),
            tid=quote(str(tid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AbortTransactionResponseDefault:
    response_default = AbortTransactionResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AbortTransactionResponseDefault]:
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
    tid: str,
    *,
    client: AuthenticatedClient,
    return_error: bool | Unset = True,
) -> Response[AbortTransactionResponseDefault]:
    """Abort a transaction.

     Deletes a microbranch (i.e., the branch with the microversion for the transaction).

    Args:
        did (str):
        wid (str):
        eid (str):
        tid (str):
        return_error (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AbortTransactionResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        tid=tid,
        return_error=return_error,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wid: str,
    eid: str,
    tid: str,
    *,
    client: AuthenticatedClient,
    return_error: bool | Unset = True,
) -> AbortTransactionResponseDefault | None:
    """Abort a transaction.

     Deletes a microbranch (i.e., the branch with the microversion for the transaction).

    Args:
        did (str):
        wid (str):
        eid (str):
        tid (str):
        return_error (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AbortTransactionResponseDefault
    """

    return sync_detailed(
        did=did,
        wid=wid,
        eid=eid,
        tid=tid,
        client=client,
        return_error=return_error,
    ).parsed


async def asyncio_detailed(
    did: str,
    wid: str,
    eid: str,
    tid: str,
    *,
    client: AuthenticatedClient,
    return_error: bool | Unset = True,
) -> Response[AbortTransactionResponseDefault]:
    """Abort a transaction.

     Deletes a microbranch (i.e., the branch with the microversion for the transaction).

    Args:
        did (str):
        wid (str):
        eid (str):
        tid (str):
        return_error (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AbortTransactionResponseDefault]
    """

    kwargs = _get_kwargs(
        did=did,
        wid=wid,
        eid=eid,
        tid=tid,
        return_error=return_error,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wid: str,
    eid: str,
    tid: str,
    *,
    client: AuthenticatedClient,
    return_error: bool | Unset = True,
) -> AbortTransactionResponseDefault | None:
    """Abort a transaction.

     Deletes a microbranch (i.e., the branch with the microversion for the transaction).

    Args:
        did (str):
        wid (str):
        eid (str):
        tid (str):
        return_error (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AbortTransactionResponseDefault
    """

    return (
        await asyncio_detailed(
            did=did,
            wid=wid,
            eid=eid,
            tid=tid,
            client=client,
            return_error=return_error,
        )
    ).parsed
