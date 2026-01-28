from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo


T = TypeVar("T", bound="BTActiveWorkflowTypeInfo")


@_attrs_define
class BTActiveWorkflowTypeInfo:
    """
    Attributes:
        has_inactive_custom_workflows (bool | Unset):
        pickable_workflows (list[BTPublishedWorkflowInfo] | Unset):
        workflow (BTPublishedWorkflowInfo | Unset): Captures information about a published workflow
    """

    has_inactive_custom_workflows: bool | Unset = UNSET
    pickable_workflows: list[BTPublishedWorkflowInfo] | Unset = UNSET
    workflow: BTPublishedWorkflowInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_inactive_custom_workflows = self.has_inactive_custom_workflows

        pickable_workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pickable_workflows, Unset):
            pickable_workflows = []
            for pickable_workflows_item_data in self.pickable_workflows:
                pickable_workflows_item = pickable_workflows_item_data.to_dict()
                pickable_workflows.append(pickable_workflows_item)

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_inactive_custom_workflows is not UNSET:
            field_dict["hasInactiveCustomWorkflows"] = has_inactive_custom_workflows
        if pickable_workflows is not UNSET:
            field_dict["pickableWorkflows"] = pickable_workflows
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo

        d = dict(src_dict)
        has_inactive_custom_workflows = d.pop("hasInactiveCustomWorkflows", UNSET)

        _pickable_workflows = d.pop("pickableWorkflows", UNSET)
        pickable_workflows: list[BTPublishedWorkflowInfo] | Unset = UNSET
        if _pickable_workflows is not UNSET:
            pickable_workflows = []
            for pickable_workflows_item_data in _pickable_workflows:
                pickable_workflows_item = BTPublishedWorkflowInfo.from_dict(pickable_workflows_item_data)

                pickable_workflows.append(pickable_workflows_item)

        _workflow = d.pop("workflow", UNSET)
        workflow: BTPublishedWorkflowInfo | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = BTPublishedWorkflowInfo.from_dict(_workflow)

        bt_active_workflow_type_info = cls(
            has_inactive_custom_workflows=has_inactive_custom_workflows,
            pickable_workflows=pickable_workflows,
            workflow=workflow,
        )

        bt_active_workflow_type_info.additional_properties = d
        return bt_active_workflow_type_info

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
