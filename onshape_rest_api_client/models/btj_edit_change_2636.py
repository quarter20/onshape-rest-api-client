from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_edit_change_2636_value import BTJEditChange2636Value
    from ..models.btj_path_3073 import BTJPath3073


T = TypeVar("T", bound="BTJEditChange2636")


@_attrs_define
class BTJEditChange2636:
    """Change the value of a node.

    Example:
        In the structure { 'stringKey': 'bar', 'arrayKey': [ 1, 2, 3 ], 'objectKey': { 'subKey': false } } to change
            'bar' to 'baz', specify { 'btType': 'BTJEditChange-2636', 'path': { 'btType': 'BTJPath-3073', 'startNode': '',
            'path': [ { 'btType': 'BTJPathKey-3221', 'key': 'stringKey' } ] }, 'value': 'baz' }

    Attributes:
        bt_type (str): Type of JSON object.
        value (BTJEditChange2636Value):
        path (BTJPath3073 | Unset): Identifies a value in the json data to be operated upon.
    """

    bt_type: str
    value: BTJEditChange2636Value
    path: BTJPath3073 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        value = self.value.to_dict()

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
                "value": value,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_edit_change_2636_value import BTJEditChange2636Value
        from ..models.btj_path_3073 import BTJPath3073

        d = dict(src_dict)
        bt_type = d.pop("btType")

        value = BTJEditChange2636Value.from_dict(d.pop("value"))

        _path = d.pop("path", UNSET)
        path: BTJPath3073 | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = BTJPath3073.from_dict(_path)

        btj_edit_change_2636 = cls(
            bt_type=bt_type,
            value=value,
            path=path,
        )

        btj_edit_change_2636.additional_properties = d
        return btj_edit_change_2636

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
