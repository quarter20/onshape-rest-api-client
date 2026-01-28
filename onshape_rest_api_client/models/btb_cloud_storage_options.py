from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BTBCloudStorageOptions")


@_attrs_define
class BTBCloudStorageOptions:
    """Options for exporting elements to cloud storage.

    Attributes:
        cloud_object_id (str): Folder id where to store the exported model.
        cloud_storage_account_id (str): Account id to access the cloud storage.
    """

    cloud_object_id: str
    cloud_storage_account_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_object_id = self.cloud_object_id

        cloud_storage_account_id = self.cloud_storage_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloudObjectId": cloud_object_id,
                "cloudStorageAccountId": cloud_storage_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_object_id = d.pop("cloudObjectId")

        cloud_storage_account_id = d.pop("cloudStorageAccountId")

        btb_cloud_storage_options = cls(
            cloud_object_id=cloud_object_id,
            cloud_storage_account_id=cloud_storage_account_id,
        )

        btb_cloud_storage_options.additional_properties = d
        return btb_cloud_storage_options

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
