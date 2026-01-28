from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_reference_resolve_info import BTAppElementReferenceResolveInfo


T = TypeVar("T", bound="BTAppElementReferencesResolveInfo")


@_attrs_define
class BTAppElementReferencesResolveInfo:
    """
    Attributes:
        resolved_references (list[BTAppElementReferenceResolveInfo] | Unset):
        unresolved_reference_ids (list[str] | Unset):
    """

    resolved_references: list[BTAppElementReferenceResolveInfo] | Unset = UNSET
    unresolved_reference_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resolved_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resolved_references, Unset):
            resolved_references = []
            for resolved_references_item_data in self.resolved_references:
                resolved_references_item = resolved_references_item_data.to_dict()
                resolved_references.append(resolved_references_item)

        unresolved_reference_ids: list[str] | Unset = UNSET
        if not isinstance(self.unresolved_reference_ids, Unset):
            unresolved_reference_ids = self.unresolved_reference_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolved_references is not UNSET:
            field_dict["resolvedReferences"] = resolved_references
        if unresolved_reference_ids is not UNSET:
            field_dict["unresolvedReferenceIds"] = unresolved_reference_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_reference_resolve_info import BTAppElementReferenceResolveInfo

        d = dict(src_dict)
        _resolved_references = d.pop("resolvedReferences", UNSET)
        resolved_references: list[BTAppElementReferenceResolveInfo] | Unset = UNSET
        if _resolved_references is not UNSET:
            resolved_references = []
            for resolved_references_item_data in _resolved_references:
                resolved_references_item = BTAppElementReferenceResolveInfo.from_dict(resolved_references_item_data)

                resolved_references.append(resolved_references_item)

        unresolved_reference_ids = cast(list[str], d.pop("unresolvedReferenceIds", UNSET))

        bt_app_element_references_resolve_info = cls(
            resolved_references=resolved_references,
            unresolved_reference_ids=unresolved_reference_ids,
        )

        bt_app_element_references_resolve_info.additional_properties = d
        return bt_app_element_references_resolve_info

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
