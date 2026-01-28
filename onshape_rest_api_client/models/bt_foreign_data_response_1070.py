from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_data_item_format import GBTDataItemFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTForeignDataResponse1070")


@_attrs_define
class BTForeignDataResponse1070:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        bucket_name (str | Unset):
        bucket_path (str | Unset):
        cache_chunk_list (list[str] | Unset):
        data_id (str | Unset):
        format_ (GBTDataItemFormat | Unset):
        name (str | Unset):
        region (str | Unset):
        size (int | Unset):
        storage_type (str | Unset):
        use_local_storage (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    bucket_name: str | Unset = UNSET
    bucket_path: str | Unset = UNSET
    cache_chunk_list: list[str] | Unset = UNSET
    data_id: str | Unset = UNSET
    format_: GBTDataItemFormat | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    size: int | Unset = UNSET
    storage_type: str | Unset = UNSET
    use_local_storage: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        bucket_name = self.bucket_name

        bucket_path = self.bucket_path

        cache_chunk_list: list[str] | Unset = UNSET
        if not isinstance(self.cache_chunk_list, Unset):
            cache_chunk_list = self.cache_chunk_list

        data_id = self.data_id

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        name = self.name

        region = self.region

        size = self.size

        storage_type = self.storage_type

        use_local_storage = self.use_local_storage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if bucket_name is not UNSET:
            field_dict["bucketName"] = bucket_name
        if bucket_path is not UNSET:
            field_dict["bucketPath"] = bucket_path
        if cache_chunk_list is not UNSET:
            field_dict["cacheChunkList"] = cache_chunk_list
        if data_id is not UNSET:
            field_dict["dataId"] = data_id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if size is not UNSET:
            field_dict["size"] = size
        if storage_type is not UNSET:
            field_dict["storageType"] = storage_type
        if use_local_storage is not UNSET:
            field_dict["useLocalStorage"] = use_local_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        bucket_name = d.pop("bucketName", UNSET)

        bucket_path = d.pop("bucketPath", UNSET)

        cache_chunk_list = cast(list[str], d.pop("cacheChunkList", UNSET))

        data_id = d.pop("dataId", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: GBTDataItemFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = GBTDataItemFormat(_format_)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        size = d.pop("size", UNSET)

        storage_type = d.pop("storageType", UNSET)

        use_local_storage = d.pop("useLocalStorage", UNSET)

        bt_foreign_data_response_1070 = cls(
            bt_type=bt_type,
            bucket_name=bucket_name,
            bucket_path=bucket_path,
            cache_chunk_list=cache_chunk_list,
            data_id=data_id,
            format_=format_,
            name=name,
            region=region,
            size=size,
            storage_type=storage_type,
            use_local_storage=use_local_storage,
        )

        bt_foreign_data_response_1070.additional_properties = d
        return bt_foreign_data_response_1070

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
