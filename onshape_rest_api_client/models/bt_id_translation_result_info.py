from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTIdTranslationResultInfo")


@_attrs_define
class BTIdTranslationResultInfo:
    """
    Attributes:
        source (str | Unset):
        status (str | Unset):
        target (list[str] | Unset):
    """

    source: str | Unset = UNSET
    status: str | Unset = UNSET
    target: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        status = self.status

        target: list[str] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        status = d.pop("status", UNSET)

        target = cast(list[str], d.pop("target", UNSET))

        bt_id_translation_result_info = cls(
            source=source,
            status=status,
            target=target,
        )

        bt_id_translation_result_info.additional_properties = d
        return bt_id_translation_result_info

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
