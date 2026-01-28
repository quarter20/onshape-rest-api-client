from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_individual_query_138 import BTMIndividualQuery138


T = TypeVar("T", bound="BTMRecordMetrics1169")


@_attrs_define
class BTMRecordMetrics1169:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        do_body_validation (bool | Unset):
        previous_feature_id (str | Unset):
        references (list[BTMIndividualQuery138] | Unset):
        use_latest_behavior (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    do_body_validation: bool | Unset = UNSET
    previous_feature_id: str | Unset = UNSET
    references: list[BTMIndividualQuery138] | Unset = UNSET
    use_latest_behavior: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        do_body_validation = self.do_body_validation

        previous_feature_id = self.previous_feature_id

        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        use_latest_behavior = self.use_latest_behavior

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if do_body_validation is not UNSET:
            field_dict["doBodyValidation"] = do_body_validation
        if previous_feature_id is not UNSET:
            field_dict["previousFeatureId"] = previous_feature_id
        if references is not UNSET:
            field_dict["references"] = references
        if use_latest_behavior is not UNSET:
            field_dict["useLatestBehavior"] = use_latest_behavior

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_individual_query_138 import BTMIndividualQuery138

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        do_body_validation = d.pop("doBodyValidation", UNSET)

        previous_feature_id = d.pop("previousFeatureId", UNSET)

        _references = d.pop("references", UNSET)
        references: list[BTMIndividualQuery138] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = BTMIndividualQuery138.from_dict(references_item_data)

                references.append(references_item)

        use_latest_behavior = d.pop("useLatestBehavior", UNSET)

        btm_record_metrics_1169 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            do_body_validation=do_body_validation,
            previous_feature_id=previous_feature_id,
            references=references,
            use_latest_behavior=use_latest_behavior,
        )

        btm_record_metrics_1169.additional_properties = d
        return btm_record_metrics_1169

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
