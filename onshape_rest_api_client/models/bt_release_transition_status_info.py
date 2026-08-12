from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_release_stage import BTReleaseStage
from ..models.bt_release_summary_state import BTReleaseSummaryState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTReleaseTransitionStatusInfo")


@_attrs_define
class BTReleaseTransitionStatusInfo:
    """
    Attributes:
        error_message (str | Unset):
        last_stage (BTReleaseStage | Unset):
        last_updated_at (datetime.datetime | Unset):
        retryable (bool | Unset):
        summary_state (BTReleaseSummaryState | Unset):
        support_code (str | Unset):
    """

    error_message: str | Unset = UNSET
    last_stage: BTReleaseStage | Unset = UNSET
    last_updated_at: datetime.datetime | Unset = UNSET
    retryable: bool | Unset = UNSET
    summary_state: BTReleaseSummaryState | Unset = UNSET
    support_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        last_stage: str | Unset = UNSET
        if not isinstance(self.last_stage, Unset):
            last_stage = self.last_stage.value

        last_updated_at: str | Unset = UNSET
        if not isinstance(self.last_updated_at, Unset):
            last_updated_at = self.last_updated_at.isoformat()

        retryable = self.retryable

        summary_state: str | Unset = UNSET
        if not isinstance(self.summary_state, Unset):
            summary_state = self.summary_state.value

        support_code = self.support_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if last_stage is not UNSET:
            field_dict["lastStage"] = last_stage
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if retryable is not UNSET:
            field_dict["retryable"] = retryable
        if summary_state is not UNSET:
            field_dict["summaryState"] = summary_state
        if support_code is not UNSET:
            field_dict["supportCode"] = support_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        _last_stage = d.pop("lastStage", UNSET)
        last_stage: BTReleaseStage | Unset
        if isinstance(_last_stage, Unset):
            last_stage = UNSET
        else:
            last_stage = BTReleaseStage(_last_stage)

        _last_updated_at = d.pop("lastUpdatedAt", UNSET)
        last_updated_at: datetime.datetime | Unset
        if isinstance(_last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = datetime.datetime.fromisoformat(_last_updated_at)

        retryable = d.pop("retryable", UNSET)

        _summary_state = d.pop("summaryState", UNSET)
        summary_state: BTReleaseSummaryState | Unset
        if isinstance(_summary_state, Unset):
            summary_state = UNSET
        else:
            summary_state = BTReleaseSummaryState(_summary_state)

        support_code = d.pop("supportCode", UNSET)

        bt_release_transition_status_info = cls(
            error_message=error_message,
            last_stage=last_stage,
            last_updated_at=last_updated_at,
            retryable=retryable,
            summary_state=summary_state,
            support_code=support_code,
        )

        bt_release_transition_status_info.additional_properties = d
        return bt_release_transition_status_info

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
