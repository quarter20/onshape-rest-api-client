from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_value_info import BTMetadataValueInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.config_info import ConfigInfo
    from ..models.property_ import Property


T = TypeVar("T", bound="BTProductStructureItemInfo")


@_attrs_define
class BTProductStructureItemInfo:
    """Array of items in the current page.

    Attributes:
        json_type (str):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        configuration (list[ConfigInfo] | Unset): The configuration parameters of the referring element.
        document_id (str | Unset): The document ID of the referring element.
        document_name (str | Unset): The name of the document containing the referring element.
        document_state (int | Unset):
        element_id (str | Unset): The element ID of the referring element.
        element_type (int | Unset): The element type ordinal of the referring element.
        flattened_body (bool | Unset): Whether the item represents a flattened sheet metal body.
        folder_id (str | Unset): The folder ID containing the document.
        has_drawing (bool | Unset): Whether the item has an associated drawing.
        latest_revision (bool | Unset): Whether this item is the latest revision.
        not_revision_managed (bool | Unset): Whether this item is not revision-managed.
        part_number (str | Unset): The part number of the referring element.
        project_id (str | Unset): The project ID associated with the document.
        properties (list[BTMetadataValueInfo] | Unset): Custom metadata properties of the item. Only populated when
            includeProperties is true.
        resource_type (str | Unset): The resource type of this item.
        revision (str | Unset): The revision of the referring element.
        revision_obsolete (bool | Unset): Whether the revision is obsolete.
        standard_properties (list[Property] | Unset): Standard metadata properties of the item.
        thumbnail (BTThumbnailInfo | Unset):
        thumbnail_href (str | Unset): The thumbnail href URI for the referring element.
        version_id (str | Unset): The version ID of the document containing the referring element.
        version_name (str | Unset): The version name of the document containing the referring element.
        wv_created_at (datetime.datetime | Unset): The timestamp when the version or workspace was created.
    """

    json_type: str
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    configuration: list[ConfigInfo] | Unset = UNSET
    document_id: str | Unset = UNSET
    document_name: str | Unset = UNSET
    document_state: int | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    flattened_body: bool | Unset = UNSET
    folder_id: str | Unset = UNSET
    has_drawing: bool | Unset = UNSET
    latest_revision: bool | Unset = UNSET
    not_revision_managed: bool | Unset = UNSET
    part_number: str | Unset = UNSET
    project_id: str | Unset = UNSET
    properties: list[BTMetadataValueInfo] | Unset = UNSET
    resource_type: str | Unset = UNSET
    revision: str | Unset = UNSET
    revision_obsolete: bool | Unset = UNSET
    standard_properties: list[Property] | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    thumbnail_href: str | Unset = UNSET
    version_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    wv_created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        href = self.href

        id = self.id

        name = self.name

        view_ref = self.view_ref

        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        document_id = self.document_id

        document_name = self.document_name

        document_state = self.document_state

        element_id = self.element_id

        element_type = self.element_type

        flattened_body = self.flattened_body

        folder_id = self.folder_id

        has_drawing = self.has_drawing

        latest_revision = self.latest_revision

        not_revision_managed = self.not_revision_managed

        part_number = self.part_number

        project_id = self.project_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        resource_type = self.resource_type

        revision = self.revision

        revision_obsolete = self.revision_obsolete

        standard_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.standard_properties, Unset):
            standard_properties = []
            for standard_properties_item_data in self.standard_properties:
                standard_properties_item = standard_properties_item_data.to_dict()
                standard_properties.append(standard_properties_item)

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        thumbnail_href = self.thumbnail_href

        version_id = self.version_id

        version_name = self.version_name

        wv_created_at: str | Unset = UNSET
        if not isinstance(self.wv_created_at, Unset):
            wv_created_at = self.wv_created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_state is not UNSET:
            field_dict["documentState"] = document_state
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if flattened_body is not UNSET:
            field_dict["flattenedBody"] = flattened_body
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if has_drawing is not UNSET:
            field_dict["hasDrawing"] = has_drawing
        if latest_revision is not UNSET:
            field_dict["latestRevision"] = latest_revision
        if not_revision_managed is not UNSET:
            field_dict["notRevisionManaged"] = not_revision_managed
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if revision is not UNSET:
            field_dict["revision"] = revision
        if revision_obsolete is not UNSET:
            field_dict["revisionObsolete"] = revision_obsolete
        if standard_properties is not UNSET:
            field_dict["standardProperties"] = standard_properties
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if thumbnail_href is not UNSET:
            field_dict["thumbnailHref"] = thumbnail_href
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if wv_created_at is not UNSET:
            field_dict["wvCreatedAt"] = wv_created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_value_info import BTMetadataValueInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.config_info import ConfigInfo
        from ..models.property_ import Property

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: list[ConfigInfo] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = ConfigInfo.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        document_id = d.pop("documentId", UNSET)

        document_name = d.pop("documentName", UNSET)

        document_state = d.pop("documentState", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        flattened_body = d.pop("flattenedBody", UNSET)

        folder_id = d.pop("folderId", UNSET)

        has_drawing = d.pop("hasDrawing", UNSET)

        latest_revision = d.pop("latestRevision", UNSET)

        not_revision_managed = d.pop("notRevisionManaged", UNSET)

        part_number = d.pop("partNumber", UNSET)

        project_id = d.pop("projectId", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTMetadataValueInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTMetadataValueInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        resource_type = d.pop("resourceType", UNSET)

        revision = d.pop("revision", UNSET)

        revision_obsolete = d.pop("revisionObsolete", UNSET)

        _standard_properties = d.pop("standardProperties", UNSET)
        standard_properties: list[Property] | Unset = UNSET
        if _standard_properties is not UNSET:
            standard_properties = []
            for standard_properties_item_data in _standard_properties:
                standard_properties_item = Property.from_dict(standard_properties_item_data)

                standard_properties.append(standard_properties_item)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        thumbnail_href = d.pop("thumbnailHref", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        _wv_created_at = d.pop("wvCreatedAt", UNSET)
        wv_created_at: datetime.datetime | Unset
        if isinstance(_wv_created_at, Unset):
            wv_created_at = UNSET
        else:
            wv_created_at = datetime.datetime.fromisoformat(_wv_created_at)

        bt_product_structure_item_info = cls(
            json_type=json_type,
            href=href,
            id=id,
            name=name,
            view_ref=view_ref,
            configuration=configuration,
            document_id=document_id,
            document_name=document_name,
            document_state=document_state,
            element_id=element_id,
            element_type=element_type,
            flattened_body=flattened_body,
            folder_id=folder_id,
            has_drawing=has_drawing,
            latest_revision=latest_revision,
            not_revision_managed=not_revision_managed,
            part_number=part_number,
            project_id=project_id,
            properties=properties,
            resource_type=resource_type,
            revision=revision,
            revision_obsolete=revision_obsolete,
            standard_properties=standard_properties,
            thumbnail=thumbnail,
            thumbnail_href=thumbnail_href,
            version_id=version_id,
            version_name=version_name,
            wv_created_at=wv_created_at,
        )

        bt_product_structure_item_info.additional_properties = d
        return bt_product_structure_item_info

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
