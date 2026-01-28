from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMIndividualQueryBase139")


@_attrs_define
class BTMIndividualQueryBase139:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        deterministic_id_list (BTMIndividualQueryBase139 | Unset):
        deterministic_ids (list[str] | Unset):
        generate_section_entity_query (bool | Unset):
        generated_section_query_id (str | Unset):
        query (BTMIndividualQueryBase139 | Unset):
        query_string (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    deterministic_id_list: BTMIndividualQueryBase139 | Unset = UNSET
    deterministic_ids: list[str] | Unset = UNSET
    generate_section_entity_query: bool | Unset = UNSET
    generated_section_query_id: str | Unset = UNSET
    query: BTMIndividualQueryBase139 | Unset = UNSET
    query_string: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        deterministic_id_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_id_list, Unset):
            deterministic_id_list = self.deterministic_id_list.to_dict()

        deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_ids, Unset):
            deterministic_ids = self.deterministic_ids

        generate_section_entity_query = self.generate_section_entity_query

        generated_section_query_id = self.generated_section_query_id

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        query_string = self.query_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if deterministic_id_list is not UNSET:
            field_dict["deterministicIdList"] = deterministic_id_list
        if deterministic_ids is not UNSET:
            field_dict["deterministicIds"] = deterministic_ids
        if generate_section_entity_query is not UNSET:
            field_dict["generateSectionEntityQuery"] = generate_section_entity_query
        if generated_section_query_id is not UNSET:
            field_dict["generatedSectionQueryId"] = generated_section_query_id
        if query is not UNSET:
            field_dict["query"] = query
        if query_string is not UNSET:
            field_dict["queryString"] = query_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _deterministic_id_list = d.pop("deterministicIdList", UNSET)
        deterministic_id_list: BTMIndividualQueryBase139 | Unset
        if isinstance(_deterministic_id_list, Unset):
            deterministic_id_list = UNSET
        else:
            deterministic_id_list = BTMIndividualQueryBase139.from_dict(_deterministic_id_list)

        deterministic_ids = cast(list[str], d.pop("deterministicIds", UNSET))

        generate_section_entity_query = d.pop("generateSectionEntityQuery", UNSET)

        generated_section_query_id = d.pop("generatedSectionQueryId", UNSET)

        _query = d.pop("query", UNSET)
        query: BTMIndividualQueryBase139 | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = BTMIndividualQueryBase139.from_dict(_query)

        query_string = d.pop("queryString", UNSET)

        btm_individual_query_base_139 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            deterministic_id_list=deterministic_id_list,
            deterministic_ids=deterministic_ids,
            generate_section_entity_query=generate_section_entity_query,
            generated_section_query_id=generated_section_query_id,
            query=query,
            query_string=query_string,
        )

        btm_individual_query_base_139.additional_properties = d
        return btm_individual_query_base_139

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
