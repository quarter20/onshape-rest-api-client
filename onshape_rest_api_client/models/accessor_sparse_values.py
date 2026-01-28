from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor_sparse_values_extensions import AccessorSparseValuesExtensions
    from ..models.accessor_sparse_values_extras import AccessorSparseValuesExtras


T = TypeVar("T", bound="AccessorSparseValues")


@_attrs_define
class AccessorSparseValues:
    """
    Attributes:
        buffer_view (int | Unset):
        byte_offset (int | Unset):
        extensions (AccessorSparseValuesExtensions | Unset):
        extras (AccessorSparseValuesExtras | Unset):
    """

    buffer_view: int | Unset = UNSET
    byte_offset: int | Unset = UNSET
    extensions: AccessorSparseValuesExtensions | Unset = UNSET
    extras: AccessorSparseValuesExtras | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer_view = self.buffer_view

        byte_offset = self.byte_offset

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer_view is not UNSET:
            field_dict["bufferView"] = buffer_view
        if byte_offset is not UNSET:
            field_dict["byteOffset"] = byte_offset
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor_sparse_values_extensions import AccessorSparseValuesExtensions
        from ..models.accessor_sparse_values_extras import AccessorSparseValuesExtras

        d = dict(src_dict)
        buffer_view = d.pop("bufferView", UNSET)

        byte_offset = d.pop("byteOffset", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: AccessorSparseValuesExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AccessorSparseValuesExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AccessorSparseValuesExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AccessorSparseValuesExtras.from_dict(_extras)

        accessor_sparse_values = cls(
            buffer_view=buffer_view,
            byte_offset=byte_offset,
            extensions=extensions,
            extras=extras,
        )

        accessor_sparse_values.additional_properties = d
        return accessor_sparse_values

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
