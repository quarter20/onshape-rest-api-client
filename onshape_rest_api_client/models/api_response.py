from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response_content import ApiResponseContent
    from ..models.api_response_extensions import ApiResponseExtensions
    from ..models.api_response_headers import ApiResponseHeaders
    from ..models.api_response_links import ApiResponseLinks


T = TypeVar("T", bound="ApiResponse")


@_attrs_define
class ApiResponse:
    """
    Attributes:
        content (ApiResponseContent | Unset):
        description (str | Unset):
        extensions (ApiResponseExtensions | Unset):
        getref (str | Unset):
        headers (ApiResponseHeaders | Unset):
        links (ApiResponseLinks | Unset):
    """

    content: ApiResponseContent | Unset = UNSET
    description: str | Unset = UNSET
    extensions: ApiResponseExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    headers: ApiResponseHeaders | Unset = UNSET
    links: ApiResponseLinks | Unset = UNSET
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

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

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
        if headers is not UNSET:
            field_dict["headers"] = headers
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response_content import ApiResponseContent
        from ..models.api_response_extensions import ApiResponseExtensions
        from ..models.api_response_headers import ApiResponseHeaders
        from ..models.api_response_links import ApiResponseLinks

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: ApiResponseContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ApiResponseContent.from_dict(_content)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: ApiResponseExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ApiResponseExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ApiResponseHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ApiResponseHeaders.from_dict(_headers)

        _links = d.pop("links", UNSET)
        links: ApiResponseLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ApiResponseLinks.from_dict(_links)

        api_response = cls(
            content=content,
            description=description,
            extensions=extensions,
            getref=getref,
            headers=headers,
            links=links,
        )

        api_response.additional_properties = d
        return api_response

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
