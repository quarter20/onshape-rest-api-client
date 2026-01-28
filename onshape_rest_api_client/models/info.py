from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import Contact
    from ..models.info_extensions import InfoExtensions
    from ..models.license_ import License


T = TypeVar("T", bound="Info")


@_attrs_define
class Info:
    """
    Attributes:
        contact (Contact | Unset):
        description (str | Unset):
        extensions (InfoExtensions | Unset):
        license_ (License | Unset):
        summary (str | Unset):
        terms_of_service (str | Unset):
        title (str | Unset):
        version (str | Unset):
    """

    contact: Contact | Unset = UNSET
    description: str | Unset = UNSET
    extensions: InfoExtensions | Unset = UNSET
    license_: License | Unset = UNSET
    summary: str | Unset = UNSET
    terms_of_service: str | Unset = UNSET
    title: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        summary = self.summary

        terms_of_service = self.terms_of_service

        title = self.title

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if license_ is not UNSET:
            field_dict["license"] = license_
        if summary is not UNSET:
            field_dict["summary"] = summary
        if terms_of_service is not UNSET:
            field_dict["termsOfService"] = terms_of_service
        if title is not UNSET:
            field_dict["title"] = title
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact import Contact
        from ..models.info_extensions import InfoExtensions
        from ..models.license_ import License

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: Contact | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = Contact.from_dict(_contact)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: InfoExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = InfoExtensions.from_dict(_extensions)

        _license_ = d.pop("license", UNSET)
        license_: License | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = License.from_dict(_license_)

        summary = d.pop("summary", UNSET)

        terms_of_service = d.pop("termsOfService", UNSET)

        title = d.pop("title", UNSET)

        version = d.pop("version", UNSET)

        info = cls(
            contact=contact,
            description=description,
            extensions=extensions,
            license_=license_,
            summary=summary,
            terms_of_service=terms_of_service,
            title=title,
            version=version,
        )

        info.additional_properties = d
        return info

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
