from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_path_3073 import BTJPath3073


T = TypeVar("T", bound="BTJEditDelete1992")


@_attrs_define
class BTJEditDelete1992:
    """Deletes the specified node.

    Example:
        In the structure { 'stringKey': 'bar', 'arrayKey': [ 1, 2, 3 ], 'objectKey': { 'subKey': false } } to delete the
            'stringKey' node, specify { 'btType' : 'BTJEditDelete-1992', 'path': { 'btType': 'BTJPath-3073', 'startNode':
            '', 'path': [ { 'btType': 'BTJPathKey-3221', 'key': 'stringKey' } ] } }

    Attributes:
        bt_type (str): Type of JSON object.
        path (BTJPath3073 | Unset): Identifies a value in the json data to be operated upon.
    """

    bt_type: str
    path: BTJPath3073 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_path_3073 import BTJPath3073

        d = dict(src_dict)
        bt_type = d.pop("btType")

        _path = d.pop("path", UNSET)
        path: BTJPath3073 | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = BTJPath3073.from_dict(_path)

        btj_edit_delete_1992 = cls(
            bt_type=bt_type,
            path=path,
        )

        btj_edit_delete_1992.additional_properties = d
        return btj_edit_delete_1992

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
