from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_individual_query_138 import BTMIndividualQuery138
    from ..models.btm_individual_query_base_139 import BTMIndividualQueryBase139
    from ..models.btp_statement_269 import BTPStatement269


T = TypeVar("T", bound="BTMIndividualSketchUniqueVerticesQuery1472")


@_attrs_define
class BTMIndividualSketchUniqueVerticesQuery1472:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_id_list (BTMIndividualQueryBase139 | Unset):
        deterministic_ids (list[str] | Unset):
        generate_section_entity_query (bool | Unset):
        generated_section_query_id (str | Unset):
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        persistent_query (BTPStatement269 | Unset):
        query (BTMIndividualQueryBase139 | Unset):
        query_statement (BTPStatement269 | Unset):
        query_string (str | Unset):
        variable_name (BTMIndividualQuery138 | Unset):
        feature_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_id_list: BTMIndividualQueryBase139 | Unset = UNSET
    deterministic_ids: list[str] | Unset = UNSET
    generate_section_entity_query: bool | Unset = UNSET
    generated_section_query_id: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    persistent_query: BTPStatement269 | Unset = UNSET
    query: BTMIndividualQueryBase139 | Unset = UNSET
    query_statement: BTPStatement269 | Unset = UNSET
    query_string: str | Unset = UNSET
    variable_name: BTMIndividualQuery138 | Unset = UNSET
    feature_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_id_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deterministic_id_list, Unset):
            deterministic_id_list = self.deterministic_id_list.to_dict()

        deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_ids, Unset):
            deterministic_ids = self.deterministic_ids

        generate_section_entity_query = self.generate_section_entity_query

        generated_section_query_id = self.generated_section_query_id

        import_microversion = self.import_microversion

        node_id = self.node_id

        persistent_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.persistent_query, Unset):
            persistent_query = self.persistent_query.to_dict()

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        query_statement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_statement, Unset):
            query_statement = self.query_statement.to_dict()

        query_string = self.query_string

        variable_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variable_name, Unset):
            variable_name = self.variable_name.to_dict()

        feature_id = self.feature_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_id_list is not UNSET:
            field_dict["deterministicIdList"] = deterministic_id_list
        if deterministic_ids is not UNSET:
            field_dict["deterministicIds"] = deterministic_ids
        if generate_section_entity_query is not UNSET:
            field_dict["generateSectionEntityQuery"] = generate_section_entity_query
        if generated_section_query_id is not UNSET:
            field_dict["generatedSectionQueryId"] = generated_section_query_id
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if persistent_query is not UNSET:
            field_dict["persistentQuery"] = persistent_query
        if query is not UNSET:
            field_dict["query"] = query
        if query_statement is not UNSET:
            field_dict["queryStatement"] = query_statement
        if query_string is not UNSET:
            field_dict["queryString"] = query_string
        if variable_name is not UNSET:
            field_dict["variableName"] = variable_name
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_individual_query_138 import BTMIndividualQuery138
        from ..models.btm_individual_query_base_139 import BTMIndividualQueryBase139
        from ..models.btp_statement_269 import BTPStatement269

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _deterministic_id_list = d.pop("deterministicIdList", UNSET)
        deterministic_id_list: BTMIndividualQueryBase139 | Unset
        if isinstance(_deterministic_id_list, Unset):
            deterministic_id_list = UNSET
        else:
            deterministic_id_list = BTMIndividualQueryBase139.from_dict(_deterministic_id_list)

        deterministic_ids = cast(list[str], d.pop("deterministicIds", UNSET))

        generate_section_entity_query = d.pop("generateSectionEntityQuery", UNSET)

        generated_section_query_id = d.pop("generatedSectionQueryId", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _persistent_query = d.pop("persistentQuery", UNSET)
        persistent_query: BTPStatement269 | Unset
        if isinstance(_persistent_query, Unset):
            persistent_query = UNSET
        else:
            persistent_query = BTPStatement269.from_dict(_persistent_query)

        _query = d.pop("query", UNSET)
        query: BTMIndividualQueryBase139 | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = BTMIndividualQueryBase139.from_dict(_query)

        _query_statement = d.pop("queryStatement", UNSET)
        query_statement: BTPStatement269 | Unset
        if isinstance(_query_statement, Unset):
            query_statement = UNSET
        else:
            query_statement = BTPStatement269.from_dict(_query_statement)

        query_string = d.pop("queryString", UNSET)

        _variable_name = d.pop("variableName", UNSET)
        variable_name: BTMIndividualQuery138 | Unset
        if isinstance(_variable_name, Unset):
            variable_name = UNSET
        else:
            variable_name = BTMIndividualQuery138.from_dict(_variable_name)

        feature_id = d.pop("featureId", UNSET)

        btm_individual_sketch_unique_vertices_query_1472 = cls(
            bt_type=bt_type,
            deterministic_id_list=deterministic_id_list,
            deterministic_ids=deterministic_ids,
            generate_section_entity_query=generate_section_entity_query,
            generated_section_query_id=generated_section_query_id,
            import_microversion=import_microversion,
            node_id=node_id,
            persistent_query=persistent_query,
            query=query,
            query_statement=query_statement,
            query_string=query_string,
            variable_name=variable_name,
            feature_id=feature_id,
        )

        btm_individual_sketch_unique_vertices_query_1472.additional_properties = d
        return btm_individual_sketch_unique_vertices_query_1472

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
