from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTOccurrence74")


@_attrs_define
class BTOccurrence74:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        full_path_as_string (str | Unset):
        head_instance_id (str | Unset):
        internal_occurrence (bool | Unset):
        path (list[str] | Unset):
        root_occurrence (bool | Unset):
        tail_instance_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    full_path_as_string: str | Unset = UNSET
    head_instance_id: str | Unset = UNSET
    internal_occurrence: bool | Unset = UNSET
    path: list[str] | Unset = UNSET
    root_occurrence: bool | Unset = UNSET
    tail_instance_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        full_path_as_string = self.full_path_as_string

        head_instance_id = self.head_instance_id

        internal_occurrence = self.internal_occurrence

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        root_occurrence = self.root_occurrence

        tail_instance_id = self.tail_instance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if full_path_as_string is not UNSET:
            field_dict["fullPathAsString"] = full_path_as_string
        if head_instance_id is not UNSET:
            field_dict["headInstanceId"] = head_instance_id
        if internal_occurrence is not UNSET:
            field_dict["internalOccurrence"] = internal_occurrence
        if path is not UNSET:
            field_dict["path"] = path
        if root_occurrence is not UNSET:
            field_dict["rootOccurrence"] = root_occurrence
        if tail_instance_id is not UNSET:
            field_dict["tailInstanceId"] = tail_instance_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        full_path_as_string = d.pop("fullPathAsString", UNSET)

        head_instance_id = d.pop("headInstanceId", UNSET)

        internal_occurrence = d.pop("internalOccurrence", UNSET)

        path = cast(list[str], d.pop("path", UNSET))

        root_occurrence = d.pop("rootOccurrence", UNSET)

        tail_instance_id = d.pop("tailInstanceId", UNSET)

        bt_occurrence_74 = cls(
            bt_type=bt_type,
            full_path_as_string=full_path_as_string,
            head_instance_id=head_instance_id,
            internal_occurrence=internal_occurrence,
            path=path,
            root_occurrence=root_occurrence,
            tail_instance_id=tail_instance_id,
        )

        bt_occurrence_74.additional_properties = d
        return bt_occurrence_74

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
