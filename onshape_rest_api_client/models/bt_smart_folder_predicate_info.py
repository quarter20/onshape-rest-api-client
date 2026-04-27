from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_smart_folder_predicate_info_value import BTSmartFolderPredicateInfoValue


T = TypeVar("T", bound="BTSmartFolderPredicateInfo")


@_attrs_define
class BTSmartFolderPredicateInfo:
    """
    Attributes:
        field (str | Unset):
        operation (int | Unset):
        value (BTSmartFolderPredicateInfoValue | Unset):
    """

    field: str | Unset = UNSET
    operation: int | Unset = UNSET
    value: BTSmartFolderPredicateInfoValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operation = self.operation

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operation is not UNSET:
            field_dict["operation"] = operation
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_smart_folder_predicate_info_value import BTSmartFolderPredicateInfoValue

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        operation = d.pop("operation", UNSET)

        _value = d.pop("value", UNSET)
        value: BTSmartFolderPredicateInfoValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTSmartFolderPredicateInfoValue.from_dict(_value)

        bt_smart_folder_predicate_info = cls(
            field=field,
            operation=operation,
            value=value,
        )

        bt_smart_folder_predicate_info.additional_properties = d
        return bt_smart_folder_predicate_info

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
