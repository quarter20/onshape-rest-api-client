from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_metadata_state_type import BTMetadataStateType
from ..models.gbt_mesh_state import GBTMeshState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_part_appearance_info import BTPartAppearanceInfo
    from ..models.bt_part_material_info import BTPartMaterialInfo
    from ..models.bt_part_metadata_info_custom_properties import BTPartMetadataInfoCustomProperties
    from ..models.bt_part_metadata_info_property_source_types import BTPartMetadataInfoPropertySourceTypes
    from ..models.bt_thumbnail_info import BTThumbnailInfo


T = TypeVar("T", bound="BTPartMetadataInfo")


@_attrs_define
class BTPartMetadataInfo:
    """
    Attributes:
        appearance (BTPartAppearanceInfo | Unset):
        body_type (str | Unset):
        configuration_id (str | Unset):
        custom_properties (BTPartMetadataInfoCustomProperties | Unset):
        default_color_hash (str | Unset):
        description (str | Unset):
        element_id (str | Unset):
        href (str | Unset):
        id (str | Unset):
        is_flattened_body (bool | Unset):
        is_hidden (bool | Unset):
        is_mesh (bool | Unset):
        material (BTPartMaterialInfo | Unset):
        mesh_state (GBTMeshState | Unset):
        metadata_microversion (str | Unset):
        microversion_id (str | Unset):
        name (str | Unset):
        ordinal (int | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        part_number (str | Unset):
        part_query (str | Unset):
        product_line (str | Unset):
        project (str | Unset):
        property_source_types (BTPartMetadataInfoPropertySourceTypes | Unset): `0: AUTOMATIC` Set automatically, like a
            part name |
            `1: MERGED` Merged from another Part Studio | `2: FEATURE` Custom feature | `3: UNCONFIGURED` | `4: CONFIGURED`
            |
            `5: STANDARD_CONTENT` | `6: DEFAULT` Applied from metadata property configuration | `7: COMPUTED` Non-
            overridden, non-configured, computed property |
            `8: COMPUTED_CONFIGURED` Property is computed in this configuration; may also be configured in other
            configurations
            `9: IMPORT` Imported properties are handled separately
        referencing_configured_part_node_ids (list[str] | Unset):
        revision (str | Unset):
        state (BTMetadataStateType | Unset): The current state metadata values if applicable.
        thumbnail_configuration_id (str | Unset):
        thumbnail_info (BTThumbnailInfo | Unset):
        title1 (str | Unset):
        title2 (str | Unset):
        title3 (str | Unset):
        unflattened_part_id (str | Unset):
        vendor (str | Unset):
    """

    appearance: BTPartAppearanceInfo | Unset = UNSET
    body_type: str | Unset = UNSET
    configuration_id: str | Unset = UNSET
    custom_properties: BTPartMetadataInfoCustomProperties | Unset = UNSET
    default_color_hash: str | Unset = UNSET
    description: str | Unset = UNSET
    element_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_flattened_body: bool | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_mesh: bool | Unset = UNSET
    material: BTPartMaterialInfo | Unset = UNSET
    mesh_state: GBTMeshState | Unset = UNSET
    metadata_microversion: str | Unset = UNSET
    microversion_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ordinal: int | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_number: str | Unset = UNSET
    part_query: str | Unset = UNSET
    product_line: str | Unset = UNSET
    project: str | Unset = UNSET
    property_source_types: BTPartMetadataInfoPropertySourceTypes | Unset = UNSET
    referencing_configured_part_node_ids: list[str] | Unset = UNSET
    revision: str | Unset = UNSET
    state: BTMetadataStateType | Unset = UNSET
    thumbnail_configuration_id: str | Unset = UNSET
    thumbnail_info: BTThumbnailInfo | Unset = UNSET
    title1: str | Unset = UNSET
    title2: str | Unset = UNSET
    title3: str | Unset = UNSET
    unflattened_part_id: str | Unset = UNSET
    vendor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        body_type = self.body_type

        configuration_id = self.configuration_id

        custom_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = self.custom_properties.to_dict()

        default_color_hash = self.default_color_hash

        description = self.description

        element_id = self.element_id

        href = self.href

        id = self.id

        is_flattened_body = self.is_flattened_body

        is_hidden = self.is_hidden

        is_mesh = self.is_mesh

        material: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material, Unset):
            material = self.material.to_dict()

        mesh_state: str | Unset = UNSET
        if not isinstance(self.mesh_state, Unset):
            mesh_state = self.mesh_state.value

        metadata_microversion = self.metadata_microversion

        microversion_id = self.microversion_id

        name = self.name

        ordinal = self.ordinal

        part_id = self.part_id

        part_identity = self.part_identity

        part_number = self.part_number

        part_query = self.part_query

        product_line = self.product_line

        project = self.project

        property_source_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_source_types, Unset):
            property_source_types = self.property_source_types.to_dict()

        referencing_configured_part_node_ids: list[str] | Unset = UNSET
        if not isinstance(self.referencing_configured_part_node_ids, Unset):
            referencing_configured_part_node_ids = self.referencing_configured_part_node_ids

        revision = self.revision

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        thumbnail_configuration_id = self.thumbnail_configuration_id

        thumbnail_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_info, Unset):
            thumbnail_info = self.thumbnail_info.to_dict()

        title1 = self.title1

        title2 = self.title2

        title3 = self.title3

        unflattened_part_id = self.unflattened_part_id

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if configuration_id is not UNSET:
            field_dict["configurationId"] = configuration_id
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if default_color_hash is not UNSET:
            field_dict["defaultColorHash"] = default_color_hash
        if description is not UNSET:
            field_dict["description"] = description
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_flattened_body is not UNSET:
            field_dict["isFlattenedBody"] = is_flattened_body
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_mesh is not UNSET:
            field_dict["isMesh"] = is_mesh
        if material is not UNSET:
            field_dict["material"] = material
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if metadata_microversion is not UNSET:
            field_dict["metadataMicroversion"] = metadata_microversion
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if name is not UNSET:
            field_dict["name"] = name
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if part_query is not UNSET:
            field_dict["partQuery"] = part_query
        if product_line is not UNSET:
            field_dict["productLine"] = product_line
        if project is not UNSET:
            field_dict["project"] = project
        if property_source_types is not UNSET:
            field_dict["propertySourceTypes"] = property_source_types
        if referencing_configured_part_node_ids is not UNSET:
            field_dict["referencingConfiguredPartNodeIds"] = referencing_configured_part_node_ids
        if revision is not UNSET:
            field_dict["revision"] = revision
        if state is not UNSET:
            field_dict["state"] = state
        if thumbnail_configuration_id is not UNSET:
            field_dict["thumbnailConfigurationId"] = thumbnail_configuration_id
        if thumbnail_info is not UNSET:
            field_dict["thumbnailInfo"] = thumbnail_info
        if title1 is not UNSET:
            field_dict["title1"] = title1
        if title2 is not UNSET:
            field_dict["title2"] = title2
        if title3 is not UNSET:
            field_dict["title3"] = title3
        if unflattened_part_id is not UNSET:
            field_dict["unflattenedPartId"] = unflattened_part_id
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_part_appearance_info import BTPartAppearanceInfo
        from ..models.bt_part_material_info import BTPartMaterialInfo
        from ..models.bt_part_metadata_info_custom_properties import BTPartMetadataInfoCustomProperties
        from ..models.bt_part_metadata_info_property_source_types import BTPartMetadataInfoPropertySourceTypes
        from ..models.bt_thumbnail_info import BTThumbnailInfo

        d = dict(src_dict)
        _appearance = d.pop("appearance", UNSET)
        appearance: BTPartAppearanceInfo | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTPartAppearanceInfo.from_dict(_appearance)

        body_type = d.pop("bodyType", UNSET)

        configuration_id = d.pop("configurationId", UNSET)

        _custom_properties = d.pop("customProperties", UNSET)
        custom_properties: BTPartMetadataInfoCustomProperties | Unset
        if isinstance(_custom_properties, Unset):
            custom_properties = UNSET
        else:
            custom_properties = BTPartMetadataInfoCustomProperties.from_dict(_custom_properties)

        default_color_hash = d.pop("defaultColorHash", UNSET)

        description = d.pop("description", UNSET)

        element_id = d.pop("elementId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_flattened_body = d.pop("isFlattenedBody", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        is_mesh = d.pop("isMesh", UNSET)

        _material = d.pop("material", UNSET)
        material: BTPartMaterialInfo | Unset
        if isinstance(_material, Unset):
            material = UNSET
        else:
            material = BTPartMaterialInfo.from_dict(_material)

        _mesh_state = d.pop("meshState", UNSET)
        mesh_state: GBTMeshState | Unset
        if isinstance(_mesh_state, Unset):
            mesh_state = UNSET
        else:
            mesh_state = GBTMeshState(_mesh_state)

        metadata_microversion = d.pop("metadataMicroversion", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        name = d.pop("name", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        part_query = d.pop("partQuery", UNSET)

        product_line = d.pop("productLine", UNSET)

        project = d.pop("project", UNSET)

        _property_source_types = d.pop("propertySourceTypes", UNSET)
        property_source_types: BTPartMetadataInfoPropertySourceTypes | Unset
        if isinstance(_property_source_types, Unset):
            property_source_types = UNSET
        else:
            property_source_types = BTPartMetadataInfoPropertySourceTypes.from_dict(_property_source_types)

        referencing_configured_part_node_ids = cast(list[str], d.pop("referencingConfiguredPartNodeIds", UNSET))

        revision = d.pop("revision", UNSET)

        _state = d.pop("state", UNSET)
        state: BTMetadataStateType | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BTMetadataStateType(_state)

        thumbnail_configuration_id = d.pop("thumbnailConfigurationId", UNSET)

        _thumbnail_info = d.pop("thumbnailInfo", UNSET)
        thumbnail_info: BTThumbnailInfo | Unset
        if isinstance(_thumbnail_info, Unset):
            thumbnail_info = UNSET
        else:
            thumbnail_info = BTThumbnailInfo.from_dict(_thumbnail_info)

        title1 = d.pop("title1", UNSET)

        title2 = d.pop("title2", UNSET)

        title3 = d.pop("title3", UNSET)

        unflattened_part_id = d.pop("unflattenedPartId", UNSET)

        vendor = d.pop("vendor", UNSET)

        bt_part_metadata_info = cls(
            appearance=appearance,
            body_type=body_type,
            configuration_id=configuration_id,
            custom_properties=custom_properties,
            default_color_hash=default_color_hash,
            description=description,
            element_id=element_id,
            href=href,
            id=id,
            is_flattened_body=is_flattened_body,
            is_hidden=is_hidden,
            is_mesh=is_mesh,
            material=material,
            mesh_state=mesh_state,
            metadata_microversion=metadata_microversion,
            microversion_id=microversion_id,
            name=name,
            ordinal=ordinal,
            part_id=part_id,
            part_identity=part_identity,
            part_number=part_number,
            part_query=part_query,
            product_line=product_line,
            project=project,
            property_source_types=property_source_types,
            referencing_configured_part_node_ids=referencing_configured_part_node_ids,
            revision=revision,
            state=state,
            thumbnail_configuration_id=thumbnail_configuration_id,
            thumbnail_info=thumbnail_info,
            title1=title1,
            title2=title2,
            title3=title3,
            unflattened_part_id=unflattened_part_id,
            vendor=vendor,
        )

        bt_part_metadata_info.additional_properties = d
        return bt_part_metadata_info

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
