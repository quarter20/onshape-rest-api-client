from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_path_3073 import BTJPath3073


T = TypeVar("T", bound="BTJEditMove3245")


@_attrs_define
class BTJEditMove3245:
    """Move an existing node from one path to another.

    Example:
        In the structure { 'stringKey': 'bar', 'arrayKey': [ 1, 2, 3 ], 'objectKey': { 'subKey': false } } to move the
            third value out of 'arrayKey' and into its own node, specify { 'btType': 'BTJEditMove-3245', 'sourcePath': {
            'btType': 'BTJPath-3073', 'startNode': '', 'path': [ { 'btType': 'BTJPathKey-3221', 'key': 'arrayKey' }, {
            'btType': 'BTJPathIndex-1871', 'index': 2 } ] }, 'destinationPath': { 'btType': 'BTJPath-3073', 'startNode': '',
            'path': [ { 'btType': 'BTJPathKey-3221', 'key': 'newKey' } ] } }

    Attributes:
        bt_type (str): Type of JSON object.
        destination_path (BTJPath3073 | Unset): Identifies a value in the json data to be operated upon.
        source_path (BTJPath3073 | Unset): Identifies a value in the json data to be operated upon.
    """

    bt_type: str
    destination_path: BTJPath3073 | Unset = UNSET
    source_path: BTJPath3073 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        destination_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination_path, Unset):
            destination_path = self.destination_path.to_dict()

        source_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_path, Unset):
            source_path = self.source_path.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if destination_path is not UNSET:
            field_dict["destinationPath"] = destination_path
        if source_path is not UNSET:
            field_dict["sourcePath"] = source_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_path_3073 import BTJPath3073

        d = dict(src_dict)
        bt_type = d.pop("btType")

        _destination_path = d.pop("destinationPath", UNSET)
        destination_path: BTJPath3073 | Unset
        if isinstance(_destination_path, Unset):
            destination_path = UNSET
        else:
            destination_path = BTJPath3073.from_dict(_destination_path)

        _source_path = d.pop("sourcePath", UNSET)
        source_path: BTJPath3073 | Unset
        if isinstance(_source_path, Unset):
            source_path = UNSET
        else:
            source_path = BTJPath3073.from_dict(_source_path)

        btj_edit_move_3245 = cls(
            bt_type=bt_type,
            destination_path=destination_path,
            source_path=source_path,
        )

        btj_edit_move_3245.additional_properties = d
        return btj_edit_move_3245

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
