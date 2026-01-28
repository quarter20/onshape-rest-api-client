from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_feature_script_eval_call_2377 import BTFeatureScriptEvalCall2377
from ...models.bt_feature_script_eval_response_1859 import BTFeatureScriptEvalResponse1859
from ...models.eval_feature_script_wvm import EvalFeatureScriptWvm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: EvalFeatureScriptWvm,
    wvmid: str,
    eid: str,
    *,
    body: BTFeatureScriptEvalCall2377 | Unset = UNSET,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["linkDocumentId"] = link_document_id

    params["configuration"] = configuration

    params["rollbackBarIndex"] = rollback_bar_index

    params["elementMicroversionId"] = element_microversion_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/featurescript".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json;charset=UTF-8; qs=0.09"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BTFeatureScriptEvalResponse1859:
    response_default = BTFeatureScriptEvalResponse1859.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTFeatureScriptEvalResponse1859]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    did: str,
    wvm: EvalFeatureScriptWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureScriptEvalCall2377 | Unset = UNSET,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> Response[BTFeatureScriptEvalResponse1859]:
    """Evaluate the FeatureScript snippet for a Part Studio.

     See [API Guide: Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/fs/) for
    more details.

    Note that only lambda expressions can be evaulated with this endpoint.

    Args:
        did (str):
        wvm (EvalFeatureScriptWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (BTFeatureScriptEvalCall2377 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureScriptEvalResponse1859]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    did: str,
    wvm: EvalFeatureScriptWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureScriptEvalCall2377 | Unset = UNSET,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> BTFeatureScriptEvalResponse1859 | None:
    """Evaluate the FeatureScript snippet for a Part Studio.

     See [API Guide: Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/fs/) for
    more details.

    Note that only lambda expressions can be evaulated with this endpoint.

    Args:
        did (str):
        wvm (EvalFeatureScriptWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (BTFeatureScriptEvalCall2377 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureScriptEvalResponse1859
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: EvalFeatureScriptWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureScriptEvalCall2377 | Unset = UNSET,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> Response[BTFeatureScriptEvalResponse1859]:
    """Evaluate the FeatureScript snippet for a Part Studio.

     See [API Guide: Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/fs/) for
    more details.

    Note that only lambda expressions can be evaulated with this endpoint.

    Args:
        did (str):
        wvm (EvalFeatureScriptWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (BTFeatureScriptEvalCall2377 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTFeatureScriptEvalResponse1859]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        body=body,
        link_document_id=link_document_id,
        configuration=configuration,
        rollback_bar_index=rollback_bar_index,
        element_microversion_id=element_microversion_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    did: str,
    wvm: EvalFeatureScriptWvm,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    body: BTFeatureScriptEvalCall2377 | Unset = UNSET,
    link_document_id: str | Unset = "",
    configuration: str | Unset = "",
    rollback_bar_index: int | Unset = -1,
    element_microversion_id: str | Unset = UNSET,
) -> BTFeatureScriptEvalResponse1859 | None:
    """Evaluate the FeatureScript snippet for a Part Studio.

     See [API Guide: Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/fs/) for
    more details.

    Note that only lambda expressions can be evaulated with this endpoint.

    Args:
        did (str):
        wvm (EvalFeatureScriptWvm):
        wvmid (str):
        eid (str):
        link_document_id (str | Unset):  Default: ''.
        configuration (str | Unset):  Default: ''.
        rollback_bar_index (int | Unset):  Default: -1.
        element_microversion_id (str | Unset):
        body (BTFeatureScriptEvalCall2377 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTFeatureScriptEvalResponse1859
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            body=body,
            link_document_id=link_document_id,
            configuration=configuration,
            rollback_bar_index=rollback_bar_index,
            element_microversion_id=element_microversion_id,
        )
    ).parsed
