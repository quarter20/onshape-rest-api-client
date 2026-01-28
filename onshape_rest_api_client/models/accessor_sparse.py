from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor_sparse_extensions import AccessorSparseExtensions
    from ..models.accessor_sparse_extras import AccessorSparseExtras
    from ..models.accessor_sparse_indices import AccessorSparseIndices
    from ..models.accessor_sparse_values import AccessorSparseValues


T = TypeVar("T", bound="AccessorSparse")


@_attrs_define
class AccessorSparse:
    """
    Attributes:
        count (int | Unset):
        extensions (AccessorSparseExtensions | Unset):
        extras (AccessorSparseExtras | Unset):
        indices (AccessorSparseIndices | Unset):
        values (AccessorSparseValues | Unset):
    """

    count: int | Unset = UNSET
    extensions: AccessorSparseExtensions | Unset = UNSET
    extras: AccessorSparseExtras | Unset = UNSET
    indices: AccessorSparseIndices | Unset = UNSET
    values: AccessorSparseValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indices, Unset):
            indices = self.indices.to_dict()

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if indices is not UNSET:
            field_dict["indices"] = indices
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor_sparse_extensions import AccessorSparseExtensions
        from ..models.accessor_sparse_extras import AccessorSparseExtras
        from ..models.accessor_sparse_indices import AccessorSparseIndices
        from ..models.accessor_sparse_values import AccessorSparseValues

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: AccessorSparseExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AccessorSparseExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AccessorSparseExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AccessorSparseExtras.from_dict(_extras)

        _indices = d.pop("indices", UNSET)
        indices: AccessorSparseIndices | Unset
        if isinstance(_indices, Unset):
            indices = UNSET
        else:
            indices = AccessorSparseIndices.from_dict(_indices)

        _values = d.pop("values", UNSET)
        values: AccessorSparseValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AccessorSparseValues.from_dict(_values)

        accessor_sparse = cls(
            count=count,
            extensions=extensions,
            extras=extras,
            indices=indices,
            values=values,
        )

        accessor_sparse.additional_properties = d
        return accessor_sparse

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
