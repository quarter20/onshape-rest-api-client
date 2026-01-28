from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.gbt_element_branch_status import GBTElementBranchStatus
from ..models.gbt_element_type import GBTElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTElementMergeInfo")


@_attrs_define
class BTElementMergeInfo:
    """
    Attributes:
        branch_point_element_name (str | Unset):
        branch_point_element_path (list[str] | Unset):
        dependent_element_merge_info (BTElementMergeInfo | Unset):
        element_data_type (str | Unset):
        element_id (str | Unset):
        element_type (GBTElementType | Unset):
        mergeable (bool | Unset):
        source_element_name (str | Unset):
        source_element_path (list[str] | Unset):
        source_element_status (GBTElementBranchStatus | Unset):
        source_library_version (int | Unset):
        source_modified_at (datetime.datetime | Unset):
        source_modified_by (BTUserBasicSummaryInfo | Unset):
        source_out_of_date (bool | Unset):
        target_element_name (str | Unset):
        target_element_path (list[str] | Unset):
        target_element_status (GBTElementBranchStatus | Unset):
        target_library_version (int | Unset):
        target_modified_at (datetime.datetime | Unset):
        target_modified_by (BTUserBasicSummaryInfo | Unset):
        target_out_of_date (bool | Unset):
        version_compatible (bool | Unset):
    """

    branch_point_element_name: str | Unset = UNSET
    branch_point_element_path: list[str] | Unset = UNSET
    dependent_element_merge_info: BTElementMergeInfo | Unset = UNSET
    element_data_type: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: GBTElementType | Unset = UNSET
    mergeable: bool | Unset = UNSET
    source_element_name: str | Unset = UNSET
    source_element_path: list[str] | Unset = UNSET
    source_element_status: GBTElementBranchStatus | Unset = UNSET
    source_library_version: int | Unset = UNSET
    source_modified_at: datetime.datetime | Unset = UNSET
    source_modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    source_out_of_date: bool | Unset = UNSET
    target_element_name: str | Unset = UNSET
    target_element_path: list[str] | Unset = UNSET
    target_element_status: GBTElementBranchStatus | Unset = UNSET
    target_library_version: int | Unset = UNSET
    target_modified_at: datetime.datetime | Unset = UNSET
    target_modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    target_out_of_date: bool | Unset = UNSET
    version_compatible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_point_element_name = self.branch_point_element_name

        branch_point_element_path: list[str] | Unset = UNSET
        if not isinstance(self.branch_point_element_path, Unset):
            branch_point_element_path = self.branch_point_element_path

        dependent_element_merge_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependent_element_merge_info, Unset):
            dependent_element_merge_info = self.dependent_element_merge_info.to_dict()

        element_data_type = self.element_data_type

        element_id = self.element_id

        element_type: str | Unset = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.value

        mergeable = self.mergeable

        source_element_name = self.source_element_name

        source_element_path: list[str] | Unset = UNSET
        if not isinstance(self.source_element_path, Unset):
            source_element_path = self.source_element_path

        source_element_status: str | Unset = UNSET
        if not isinstance(self.source_element_status, Unset):
            source_element_status = self.source_element_status.value

        source_library_version = self.source_library_version

        source_modified_at: str | Unset = UNSET
        if not isinstance(self.source_modified_at, Unset):
            source_modified_at = self.source_modified_at.isoformat()

        source_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_modified_by, Unset):
            source_modified_by = self.source_modified_by.to_dict()

        source_out_of_date = self.source_out_of_date

        target_element_name = self.target_element_name

        target_element_path: list[str] | Unset = UNSET
        if not isinstance(self.target_element_path, Unset):
            target_element_path = self.target_element_path

        target_element_status: str | Unset = UNSET
        if not isinstance(self.target_element_status, Unset):
            target_element_status = self.target_element_status.value

        target_library_version = self.target_library_version

        target_modified_at: str | Unset = UNSET
        if not isinstance(self.target_modified_at, Unset):
            target_modified_at = self.target_modified_at.isoformat()

        target_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_modified_by, Unset):
            target_modified_by = self.target_modified_by.to_dict()

        target_out_of_date = self.target_out_of_date

        version_compatible = self.version_compatible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_point_element_name is not UNSET:
            field_dict["branchPointElementName"] = branch_point_element_name
        if branch_point_element_path is not UNSET:
            field_dict["branchPointElementPath"] = branch_point_element_path
        if dependent_element_merge_info is not UNSET:
            field_dict["dependentElementMergeInfo"] = dependent_element_merge_info
        if element_data_type is not UNSET:
            field_dict["elementDataType"] = element_data_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if mergeable is not UNSET:
            field_dict["mergeable"] = mergeable
        if source_element_name is not UNSET:
            field_dict["sourceElementName"] = source_element_name
        if source_element_path is not UNSET:
            field_dict["sourceElementPath"] = source_element_path
        if source_element_status is not UNSET:
            field_dict["sourceElementStatus"] = source_element_status
        if source_library_version is not UNSET:
            field_dict["sourceLibraryVersion"] = source_library_version
        if source_modified_at is not UNSET:
            field_dict["sourceModifiedAt"] = source_modified_at
        if source_modified_by is not UNSET:
            field_dict["sourceModifiedBy"] = source_modified_by
        if source_out_of_date is not UNSET:
            field_dict["sourceOutOfDate"] = source_out_of_date
        if target_element_name is not UNSET:
            field_dict["targetElementName"] = target_element_name
        if target_element_path is not UNSET:
            field_dict["targetElementPath"] = target_element_path
        if target_element_status is not UNSET:
            field_dict["targetElementStatus"] = target_element_status
        if target_library_version is not UNSET:
            field_dict["targetLibraryVersion"] = target_library_version
        if target_modified_at is not UNSET:
            field_dict["targetModifiedAt"] = target_modified_at
        if target_modified_by is not UNSET:
            field_dict["targetModifiedBy"] = target_modified_by
        if target_out_of_date is not UNSET:
            field_dict["targetOutOfDate"] = target_out_of_date
        if version_compatible is not UNSET:
            field_dict["versionCompatible"] = version_compatible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

        d = dict(src_dict)
        branch_point_element_name = d.pop("branchPointElementName", UNSET)

        branch_point_element_path = cast(list[str], d.pop("branchPointElementPath", UNSET))

        _dependent_element_merge_info = d.pop("dependentElementMergeInfo", UNSET)
        dependent_element_merge_info: BTElementMergeInfo | Unset
        if isinstance(_dependent_element_merge_info, Unset):
            dependent_element_merge_info = UNSET
        else:
            dependent_element_merge_info = BTElementMergeInfo.from_dict(_dependent_element_merge_info)

        element_data_type = d.pop("elementDataType", UNSET)

        element_id = d.pop("elementId", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: GBTElementType | Unset
        if isinstance(_element_type, Unset):
            element_type = UNSET
        else:
            element_type = GBTElementType(_element_type)

        mergeable = d.pop("mergeable", UNSET)

        source_element_name = d.pop("sourceElementName", UNSET)

        source_element_path = cast(list[str], d.pop("sourceElementPath", UNSET))

        _source_element_status = d.pop("sourceElementStatus", UNSET)
        source_element_status: GBTElementBranchStatus | Unset
        if isinstance(_source_element_status, Unset):
            source_element_status = UNSET
        else:
            source_element_status = GBTElementBranchStatus(_source_element_status)

        source_library_version = d.pop("sourceLibraryVersion", UNSET)

        _source_modified_at = d.pop("sourceModifiedAt", UNSET)
        source_modified_at: datetime.datetime | Unset
        if isinstance(_source_modified_at, Unset):
            source_modified_at = UNSET
        else:
            source_modified_at = isoparse(_source_modified_at)

        _source_modified_by = d.pop("sourceModifiedBy", UNSET)
        source_modified_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_source_modified_by, Unset):
            source_modified_by = UNSET
        else:
            source_modified_by = BTUserBasicSummaryInfo.from_dict(_source_modified_by)

        source_out_of_date = d.pop("sourceOutOfDate", UNSET)

        target_element_name = d.pop("targetElementName", UNSET)

        target_element_path = cast(list[str], d.pop("targetElementPath", UNSET))

        _target_element_status = d.pop("targetElementStatus", UNSET)
        target_element_status: GBTElementBranchStatus | Unset
        if isinstance(_target_element_status, Unset):
            target_element_status = UNSET
        else:
            target_element_status = GBTElementBranchStatus(_target_element_status)

        target_library_version = d.pop("targetLibraryVersion", UNSET)

        _target_modified_at = d.pop("targetModifiedAt", UNSET)
        target_modified_at: datetime.datetime | Unset
        if isinstance(_target_modified_at, Unset):
            target_modified_at = UNSET
        else:
            target_modified_at = isoparse(_target_modified_at)

        _target_modified_by = d.pop("targetModifiedBy", UNSET)
        target_modified_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_target_modified_by, Unset):
            target_modified_by = UNSET
        else:
            target_modified_by = BTUserBasicSummaryInfo.from_dict(_target_modified_by)

        target_out_of_date = d.pop("targetOutOfDate", UNSET)

        version_compatible = d.pop("versionCompatible", UNSET)

        bt_element_merge_info = cls(
            branch_point_element_name=branch_point_element_name,
            branch_point_element_path=branch_point_element_path,
            dependent_element_merge_info=dependent_element_merge_info,
            element_data_type=element_data_type,
            element_id=element_id,
            element_type=element_type,
            mergeable=mergeable,
            source_element_name=source_element_name,
            source_element_path=source_element_path,
            source_element_status=source_element_status,
            source_library_version=source_library_version,
            source_modified_at=source_modified_at,
            source_modified_by=source_modified_by,
            source_out_of_date=source_out_of_date,
            target_element_name=target_element_name,
            target_element_path=target_element_path,
            target_element_status=target_element_status,
            target_library_version=target_library_version,
            target_modified_at=target_modified_at,
            target_modified_by=target_modified_by,
            target_out_of_date=target_out_of_date,
            version_compatible=version_compatible,
        )

        bt_element_merge_info.additional_properties = d
        return bt_element_merge_info

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
