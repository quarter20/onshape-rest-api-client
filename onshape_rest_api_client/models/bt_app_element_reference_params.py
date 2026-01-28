from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementReferenceParams")


@_attrs_define
class BTAppElementReferenceParams:
    """
    Attributes:
        has_document_microversions (bool | Unset):
        id_tag (str | Unset):
        id_tag_microversion_id (str | Unset):
        is_locked (bool | Unset):
        is_sketch_only (bool | Unset):
        parent_change_id (str | Unset):
        parent_view_id (str | Unset):
        part_number (str | Unset):
        pure_sketch (bool | Unset):
        reference_type (int | Unset):
        return_error (bool | Unset):
        revision (str | Unset):
        sketch_ids (list[str] | Unset):
        target_configuration (str | Unset):
        target_document_id (str | Unset):
        target_element_id (str | Unset):
        target_microversion_id (str | Unset):
        target_version_id (str | Unset):
        track_new_versions (bool | Unset):
        transaction_id (str | Unset):
        update_sketch_info (bool | Unset):
    """

    has_document_microversions: bool | Unset = UNSET
    id_tag: str | Unset = UNSET
    id_tag_microversion_id: str | Unset = UNSET
    is_locked: bool | Unset = UNSET
    is_sketch_only: bool | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    parent_view_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    pure_sketch: bool | Unset = UNSET
    reference_type: int | Unset = UNSET
    return_error: bool | Unset = UNSET
    revision: str | Unset = UNSET
    sketch_ids: list[str] | Unset = UNSET
    target_configuration: str | Unset = UNSET
    target_document_id: str | Unset = UNSET
    target_element_id: str | Unset = UNSET
    target_microversion_id: str | Unset = UNSET
    target_version_id: str | Unset = UNSET
    track_new_versions: bool | Unset = UNSET
    transaction_id: str | Unset = UNSET
    update_sketch_info: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_document_microversions = self.has_document_microversions

        id_tag = self.id_tag

        id_tag_microversion_id = self.id_tag_microversion_id

        is_locked = self.is_locked

        is_sketch_only = self.is_sketch_only

        parent_change_id = self.parent_change_id

        parent_view_id = self.parent_view_id

        part_number = self.part_number

        pure_sketch = self.pure_sketch

        reference_type = self.reference_type

        return_error = self.return_error

        revision = self.revision

        sketch_ids: list[str] | Unset = UNSET
        if not isinstance(self.sketch_ids, Unset):
            sketch_ids = self.sketch_ids

        target_configuration = self.target_configuration

        target_document_id = self.target_document_id

        target_element_id = self.target_element_id

        target_microversion_id = self.target_microversion_id

        target_version_id = self.target_version_id

        track_new_versions = self.track_new_versions

        transaction_id = self.transaction_id

        update_sketch_info = self.update_sketch_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_document_microversions is not UNSET:
            field_dict["hasDocumentMicroversions"] = has_document_microversions
        if id_tag is not UNSET:
            field_dict["idTag"] = id_tag
        if id_tag_microversion_id is not UNSET:
            field_dict["idTagMicroversionId"] = id_tag_microversion_id
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_sketch_only is not UNSET:
            field_dict["isSketchOnly"] = is_sketch_only
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if parent_view_id is not UNSET:
            field_dict["parentViewId"] = parent_view_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if pure_sketch is not UNSET:
            field_dict["pureSketch"] = pure_sketch
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if return_error is not UNSET:
            field_dict["returnError"] = return_error
        if revision is not UNSET:
            field_dict["revision"] = revision
        if sketch_ids is not UNSET:
            field_dict["sketchIds"] = sketch_ids
        if target_configuration is not UNSET:
            field_dict["targetConfiguration"] = target_configuration
        if target_document_id is not UNSET:
            field_dict["targetDocumentId"] = target_document_id
        if target_element_id is not UNSET:
            field_dict["targetElementId"] = target_element_id
        if target_microversion_id is not UNSET:
            field_dict["targetMicroversionId"] = target_microversion_id
        if target_version_id is not UNSET:
            field_dict["targetVersionId"] = target_version_id
        if track_new_versions is not UNSET:
            field_dict["trackNewVersions"] = track_new_versions
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if update_sketch_info is not UNSET:
            field_dict["updateSketchInfo"] = update_sketch_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_document_microversions = d.pop("hasDocumentMicroversions", UNSET)

        id_tag = d.pop("idTag", UNSET)

        id_tag_microversion_id = d.pop("idTagMicroversionId", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_sketch_only = d.pop("isSketchOnly", UNSET)

        parent_change_id = d.pop("parentChangeId", UNSET)

        parent_view_id = d.pop("parentViewId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        pure_sketch = d.pop("pureSketch", UNSET)

        reference_type = d.pop("referenceType", UNSET)

        return_error = d.pop("returnError", UNSET)

        revision = d.pop("revision", UNSET)

        sketch_ids = cast(list[str], d.pop("sketchIds", UNSET))

        target_configuration = d.pop("targetConfiguration", UNSET)

        target_document_id = d.pop("targetDocumentId", UNSET)

        target_element_id = d.pop("targetElementId", UNSET)

        target_microversion_id = d.pop("targetMicroversionId", UNSET)

        target_version_id = d.pop("targetVersionId", UNSET)

        track_new_versions = d.pop("trackNewVersions", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        update_sketch_info = d.pop("updateSketchInfo", UNSET)

        bt_app_element_reference_params = cls(
            has_document_microversions=has_document_microversions,
            id_tag=id_tag,
            id_tag_microversion_id=id_tag_microversion_id,
            is_locked=is_locked,
            is_sketch_only=is_sketch_only,
            parent_change_id=parent_change_id,
            parent_view_id=parent_view_id,
            part_number=part_number,
            pure_sketch=pure_sketch,
            reference_type=reference_type,
            return_error=return_error,
            revision=revision,
            sketch_ids=sketch_ids,
            target_configuration=target_configuration,
            target_document_id=target_document_id,
            target_element_id=target_element_id,
            target_microversion_id=target_microversion_id,
            target_version_id=target_version_id,
            track_new_versions=track_new_versions,
            transaction_id=transaction_id,
            update_sketch_info=update_sketch_info,
        )

        bt_app_element_reference_params.additional_properties = d
        return bt_app_element_reference_params

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
