from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_thumbnail_info import BTThumbnailInfo


T = TypeVar("T", bound="BTBillOfMaterialsItemSourceInfo")


@_attrs_define
class BTBillOfMaterialsItemSourceInfo:
    """
    Attributes:
        configuration (str | Unset):
        distinct_configurations (list[str] | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        full_configuration (str | Unset):
        href (str | Unset):
        is_standard_content (bool | Unset):
        non_geometric_item_id (str | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        source_element_microversion_id (str | Unset):
        thumbnail_info (BTThumbnailInfo | Unset):
        version_metadata_workspace_microversion_id (str | Unset):
        view_href (str | Unset):
        wvm_id (str | Unset):
        wvm_type (str | Unset):
    """

    configuration: str | Unset = UNSET
    distinct_configurations: list[str] | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    full_configuration: str | Unset = UNSET
    href: str | Unset = UNSET
    is_standard_content: bool | Unset = UNSET
    non_geometric_item_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    source_element_microversion_id: str | Unset = UNSET
    thumbnail_info: BTThumbnailInfo | Unset = UNSET
    version_metadata_workspace_microversion_id: str | Unset = UNSET
    view_href: str | Unset = UNSET
    wvm_id: str | Unset = UNSET
    wvm_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        distinct_configurations: list[str] | Unset = UNSET
        if not isinstance(self.distinct_configurations, Unset):
            distinct_configurations = self.distinct_configurations

        document_id = self.document_id

        element_id = self.element_id

        full_configuration = self.full_configuration

        href = self.href

        is_standard_content = self.is_standard_content

        non_geometric_item_id = self.non_geometric_item_id

        part_id = self.part_id

        part_identity = self.part_identity

        source_element_microversion_id = self.source_element_microversion_id

        thumbnail_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_info, Unset):
            thumbnail_info = self.thumbnail_info.to_dict()

        version_metadata_workspace_microversion_id = self.version_metadata_workspace_microversion_id

        view_href = self.view_href

        wvm_id = self.wvm_id

        wvm_type = self.wvm_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if distinct_configurations is not UNSET:
            field_dict["distinctConfigurations"] = distinct_configurations
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if full_configuration is not UNSET:
            field_dict["fullConfiguration"] = full_configuration
        if href is not UNSET:
            field_dict["href"] = href
        if is_standard_content is not UNSET:
            field_dict["isStandardContent"] = is_standard_content
        if non_geometric_item_id is not UNSET:
            field_dict["nonGeometricItemId"] = non_geometric_item_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if source_element_microversion_id is not UNSET:
            field_dict["sourceElementMicroversionId"] = source_element_microversion_id
        if thumbnail_info is not UNSET:
            field_dict["thumbnailInfo"] = thumbnail_info
        if version_metadata_workspace_microversion_id is not UNSET:
            field_dict["versionMetadataWorkspaceMicroversionId"] = version_metadata_workspace_microversion_id
        if view_href is not UNSET:
            field_dict["viewHref"] = view_href
        if wvm_id is not UNSET:
            field_dict["wvmId"] = wvm_id
        if wvm_type is not UNSET:
            field_dict["wvmType"] = wvm_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_thumbnail_info import BTThumbnailInfo

        d = dict(src_dict)
        configuration = d.pop("configuration", UNSET)

        distinct_configurations = cast(list[str], d.pop("distinctConfigurations", UNSET))

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        full_configuration = d.pop("fullConfiguration", UNSET)

        href = d.pop("href", UNSET)

        is_standard_content = d.pop("isStandardContent", UNSET)

        non_geometric_item_id = d.pop("nonGeometricItemId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        source_element_microversion_id = d.pop("sourceElementMicroversionId", UNSET)

        _thumbnail_info = d.pop("thumbnailInfo", UNSET)
        thumbnail_info: BTThumbnailInfo | Unset
        if isinstance(_thumbnail_info, Unset):
            thumbnail_info = UNSET
        else:
            thumbnail_info = BTThumbnailInfo.from_dict(_thumbnail_info)

        version_metadata_workspace_microversion_id = d.pop("versionMetadataWorkspaceMicroversionId", UNSET)

        view_href = d.pop("viewHref", UNSET)

        wvm_id = d.pop("wvmId", UNSET)

        wvm_type = d.pop("wvmType", UNSET)

        bt_bill_of_materials_item_source_info = cls(
            configuration=configuration,
            distinct_configurations=distinct_configurations,
            document_id=document_id,
            element_id=element_id,
            full_configuration=full_configuration,
            href=href,
            is_standard_content=is_standard_content,
            non_geometric_item_id=non_geometric_item_id,
            part_id=part_id,
            part_identity=part_identity,
            source_element_microversion_id=source_element_microversion_id,
            thumbnail_info=thumbnail_info,
            version_metadata_workspace_microversion_id=version_metadata_workspace_microversion_id,
            view_href=view_href,
            wvm_id=wvm_id,
            wvm_type=wvm_type,
        )

        bt_bill_of_materials_item_source_info.additional_properties = d
        return bt_bill_of_materials_item_source_info

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
