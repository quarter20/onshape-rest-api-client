from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_params import UpdateParams


T = TypeVar("T", bound="BTUpdateReferenceParams")


@_attrs_define
class BTUpdateReferenceParams:
    """
    Attributes:
        connection_id (str | Unset):
        edit_description (str | Unset):
        reference_updates (list[UpdateParams] | Unset):
    """

    connection_id: str | Unset = UNSET
    edit_description: str | Unset = UNSET
    reference_updates: list[UpdateParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        edit_description = self.edit_description

        reference_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_updates, Unset):
            reference_updates = []
            for reference_updates_item_data in self.reference_updates:
                reference_updates_item = reference_updates_item_data.to_dict()
                reference_updates.append(reference_updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if edit_description is not UNSET:
            field_dict["editDescription"] = edit_description
        if reference_updates is not UNSET:
            field_dict["referenceUpdates"] = reference_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_params import UpdateParams

        d = dict(src_dict)
        connection_id = d.pop("connectionId", UNSET)

        edit_description = d.pop("editDescription", UNSET)

        _reference_updates = d.pop("referenceUpdates", UNSET)
        reference_updates: list[UpdateParams] | Unset = UNSET
        if _reference_updates is not UNSET:
            reference_updates = []
            for reference_updates_item_data in _reference_updates:
                reference_updates_item = UpdateParams.from_dict(reference_updates_item_data)

                reference_updates.append(reference_updates_item)

        bt_update_reference_params = cls(
            connection_id=connection_id,
            edit_description=edit_description,
            reference_updates=reference_updates,
        )

        bt_update_reference_params.additional_properties = d
        return bt_update_reference_params

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
