from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_body_content import RequestBodyContent
    from ..models.request_body_extensions import RequestBodyExtensions


T = TypeVar("T", bound="RequestBody")


@_attrs_define
class RequestBody:
    """
    Attributes:
        content (RequestBodyContent | Unset):
        description (str | Unset):
        extensions (RequestBodyExtensions | Unset):
        getref (str | Unset):
        required (bool | Unset):
    """

    content: RequestBodyContent | Unset = UNSET
    description: str | Unset = UNSET
    extensions: RequestBodyExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        getref = self.getref

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_body_content import RequestBodyContent
        from ..models.request_body_extensions import RequestBodyExtensions

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: RequestBodyContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = RequestBodyContent.from_dict(_content)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: RequestBodyExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = RequestBodyExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        required = d.pop("required", UNSET)

        request_body = cls(
            content=content,
            description=description,
            extensions=extensions,
            getref=getref,
            required=required,
        )

        request_body.additional_properties = d
        return request_body

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
