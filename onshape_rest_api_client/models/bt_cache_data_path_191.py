from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCacheDataPath191")


@_attrs_define
class BTCacheDataPath191:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        can_accept_new_context (bool | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        immutable_context_version (str | Unset):
        immutable_path_contents_should_exist (bool | Unset):
        is_immutable_context_path (bool | Unset):
        key (str | Unset):
        key_contains_configuration (bool | Unset):
        region (str | Unset):
        use_local_file_cache (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    can_accept_new_context: bool | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    immutable_context_version: str | Unset = UNSET
    immutable_path_contents_should_exist: bool | Unset = UNSET
    is_immutable_context_path: bool | Unset = UNSET
    key: str | Unset = UNSET
    key_contains_configuration: bool | Unset = UNSET
    region: str | Unset = UNSET
    use_local_file_cache: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        can_accept_new_context = self.can_accept_new_context

        document_id = self.document_id

        element_id = self.element_id

        immutable_context_version = self.immutable_context_version

        immutable_path_contents_should_exist = self.immutable_path_contents_should_exist

        is_immutable_context_path = self.is_immutable_context_path

        key = self.key

        key_contains_configuration = self.key_contains_configuration

        region = self.region

        use_local_file_cache = self.use_local_file_cache

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if can_accept_new_context is not UNSET:
            field_dict["canAcceptNewContext"] = can_accept_new_context
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if immutable_context_version is not UNSET:
            field_dict["immutableContextVersion"] = immutable_context_version
        if immutable_path_contents_should_exist is not UNSET:
            field_dict["immutablePathContentsShouldExist"] = immutable_path_contents_should_exist
        if is_immutable_context_path is not UNSET:
            field_dict["isImmutableContextPath"] = is_immutable_context_path
        if key is not UNSET:
            field_dict["key"] = key
        if key_contains_configuration is not UNSET:
            field_dict["keyContainsConfiguration"] = key_contains_configuration
        if region is not UNSET:
            field_dict["region"] = region
        if use_local_file_cache is not UNSET:
            field_dict["useLocalFileCache"] = use_local_file_cache

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        can_accept_new_context = d.pop("canAcceptNewContext", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        immutable_context_version = d.pop("immutableContextVersion", UNSET)

        immutable_path_contents_should_exist = d.pop("immutablePathContentsShouldExist", UNSET)

        is_immutable_context_path = d.pop("isImmutableContextPath", UNSET)

        key = d.pop("key", UNSET)

        key_contains_configuration = d.pop("keyContainsConfiguration", UNSET)

        region = d.pop("region", UNSET)

        use_local_file_cache = d.pop("useLocalFileCache", UNSET)

        bt_cache_data_path_191 = cls(
            bt_type=bt_type,
            can_accept_new_context=can_accept_new_context,
            document_id=document_id,
            element_id=element_id,
            immutable_context_version=immutable_context_version,
            immutable_path_contents_should_exist=immutable_path_contents_should_exist,
            is_immutable_context_path=is_immutable_context_path,
            key=key,
            key_contains_configuration=key_contains_configuration,
            region=region,
            use_local_file_cache=use_local_file_cache,
        )

        bt_cache_data_path_191.additional_properties = d
        return bt_cache_data_path_191

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
