from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPublishedWorkflowId")


@_attrs_define
class BTPublishedWorkflowId:
    """
    Attributes:
        company_id (str | Unset):
        version_id (str | Unset):
        workflow_id (str | Unset):
    """

    company_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        version_id = self.version_id

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        version_id = d.pop("versionId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        bt_published_workflow_id = cls(
            company_id=company_id,
            version_id=version_id,
            workflow_id=workflow_id,
        )

        bt_published_workflow_id.additional_properties = d
        return bt_published_workflow_id

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
