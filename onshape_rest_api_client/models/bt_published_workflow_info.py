from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPublishedWorkflowInfo")


@_attrs_define
class BTPublishedWorkflowInfo:
    """Captures information about a published workflow

    Attributes:
        active_state (int | Unset):
        company_id (str | Unset):
        description (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        id (str | Unset):
        image_src (str | Unset):
        is_pickable (bool | Unset):
        json (str | Unset):
        name (str | Unset):
        object_type (int | Unset):
        owner_type (int | Unset):
        published_date (datetime.datetime | Unset): The date of publication of workflow
        uses_external_plm (bool | Unset): Whether the workflow connects to an external PLM service like Arena
        version_id (str | Unset):
    """

    active_state: int | Unset = UNSET
    company_id: str | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    id: str | Unset = UNSET
    image_src: str | Unset = UNSET
    is_pickable: bool | Unset = UNSET
    json: str | Unset = UNSET
    name: str | Unset = UNSET
    object_type: int | Unset = UNSET
    owner_type: int | Unset = UNSET
    published_date: datetime.datetime | Unset = UNSET
    uses_external_plm: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_state = self.active_state

        company_id = self.company_id

        description = self.description

        document_id = self.document_id

        element_id = self.element_id

        id = self.id

        image_src = self.image_src

        is_pickable = self.is_pickable

        json = self.json

        name = self.name

        object_type = self.object_type

        owner_type = self.owner_type

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        uses_external_plm = self.uses_external_plm

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_state is not UNSET:
            field_dict["activeState"] = active_state
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if id is not UNSET:
            field_dict["id"] = id
        if image_src is not UNSET:
            field_dict["imageSrc"] = image_src
        if is_pickable is not UNSET:
            field_dict["isPickable"] = is_pickable
        if json is not UNSET:
            field_dict["json"] = json
        if name is not UNSET:
            field_dict["name"] = name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if uses_external_plm is not UNSET:
            field_dict["usesExternalPlm"] = uses_external_plm
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_state = d.pop("activeState", UNSET)

        company_id = d.pop("companyId", UNSET)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        id = d.pop("id", UNSET)

        image_src = d.pop("imageSrc", UNSET)

        is_pickable = d.pop("isPickable", UNSET)

        json = d.pop("json", UNSET)

        name = d.pop("name", UNSET)

        object_type = d.pop("objectType", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.datetime | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = isoparse(_published_date)

        uses_external_plm = d.pop("usesExternalPlm", UNSET)

        version_id = d.pop("versionId", UNSET)

        bt_published_workflow_info = cls(
            active_state=active_state,
            company_id=company_id,
            description=description,
            document_id=document_id,
            element_id=element_id,
            id=id,
            image_src=image_src,
            is_pickable=is_pickable,
            json=json,
            name=name,
            object_type=object_type,
            owner_type=owner_type,
            published_date=published_date,
            uses_external_plm=uses_external_plm,
            version_id=version_id,
        )

        bt_published_workflow_info.additional_properties = d
        return bt_published_workflow_info

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
