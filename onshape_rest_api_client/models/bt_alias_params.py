from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_alias_entry_params import BTAliasEntryParams


T = TypeVar("T", bound="BTAliasParams")


@_attrs_define
class BTAliasParams:
    """
    Attributes:
        additions (list[BTAliasEntryParams] | Unset):
        description (str | Unset):
        entries (list[BTAliasEntryParams] | Unset):
        name (str | Unset):
        removals (list[BTAliasEntryParams] | Unset):
    """

    additions: list[BTAliasEntryParams] | Unset = UNSET
    description: str | Unset = UNSET
    entries: list[BTAliasEntryParams] | Unset = UNSET
    name: str | Unset = UNSET
    removals: list[BTAliasEntryParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additions, Unset):
            additions = []
            for additions_item_data in self.additions:
                additions_item = additions_item_data.to_dict()
                additions.append(additions_item)

        description = self.description

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        name = self.name

        removals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.removals, Unset):
            removals = []
            for removals_item_data in self.removals:
                removals_item = removals_item_data.to_dict()
                removals.append(removals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if name is not UNSET:
            field_dict["name"] = name
        if removals is not UNSET:
            field_dict["removals"] = removals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_alias_entry_params import BTAliasEntryParams

        d = dict(src_dict)
        _additions = d.pop("additions", UNSET)
        additions: list[BTAliasEntryParams] | Unset = UNSET
        if _additions is not UNSET:
            additions = []
            for additions_item_data in _additions:
                additions_item = BTAliasEntryParams.from_dict(additions_item_data)

                additions.append(additions_item)

        description = d.pop("description", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BTAliasEntryParams] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTAliasEntryParams.from_dict(entries_item_data)

                entries.append(entries_item)

        name = d.pop("name", UNSET)

        _removals = d.pop("removals", UNSET)
        removals: list[BTAliasEntryParams] | Unset = UNSET
        if _removals is not UNSET:
            removals = []
            for removals_item_data in _removals:
                removals_item = BTAliasEntryParams.from_dict(removals_item_data)

                removals.append(removals_item)

        bt_alias_params = cls(
            additions=additions,
            description=description,
            entries=entries,
            name=name,
            removals=removals,
        )

        bt_alias_params.additional_properties = d
        return bt_alias_params

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
