from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_display_data_usage import GBTDisplayDataUsage
from ..models.gbt_part_studio_display_data_version import GBTPartStudioDisplayDataVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
    from ..models.bt_assembly_references_display_data_1562 import BTAssemblyReferencesDisplayData1562
    from ..models.bt_base_part_color_cycle_2614 import BTBasePartColorCycle2614
    from ..models.bt_dimension_display_data_323 import BTDimensionDisplayData323
    from ..models.bt_element_display_data_326 import BTElementDisplayData326
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_microversion_id_and_configuration_interval_2364 import BTMicroversionIdAndConfigurationInterval2364
    from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367
    from ..models.bt_part_display_data_17 import BTPartDisplayData17
    from ..models.bt_part_studio_display_data_346_all_insertable_display_data import (
        BTPartStudioDisplayData346AllInsertableDisplayData,
    )
    from ..models.bt_part_studio_display_data_346_appearance_id_to_appearance_override import (
        BTPartStudioDisplayData346AppearanceIdToAppearanceOverride,
    )
    from ..models.bt_part_studio_display_data_346_body_id_to_entity_appearance_settings import (
        BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings,
    )
    from ..models.bt_part_studio_display_data_346_decal_id_to_decal import BTPartStudioDisplayData346DecalIdToDecal
    from ..models.bt_part_studio_display_data_346_deterministic_id_to_associated_feature_ids import (
        BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds,
    )
    from ..models.bt_part_studio_display_data_346_deterministic_id_to_entity import (
        BTPartStudioDisplayData346DeterministicIdToEntity,
    )
    from ..models.bt_part_studio_display_data_346_deterministic_id_to_part_display_data import (
        BTPartStudioDisplayData346DeterministicIdToPartDisplayData,
    )
    from ..models.bt_part_studio_display_data_346_deterministic_part_id_to_data import (
        BTPartStudioDisplayData346DeterministicPartIdToData,
    )
    from ..models.bt_part_studio_display_data_346_feature_id_to_operation_indices import (
        BTPartStudioDisplayData346FeatureIdToOperationIndices,
    )
    from ..models.bt_part_studio_display_data_346_part_id_and_tessellation_setting_to_buffers import (
        BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers,
    )
    from ..models.bt_part_studio_display_data_346_sketch_feature_id_and_tessellation_setting_to_buffers import (
        BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers,
    )
    from ..models.bt_part_studio_display_data_346_sketch_images import BTPartStudioDisplayData346SketchImages


T = TypeVar("T", bound="BTPartStudioDisplayData346")


