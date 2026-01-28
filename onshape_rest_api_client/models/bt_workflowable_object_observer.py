from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_workflow_observer_entry_type import BTWorkflowObserverEntryType
from ..models.bt_workflow_observer_state import BTWorkflowObserverState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWorkflowableObjectObserver")


@_attrs_define
class BTWorkflowableObjectObserver:
    """
    Attributes:
        admin_override (bool | Unset):
        approval_date (datetime.datetime | Unset):
        approval_state (BTWorkflowObserverState | Unset):
        approver_id (str | Unset):
        approver_name (str | Unset):
        associated_states (str | Unset):
        company_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by (str | Unset):
        creator_override (bool | Unset):
        description (str | Unset):
        entry_id (str | Unset):
        entry_type (BTWorkflowObserverEntryType | Unset):
        id (str | Unset):
        is_external (bool | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (str | Unset):
        name (str | Unset):
        new (bool | Unset):
        object_id (str | Unset):
        observation_type (int | Unset):
        property_id (str | Unset):
        rejection_date (datetime.datetime | Unset):
        removable (bool | Unset):
    """

    admin_override: bool | Unset = UNSET
    approval_date: datetime.datetime | Unset = UNSET
    approval_state: BTWorkflowObserverState | Unset = UNSET
    approver_id: str | Unset = UNSET
    approver_name: str | Unset = UNSET
    associated_states: str | Unset = UNSET
    company_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    creator_override: bool | Unset = UNSET
    description: str | Unset = UNSET
    entry_id: str | Unset = UNSET
    entry_type: BTWorkflowObserverEntryType | Unset = UNSET
    id: str | Unset = UNSET
    is_external: bool | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    name: str | Unset = UNSET
    new: bool | Unset = UNSET
    object_id: str | Unset = UNSET
    observation_type: int | Unset = UNSET
    property_id: str | Unset = UNSET
    rejection_date: datetime.datetime | Unset = UNSET
    removable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_override = self.admin_override

        approval_date: str | Unset = UNSET
        if not isinstance(self.approval_date, Unset):
            approval_date = self.approval_date.isoformat()

        approval_state: str | Unset = UNSET
        if not isinstance(self.approval_state, Unset):
            approval_state = self.approval_state.value

        approver_id = self.approver_id

        approver_name = self.approver_name

        associated_states = self.associated_states

        company_id = self.company_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        creator_override = self.creator_override

        description = self.description

        entry_id = self.entry_id

        entry_type: str | Unset = UNSET
        if not isinstance(self.entry_type, Unset):
            entry_type = self.entry_type.value

        id = self.id

        is_external = self.is_external

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        name = self.name

        new = self.new

        object_id = self.object_id

        observation_type = self.observation_type

        property_id = self.property_id

        rejection_date: str | Unset = UNSET
        if not isinstance(self.rejection_date, Unset):
            rejection_date = self.rejection_date.isoformat()

        removable = self.removable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_override is not UNSET:
            field_dict["adminOverride"] = admin_override
        if approval_date is not UNSET:
            field_dict["approvalDate"] = approval_date
        if approval_state is not UNSET:
            field_dict["approvalState"] = approval_state
        if approver_id is not UNSET:
            field_dict["approverId"] = approver_id
        if approver_name is not UNSET:
            field_dict["approverName"] = approver_name
        if associated_states is not UNSET:
            field_dict["associatedStates"] = associated_states
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if creator_override is not UNSET:
            field_dict["creatorOverride"] = creator_override
        if description is not UNSET:
            field_dict["description"] = description
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if id is not UNSET:
            field_dict["id"] = id
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if new is not UNSET:
            field_dict["new"] = new
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if observation_type is not UNSET:
            field_dict["observationType"] = observation_type
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if rejection_date is not UNSET:
            field_dict["rejectionDate"] = rejection_date
        if removable is not UNSET:
            field_dict["removable"] = removable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_override = d.pop("adminOverride", UNSET)

        _approval_date = d.pop("approvalDate", UNSET)
        approval_date: datetime.datetime | Unset
        if isinstance(_approval_date, Unset):
            approval_date = UNSET
        else:
            approval_date = isoparse(_approval_date)

        _approval_state = d.pop("approvalState", UNSET)
        approval_state: BTWorkflowObserverState | Unset
        if isinstance(_approval_state, Unset):
            approval_state = UNSET
        else:
            approval_state = BTWorkflowObserverState(_approval_state)

        approver_id = d.pop("approverId", UNSET)

        approver_name = d.pop("approverName", UNSET)

        associated_states = d.pop("associatedStates", UNSET)

        company_id = d.pop("companyId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        creator_override = d.pop("creatorOverride", UNSET)

        description = d.pop("description", UNSET)

        entry_id = d.pop("entryId", UNSET)

        _entry_type = d.pop("entryType", UNSET)
        entry_type: BTWorkflowObserverEntryType | Unset
        if isinstance(_entry_type, Unset):
            entry_type = UNSET
        else:
            entry_type = BTWorkflowObserverEntryType(_entry_type)

        id = d.pop("id", UNSET)

        is_external = d.pop("isExternal", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        modified_by = d.pop("modifiedBy", UNSET)

        name = d.pop("name", UNSET)

        new = d.pop("new", UNSET)

        object_id = d.pop("objectId", UNSET)

        observation_type = d.pop("observationType", UNSET)

        property_id = d.pop("propertyId", UNSET)

        _rejection_date = d.pop("rejectionDate", UNSET)
        rejection_date: datetime.datetime | Unset
        if isinstance(_rejection_date, Unset):
            rejection_date = UNSET
        else:
            rejection_date = isoparse(_rejection_date)

        removable = d.pop("removable", UNSET)

        bt_workflowable_object_observer = cls(
            admin_override=admin_override,
            approval_date=approval_date,
            approval_state=approval_state,
            approver_id=approver_id,
            approver_name=approver_name,
            associated_states=associated_states,
            company_id=company_id,
            created_at=created_at,
            created_by=created_by,
            creator_override=creator_override,
            description=description,
            entry_id=entry_id,
            entry_type=entry_type,
            id=id,
            is_external=is_external,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            new=new,
            object_id=object_id,
            observation_type=observation_type,
            property_id=property_id,
            rejection_date=rejection_date,
            removable=removable,
        )

        bt_workflowable_object_observer.additional_properties = d
        return bt_workflowable_object_observer

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
