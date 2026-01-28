from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bill_of_materials_element_info import BTBillOfMaterialsElementInfo
    from ..models.bt_bill_of_materials_object_with_properties_info import BTBillOfMaterialsObjectWithPropertiesInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo


T = TypeVar("T", bound="BTBillOfMaterialsSourceInfo")


@_attrs_define
class BTBillOfMaterialsSourceInfo:
    """
    Attributes:
        document (BTBillOfMaterialsObjectWithPropertiesInfo | Unset):
        document_microversion (BTBillOfMaterialsObjectWithPropertiesInfo | Unset):
        element (BTBillOfMaterialsElementInfo | Unset):
        href (str | Unset):
        thumbnail_info (BTThumbnailInfo | Unset):
        version (BTBillOfMaterialsObjectWithPropertiesInfo | Unset):
        view_href (str | Unset):
        workspace (BTBillOfMaterialsObjectWithPropertiesInfo | Unset):
    """

    document: BTBillOfMaterialsObjectWithPropertiesInfo | Unset = UNSET
    document_microversion: BTBillOfMaterialsObjectWithPropertiesInfo | Unset = UNSET
    element: BTBillOfMaterialsElementInfo | Unset = UNSET
    href: str | Unset = UNSET
    thumbnail_info: BTThumbnailInfo | Unset = UNSET
    version: BTBillOfMaterialsObjectWithPropertiesInfo | Unset = UNSET
    view_href: str | Unset = UNSET
    workspace: BTBillOfMaterialsObjectWithPropertiesInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        document_microversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_microversion, Unset):
            document_microversion = self.document_microversion.to_dict()

        element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element, Unset):
            element = self.element.to_dict()

        href = self.href

        thumbnail_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_info, Unset):
            thumbnail_info = self.thumbnail_info.to_dict()

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        view_href = self.view_href

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if document_microversion is not UNSET:
            field_dict["documentMicroversion"] = document_microversion
        if element is not UNSET:
            field_dict["element"] = element
        if href is not UNSET:
            field_dict["href"] = href
        if thumbnail_info is not UNSET:
            field_dict["thumbnailInfo"] = thumbnail_info
        if version is not UNSET:
            field_dict["version"] = version
        if view_href is not UNSET:
            field_dict["viewHref"] = view_href
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bill_of_materials_element_info import BTBillOfMaterialsElementInfo
        from ..models.bt_bill_of_materials_object_with_properties_info import BTBillOfMaterialsObjectWithPropertiesInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: BTBillOfMaterialsObjectWithPropertiesInfo | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = BTBillOfMaterialsObjectWithPropertiesInfo.from_dict(_document)

        _document_microversion = d.pop("documentMicroversion", UNSET)
        document_microversion: BTBillOfMaterialsObjectWithPropertiesInfo | Unset
        if isinstance(_document_microversion, Unset):
            document_microversion = UNSET
        else:
            document_microversion = BTBillOfMaterialsObjectWithPropertiesInfo.from_dict(_document_microversion)

        _element = d.pop("element", UNSET)
        element: BTBillOfMaterialsElementInfo | Unset
        if isinstance(_element, Unset):
            element = UNSET
        else:
            element = BTBillOfMaterialsElementInfo.from_dict(_element)

        href = d.pop("href", UNSET)

        _thumbnail_info = d.pop("thumbnailInfo", UNSET)
        thumbnail_info: BTThumbnailInfo | Unset
        if isinstance(_thumbnail_info, Unset):
            thumbnail_info = UNSET
        else:
            thumbnail_info = BTThumbnailInfo.from_dict(_thumbnail_info)

        _version = d.pop("version", UNSET)
        version: BTBillOfMaterialsObjectWithPropertiesInfo | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = BTBillOfMaterialsObjectWithPropertiesInfo.from_dict(_version)

        view_href = d.pop("viewHref", UNSET)

        _workspace = d.pop("workspace", UNSET)
        workspace: BTBillOfMaterialsObjectWithPropertiesInfo | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = BTBillOfMaterialsObjectWithPropertiesInfo.from_dict(_workspace)

        bt_bill_of_materials_source_info = cls(
            document=document,
            document_microversion=document_microversion,
            element=element,
            href=href,
            thumbnail_info=thumbnail_info,
            version=version,
            view_href=view_href,
            workspace=workspace,
        )

        bt_bill_of_materials_source_info.additional_properties = d
        return bt_bill_of_materials_source_info

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
