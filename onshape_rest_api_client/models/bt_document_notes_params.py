from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTDocumentNotesParams")


@_attrs_define
class BTDocumentNotesParams:
    """Parameters for updating document notes.

    Attributes:
        notes (str | Unset): Document notes.
        old_client_notes (str | Unset): Historical document notes.
    """

    notes: str | Unset = UNSET
    old_client_notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notes = self.notes

        old_client_notes = self.old_client_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes
        if old_client_notes is not UNSET:
            field_dict["oldClientNotes"] = old_client_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notes = d.pop("notes", UNSET)

        old_client_notes = d.pop("oldClientNotes", UNSET)

        bt_document_notes_params = cls(
            notes=notes,
            old_client_notes=old_client_notes,
        )

        bt_document_notes_params.additional_properties = d
        return bt_document_notes_params

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
