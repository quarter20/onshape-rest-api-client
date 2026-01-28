from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BTVariableStudioScopeInfo")


@_attrs_define
class BTVariableStudioScopeInfo:
    """
    Attributes:
        is_automatically_inserted (bool): Whether variable studio is automatically inserted into part studios and
            assemblies in the workspace
    """

    is_automatically_inserted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_automatically_inserted = self.is_automatically_inserted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAutomaticallyInserted": is_automatically_inserted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_automatically_inserted = d.pop("isAutomaticallyInserted")

        bt_variable_studio_scope_info = cls(
            is_automatically_inserted=is_automatically_inserted,
        )

        bt_variable_studio_scope_info.additional_properties = d
        return bt_variable_studio_scope_info

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
