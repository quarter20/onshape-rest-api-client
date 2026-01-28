from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_path_element_2297 import BTJPathElement2297


T = TypeVar("T", bound="BTJPath3073")


@_attrs_define
class BTJPath3073:
    """Identifies a value in the json data to be operated upon.

    Attributes:
        start_node (str): Either empty (root) or the nodeId of a node in the tree.
        bt_type (str | Unset): Type of JSON object.
        path (list[BTJPathElement2297] | Unset):
    """

    start_node: str
    bt_type: str | Unset = UNSET
    path: list[BTJPathElement2297] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_node = self.start_node

        bt_type = self.bt_type

        path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startNode": start_node,
            }
        )
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_path_element_2297 import BTJPathElement2297

        d = dict(src_dict)
        start_node = d.pop("startNode")

        bt_type = d.pop("btType", UNSET)

        _path = d.pop("path", UNSET)
        path: list[BTJPathElement2297] | Unset = UNSET
        if _path is not UNSET:
            path = []
            for path_item_data in _path:
                path_item = BTJPathElement2297.from_dict(path_item_data)

                path.append(path_item)

        btj_path_3073 = cls(
            start_node=start_node,
            bt_type=bt_type,
            path=path,
        )

        btj_path_3073.additional_properties = d
        return btj_path_3073

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
