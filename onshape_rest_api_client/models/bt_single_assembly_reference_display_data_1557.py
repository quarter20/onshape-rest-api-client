from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..models.gbtbs_feature_visibility import GBTBSFeatureVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_context_named_position_info_3801 import BTAssemblyContextNamedPositionInfo3801
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.bt_root_assembly_display_data_96 import BTRootAssemblyDisplayData96
    from ..models.btbs_matrix_386 import BTBSMatrix386


T = TypeVar("T", bound="BTSingleAssemblyReferenceDisplayData1557")


@_attrs_define
class BTSingleAssemblyReferenceDisplayData1557:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        context_workspace_id (str | Unset):
        document_id (str | Unset):
        error (GBTErrorStringEnum | Unset):
        error_message (str | Unset):
        full_element_id (BTFullElementId756 | Unset):
        is_transient (bool | Unset):
        name (str | Unset):
        reference_name (str | Unset):
        reference_node_id (str | Unset):
        visibility (GBTBSFeatureVisibility | Unset):
        assembly_display_data (BTRootAssemblyDisplayData96 | Unset):
        assembly_named_positions (list[BTAssemblyContextNamedPositionInfo3801] | Unset):
        has_configuration (bool | Unset):
        occurrences_to_exclude (list[BTOccurrence74] | Unset):
        selected_named_position_id (str | Unset):
        transform (BTBSMatrix386 | Unset):
    """

    bt_type: str | Unset = UNSET
    context_workspace_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    error: GBTErrorStringEnum | Unset = UNSET
    error_message: str | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    is_transient: bool | Unset = UNSET
    name: str | Unset = UNSET
    reference_name: str | Unset = UNSET
    reference_node_id: str | Unset = UNSET
    visibility: GBTBSFeatureVisibility | Unset = UNSET
    assembly_display_data: BTRootAssemblyDisplayData96 | Unset = UNSET
    assembly_named_positions: list[BTAssemblyContextNamedPositionInfo3801] | Unset = UNSET
    has_configuration: bool | Unset = UNSET
    occurrences_to_exclude: list[BTOccurrence74] | Unset = UNSET
    selected_named_position_id: str | Unset = UNSET
    transform: BTBSMatrix386 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        context_workspace_id = self.context_workspace_id

        document_id = self.document_id

        error: str | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        error_message = self.error_message

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        is_transient = self.is_transient

        name = self.name

        reference_name = self.reference_name

        reference_node_id = self.reference_node_id

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        assembly_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assembly_display_data, Unset):
            assembly_display_data = self.assembly_display_data.to_dict()

        assembly_named_positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assembly_named_positions, Unset):
            assembly_named_positions = []
            for assembly_named_positions_item_data in self.assembly_named_positions:
                assembly_named_positions_item = assembly_named_positions_item_data.to_dict()
                assembly_named_positions.append(assembly_named_positions_item)

        has_configuration = self.has_configuration

        occurrences_to_exclude: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences_to_exclude, Unset):
            occurrences_to_exclude = []
            for occurrences_to_exclude_item_data in self.occurrences_to_exclude:
                occurrences_to_exclude_item = occurrences_to_exclude_item_data.to_dict()
                occurrences_to_exclude.append(occurrences_to_exclude_item)

        selected_named_position_id = self.selected_named_position_id

        transform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = self.transform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if context_workspace_id is not UNSET:
            field_dict["contextWorkspaceId"] = context_workspace_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if error is not UNSET:
            field_dict["error"] = error
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if is_transient is not UNSET:
            field_dict["isTransient"] = is_transient
        if name is not UNSET:
            field_dict["name"] = name
        if reference_name is not UNSET:
            field_dict["referenceName"] = reference_name
        if reference_node_id is not UNSET:
            field_dict["referenceNodeId"] = reference_node_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if assembly_display_data is not UNSET:
            field_dict["assemblyDisplayData"] = assembly_display_data
        if assembly_named_positions is not UNSET:
            field_dict["assemblyNamedPositions"] = assembly_named_positions
        if has_configuration is not UNSET:
            field_dict["hasConfiguration"] = has_configuration
        if occurrences_to_exclude is not UNSET:
            field_dict["occurrencesToExclude"] = occurrences_to_exclude
        if selected_named_position_id is not UNSET:
            field_dict["selectedNamedPositionId"] = selected_named_position_id
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_context_named_position_info_3801 import BTAssemblyContextNamedPositionInfo3801
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.bt_root_assembly_display_data_96 import BTRootAssemblyDisplayData96
        from ..models.btbs_matrix_386 import BTBSMatrix386

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        context_workspace_id = d.pop("contextWorkspaceId", UNSET)

        document_id = d.pop("documentId", UNSET)

        _error = d.pop("error", UNSET)
        error: GBTErrorStringEnum | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GBTErrorStringEnum(_error)

        error_message = d.pop("errorMessage", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        is_transient = d.pop("isTransient", UNSET)

        name = d.pop("name", UNSET)

        reference_name = d.pop("referenceName", UNSET)

        reference_node_id = d.pop("referenceNodeId", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTBSFeatureVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTBSFeatureVisibility(_visibility)

        _assembly_display_data = d.pop("assemblyDisplayData", UNSET)
        assembly_display_data: BTRootAssemblyDisplayData96 | Unset
        if isinstance(_assembly_display_data, Unset):
            assembly_display_data = UNSET
        else:
            assembly_display_data = BTRootAssemblyDisplayData96.from_dict(_assembly_display_data)

        _assembly_named_positions = d.pop("assemblyNamedPositions", UNSET)
        assembly_named_positions: list[BTAssemblyContextNamedPositionInfo3801] | Unset = UNSET
        if _assembly_named_positions is not UNSET:
            assembly_named_positions = []
            for assembly_named_positions_item_data in _assembly_named_positions:
                assembly_named_positions_item = BTAssemblyContextNamedPositionInfo3801.from_dict(
                    assembly_named_positions_item_data
                )

                assembly_named_positions.append(assembly_named_positions_item)

        has_configuration = d.pop("hasConfiguration", UNSET)

        _occurrences_to_exclude = d.pop("occurrencesToExclude", UNSET)
        occurrences_to_exclude: list[BTOccurrence74] | Unset = UNSET
        if _occurrences_to_exclude is not UNSET:
            occurrences_to_exclude = []
            for occurrences_to_exclude_item_data in _occurrences_to_exclude:
                occurrences_to_exclude_item = BTOccurrence74.from_dict(occurrences_to_exclude_item_data)

                occurrences_to_exclude.append(occurrences_to_exclude_item)

        selected_named_position_id = d.pop("selectedNamedPositionId", UNSET)

        _transform = d.pop("transform", UNSET)
        transform: BTBSMatrix386 | Unset
        if isinstance(_transform, Unset):
            transform = UNSET
        else:
            transform = BTBSMatrix386.from_dict(_transform)

        bt_single_assembly_reference_display_data_1557 = cls(
            bt_type=bt_type,
            context_workspace_id=context_workspace_id,
            document_id=document_id,
            error=error,
            error_message=error_message,
            full_element_id=full_element_id,
            is_transient=is_transient,
            name=name,
            reference_name=reference_name,
            reference_node_id=reference_node_id,
            visibility=visibility,
            assembly_display_data=assembly_display_data,
            assembly_named_positions=assembly_named_positions,
            has_configuration=has_configuration,
            occurrences_to_exclude=occurrences_to_exclude,
            selected_named_position_id=selected_named_position_id,
            transform=transform,
        )

        bt_single_assembly_reference_display_data_1557.additional_properties = d
        return bt_single_assembly_reference_display_data_1557

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
