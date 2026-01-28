from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_item_metadata_info_property_id_to_error import BTAssemblyItemMetadataInfoPropertyIdToError
    from ..models.bt_assembly_item_metadata_info_property_id_to_eval_info import (
        BTAssemblyItemMetadataInfoPropertyIdToEvalInfo,
    )
    from ..models.bt_assembly_item_metadata_info_property_id_to_override_status import (
        BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus,
    )
    from ..models.bt_assembly_item_metadata_info_property_id_to_source_type import (
        BTAssemblyItemMetadataInfoPropertyIdToSourceType,
    )
    from ..models.bt_assembly_item_metadata_info_property_id_to_value import BTAssemblyItemMetadataInfoPropertyIdToValue
    from ..models.bt_assembly_item_metadata_request_info import BTAssemblyItemMetadataRequestInfo


T = TypeVar("T", bound="BTAssemblyItemMetadataInfo")


@_attrs_define
class BTAssemblyItemMetadataInfo:
    """
    Attributes:
        children (list[BTAssemblyItemMetadataInfo] | Unset):
        property_id_to_error (BTAssemblyItemMetadataInfoPropertyIdToError | Unset):
        property_id_to_eval_info (BTAssemblyItemMetadataInfoPropertyIdToEvalInfo | Unset):
        property_id_to_override_status (BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus | Unset):
        property_id_to_source_type (BTAssemblyItemMetadataInfoPropertyIdToSourceType | Unset):
        property_id_to_value (BTAssemblyItemMetadataInfoPropertyIdToValue | Unset):
        request_info (BTAssemblyItemMetadataRequestInfo | Unset):
    """

    children: list[BTAssemblyItemMetadataInfo] | Unset = UNSET
    property_id_to_error: BTAssemblyItemMetadataInfoPropertyIdToError | Unset = UNSET
    property_id_to_eval_info: BTAssemblyItemMetadataInfoPropertyIdToEvalInfo | Unset = UNSET
    property_id_to_override_status: BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus | Unset = UNSET
    property_id_to_source_type: BTAssemblyItemMetadataInfoPropertyIdToSourceType | Unset = UNSET
    property_id_to_value: BTAssemblyItemMetadataInfoPropertyIdToValue | Unset = UNSET
    request_info: BTAssemblyItemMetadataRequestInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        property_id_to_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_error, Unset):
            property_id_to_error = self.property_id_to_error.to_dict()

        property_id_to_eval_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_eval_info, Unset):
            property_id_to_eval_info = self.property_id_to_eval_info.to_dict()

        property_id_to_override_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_override_status, Unset):
            property_id_to_override_status = self.property_id_to_override_status.to_dict()

        property_id_to_source_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_source_type, Unset):
            property_id_to_source_type = self.property_id_to_source_type.to_dict()

        property_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_value, Unset):
            property_id_to_value = self.property_id_to_value.to_dict()

        request_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_info, Unset):
            request_info = self.request_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if property_id_to_error is not UNSET:
            field_dict["propertyIdToError"] = property_id_to_error
        if property_id_to_eval_info is not UNSET:
            field_dict["propertyIdToEvalInfo"] = property_id_to_eval_info
        if property_id_to_override_status is not UNSET:
            field_dict["propertyIdToOverrideStatus"] = property_id_to_override_status
        if property_id_to_source_type is not UNSET:
            field_dict["propertyIdToSourceType"] = property_id_to_source_type
        if property_id_to_value is not UNSET:
            field_dict["propertyIdToValue"] = property_id_to_value
        if request_info is not UNSET:
            field_dict["requestInfo"] = request_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_item_metadata_info_property_id_to_error import (
            BTAssemblyItemMetadataInfoPropertyIdToError,
        )
        from ..models.bt_assembly_item_metadata_info_property_id_to_eval_info import (
            BTAssemblyItemMetadataInfoPropertyIdToEvalInfo,
        )
        from ..models.bt_assembly_item_metadata_info_property_id_to_override_status import (
            BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus,
        )
        from ..models.bt_assembly_item_metadata_info_property_id_to_source_type import (
            BTAssemblyItemMetadataInfoPropertyIdToSourceType,
        )
        from ..models.bt_assembly_item_metadata_info_property_id_to_value import (
            BTAssemblyItemMetadataInfoPropertyIdToValue,
        )
        from ..models.bt_assembly_item_metadata_request_info import BTAssemblyItemMetadataRequestInfo

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: list[BTAssemblyItemMetadataInfo] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = BTAssemblyItemMetadataInfo.from_dict(children_item_data)

                children.append(children_item)

        _property_id_to_error = d.pop("propertyIdToError", UNSET)
        property_id_to_error: BTAssemblyItemMetadataInfoPropertyIdToError | Unset
        if isinstance(_property_id_to_error, Unset):
            property_id_to_error = UNSET
        else:
            property_id_to_error = BTAssemblyItemMetadataInfoPropertyIdToError.from_dict(_property_id_to_error)

        _property_id_to_eval_info = d.pop("propertyIdToEvalInfo", UNSET)
        property_id_to_eval_info: BTAssemblyItemMetadataInfoPropertyIdToEvalInfo | Unset
        if isinstance(_property_id_to_eval_info, Unset):
            property_id_to_eval_info = UNSET
        else:
            property_id_to_eval_info = BTAssemblyItemMetadataInfoPropertyIdToEvalInfo.from_dict(
                _property_id_to_eval_info
            )

        _property_id_to_override_status = d.pop("propertyIdToOverrideStatus", UNSET)
        property_id_to_override_status: BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus | Unset
        if isinstance(_property_id_to_override_status, Unset):
            property_id_to_override_status = UNSET
        else:
            property_id_to_override_status = BTAssemblyItemMetadataInfoPropertyIdToOverrideStatus.from_dict(
                _property_id_to_override_status
            )

        _property_id_to_source_type = d.pop("propertyIdToSourceType", UNSET)
        property_id_to_source_type: BTAssemblyItemMetadataInfoPropertyIdToSourceType | Unset
        if isinstance(_property_id_to_source_type, Unset):
            property_id_to_source_type = UNSET
        else:
            property_id_to_source_type = BTAssemblyItemMetadataInfoPropertyIdToSourceType.from_dict(
                _property_id_to_source_type
            )

        _property_id_to_value = d.pop("propertyIdToValue", UNSET)
        property_id_to_value: BTAssemblyItemMetadataInfoPropertyIdToValue | Unset
        if isinstance(_property_id_to_value, Unset):
            property_id_to_value = UNSET
        else:
            property_id_to_value = BTAssemblyItemMetadataInfoPropertyIdToValue.from_dict(_property_id_to_value)

        _request_info = d.pop("requestInfo", UNSET)
        request_info: BTAssemblyItemMetadataRequestInfo | Unset
        if isinstance(_request_info, Unset):
            request_info = UNSET
        else:
            request_info = BTAssemblyItemMetadataRequestInfo.from_dict(_request_info)

        bt_assembly_item_metadata_info = cls(
            children=children,
            property_id_to_error=property_id_to_error,
            property_id_to_eval_info=property_id_to_eval_info,
            property_id_to_override_status=property_id_to_override_status,
            property_id_to_source_type=property_id_to_source_type,
            property_id_to_value=property_id_to_value,
            request_info=request_info,
        )

        bt_assembly_item_metadata_info.additional_properties = d
        return bt_assembly_item_metadata_info

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
