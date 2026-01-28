from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_variable_studio_reference_info import BTVariableStudioReferenceInfo


T = TypeVar("T", bound="BTVariableStudioReferenceListInfo")


@_attrs_define
class BTVariableStudioReferenceListInfo:
    """
    Attributes:
        references (list[BTVariableStudioReferenceInfo] | Unset): List of variable studio references
    """

    references: list[BTVariableStudioReferenceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_variable_studio_reference_info import BTVariableStudioReferenceInfo

        d = dict(src_dict)
        _references = d.pop("references", UNSET)
        references: list[BTVariableStudioReferenceInfo] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = BTVariableStudioReferenceInfo.from_dict(references_item_data)

                references.append(references_item)

        bt_variable_studio_reference_list_info = cls(
            references=references,
        )

        bt_variable_studio_reference_list_info.additional_properties = d
        return bt_variable_studio_reference_list_info

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