@_attrs_define
class BTPartStudioDisplayData346:
    """
    Attributes:
        all_insertable_display_data (BTPartStudioDisplayData346AllInsertableDisplayData | Unset):
        annotations_for_element (BTAnnotationElementDisplayData894 | Unset):
        appearance_id_to_appearance_override (BTPartStudioDisplayData346AppearanceIdToAppearanceOverride | Unset):
        assembly_reference_display_data (BTAssemblyReferencesDisplayData1562 | Unset):
        body_id_to_entity_appearance_settings (BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings | Unset):
        body_id_to_entity_appearance_settings_changed (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        cacheable_part_studio_display_data_version (GBTPartStudioDisplayDataVersion | Unset):
        decal_id_to_decal (BTPartStudioDisplayData346DecalIdToDecal | Unset):
        deterministic_id_to_associated_feature_ids (BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds |
            Unset):
        deterministic_id_to_entity (BTPartStudioDisplayData346DeterministicIdToEntity | Unset):
        deterministic_id_to_part_display_data (BTPartStudioDisplayData346DeterministicIdToPartDisplayData | Unset):
        deterministic_part_id_to_data (BTPartStudioDisplayData346DeterministicPartIdToData | Unset):
        dimensions (list[BTDimensionDisplayData323] | Unset):
        display_state_id (str | Unset):
        element_id (str | Unset):
        feature_id_to_operation_indices (BTPartStudioDisplayData346FeatureIdToOperationIndices | Unset):
        from_cache (bool | Unset):
        from_full_element_id (BTFullElementId756 | Unset):
        full_element_id (BTFullElementId756 | Unset):
        incremental (bool | Unset):
        instance_count (int | Unset):
        is_base (bool | Unset):
        is_external (bool | Unset):
        is_noop (bool | Unset):
        keep_from_microversion (bool | Unset):
        microversion_config_interval_advancing (bool | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        microversion_id_and_configuration_interval (BTMicroversionIdAndConfigurationInterval2364 | Unset):
        microversion_interval (BTMicroversionIdInterval367 | Unset):
        number_of_sketch_entities (int | Unset):
        part_color_cycle (BTBasePartColorCycle2614 | Unset):
        part_display_data (list[BTPartDisplayData17] | Unset):
        part_id_and_tessellation_setting_to_buffers (BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers |
            Unset):
        sketch_feature_id_and_tessellation_setting_to_buffers
            (BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers | Unset):
        sketch_images (BTPartStudioDisplayData346SketchImages | Unset):
        updated_parts (list[str] | Unset):
        usage (GBTDisplayDataUsage | Unset):
        uses_multiple_tessellation_settings (bool | Unset):
        version_for_rasterization (BTElementDisplayData326 | Unset):
    """

    all_insertable_display_data: BTPartStudioDisplayData346AllInsertableDisplayData | Unset = UNSET
    annotations_for_element: BTAnnotationElementDisplayData894 | Unset = UNSET
    appearance_id_to_appearance_override: BTPartStudioDisplayData346AppearanceIdToAppearanceOverride | Unset = UNSET
    assembly_reference_display_data: BTAssemblyReferencesDisplayData1562 | Unset = UNSET
    body_id_to_entity_appearance_settings: BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings | Unset = UNSET
    body_id_to_entity_appearance_settings_changed: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    cacheable_part_studio_display_data_version: GBTPartStudioDisplayDataVersion | Unset = UNSET
    decal_id_to_decal: BTPartStudioDisplayData346DecalIdToDecal | Unset = UNSET
    deterministic_id_to_associated_feature_ids: (
        BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds | Unset
    ) = UNSET
    deterministic_id_to_entity: BTPartStudioDisplayData346DeterministicIdToEntity | Unset = UNSET
    deterministic_id_to_part_display_data: BTPartStudioDisplayData346DeterministicIdToPartDisplayData | Unset = UNSET
    deterministic_part_id_to_data: BTPartStudioDisplayData346DeterministicPartIdToData | Unset = UNSET
    dimensions: list[BTDimensionDisplayData323] | Unset = UNSET
    display_state_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    feature_id_to_operation_indices: BTPartStudioDisplayData346FeatureIdToOperationIndices | Unset = UNSET
    from_cache: bool | Unset = UNSET
    from_full_element_id: BTFullElementId756 | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    incremental: bool | Unset = UNSET
    instance_count: int | Unset = UNSET
    is_base: bool | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_noop: bool | Unset = UNSET
    keep_from_microversion: bool | Unset = UNSET
    microversion_config_interval_advancing: bool | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset = UNSET
    microversion_interval: BTMicroversionIdInterval367 | Unset = UNSET
    number_of_sketch_entities: int | Unset = UNSET
    part_color_cycle: BTBasePartColorCycle2614 | Unset = UNSET
    part_display_data: list[BTPartDisplayData17] | Unset = UNSET
    part_id_and_tessellation_setting_to_buffers: (
        BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers | Unset
    ) = UNSET
    sketch_feature_id_and_tessellation_setting_to_buffers: (
        BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers | Unset
    ) = UNSET
    sketch_images: BTPartStudioDisplayData346SketchImages | Unset = UNSET
    updated_parts: list[str] | Unset = UNSET
    usage: GBTDisplayDataUsage | Unset = UNSET
    uses_multiple_tessellation_settings: bool | Unset = UNSET
    version_for_rasterization: BTElementDisplayData326 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_insertable_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_insertable_display_data, Unset):
            all_insertable_display_data = self.all_insertable_display_data.to_dict()

        annotations_for_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations_for_element, Unset):
            annotations_for_element = self.annotations_for_element.to_dict()

        appearance_id_to_appearance_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance_id_to_appearance_override, Unset):
            appearance_id_to_appearance_override = self.appearance_id_to_appearance_override.to_dict()

        assembly_reference_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assembly_reference_display_data, Unset):
            assembly_reference_display_data = self.assembly_reference_display_data.to_dict()

        body_id_to_entity_appearance_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_id_to_entity_appearance_settings, Unset):
            body_id_to_entity_appearance_settings = self.body_id_to_entity_appearance_settings.to_dict()

        body_id_to_entity_appearance_settings_changed = self.body_id_to_entity_appearance_settings_changed

        bt_type = self.bt_type

        cacheable_part_studio_display_data_version: str | Unset = UNSET
        if not isinstance(self.cacheable_part_studio_display_data_version, Unset):
            cacheable_part_studio_display_data_version = self.cacheable_part_studio_display_data_version.value

        decal_id_to_decal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decal_id_to_decal, Unset):
            decal_id_to_decal = self.decal_id_to_decal.to_dict()

        deterministic_id_to_associated_feature_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_id_to_associated_feature_ids, Unset):
            deterministic_id_to_associated_feature_ids = self.deterministic_id_to_associated_feature_ids.to_dict()

        deterministic_id_to_entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_id_to_entity, Unset):
            deterministic_id_to_entity = self.deterministic_id_to_entity.to_dict()

        deterministic_id_to_part_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_id_to_part_display_data, Unset):
            deterministic_id_to_part_display_data = self.deterministic_id_to_part_display_data.to_dict()

        deterministic_part_id_to_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_part_id_to_data, Unset):
            deterministic_part_id_to_data = self.deterministic_part_id_to_data.to_dict()

        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)

        display_state_id = self.display_state_id

        element_id = self.element_id

        feature_id_to_operation_indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_id_to_operation_indices, Unset):
            feature_id_to_operation_indices = self.feature_id_to_operation_indices.to_dict()

        from_cache = self.from_cache

        from_full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_full_element_id, Unset):
            from_full_element_id = self.from_full_element_id.to_dict()

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        incremental = self.incremental

        instance_count = self.instance_count

        is_base = self.is_base

        is_external = self.is_external

        is_noop = self.is_noop

        keep_from_microversion = self.keep_from_microversion

        microversion_config_interval_advancing = self.microversion_config_interval_advancing

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        microversion_id_and_configuration_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = self.microversion_id_and_configuration_interval.to_dict()

        microversion_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_interval, Unset):
            microversion_interval = self.microversion_interval.to_dict()

        number_of_sketch_entities = self.number_of_sketch_entities

        part_color_cycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_color_cycle, Unset):
            part_color_cycle = self.part_color_cycle.to_dict()

        part_display_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.part_display_data, Unset):
            part_display_data = []
            for part_display_data_item_data in self.part_display_data:
                part_display_data_item = part_display_data_item_data.to_dict()
                part_display_data.append(part_display_data_item)

        part_id_and_tessellation_setting_to_buffers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_id_and_tessellation_setting_to_buffers, Unset):
            part_id_and_tessellation_setting_to_buffers = self.part_id_and_tessellation_setting_to_buffers.to_dict()

        sketch_feature_id_and_tessellation_setting_to_buffers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sketch_feature_id_and_tessellation_setting_to_buffers, Unset):
            sketch_feature_id_and_tessellation_setting_to_buffers = (
                self.sketch_feature_id_and_tessellation_setting_to_buffers.to_dict()
            )

        sketch_images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sketch_images, Unset):
            sketch_images = self.sketch_images.to_dict()

        updated_parts: list[str] | Unset = UNSET
        if not isinstance(self.updated_parts, Unset):
            updated_parts = self.updated_parts

        usage: str | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.value

        uses_multiple_tessellation_settings = self.uses_multiple_tessellation_settings

        version_for_rasterization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_for_rasterization, Unset):
            version_for_rasterization = self.version_for_rasterization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_insertable_display_data is not UNSET:
            field_dict["allInsertableDisplayData"] = all_insertable_display_data
        if annotations_for_element is not UNSET:
            field_dict["annotationsForElement"] = annotations_for_element
        if appearance_id_to_appearance_override is not UNSET:
            field_dict["appearanceIdToAppearanceOverride"] = appearance_id_to_appearance_override
        if assembly_reference_display_data is not UNSET:
            field_dict["assemblyReferenceDisplayData"] = assembly_reference_display_data
        if body_id_to_entity_appearance_settings is not UNSET:
            field_dict["bodyIdToEntityAppearanceSettings"] = body_id_to_entity_appearance_settings
        if body_id_to_entity_appearance_settings_changed is not UNSET:
            field_dict["bodyIdToEntityAppearanceSettingsChanged"] = body_id_to_entity_appearance_settings_changed
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cacheable_part_studio_display_data_version is not UNSET:
            field_dict["cacheablePartStudioDisplayDataVersion"] = cacheable_part_studio_display_data_version
        if decal_id_to_decal is not UNSET:
            field_dict["decalIdToDecal"] = decal_id_to_decal
        if deterministic_id_to_associated_feature_ids is not UNSET:
            field_dict["deterministicIdToAssociatedFeatureIds"] = deterministic_id_to_associated_feature_ids
        if deterministic_id_to_entity is not UNSET:
            field_dict["deterministicIdToEntity"] = deterministic_id_to_entity
        if deterministic_id_to_part_display_data is not UNSET:
            field_dict["deterministicIdToPartDisplayData"] = deterministic_id_to_part_display_data
        if deterministic_part_id_to_data is not UNSET:
            field_dict["deterministicPartIdToData"] = deterministic_part_id_to_data
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if display_state_id is not UNSET:
            field_dict["displayStateId"] = display_state_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if feature_id_to_operation_indices is not UNSET:
            field_dict["featureIdToOperationIndices"] = feature_id_to_operation_indices
        if from_cache is not UNSET:
            field_dict["fromCache"] = from_cache
        if from_full_element_id is not UNSET:
            field_dict["fromFullElementId"] = from_full_element_id
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if incremental is not UNSET:
            field_dict["incremental"] = incremental
        if instance_count is not UNSET:
            field_dict["instanceCount"] = instance_count
        if is_base is not UNSET:
            field_dict["isBase"] = is_base
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_noop is not UNSET:
            field_dict["isNoop"] = is_noop
        if keep_from_microversion is not UNSET:
            field_dict["keepFromMicroversion"] = keep_from_microversion
        if microversion_config_interval_advancing is not UNSET:
            field_dict["microversionConfigIntervalAdvancing"] = microversion_config_interval_advancing
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if microversion_id_and_configuration_interval is not UNSET:
            field_dict["microversionIdAndConfigurationInterval"] = microversion_id_and_configuration_interval
        if microversion_interval is not UNSET:
            field_dict["microversionInterval"] = microversion_interval
        if number_of_sketch_entities is not UNSET:
            field_dict["numberOfSketchEntities"] = number_of_sketch_entities
        if part_color_cycle is not UNSET:
            field_dict["partColorCycle"] = part_color_cycle
        if part_display_data is not UNSET:
            field_dict["partDisplayData"] = part_display_data
        if part_id_and_tessellation_setting_to_buffers is not UNSET:
            field_dict["partIdAndTessellationSettingToBuffers"] = part_id_and_tessellation_setting_to_buffers
        if sketch_feature_id_and_tessellation_setting_to_buffers is not UNSET:
            field_dict["sketchFeatureIdAndTessellationSettingToBuffers"] = (
                sketch_feature_id_and_tessellation_setting_to_buffers
            )
        if sketch_images is not UNSET:
            field_dict["sketchImages"] = sketch_images
        if updated_parts is not UNSET:
            field_dict["updatedParts"] = updated_parts
        if usage is not UNSET:
            field_dict["usage"] = usage
        if uses_multiple_tessellation_settings is not UNSET:
            field_dict["usesMultipleTessellationSettings"] = uses_multiple_tessellation_settings
        if version_for_rasterization is not UNSET:
            field_dict["versionForRasterization"] = version_for_rasterization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
        from ..models.bt_assembly_references_display_data_1562 import BTAssemblyReferencesDisplayData1562
        from ..models.bt_base_part_color_cycle_2614 import BTBasePartColorCycle2614
        from ..models.bt_dimension_display_data_323 import BTDimensionDisplayData323
        from ..models.bt_element_display_data_326 import BTElementDisplayData326
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_microversion_id_and_configuration_interval_2364 import (
            BTMicroversionIdAndConfigurationInterval2364,
        )
        from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367
        from ..models.bt_part_display_data_17 import BTPartDisplayData17
        from ..models.bt_part_studio_display_data_346_all_insertable_display_data import (
            BTPartStudioDisplayData346AllInsertableDisplayData,
        )
        from ..models.bt_part_studio_display_data_346_appearance_id_to_appearance_override import (
            BTPartStudioDisplayData346AppearanceIdToAppearanceOverride,
        )
        from ..models.bt_part_studio_display_data_346_body_id_to_entity_appearance_settings import (
            BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings,
        )
        from ..models.bt_part_studio_display_data_346_decal_id_to_decal import BTPartStudioDisplayData346DecalIdToDecal
        from ..models.bt_part_studio_display_data_346_deterministic_id_to_associated_feature_ids import (
            BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds,
        )
        from ..models.bt_part_studio_display_data_346_deterministic_id_to_entity import (
            BTPartStudioDisplayData346DeterministicIdToEntity,
        )
        from ..models.bt_part_studio_display_data_346_deterministic_id_to_part_display_data import (
            BTPartStudioDisplayData346DeterministicIdToPartDisplayData,
        )
        from ..models.bt_part_studio_display_data_346_deterministic_part_id_to_data import (
            BTPartStudioDisplayData346DeterministicPartIdToData,
        )
        from ..models.bt_part_studio_display_data_346_feature_id_to_operation_indices import (
            BTPartStudioDisplayData346FeatureIdToOperationIndices,
        )
        from ..models.bt_part_studio_display_data_346_part_id_and_tessellation_setting_to_buffers import (
            BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers,
        )
        from ..models.bt_part_studio_display_data_346_sketch_feature_id_and_tessellation_setting_to_buffers import (
            BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers,
        )
        from ..models.bt_part_studio_display_data_346_sketch_images import BTPartStudioDisplayData346SketchImages

        d = dict(src_dict)
        _all_insertable_display_data = d.pop("allInsertableDisplayData", UNSET)
        all_insertable_display_data: BTPartStudioDisplayData346AllInsertableDisplayData | Unset
        if isinstance(_all_insertable_display_data, Unset):
            all_insertable_display_data = UNSET
        else:
            all_insertable_display_data = BTPartStudioDisplayData346AllInsertableDisplayData.from_dict(
                _all_insertable_display_data
            )

        _annotations_for_element = d.pop("annotationsForElement", UNSET)
        annotations_for_element: BTAnnotationElementDisplayData894 | Unset
        if isinstance(_annotations_for_element, Unset):
            annotations_for_element = UNSET
        else:
            annotations_for_element = BTAnnotationElementDisplayData894.from_dict(_annotations_for_element)

        _appearance_id_to_appearance_override = d.pop("appearanceIdToAppearanceOverride", UNSET)
        appearance_id_to_appearance_override: BTPartStudioDisplayData346AppearanceIdToAppearanceOverride | Unset
        if isinstance(_appearance_id_to_appearance_override, Unset):
            appearance_id_to_appearance_override = UNSET
        else:
            appearance_id_to_appearance_override = BTPartStudioDisplayData346AppearanceIdToAppearanceOverride.from_dict(
                _appearance_id_to_appearance_override
            )

        _assembly_reference_display_data = d.pop("assemblyReferenceDisplayData", UNSET)
        assembly_reference_display_data: BTAssemblyReferencesDisplayData1562 | Unset
        if isinstance(_assembly_reference_display_data, Unset):
            assembly_reference_display_data = UNSET
        else:
            assembly_reference_display_data = BTAssemblyReferencesDisplayData1562.from_dict(
                _assembly_reference_display_data
            )

        _body_id_to_entity_appearance_settings = d.pop("bodyIdToEntityAppearanceSettings", UNSET)
        body_id_to_entity_appearance_settings: BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings | Unset
        if isinstance(_body_id_to_entity_appearance_settings, Unset):
            body_id_to_entity_appearance_settings = UNSET
        else:
            body_id_to_entity_appearance_settings = (
                BTPartStudioDisplayData346BodyIdToEntityAppearanceSettings.from_dict(
                    _body_id_to_entity_appearance_settings
                )
            )

        body_id_to_entity_appearance_settings_changed = d.pop("bodyIdToEntityAppearanceSettingsChanged", UNSET)

        bt_type = d.pop("btType", UNSET)

        _cacheable_part_studio_display_data_version = d.pop("cacheablePartStudioDisplayDataVersion", UNSET)
        cacheable_part_studio_display_data_version: GBTPartStudioDisplayDataVersion | Unset
        if isinstance(_cacheable_part_studio_display_data_version, Unset):
            cacheable_part_studio_display_data_version = UNSET
        else:
            cacheable_part_studio_display_data_version = GBTPartStudioDisplayDataVersion(
                _cacheable_part_studio_display_data_version
            )

        _decal_id_to_decal = d.pop("decalIdToDecal", UNSET)
        decal_id_to_decal: BTPartStudioDisplayData346DecalIdToDecal | Unset
        if isinstance(_decal_id_to_decal, Unset):
            decal_id_to_decal = UNSET
        else:
            decal_id_to_decal = BTPartStudioDisplayData346DecalIdToDecal.from_dict(_decal_id_to_decal)

        _deterministic_id_to_associated_feature_ids = d.pop("deterministicIdToAssociatedFeatureIds", UNSET)
        deterministic_id_to_associated_feature_ids: (
            BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds | Unset
        )
        if isinstance(_deterministic_id_to_associated_feature_ids, Unset):
            deterministic_id_to_associated_feature_ids = UNSET
        else:
            deterministic_id_to_associated_feature_ids = (
                BTPartStudioDisplayData346DeterministicIdToAssociatedFeatureIds.from_dict(
                    _deterministic_id_to_associated_feature_ids
                )
            )

        _deterministic_id_to_entity = d.pop("deterministicIdToEntity", UNSET)
        deterministic_id_to_entity: BTPartStudioDisplayData346DeterministicIdToEntity | Unset
        if isinstance(_deterministic_id_to_entity, Unset):
            deterministic_id_to_entity = UNSET
        else:
            deterministic_id_to_entity = BTPartStudioDisplayData346DeterministicIdToEntity.from_dict(
                _deterministic_id_to_entity
            )

        _deterministic_id_to_part_display_data = d.pop("deterministicIdToPartDisplayData", UNSET)
        deterministic_id_to_part_display_data: BTPartStudioDisplayData346DeterministicIdToPartDisplayData | Unset
        if isinstance(_deterministic_id_to_part_display_data, Unset):
            deterministic_id_to_part_display_data = UNSET
        else:
            deterministic_id_to_part_display_data = (
                BTPartStudioDisplayData346DeterministicIdToPartDisplayData.from_dict(
                    _deterministic_id_to_part_display_data
                )
            )

        _deterministic_part_id_to_data = d.pop("deterministicPartIdToData", UNSET)
        deterministic_part_id_to_data: BTPartStudioDisplayData346DeterministicPartIdToData | Unset
        if isinstance(_deterministic_part_id_to_data, Unset):
            deterministic_part_id_to_data = UNSET
        else:
            deterministic_part_id_to_data = BTPartStudioDisplayData346DeterministicPartIdToData.from_dict(
                _deterministic_part_id_to_data
            )

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[BTDimensionDisplayData323] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = BTDimensionDisplayData323.from_dict(dimensions_item_data)

                dimensions.append(dimensions_item)

        display_state_id = d.pop("displayStateId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _feature_id_to_operation_indices = d.pop("featureIdToOperationIndices", UNSET)
        feature_id_to_operation_indices: BTPartStudioDisplayData346FeatureIdToOperationIndices | Unset
        if isinstance(_feature_id_to_operation_indices, Unset):
            feature_id_to_operation_indices = UNSET
        else:
            feature_id_to_operation_indices = BTPartStudioDisplayData346FeatureIdToOperationIndices.from_dict(
                _feature_id_to_operation_indices
            )

        from_cache = d.pop("fromCache", UNSET)

        _from_full_element_id = d.pop("fromFullElementId", UNSET)
        from_full_element_id: BTFullElementId756 | Unset
        if isinstance(_from_full_element_id, Unset):
            from_full_element_id = UNSET
        else:
            from_full_element_id = BTFullElementId756.from_dict(_from_full_element_id)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        incremental = d.pop("incremental", UNSET)

        instance_count = d.pop("instanceCount", UNSET)

        is_base = d.pop("isBase", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_noop = d.pop("isNoop", UNSET)

        keep_from_microversion = d.pop("keepFromMicroversion", UNSET)

        microversion_config_interval_advancing = d.pop("microversionConfigIntervalAdvancing", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        _microversion_id_and_configuration_interval = d.pop("microversionIdAndConfigurationInterval", UNSET)
        microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset
        if isinstance(_microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = UNSET
        else:
            microversion_id_and_configuration_interval = BTMicroversionIdAndConfigurationInterval2364.from_dict(
                _microversion_id_and_configuration_interval
            )

        _microversion_interval = d.pop("microversionInterval", UNSET)
        microversion_interval: BTMicroversionIdInterval367 | Unset
        if isinstance(_microversion_interval, Unset):
            microversion_interval = UNSET
        else:
            microversion_interval = BTMicroversionIdInterval367.from_dict(_microversion_interval)

        number_of_sketch_entities = d.pop("numberOfSketchEntities", UNSET)

        _part_color_cycle = d.pop("partColorCycle", UNSET)
        part_color_cycle: BTBasePartColorCycle2614 | Unset
        if isinstance(_part_color_cycle, Unset):
            part_color_cycle = UNSET
        else:
            part_color_cycle = BTBasePartColorCycle2614.from_dict(_part_color_cycle)

        _part_display_data = d.pop("partDisplayData", UNSET)
        part_display_data: list[BTPartDisplayData17] | Unset = UNSET
        if _part_display_data is not UNSET:
            part_display_data = []
            for part_display_data_item_data in _part_display_data:
                part_display_data_item = BTPartDisplayData17.from_dict(part_display_data_item_data)

                part_display_data.append(part_display_data_item)

        _part_id_and_tessellation_setting_to_buffers = d.pop("partIdAndTessellationSettingToBuffers", UNSET)
        part_id_and_tessellation_setting_to_buffers: (
            BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers | Unset
        )
        if isinstance(_part_id_and_tessellation_setting_to_buffers, Unset):
            part_id_and_tessellation_setting_to_buffers = UNSET
        else:
            part_id_and_tessellation_setting_to_buffers = (
                BTPartStudioDisplayData346PartIdAndTessellationSettingToBuffers.from_dict(
                    _part_id_and_tessellation_setting_to_buffers
                )
            )

        _sketch_feature_id_and_tessellation_setting_to_buffers = d.pop(
            "sketchFeatureIdAndTessellationSettingToBuffers", UNSET
        )
        sketch_feature_id_and_tessellation_setting_to_buffers: (
            BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers | Unset
        )
        if isinstance(_sketch_feature_id_and_tessellation_setting_to_buffers, Unset):
            sketch_feature_id_and_tessellation_setting_to_buffers = UNSET
        else:
            sketch_feature_id_and_tessellation_setting_to_buffers = (
                BTPartStudioDisplayData346SketchFeatureIdAndTessellationSettingToBuffers.from_dict(
                    _sketch_feature_id_and_tessellation_setting_to_buffers
                )
            )

        _sketch_images = d.pop("sketchImages", UNSET)
        sketch_images: BTPartStudioDisplayData346SketchImages | Unset
        if isinstance(_sketch_images, Unset):
            sketch_images = UNSET
        else:
            sketch_images = BTPartStudioDisplayData346SketchImages.from_dict(_sketch_images)

        updated_parts = cast(list[str], d.pop("updatedParts", UNSET))

        _usage = d.pop("usage", UNSET)
        usage: GBTDisplayDataUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = GBTDisplayDataUsage(_usage)

        uses_multiple_tessellation_settings = d.pop("usesMultipleTessellationSettings", UNSET)

        _version_for_rasterization = d.pop("versionForRasterization", UNSET)
        version_for_rasterization: BTElementDisplayData326 | Unset
        if isinstance(_version_for_rasterization, Unset):
            version_for_rasterization = UNSET
        else:
            version_for_rasterization = BTElementDisplayData326.from_dict(_version_for_rasterization)

        bt_part_studio_display_data_346 = cls(
            all_insertable_display_data=all_insertable_display_data,
            annotations_for_element=annotations_for_element,
            appearance_id_to_appearance_override=appearance_id_to_appearance_override,
            assembly_reference_display_data=assembly_reference_display_data,
            body_id_to_entity_appearance_settings=body_id_to_entity_appearance_settings,
            body_id_to_entity_appearance_settings_changed=body_id_to_entity_appearance_settings_changed,
            bt_type=bt_type,
            cacheable_part_studio_display_data_version=cacheable_part_studio_display_data_version,
            decal_id_to_decal=decal_id_to_decal,
            deterministic_id_to_associated_feature_ids=deterministic_id_to_associated_feature_ids,
            deterministic_id_to_entity=deterministic_id_to_entity,
            deterministic_id_to_part_display_data=deterministic_id_to_part_display_data,
            deterministic_part_id_to_data=deterministic_part_id_to_data,
            dimensions=dimensions,
            display_state_id=display_state_id,
            element_id=element_id,
            feature_id_to_operation_indices=feature_id_to_operation_indices,
            from_cache=from_cache,
            from_full_element_id=from_full_element_id,
            full_element_id=full_element_id,
            incremental=incremental,
            instance_count=instance_count,
            is_base=is_base,
            is_external=is_external,
            is_noop=is_noop,
            keep_from_microversion=keep_from_microversion,
            microversion_config_interval_advancing=microversion_config_interval_advancing,
            microversion_id=microversion_id,
            microversion_id_and_configuration_interval=microversion_id_and_configuration_interval,
            microversion_interval=microversion_interval,
            number_of_sketch_entities=number_of_sketch_entities,
            part_color_cycle=part_color_cycle,
            part_display_data=part_display_data,
            part_id_and_tessellation_setting_to_buffers=part_id_and_tessellation_setting_to_buffers,
            sketch_feature_id_and_tessellation_setting_to_buffers=sketch_feature_id_and_tessellation_setting_to_buffers,
            sketch_images=sketch_images,
            updated_parts=updated_parts,
            usage=usage,
            uses_multiple_tessellation_settings=uses_multiple_tessellation_settings,
            version_for_rasterization=version_for_rasterization,
        )

        bt_part_studio_display_data_346.additional_properties = d
        return bt_part_studio_display_data_346

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
