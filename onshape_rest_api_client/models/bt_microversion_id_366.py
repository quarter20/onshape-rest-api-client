from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMicroversionId366")


@_attrs_define
class BTMicroversionId366:
    """
    Attributes:
        ambiguous (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        deleted (bool | Unset):
        the_id (str | Unset):
    """

    ambiguous: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    the_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ambiguous = self.ambiguous

        bt_type = self.bt_type

        deleted = self.deleted

        the_id = self.the_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ambiguous is not UNSET:
            field_dict["ambiguous"] = ambiguous
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if the_id is not UNSET:
            field_dict["theId"] = the_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ambiguous = d.pop("ambiguous", UNSET)

        bt_type = d.pop("btType", UNSET)

        deleted = d.pop("deleted", UNSET)

        the_id = d.pop("theId", UNSET)

        bt_microversion_id_366 = cls(
            ambiguous=ambiguous,
            bt_type=bt_type,
            deleted=deleted,
            the_id=the_id,
        )

        bt_microversion_id_366.additional_properties = d
        return bt_microversion_id_366

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
