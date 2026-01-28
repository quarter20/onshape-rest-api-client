from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_unique_document_item_params import BTUniqueDocumentItemParams


T = TypeVar("T", bound="UpdateParams")


@_attrs_define
class UpdateParams:
    """
    Attributes:
        from_reference (BTUniqueDocumentItemParams | Unset):
        ids_to_update (list[str] | Unset):
        ignore_children (bool | Unset):
        to_reference (BTUniqueDocumentItemParams | Unset):
    """

    from_reference: BTUniqueDocumentItemParams | Unset = UNSET
    ids_to_update: list[str] | Unset = UNSET
    ignore_children: bool | Unset = UNSET
    to_reference: BTUniqueDocumentItemParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_reference, Unset):
            from_reference = self.from_reference.to_dict()

        ids_to_update: list[str] | Unset = UNSET
        if not isinstance(self.ids_to_update, Unset):
            ids_to_update = self.ids_to_update

        ignore_children = self.ignore_children

        to_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_reference, Unset):
            to_reference = self.to_reference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_reference is not UNSET:
            field_dict["fromReference"] = from_reference
        if ids_to_update is not UNSET:
            field_dict["idsToUpdate"] = ids_to_update
        if ignore_children is not UNSET:
            field_dict["ignoreChildren"] = ignore_children
        if to_reference is not UNSET:
            field_dict["toReference"] = to_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_unique_document_item_params import BTUniqueDocumentItemParams

        d = dict(src_dict)
        _from_reference = d.pop("fromReference", UNSET)
        from_reference: BTUniqueDocumentItemParams | Unset
        if isinstance(_from_reference, Unset):
            from_reference = UNSET
        else:
            from_reference = BTUniqueDocumentItemParams.from_dict(_from_reference)

        ids_to_update = cast(list[str], d.pop("idsToUpdate", UNSET))

        ignore_children = d.pop("ignoreChildren", UNSET)

        _to_reference = d.pop("toReference", UNSET)
        to_reference: BTUniqueDocumentItemParams | Unset
        if isinstance(_to_reference, Unset):
            to_reference = UNSET
        else:
            to_reference = BTUniqueDocumentItemParams.from_dict(_to_reference)

        update_params = cls(
            from_reference=from_reference,
            ids_to_update=ids_to_update,
            ignore_children=ignore_children,
            to_reference=to_reference,
        )

        update_params.additional_properties = d
        return update_params

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
