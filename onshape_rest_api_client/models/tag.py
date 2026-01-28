from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_documentation import ExternalDocumentation
    from ..models.tag_extensions import TagExtensions


T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """
    Attributes:
        description (str | Unset):
        extensions (TagExtensions | Unset):
        external_docs (ExternalDocumentation | Unset):
        name (str | Unset):
    """

    description: str | Unset = UNSET
    extensions: TagExtensions | Unset = UNSET
    external_docs: ExternalDocumentation | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        external_docs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_docs, Unset):
            external_docs = self.external_docs.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if external_docs is not UNSET:
            field_dict["externalDocs"] = external_docs
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_documentation import ExternalDocumentation
        from ..models.tag_extensions import TagExtensions

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: TagExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = TagExtensions.from_dict(_extensions)

        _external_docs = d.pop("externalDocs", UNSET)
        external_docs: ExternalDocumentation | Unset
        if isinstance(_external_docs, Unset):
            external_docs = UNSET
        else:
            external_docs = ExternalDocumentation.from_dict(_external_docs)

        name = d.pop("name", UNSET)

        tag = cls(
            description=description,
            extensions=extensions,
            external_docs=external_docs,
            name=name,
        )

        tag.additional_properties = d
        return tag

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
