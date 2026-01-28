from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTRevertUnchangedElementParams")


@_attrs_define
class BTRevertUnchangedElementParams:
    """
    Attributes:
        configuration (str | Unset):
        element_id (str | Unset):
        reference_ids (list[str] | Unset):
    """

    configuration: str | Unset = UNSET
    element_id: str | Unset = UNSET
    reference_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        element_id = self.element_id

        reference_ids: list[str] | Unset = UNSET
        if not isinstance(self.reference_ids, Unset):
            reference_ids = self.reference_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if reference_ids is not UNSET:
            field_dict["referenceIds"] = reference_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configuration = d.pop("configuration", UNSET)

        element_id = d.pop("elementId", UNSET)

        reference_ids = cast(list[str], d.pop("referenceIds", UNSET))

        bt_revert_unchanged_element_params = cls(
            configuration=configuration,
            element_id=element_id,
            reference_ids=reference_ids,
        )

        bt_revert_unchanged_element_params.additional_properties = d
        return bt_revert_unchanged_element_params

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
