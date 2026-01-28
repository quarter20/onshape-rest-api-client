from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bt_app_element_basic_info import BTAppElementBasicInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    transaction_id: str | Unset = "",
    parent_change_id: str | Unset = "",
    associative_data_id: list[str] | Unset = UNSET,
    external_document_id: str | Unset = "",
    element_id: str | Unset = "",
    view_id: str | Unset = "",
    microversion_id: str | Unset = "",
    document_microversion: str | Unset = "",
    deterministic_id: str | Unset = "",
    feature_id: str | Unset = "",
    entity_id: str | Unset = "",
    occurrence_id: str | Unset = "",
    reference_id: str | Unset = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionId"] = transaction_id

    params["parentChangeId"] = parent_change_id

    json_associative_data_id: list[str] | Unset = UNSET
    if not isinstance(associative_data_id, Unset):
        json_associative_data_id = associative_data_id

    params["associativeDataId"] = json_associative_data_id

    params["externalDocumentId"] = external_document_id

    params["elementId"] = element_id

    params["viewId"] = view_id

    params["microversionId"] = microversion_id

    params["documentMicroversion"] = document_microversion

    params["deterministicId"] = deterministic_id

    params["featureId"] = feature_id

    params["entityId"] = entity_id

    params["occurrenceId"] = occurrence_id

    params["referenceId"] = reference_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/appelements/d/{did}/{wvm}/{wvmid}/e/{eid}/associativedata".format(
            did=quote(str(did), safe=""),
            wvm=quote(str(wvm), safe=""),
            wvmid=quote(str(wvmid), safe=""),
            eid=quote(str(eid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BTAppElementBasicInfo:
    response_default = BTAppElementBasicInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BTAppElementBasicInfo]:
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
    transaction_id: str | Unset = "",
    parent_change_id: str | Unset = "",
    associative_data_id: list[str] | Unset = UNSET,
    external_document_id: str | Unset = "",
    element_id: str | Unset = "",
    view_id: str | Unset = "",
    microversion_id: str | Unset = "",
    document_microversion: str | Unset = "",
    deterministic_id: str | Unset = "",
    feature_id: str | Unset = "",
    entity_id: str | Unset = "",
    occurrence_id: str | Unset = "",
    reference_id: str | Unset = "",
) -> Response[BTAppElementBasicInfo]:
    """Delete the associative data from the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):  Default: ''.
        associative_data_id (list[str] | Unset):
        external_document_id (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        view_id (str | Unset):  Default: ''.
        microversion_id (str | Unset):  Default: ''.
        document_microversion (str | Unset):  Default: ''.
        deterministic_id (str | Unset):  Default: ''.
        feature_id (str | Unset):  Default: ''.
        entity_id (str | Unset):  Default: ''.
        occurrence_id (str | Unset):  Default: ''.
        reference_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementBasicInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        associative_data_id=associative_data_id,
        external_document_id=external_document_id,
        element_id=element_id,
        view_id=view_id,
        microversion_id=microversion_id,
        document_microversion=document_microversion,
        deterministic_id=deterministic_id,
        feature_id=feature_id,
        entity_id=entity_id,
        occurrence_id=occurrence_id,
        reference_id=reference_id,
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
    transaction_id: str | Unset = "",
    parent_change_id: str | Unset = "",
    associative_data_id: list[str] | Unset = UNSET,
    external_document_id: str | Unset = "",
    element_id: str | Unset = "",
    view_id: str | Unset = "",
    microversion_id: str | Unset = "",
    document_microversion: str | Unset = "",
    deterministic_id: str | Unset = "",
    feature_id: str | Unset = "",
    entity_id: str | Unset = "",
    occurrence_id: str | Unset = "",
    reference_id: str | Unset = "",
) -> BTAppElementBasicInfo | None:
    """Delete the associative data from the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):  Default: ''.
        associative_data_id (list[str] | Unset):
        external_document_id (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        view_id (str | Unset):  Default: ''.
        microversion_id (str | Unset):  Default: ''.
        document_microversion (str | Unset):  Default: ''.
        deterministic_id (str | Unset):  Default: ''.
        feature_id (str | Unset):  Default: ''.
        entity_id (str | Unset):  Default: ''.
        occurrence_id (str | Unset):  Default: ''.
        reference_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementBasicInfo
    """

    return sync_detailed(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        client=client,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        associative_data_id=associative_data_id,
        external_document_id=external_document_id,
        element_id=element_id,
        view_id=view_id,
        microversion_id=microversion_id,
        document_microversion=document_microversion,
        deterministic_id=deterministic_id,
        feature_id=feature_id,
        entity_id=entity_id,
        occurrence_id=occurrence_id,
        reference_id=reference_id,
    ).parsed


async def asyncio_detailed(
    did: str,
    wvm: str,
    wvmid: str,
    eid: str,
    *,
    client: AuthenticatedClient,
    transaction_id: str | Unset = "",
    parent_change_id: str | Unset = "",
    associative_data_id: list[str] | Unset = UNSET,
    external_document_id: str | Unset = "",
    element_id: str | Unset = "",
    view_id: str | Unset = "",
    microversion_id: str | Unset = "",
    document_microversion: str | Unset = "",
    deterministic_id: str | Unset = "",
    feature_id: str | Unset = "",
    entity_id: str | Unset = "",
    occurrence_id: str | Unset = "",
    reference_id: str | Unset = "",
) -> Response[BTAppElementBasicInfo]:
    """Delete the associative data from the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):  Default: ''.
        associative_data_id (list[str] | Unset):
        external_document_id (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        view_id (str | Unset):  Default: ''.
        microversion_id (str | Unset):  Default: ''.
        document_microversion (str | Unset):  Default: ''.
        deterministic_id (str | Unset):  Default: ''.
        feature_id (str | Unset):  Default: ''.
        entity_id (str | Unset):  Default: ''.
        occurrence_id (str | Unset):  Default: ''.
        reference_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BTAppElementBasicInfo]
    """

    kwargs = _get_kwargs(
        did=did,
        wvm=wvm,
        wvmid=wvmid,
        eid=eid,
        transaction_id=transaction_id,
        parent_change_id=parent_change_id,
        associative_data_id=associative_data_id,
        external_document_id=external_document_id,
        element_id=element_id,
        view_id=view_id,
        microversion_id=microversion_id,
        document_microversion=document_microversion,
        deterministic_id=deterministic_id,
        feature_id=feature_id,
        entity_id=entity_id,
        occurrence_id=occurrence_id,
        reference_id=reference_id,
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
    transaction_id: str | Unset = "",
    parent_change_id: str | Unset = "",
    associative_data_id: list[str] | Unset = UNSET,
    external_document_id: str | Unset = "",
    element_id: str | Unset = "",
    view_id: str | Unset = "",
    microversion_id: str | Unset = "",
    document_microversion: str | Unset = "",
    deterministic_id: str | Unset = "",
    feature_id: str | Unset = "",
    entity_id: str | Unset = "",
    occurrence_id: str | Unset = "",
    reference_id: str | Unset = "",
) -> BTAppElementBasicInfo | None:
    """Delete the associative data from the specified app element.

     You can manage associativity with
    [translateIds](https://cad.onshape.com/glassworks/explorer/#/PartStudio/translateIds).

    Args:
        did (str):
        wvm (str):
        wvmid (str):
        eid (str):
        transaction_id (str | Unset):  Default: ''.
        parent_change_id (str | Unset):  Default: ''.
        associative_data_id (list[str] | Unset):
        external_document_id (str | Unset):  Default: ''.
        element_id (str | Unset):  Default: ''.
        view_id (str | Unset):  Default: ''.
        microversion_id (str | Unset):  Default: ''.
        document_microversion (str | Unset):  Default: ''.
        deterministic_id (str | Unset):  Default: ''.
        feature_id (str | Unset):  Default: ''.
        entity_id (str | Unset):  Default: ''.
        occurrence_id (str | Unset):  Default: ''.
        reference_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BTAppElementBasicInfo
    """

    return (
        await asyncio_detailed(
            did=did,
            wvm=wvm,
            wvmid=wvmid,
            eid=eid,
            client=client,
            transaction_id=transaction_id,
            parent_change_id=parent_change_id,
            associative_data_id=associative_data_id,
            external_document_id=external_document_id,
            element_id=element_id,
            view_id=view_id,
            microversion_id=microversion_id,
            document_microversion=document_microversion,
            deterministic_id=deterministic_id,
            feature_id=feature_id,
            entity_id=entity_id,
            occurrence_id=occurrence_id,
            reference_id=reference_id,
        )
    ).parsed
