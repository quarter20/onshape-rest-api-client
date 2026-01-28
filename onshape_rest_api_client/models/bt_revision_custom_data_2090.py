from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTRevisionCustomData2090")


@_attrs_define
class BTRevisionCustomData2090:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        part_number (str | Unset):
        revision (str | Unset):
        valid_revision_reference (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        part_number = self.part_number

        revision = self.revision

        valid_revision_reference = self.valid_revision_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        bt_revision_custom_data_2090 = cls(
            bt_type=bt_type,
            part_number=part_number,
            revision=revision,
            valid_revision_reference=valid_revision_reference,
        )

        bt_revision_custom_data_2090.additional_properties = d
        return bt_revision_custom_data_2090

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
