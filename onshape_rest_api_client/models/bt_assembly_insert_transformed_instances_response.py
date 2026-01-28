from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_instance_occurrence_info import BTAssemblyInstanceOccurrenceInfo
    from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo


T = TypeVar("T", bound="BTAssemblyInsertTransformedInstancesResponse")


@_attrs_define
class BTAssemblyInsertTransformedInstancesResponse:
    """
    Attributes:
        insert_instance_responses (list[BTAssemblyInstanceOccurrenceInfo] | Unset):
        insert_responses (list[BTAssemblyOccurrenceInfo] | Unset):
    """

    insert_instance_responses: list[BTAssemblyInstanceOccurrenceInfo] | Unset = UNSET
    insert_responses: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        insert_instance_responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.insert_instance_responses, Unset):
            insert_instance_responses = []
            for insert_instance_responses_item_data in self.insert_instance_responses:
                insert_instance_responses_item = insert_instance_responses_item_data.to_dict()
                insert_instance_responses.append(insert_instance_responses_item)

        insert_responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.insert_responses, Unset):
            insert_responses = []
            for insert_responses_item_data in self.insert_responses:
                insert_responses_item = insert_responses_item_data.to_dict()
                insert_responses.append(insert_responses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if insert_instance_responses is not UNSET:
            field_dict["insertInstanceResponses"] = insert_instance_responses
        if insert_responses is not UNSET:
            field_dict["insertResponses"] = insert_responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_instance_occurrence_info import BTAssemblyInstanceOccurrenceInfo
        from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo

        d = dict(src_dict)
        _insert_instance_responses = d.pop("insertInstanceResponses", UNSET)
        insert_instance_responses: list[BTAssemblyInstanceOccurrenceInfo] | Unset = UNSET
        if _insert_instance_responses is not UNSET:
            insert_instance_responses = []
            for insert_instance_responses_item_data in _insert_instance_responses:
                insert_instance_responses_item = BTAssemblyInstanceOccurrenceInfo.from_dict(
                    insert_instance_responses_item_data
                )

                insert_instance_responses.append(insert_instance_responses_item)

        _insert_responses = d.pop("insertResponses", UNSET)
        insert_responses: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
        if _insert_responses is not UNSET:
            insert_responses = []
            for insert_responses_item_data in _insert_responses:
                insert_responses_item = BTAssemblyOccurrenceInfo.from_dict(insert_responses_item_data)

                insert_responses.append(insert_responses_item)

        bt_assembly_insert_transformed_instances_response = cls(
            insert_instance_responses=insert_instance_responses,
            insert_responses=insert_responses,
        )

        bt_assembly_insert_transformed_instances_response.additional_properties = d
        return bt_assembly_insert_transformed_instances_response

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
