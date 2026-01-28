from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_modify_info import BTAppElementModifyInfo


T = TypeVar("T", bound="BTAppElementBulkModifyInfo")


@_attrs_define
class BTAppElementBulkModifyInfo:
    """
    Attributes:
        change_id (str | Unset): The latest change id for the element, after the edit was committed. Deprecated in favor
            of elementChangeResults.
        document_microversion_id (str | Unset): The latest change id for the document, after the edit was committed.
        element_change_results (list[BTAppElementModifyInfo] | Unset): The results of editing each element affected by
            the edit.
        element_id (str | Unset): The id of the edited element, if a single element was edited. Deprecated in favor of
            elementChangeResults.
        element_ids (list[str] | Unset): The ids of the edited elements. Deprecated in favor of elementChangeResults.
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
        parent_change_id (str | Unset): The latest change id for the element, before the edit was made. Deprecated in
            favor of elementChangeResults.
        parent_document_microversion_id (str | Unset): The latest change id for the document, before the edit was made.
        property_edits_merged (bool | Unset): Whether the properties of any edited application element were changed
            after the transaction was created. Deprecated in favor of elementChangeResults.
        transaction_id (str | Unset): The id of the transaction in which the edit was applied. Deprecated in favor of
            elementChangeResults.
    """

    change_id: str | Unset = UNSET
    document_microversion_id: str | Unset = UNSET
    element_change_results: list[BTAppElementModifyInfo] | Unset = UNSET
    element_id: str | Unset = UNSET
    element_ids: list[str] | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    parent_document_microversion_id: str | Unset = UNSET
    property_edits_merged: bool | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        document_microversion_id = self.document_microversion_id

        element_change_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element_change_results, Unset):
            element_change_results = []
            for element_change_results_item_data in self.element_change_results:
                element_change_results_item = element_change_results_item_data.to_dict()
                element_change_results.append(element_change_results_item)

        element_id = self.element_id

        element_ids: list[str] | Unset = UNSET
        if not isinstance(self.element_ids, Unset):
            element_ids = self.element_ids

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        parent_change_id = self.parent_change_id

        parent_document_microversion_id = self.parent_document_microversion_id

        property_edits_merged = self.property_edits_merged

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if document_microversion_id is not UNSET:
            field_dict["documentMicroversionId"] = document_microversion_id
        if element_change_results is not UNSET:
            field_dict["elementChangeResults"] = element_change_results
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_ids is not UNSET:
            field_dict["elementIds"] = element_ids
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if parent_document_microversion_id is not UNSET:
            field_dict["parentDocumentMicroversionId"] = parent_document_microversion_id
        if property_edits_merged is not UNSET:
            field_dict["propertyEditsMerged"] = property_edits_merged
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_modify_info import BTAppElementModifyInfo

        d = dict(src_dict)
        change_id = d.pop("changeId", UNSET)

        document_microversion_id = d.pop("documentMicroversionId", UNSET)

        _element_change_results = d.pop("elementChangeResults", UNSET)
        element_change_results: list[BTAppElementModifyInfo] | Unset = UNSET
        if _element_change_results is not UNSET:
            element_change_results = []
            for element_change_results_item_data in _element_change_results:
                element_change_results_item = BTAppElementModifyInfo.from_dict(element_change_results_item_data)

                element_change_results.append(element_change_results_item)

        element_id = d.pop("elementId", UNSET)

        element_ids = cast(list[str], d.pop("elementIds", UNSET))

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        parent_change_id = d.pop("parentChangeId", UNSET)

        parent_document_microversion_id = d.pop("parentDocumentMicroversionId", UNSET)

        property_edits_merged = d.pop("propertyEditsMerged", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        bt_app_element_bulk_modify_info = cls(
            change_id=change_id,
            document_microversion_id=document_microversion_id,
            element_change_results=element_change_results,
            element_id=element_id,
            element_ids=element_ids,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
            parent_change_id=parent_change_id,
            parent_document_microversion_id=parent_document_microversion_id,
            property_edits_merged=property_edits_merged,
            transaction_id=transaction_id,
        )

        bt_app_element_bulk_modify_info.additional_properties = d
        return bt_app_element_bulk_modify_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
