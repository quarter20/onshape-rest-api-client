from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_app_element_associative_data_type import GBTAppElementAssociativeDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_name_value_pair import BTNameValuePair


T = TypeVar("T", bound="BTAssociativeDataInfo")


@_attrs_define
class BTAssociativeDataInfo:
    """
    Attributes:
        associative_data_id (str | Unset):
        data (list[BTNameValuePair] | Unset):
        document_id (str | Unset):
        document_microversion (str | Unset):
        element_id (str | Unset):
        error (str | Unset):
        id_tag (str | Unset):
        microversion_id (str | Unset):
        occurrence_id (str | Unset):
        type_ (GBTAppElementAssociativeDataType | Unset):
        version_id (str | Unset):
    """

    associative_data_id: str | Unset = UNSET
    data: list[BTNameValuePair] | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion: str | Unset = UNSET
    element_id: str | Unset = UNSET
    error: str | Unset = UNSET
    id_tag: str | Unset = UNSET
    microversion_id: str | Unset = UNSET
    occurrence_id: str | Unset = UNSET
    type_: GBTAppElementAssociativeDataType | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associative_data_id = self.associative_data_id

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        document_id = self.document_id

        document_microversion = self.document_microversion

        element_id = self.element_id

        error = self.error

        id_tag = self.id_tag

        microversion_id = self.microversion_id

        occurrence_id = self.occurrence_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associative_data_id is not UNSET:
            field_dict["associativeDataId"] = associative_data_id
        if data is not UNSET:
            field_dict["data"] = data
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_microversion is not UNSET:
            field_dict["documentMicroversion"] = document_microversion
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if error is not UNSET:
            field_dict["error"] = error
        if id_tag is not UNSET:
            field_dict["idTag"] = id_tag
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if occurrence_id is not UNSET:
            field_dict["occurrenceId"] = occurrence_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_name_value_pair import BTNameValuePair

        d = dict(src_dict)
        associative_data_id = d.pop("associativeDataId", UNSET)

        _data = d.pop("data", UNSET)
        data: list[BTNameValuePair] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = BTNameValuePair.from_dict(data_item_data)

                data.append(data_item)

        document_id = d.pop("documentId", UNSET)

        document_microversion = d.pop("documentMicroversion", UNSET)

        element_id = d.pop("elementId", UNSET)

        error = d.pop("error", UNSET)

        id_tag = d.pop("idTag", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        occurrence_id = d.pop("occurrenceId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GBTAppElementAssociativeDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTAppElementAssociativeDataType(_type_)

        version_id = d.pop("versionId", UNSET)

        bt_associative_data_info = cls(
            associative_data_id=associative_data_id,
            data=data,
            document_id=document_id,
            document_microversion=document_microversion,
            element_id=element_id,
            error=error,
            id_tag=id_tag,
            microversion_id=microversion_id,
            occurrence_id=occurrence_id,
            type_=type_,
            version_id=version_id,
        )

        bt_associative_data_info.additional_properties = d
        return bt_associative_data_info

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
