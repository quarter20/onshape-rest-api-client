from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor_extensions import AccessorExtensions
    from ..models.accessor_extras import AccessorExtras
    from ..models.accessor_sparse import AccessorSparse


T = TypeVar("T", bound="Accessor")


@_attrs_define
class Accessor:
    """
    Attributes:
        buffer_view (int | Unset):
        byte_offset (int | Unset):
        component_type (int | Unset):
        count (int | Unset):
        extensions (AccessorExtensions | Unset):
        extras (AccessorExtras | Unset):
        max_ (list[float] | Unset):
        min_ (list[float] | Unset):
        name (str | Unset):
        normalized (bool | Unset):
        sparse (AccessorSparse | Unset):
        type_ (str | Unset):
    """

    buffer_view: int | Unset = UNSET
    byte_offset: int | Unset = UNSET
    component_type: int | Unset = UNSET
    count: int | Unset = UNSET
    extensions: AccessorExtensions | Unset = UNSET
    extras: AccessorExtras | Unset = UNSET
    max_: list[float] | Unset = UNSET
    min_: list[float] | Unset = UNSET
    name: str | Unset = UNSET
    normalized: bool | Unset = UNSET
    sparse: AccessorSparse | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer_view = self.buffer_view

        byte_offset = self.byte_offset

        component_type = self.component_type

        count = self.count

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        max_: list[float] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_

        min_: list[float] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_

        name = self.name

        normalized = self.normalized

        sparse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sparse, Unset):
            sparse = self.sparse.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer_view is not UNSET:
            field_dict["bufferView"] = buffer_view
        if byte_offset is not UNSET:
            field_dict["byteOffset"] = byte_offset
        if component_type is not UNSET:
            field_dict["componentType"] = component_type
        if count is not UNSET:
            field_dict["count"] = count
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name
        if normalized is not UNSET:
            field_dict["normalized"] = normalized
        if sparse is not UNSET:
            field_dict["sparse"] = sparse
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor_extensions import AccessorExtensions
        from ..models.accessor_extras import AccessorExtras
        from ..models.accessor_sparse import AccessorSparse

        d = dict(src_dict)
        buffer_view = d.pop("bufferView", UNSET)

        byte_offset = d.pop("byteOffset", UNSET)

        component_type = d.pop("componentType", UNSET)

        count = d.pop("count", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: AccessorExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AccessorExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AccessorExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AccessorExtras.from_dict(_extras)

        max_ = cast(list[float], d.pop("max", UNSET))

        min_ = cast(list[float], d.pop("min", UNSET))

        name = d.pop("name", UNSET)

        normalized = d.pop("normalized", UNSET)

        _sparse = d.pop("sparse", UNSET)
        sparse: AccessorSparse | Unset
        if isinstance(_sparse, Unset):
            sparse = UNSET
        else:
            sparse = AccessorSparse.from_dict(_sparse)

        type_ = d.pop("type", UNSET)

        accessor = cls(
            buffer_view=buffer_view,
            byte_offset=byte_offset,
            component_type=component_type,
            count=count,
            extensions=extensions,
            extras=extras,
            max_=max_,
            min_=min_,
            name=name,
            normalized=normalized,
            sparse=sparse,
            type_=type_,
        )

        accessor.additional_properties = d
        return accessor

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
