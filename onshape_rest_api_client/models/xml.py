from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.xml_extensions import XMLExtensions


T = TypeVar("T", bound="XML")


@_attrs_define
class XML:
    """
    Attributes:
        attribute (bool | Unset):
        extensions (XMLExtensions | Unset):
        name (str | Unset):
        namespace (str | Unset):
        prefix (str | Unset):
        wrapped (bool | Unset):
    """

    attribute: bool | Unset = UNSET
    extensions: XMLExtensions | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    prefix: str | Unset = UNSET
    wrapped: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute = self.attribute

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        name = self.name

        namespace = self.namespace

        prefix = self.prefix

        wrapped = self.wrapped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if wrapped is not UNSET:
            field_dict["wrapped"] = wrapped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.xml_extensions import XMLExtensions

        d = dict(src_dict)
        attribute = d.pop("attribute", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: XMLExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = XMLExtensions.from_dict(_extensions)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        prefix = d.pop("prefix", UNSET)

        wrapped = d.pop("wrapped", UNSET)

        xml = cls(
            attribute=attribute,
            extensions=extensions,
            name=name,
            namespace=namespace,
            prefix=prefix,
            wrapped=wrapped,
        )

        xml.additional_properties = d
        return xml

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
