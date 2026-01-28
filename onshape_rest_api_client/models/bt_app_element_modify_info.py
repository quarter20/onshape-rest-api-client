from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_diff_json_response_2725 import BTDiffJsonResponse2725


T = TypeVar("T", bound="BTAppElementModifyInfo")


@_attrs_define
class BTAppElementModifyInfo:
    """
    Attributes:
        change_id (str): The latest change id for the element, after the edit was committed.
        element_id (str | Unset): The id of the edited element.
        element_ids (list[str] | Unset): The ids of the edited elements, if multiple elements were edited.
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
        json_difference (BTDiffJsonResponse2725 | Unset):
        parent_change_id (str | Unset): The latest change id for the element, before the edit was made.
        property_edits_merged (bool | Unset): When committing a transaction, this field indicates if the properties of
            the application element were changed after the transaction was created.
        transaction_id (str | Unset): The id of the transaction in which the edit was applied.
    """

    change_id: str
    element_id: str | Unset = UNSET
    element_ids: list[str] | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    json_difference: BTDiffJsonResponse2725 | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    property_edits_merged: bool | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        element_id = self.element_id

        element_ids: list[str] | Unset = UNSET
        if not isinstance(self.element_ids, Unset):
            element_ids = self.element_ids

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        json_difference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_difference, Unset):
            json_difference = self.json_difference.to_dict()

        parent_change_id = self.parent_change_id

        property_edits_merged = self.property_edits_merged

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeId": change_id,
            }
        )
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
        if json_difference is not UNSET:
            field_dict["jsonDifference"] = json_difference
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if property_edits_merged is not UNSET:
            field_dict["propertyEditsMerged"] = property_edits_merged
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_diff_json_response_2725 import BTDiffJsonResponse2725

        d = dict(src_dict)
        change_id = d.pop("changeId")

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

        _json_difference = d.pop("jsonDifference", UNSET)
        json_difference: BTDiffJsonResponse2725 | Unset
        if isinstance(_json_difference, Unset):
            json_difference = UNSET
        else:
            json_difference = BTDiffJsonResponse2725.from_dict(_json_difference)

        parent_change_id = d.pop("parentChangeId", UNSET)

        property_edits_merged = d.pop("propertyEditsMerged", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        bt_app_element_modify_info = cls(
            change_id=change_id,
            element_id=element_id,
            element_ids=element_ids,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
            json_difference=json_difference,
            parent_change_id=parent_change_id,
            property_edits_merged=property_edits_merged,
            transaction_id=transaction_id,
        )

        bt_app_element_modify_info.additional_properties = d
        return bt_app_element_modify_info

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
