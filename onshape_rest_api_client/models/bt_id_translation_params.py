from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTIdTranslationParams")


@_attrs_define
class BTIdTranslationParams:
    """
    Attributes:
        ids (list[str] | Unset):
        link_document_id (str | Unset):
        source_configuration (str | Unset):
        source_document_microversion (str | Unset):
        target_configuration (str | Unset):
    """

    ids: list[str] | Unset = UNSET
    link_document_id: str | Unset = UNSET
    source_configuration: str | Unset = UNSET
    source_document_microversion: str | Unset = UNSET
    target_configuration: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        link_document_id = self.link_document_id

        source_configuration = self.source_configuration

        source_document_microversion = self.source_document_microversion

        target_configuration = self.target_configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if link_document_id is not UNSET:
            field_dict["linkDocumentId"] = link_document_id
        if source_configuration is not UNSET:
            field_dict["sourceConfiguration"] = source_configuration
        if source_document_microversion is not UNSET:
            field_dict["sourceDocumentMicroversion"] = source_document_microversion
        if target_configuration is not UNSET:
            field_dict["targetConfiguration"] = target_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids", UNSET))

        link_document_id = d.pop("linkDocumentId", UNSET)

        source_configuration = d.pop("sourceConfiguration", UNSET)

        source_document_microversion = d.pop("sourceDocumentMicroversion", UNSET)

        target_configuration = d.pop("targetConfiguration", UNSET)

        bt_id_translation_params = cls(
            ids=ids,
            link_document_id=link_document_id,
            source_configuration=source_configuration,
            source_document_microversion=source_document_microversion,
            target_configuration=target_configuration,
        )

        bt_id_translation_params.additional_properties = d
        return bt_id_translation_params

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
