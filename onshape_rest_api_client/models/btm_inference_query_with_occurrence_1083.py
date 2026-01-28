from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_entity_inference_type import GBTEntityInferenceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.btm_individual_query_base_139 import BTMIndividualQueryBase139


T = TypeVar("T", bound="BTMInferenceQueryWithOccurrence1083")


@_attrs_define
class BTMInferenceQueryWithOccurrence1083:
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
        full_path_as_string (str | Unset):
        node_id_from_current_query (str | Unset):
        occurrence (BTOccurrence74 | Unset):
        path (list[str] | Unset):
        query_path (list[str] | Unset):
        entity_query (str | Unset):
        inference_type (GBTEntityInferenceType | Unset):
        second_deterministic_id (str | Unset):
        second_entity_query (str | Unset):
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
    full_path_as_string: str | Unset = UNSET
    node_id_from_current_query: str | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
    path: list[str] | Unset = UNSET
    query_path: list[str] | Unset = UNSET
    entity_query: str | Unset = UNSET
    inference_type: GBTEntityInferenceType | Unset = UNSET
    second_deterministic_id: str | Unset = UNSET
    second_entity_query: str | Unset = UNSET
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

        full_path_as_string = self.full_path_as_string

        node_id_from_current_query = self.node_id_from_current_query

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        query_path: list[str] | Unset = UNSET
        if not isinstance(self.query_path, Unset):
            query_path = self.query_path

        entity_query = self.entity_query

        inference_type: str | Unset = UNSET
        if not isinstance(self.inference_type, Unset):
            inference_type = self.inference_type.value

        second_deterministic_id = self.second_deterministic_id

        second_entity_query = self.second_entity_query

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
        if full_path_as_string is not UNSET:
            field_dict["fullPathAsString"] = full_path_as_string
        if node_id_from_current_query is not UNSET:
            field_dict["nodeIdFromCurrentQuery"] = node_id_from_current_query
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if path is not UNSET:
            field_dict["path"] = path
        if query_path is not UNSET:
            field_dict["queryPath"] = query_path
        if entity_query is not UNSET:
            field_dict["entityQuery"] = entity_query
        if inference_type is not UNSET:
            field_dict["inferenceType"] = inference_type
        if second_deterministic_id is not UNSET:
            field_dict["secondDeterministicId"] = second_deterministic_id
        if second_entity_query is not UNSET:
            field_dict["secondEntityQuery"] = second_entity_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.btm_individual_query_base_139 import BTMIndividualQueryBase139

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

        full_path_as_string = d.pop("fullPathAsString", UNSET)

        node_id_from_current_query = d.pop("nodeIdFromCurrentQuery", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        path = cast(list[str], d.pop("path", UNSET))

        query_path = cast(list[str], d.pop("queryPath", UNSET))

        entity_query = d.pop("entityQuery", UNSET)

        _inference_type = d.pop("inferenceType", UNSET)
        inference_type: GBTEntityInferenceType | Unset
        if isinstance(_inference_type, Unset):
            inference_type = UNSET
        else:
            inference_type = GBTEntityInferenceType(_inference_type)

        second_deterministic_id = d.pop("secondDeterministicId", UNSET)

        second_entity_query = d.pop("secondEntityQuery", UNSET)

        btm_inference_query_with_occurrence_1083 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            deterministic_id_list=deterministic_id_list,
            deterministic_ids=deterministic_ids,
            generate_section_entity_query=generate_section_entity_query,
            generated_section_query_id=generated_section_query_id,
            query=query,
            query_string=query_string,
            full_path_as_string=full_path_as_string,
            node_id_from_current_query=node_id_from_current_query,
            occurrence=occurrence,
            path=path,
            query_path=query_path,
            entity_query=entity_query,
            inference_type=inference_type,
            second_deterministic_id=second_deterministic_id,
            second_entity_query=second_entity_query,
        )

        btm_inference_query_with_occurrence_1083.additional_properties = d
        return btm_inference_query_with_occurrence_1083

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
