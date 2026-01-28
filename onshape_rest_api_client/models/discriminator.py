from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discriminator_extensions import DiscriminatorExtensions
    from ..models.discriminator_mapping import DiscriminatorMapping


T = TypeVar("T", bound="Discriminator")


@_attrs_define
class Discriminator:
    """
    Attributes:
        extensions (DiscriminatorExtensions | Unset):
        mapping (DiscriminatorMapping | Unset):
        property_name (str | Unset):
    """

    extensions: DiscriminatorExtensions | Unset = UNSET
    mapping: DiscriminatorMapping | Unset = UNSET
    property_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = self.mapping.to_dict()

        property_name = self.property_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if property_name is not UNSET:
            field_dict["propertyName"] = property_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discriminator_extensions import DiscriminatorExtensions
        from ..models.discriminator_mapping import DiscriminatorMapping

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: DiscriminatorExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = DiscriminatorExtensions.from_dict(_extensions)

        _mapping = d.pop("mapping", UNSET)
        mapping: DiscriminatorMapping | Unset
        if isinstance(_mapping, Unset):
            mapping = UNSET
        else:
            mapping = DiscriminatorMapping.from_dict(_mapping)

        property_name = d.pop("propertyName", UNSET)

        discriminator = cls(
            extensions=extensions,
            mapping=mapping,
            property_name=property_name,
        )

        discriminator.additional_properties = d
        return discriminator

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
