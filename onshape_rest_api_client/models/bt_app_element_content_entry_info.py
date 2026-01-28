from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_content_delta_info import BTAppElementContentDeltaInfo


T = TypeVar("T", bound="BTAppElementContentEntryInfo")


@_attrs_define
class BTAppElementContentEntryInfo:
    """
    Attributes:
        base_content (str | Unset):
        deltas (list[BTAppElementContentDeltaInfo] | Unset):
        subelement_id (str | Unset):
    """

    base_content: str | Unset = UNSET
    deltas: list[BTAppElementContentDeltaInfo] | Unset = UNSET
    subelement_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_content = self.base_content

        deltas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deltas, Unset):
            deltas = []
            for deltas_item_data in self.deltas:
                deltas_item = deltas_item_data.to_dict()
                deltas.append(deltas_item)

        subelement_id = self.subelement_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_content is not UNSET:
            field_dict["baseContent"] = base_content
        if deltas is not UNSET:
            field_dict["deltas"] = deltas
        if subelement_id is not UNSET:
            field_dict["subelementId"] = subelement_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_content_delta_info import BTAppElementContentDeltaInfo

        d = dict(src_dict)
        base_content = d.pop("baseContent", UNSET)

        _deltas = d.pop("deltas", UNSET)
        deltas: list[BTAppElementContentDeltaInfo] | Unset = UNSET
        if _deltas is not UNSET:
            deltas = []
            for deltas_item_data in _deltas:
                deltas_item = BTAppElementContentDeltaInfo.from_dict(deltas_item_data)

                deltas.append(deltas_item)

        subelement_id = d.pop("subelementId", UNSET)

        bt_app_element_content_entry_info = cls(
            base_content=base_content,
            deltas=deltas,
            subelement_id=subelement_id,
        )

        bt_app_element_content_entry_info.additional_properties = d
        return bt_app_element_content_entry_info

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
