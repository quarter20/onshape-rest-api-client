from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_edit_insert_2523_value import BTJEditInsert2523Value
    from ..models.btj_path_3073 import BTJPath3073


T = TypeVar("T", bound="BTJEditInsert2523")


@_attrs_define
class BTJEditInsert2523:
    """Inserts a value using the specified path.

    Example:
        In the structure { 'stringKey': 'bar', 'arrayKey': [ 1, 2, 3 ], 'objectKey': { 'subKey': false } } to insert 4
            at the end of 'arrayKey', specify { 'btType': 'BTJEditInsert-2523', 'path': { 'btType': 'BTJPath-3073',
            'startNode': '', 'path': [ { 'btType': 'BTJPathKey-3221', 'key': 'arrayKey' }, { 'btType': 'BTJPathIndex-1871',
            'index': -1 } ] }, 'value': 4 }

    Attributes:
        bt_type (str): Type of JSON object.
        path (BTJPath3073 | Unset): Identifies a value in the json data to be operated upon.
        upsert (bool | Unset):
        value (BTJEditInsert2523Value | Unset):
    """

    bt_type: str
    path: BTJPath3073 | Unset = UNSET
    upsert: bool | Unset = UNSET
    value: BTJEditInsert2523Value | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        upsert = self.upsert

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if upsert is not UNSET:
            field_dict["upsert"] = upsert
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_edit_insert_2523_value import BTJEditInsert2523Value
        from ..models.btj_path_3073 import BTJPath3073

        d = dict(src_dict)
        bt_type = d.pop("btType")

        _path = d.pop("path", UNSET)
        path: BTJPath3073 | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = BTJPath3073.from_dict(_path)

        upsert = d.pop("upsert", UNSET)

        _value = d.pop("value", UNSET)
        value: BTJEditInsert2523Value | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTJEditInsert2523Value.from_dict(_value)

        btj_edit_insert_2523 = cls(
            bt_type=bt_type,
            path=path,
            upsert=upsert,
            value=value,
        )

        btj_edit_insert_2523.additional_properties = d
        return btj_edit_insert_2523

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
