from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementReferenceResolveInfo")


@_attrs_define
class BTAppElementReferenceResolveInfo:
    """
    Attributes:
        change_id (str | Unset):
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
        id_tag (str | Unset):
        id_tag_is_valid (bool | Unset):
        is_configurable (bool | Unset):
        is_flattened_part (bool | Unset):
        is_locked (bool | Unset):
        is_sketch_only (bool | Unset):
        is_surface (bool | Unset):
        latest_element_microversion_id (str | Unset):
        part_identity (str | Unset):
        part_number (str | Unset):
        reference_id (str | Unset):
        reference_type (int | Unset):
        resolved_configuration (str | Unset):
        resolved_document_microversion_id (str | Unset):
        resolved_element_microversion_id (str | Unset):
        revision (str | Unset):
        sketch_ids (list[str] | Unset):
        source_element_id (str | Unset):
        target_configuration (str | Unset):
        target_document_id (str | Unset):
        target_document_microversion_id (str | Unset):
        target_element_id (str | Unset):
        target_element_microversion_id (str | Unset):
        target_version_id (str | Unset): Reference to a part or assembly in a version; `NULL` when reference is in a
            workspace.
        track_new_versions (bool | Unset):
    """

    change_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    id_tag: str | Unset = UNSET
    id_tag_is_valid: bool | Unset = UNSET
    is_configurable: bool | Unset = UNSET
    is_flattened_part: bool | Unset = UNSET
    is_locked: bool | Unset = UNSET
    is_sketch_only: bool | Unset = UNSET
    is_surface: bool | Unset = UNSET
    latest_element_microversion_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_number: str | Unset = UNSET
    reference_id: str | Unset = UNSET
    reference_type: int | Unset = UNSET
    resolved_configuration: str | Unset = UNSET
    resolved_document_microversion_id: str | Unset = UNSET
    resolved_element_microversion_id: str | Unset = UNSET
    revision: str | Unset = UNSET
    sketch_ids: list[str] | Unset = UNSET
    source_element_id: str | Unset = UNSET
    target_configuration: str | Unset = UNSET
    target_document_id: str | Unset = UNSET
    target_document_microversion_id: str | Unset = UNSET
    target_element_id: str | Unset = UNSET
    target_element_microversion_id: str | Unset = UNSET
    target_version_id: str | Unset = UNSET
    track_new_versions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        id_tag = self.id_tag

        id_tag_is_valid = self.id_tag_is_valid

        is_configurable = self.is_configurable

        is_flattened_part = self.is_flattened_part

        is_locked = self.is_locked

        is_sketch_only = self.is_sketch_only

        is_surface = self.is_surface

        latest_element_microversion_id = self.latest_element_microversion_id

        part_identity = self.part_identity

        part_number = self.part_number

        reference_id = self.reference_id

        reference_type = self.reference_type

        resolved_configuration = self.resolved_configuration

        resolved_document_microversion_id = self.resolved_document_microversion_id

        resolved_element_microversion_id = self.resolved_element_microversion_id

        revision = self.revision

        sketch_ids: list[str] | Unset = UNSET
        if not isinstance(self.sketch_ids, Unset):
            sketch_ids = self.sketch_ids

        source_element_id = self.source_element_id

        target_configuration = self.target_configuration

        target_document_id = self.target_document_id

        target_document_microversion_id = self.target_document_microversion_id

        target_element_id = self.target_element_id

        target_element_microversion_id = self.target_element_microversion_id

        target_version_id = self.target_version_id

        track_new_versions = self.track_new_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value
        if id_tag is not UNSET:
            field_dict["idTag"] = id_tag
        if id_tag_is_valid is not UNSET:
            field_dict["idTagIsValid"] = id_tag_is_valid
        if is_configurable is not UNSET:
            field_dict["isConfigurable"] = is_configurable
        if is_flattened_part is not UNSET:
            field_dict["isFlattenedPart"] = is_flattened_part
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_sketch_only is not UNSET:
            field_dict["isSketchOnly"] = is_sketch_only
        if is_surface is not UNSET:
            field_dict["isSurface"] = is_surface
        if latest_element_microversion_id is not UNSET:
            field_dict["latestElementMicroversionId"] = latest_element_microversion_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if resolved_configuration is not UNSET:
            field_dict["resolvedConfiguration"] = resolved_configuration
        if resolved_document_microversion_id is not UNSET:
            field_dict["resolvedDocumentMicroversionId"] = resolved_document_microversion_id
        if resolved_element_microversion_id is not UNSET:
            field_dict["resolvedElementMicroversionId"] = resolved_element_microversion_id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if sketch_ids is not UNSET:
            field_dict["sketchIds"] = sketch_ids
        if source_element_id is not UNSET:
            field_dict["sourceElementId"] = source_element_id
        if target_configuration is not UNSET:
            field_dict["targetConfiguration"] = target_configuration
        if target_document_id is not UNSET:
            field_dict["targetDocumentId"] = target_document_id
        if target_document_microversion_id is not UNSET:
            field_dict["targetDocumentMicroversionId"] = target_document_microversion_id
        if target_element_id is not UNSET:
            field_dict["targetElementId"] = target_element_id
        if target_element_microversion_id is not UNSET:
            field_dict["targetElementMicroversionId"] = target_element_microversion_id
        if target_version_id is not UNSET:
            field_dict["targetVersionId"] = target_version_id
        if track_new_versions is not UNSET:
            field_dict["trackNewVersions"] = track_new_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        change_id = d.pop("changeId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        id_tag = d.pop("idTag", UNSET)

        id_tag_is_valid = d.pop("idTagIsValid", UNSET)

        is_configurable = d.pop("isConfigurable", UNSET)

        is_flattened_part = d.pop("isFlattenedPart", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_sketch_only = d.pop("isSketchOnly", UNSET)

        is_surface = d.pop("isSurface", UNSET)

        latest_element_microversion_id = d.pop("latestElementMicroversionId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        reference_type = d.pop("referenceType", UNSET)

        resolved_configuration = d.pop("resolvedConfiguration", UNSET)

        resolved_document_microversion_id = d.pop("resolvedDocumentMicroversionId", UNSET)

        resolved_element_microversion_id = d.pop("resolvedElementMicroversionId", UNSET)

        revision = d.pop("revision", UNSET)

        sketch_ids = cast(list[str], d.pop("sketchIds", UNSET))

        source_element_id = d.pop("sourceElementId", UNSET)

        target_configuration = d.pop("targetConfiguration", UNSET)

        target_document_id = d.pop("targetDocumentId", UNSET)

        target_document_microversion_id = d.pop("targetDocumentMicroversionId", UNSET)

        target_element_id = d.pop("targetElementId", UNSET)

        target_element_microversion_id = d.pop("targetElementMicroversionId", UNSET)

        target_version_id = d.pop("targetVersionId", UNSET)

        track_new_versions = d.pop("trackNewVersions", UNSET)

        bt_app_element_reference_resolve_info = cls(
            change_id=change_id,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
            id_tag=id_tag,
            id_tag_is_valid=id_tag_is_valid,
            is_configurable=is_configurable,
            is_flattened_part=is_flattened_part,
            is_locked=is_locked,
            is_sketch_only=is_sketch_only,
            is_surface=is_surface,
            latest_element_microversion_id=latest_element_microversion_id,
            part_identity=part_identity,
            part_number=part_number,
            reference_id=reference_id,
            reference_type=reference_type,
            resolved_configuration=resolved_configuration,
            resolved_document_microversion_id=resolved_document_microversion_id,
            resolved_element_microversion_id=resolved_element_microversion_id,
            revision=revision,
            sketch_ids=sketch_ids,
            source_element_id=source_element_id,
            target_configuration=target_configuration,
            target_document_id=target_document_id,
            target_document_microversion_id=target_document_microversion_id,
            target_element_id=target_element_id,
            target_element_microversion_id=target_element_microversion_id,
            target_version_id=target_version_id,
            track_new_versions=track_new_versions,
        )

        bt_app_element_reference_resolve_info.additional_properties = d
        return bt_app_element_reference_resolve_info

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
