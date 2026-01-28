from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCopyViewAssociativeDataParams")


@_attrs_define
class BTCopyViewAssociativeDataParams:
    """
    Attributes:
        associative_data_ids (list[str] | Unset):
        destination_view_id (str | Unset):
        source_element_id (str | Unset):
        source_view_id (str | Unset):
    """

    associative_data_ids: list[str] | Unset = UNSET
    destination_view_id: str | Unset = UNSET
    source_element_id: str | Unset = UNSET
    source_view_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associative_data_ids: list[str] | Unset = UNSET
        if not isinstance(self.associative_data_ids, Unset):
            associative_data_ids = self.associative_data_ids

        destination_view_id = self.destination_view_id

        source_element_id = self.source_element_id

        source_view_id = self.source_view_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associative_data_ids is not UNSET:
            field_dict["associativeDataIds"] = associative_data_ids
        if destination_view_id is not UNSET:
            field_dict["destinationViewId"] = destination_view_id
        if source_element_id is not UNSET:
            field_dict["sourceElementId"] = source_element_id
        if source_view_id is not UNSET:
            field_dict["sourceViewId"] = source_view_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        associative_data_ids = cast(list[str], d.pop("associativeDataIds", UNSET))

        destination_view_id = d.pop("destinationViewId", UNSET)

        source_element_id = d.pop("sourceElementId", UNSET)

        source_view_id = d.pop("sourceViewId", UNSET)

        bt_copy_view_associative_data_params = cls(
            associative_data_ids=associative_data_ids,
            destination_view_id=destination_view_id,
            source_element_id=source_element_id,
            source_view_id=source_view_id,
        )

        bt_copy_view_associative_data_params.additional_properties = d
        return bt_copy_view_associative_data_params

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
