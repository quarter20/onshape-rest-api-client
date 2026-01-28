from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPrivacyConsentInfo")


@_attrs_define
class BTPrivacyConsentInfo:
    """
    Attributes:
        communications_opt_in_date (datetime.datetime | Unset):
        communications_opt_out_date (datetime.datetime | Unset):
        communications_status (bool | Unset):
        consent_version (str | Unset):
        data_processing_opt_in_date (datetime.datetime | Unset):
        data_processing_opt_out_date (datetime.datetime | Unset):
        data_processing_status (bool | Unset):
        eula_version (int | Unset):
        user_id (str | Unset):
    """

    communications_opt_in_date: datetime.datetime | Unset = UNSET
    communications_opt_out_date: datetime.datetime | Unset = UNSET
    communications_status: bool | Unset = UNSET
    consent_version: str | Unset = UNSET
    data_processing_opt_in_date: datetime.datetime | Unset = UNSET
    data_processing_opt_out_date: datetime.datetime | Unset = UNSET
    data_processing_status: bool | Unset = UNSET
    eula_version: int | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communications_opt_in_date: str | Unset = UNSET
        if not isinstance(self.communications_opt_in_date, Unset):
            communications_opt_in_date = self.communications_opt_in_date.isoformat()

        communications_opt_out_date: str | Unset = UNSET
        if not isinstance(self.communications_opt_out_date, Unset):
            communications_opt_out_date = self.communications_opt_out_date.isoformat()

        communications_status = self.communications_status

        consent_version = self.consent_version

        data_processing_opt_in_date: str | Unset = UNSET
        if not isinstance(self.data_processing_opt_in_date, Unset):
            data_processing_opt_in_date = self.data_processing_opt_in_date.isoformat()

        data_processing_opt_out_date: str | Unset = UNSET
        if not isinstance(self.data_processing_opt_out_date, Unset):
            data_processing_opt_out_date = self.data_processing_opt_out_date.isoformat()

        data_processing_status = self.data_processing_status

        eula_version = self.eula_version

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communications_opt_in_date is not UNSET:
            field_dict["communicationsOptInDate"] = communications_opt_in_date
        if communications_opt_out_date is not UNSET:
            field_dict["communicationsOptOutDate"] = communications_opt_out_date
        if communications_status is not UNSET:
            field_dict["communicationsStatus"] = communications_status
        if consent_version is not UNSET:
            field_dict["consentVersion"] = consent_version
        if data_processing_opt_in_date is not UNSET:
            field_dict["dataProcessingOptInDate"] = data_processing_opt_in_date
        if data_processing_opt_out_date is not UNSET:
            field_dict["dataProcessingOptOutDate"] = data_processing_opt_out_date
        if data_processing_status is not UNSET:
            field_dict["dataProcessingStatus"] = data_processing_status
        if eula_version is not UNSET:
            field_dict["eulaVersion"] = eula_version
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _communications_opt_in_date = d.pop("communicationsOptInDate", UNSET)
        communications_opt_in_date: datetime.datetime | Unset
        if isinstance(_communications_opt_in_date, Unset):
            communications_opt_in_date = UNSET
        else:
            communications_opt_in_date = isoparse(_communications_opt_in_date)

        _communications_opt_out_date = d.pop("communicationsOptOutDate", UNSET)
        communications_opt_out_date: datetime.datetime | Unset
        if isinstance(_communications_opt_out_date, Unset):
            communications_opt_out_date = UNSET
        else:
            communications_opt_out_date = isoparse(_communications_opt_out_date)

        communications_status = d.pop("communicationsStatus", UNSET)

        consent_version = d.pop("consentVersion", UNSET)

        _data_processing_opt_in_date = d.pop("dataProcessingOptInDate", UNSET)
        data_processing_opt_in_date: datetime.datetime | Unset
        if isinstance(_data_processing_opt_in_date, Unset):
            data_processing_opt_in_date = UNSET
        else:
            data_processing_opt_in_date = isoparse(_data_processing_opt_in_date)

        _data_processing_opt_out_date = d.pop("dataProcessingOptOutDate", UNSET)
        data_processing_opt_out_date: datetime.datetime | Unset
        if isinstance(_data_processing_opt_out_date, Unset):
            data_processing_opt_out_date = UNSET
        else:
            data_processing_opt_out_date = isoparse(_data_processing_opt_out_date)

        data_processing_status = d.pop("dataProcessingStatus", UNSET)

        eula_version = d.pop("eulaVersion", UNSET)

        user_id = d.pop("userId", UNSET)

        bt_privacy_consent_info = cls(
            communications_opt_in_date=communications_opt_in_date,
            communications_opt_out_date=communications_opt_out_date,
            communications_status=communications_status,
            consent_version=consent_version,
            data_processing_opt_in_date=data_processing_opt_in_date,
            data_processing_opt_out_date=data_processing_opt_out_date,
            data_processing_status=data_processing_status,
            eula_version=eula_version,
            user_id=user_id,
        )

        bt_privacy_consent_info.additional_properties = d
        return bt_privacy_consent_info

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
