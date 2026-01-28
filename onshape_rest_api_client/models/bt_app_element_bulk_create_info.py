from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementBulkCreateInfo")


@_attrs_define
class BTAppElementBulkCreateInfo:
    """
    Attributes:
        document_microversion_id (str): The latest document microversion, after the edit was committed.
        element_ids (list[str] | Unset): The ids of the created elements.
        element_microversions (list[str] | Unset): The microversion ids of the created elements, at creation time.
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
    """

    document_microversion_id: str
    element_ids: list[str] | Unset = UNSET
    element_microversions: list[str] | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_microversion_id = self.document_microversion_id

        element_ids: list[str] | Unset = UNSET
        if not isinstance(self.element_ids, Unset):
            element_ids = self.element_ids

        element_microversions: list[str] | Unset = UNSET
        if not isinstance(self.element_microversions, Unset):
            element_microversions = self.element_microversions

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentMicroversionId": document_microversion_id,
            }
        )
        if element_ids is not UNSET:
            field_dict["elementIds"] = element_ids
        if element_microversions is not UNSET:
            field_dict["elementMicroversions"] = element_microversions
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_microversion_id = d.pop("documentMicroversionId")

        element_ids = cast(list[str], d.pop("elementIds", UNSET))

        element_microversions = cast(list[str], d.pop("elementMicroversions", UNSET))

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        bt_app_element_bulk_create_info = cls(
            document_microversion_id=document_microversion_id,
            element_ids=element_ids,
            element_microversions=element_microversions,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
        )

        bt_app_element_bulk_create_info.additional_properties = d
        return bt_app_element_bulk_create_info

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
