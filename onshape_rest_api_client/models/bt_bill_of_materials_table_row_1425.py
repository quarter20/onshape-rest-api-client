from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_bill_of_materials_exclusion_status import GBTBillOfMaterialsExclusionStatus
from ..models.gbt_bill_of_materials_expansion_status import GBTBillOfMaterialsExpansionStatus
from ..models.gbt_bill_of_materials_suppression_status import GBTBillOfMaterialsSuppressionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bill_of_materials_unique_item_id_2029 import BTBillOfMaterialsUniqueItemId2029
    from ..models.bt_table_base_row_metadata_3181 import BTTableBaseRowMetadata3181
    from ..models.bt_table_row_1054_column_id_to_cell import BTTableRow1054ColumnIdToCell
    from ..models.bt_tree_node_20 import BTTreeNode20


T = TypeVar("T", bound="BTBillOfMaterialsTableRow1425")


@_attrs_define
class BTBillOfMaterialsTableRow1425:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        column_id_to_cell (BTTableRow1054ColumnIdToCell | Unset):
        id (str | Unset):
        meta_data (BTTreeNode20 | Unset):
        node_id (str | Unset):
        row_metadata (BTTableBaseRowMetadata3181 | Unset):
        exclude_is_editable (bool | Unset):
        exclusion_status (GBTBillOfMaterialsExclusionStatus | Unset):
        expansion_status (GBTBillOfMaterialsExpansionStatus | Unset):
        indent_level (int | Unset):
        is_components_only (bool | Unset):
        is_suppressed (bool | Unset):
        metadata_object_type (int | Unset):
        metadata_update_href (str | Unset):
        name (str | Unset):
        related_occurrence_paths (list[str] | Unset):
        subassembly_bom_behavior_name (str | Unset):
        suppression_status (GBTBillOfMaterialsSuppressionStatus | Unset):
        unique_item_id (BTBillOfMaterialsUniqueItemId2029 | Unset):
    """

    bt_type: str | Unset = UNSET
    column_id_to_cell: BTTableRow1054ColumnIdToCell | Unset = UNSET
    id: str | Unset = UNSET
    meta_data: BTTreeNode20 | Unset = UNSET
    node_id: str | Unset = UNSET
    row_metadata: BTTableBaseRowMetadata3181 | Unset = UNSET
    exclude_is_editable: bool | Unset = UNSET
    exclusion_status: GBTBillOfMaterialsExclusionStatus | Unset = UNSET
    expansion_status: GBTBillOfMaterialsExpansionStatus | Unset = UNSET
    indent_level: int | Unset = UNSET
    is_components_only: bool | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    metadata_object_type: int | Unset = UNSET
    metadata_update_href: str | Unset = UNSET
    name: str | Unset = UNSET
    related_occurrence_paths: list[str] | Unset = UNSET
    subassembly_bom_behavior_name: str | Unset = UNSET
    suppression_status: GBTBillOfMaterialsSuppressionStatus | Unset = UNSET
    unique_item_id: BTBillOfMaterialsUniqueItemId2029 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        column_id_to_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_id_to_cell, Unset):
            column_id_to_cell = self.column_id_to_cell.to_dict()

        id = self.id

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        node_id = self.node_id

        row_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.row_metadata, Unset):
            row_metadata = self.row_metadata.to_dict()

        exclude_is_editable = self.exclude_is_editable

        exclusion_status: str | Unset = UNSET
        if not isinstance(self.exclusion_status, Unset):
            exclusion_status = self.exclusion_status.value

        expansion_status: str | Unset = UNSET
        if not isinstance(self.expansion_status, Unset):
            expansion_status = self.expansion_status.value

        indent_level = self.indent_level

        is_components_only = self.is_components_only

        is_suppressed = self.is_suppressed

        metadata_object_type = self.metadata_object_type

        metadata_update_href = self.metadata_update_href

        name = self.name

        related_occurrence_paths: list[str] | Unset = UNSET
        if not isinstance(self.related_occurrence_paths, Unset):
            related_occurrence_paths = self.related_occurrence_paths

        subassembly_bom_behavior_name = self.subassembly_bom_behavior_name

        suppression_status: str | Unset = UNSET
        if not isinstance(self.suppression_status, Unset):
            suppression_status = self.suppression_status.value

        unique_item_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unique_item_id, Unset):
            unique_item_id = self.unique_item_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if column_id_to_cell is not UNSET:
            field_dict["columnIdToCell"] = column_id_to_cell
        if id is not UNSET:
            field_dict["id"] = id
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if row_metadata is not UNSET:
            field_dict["rowMetadata"] = row_metadata
        if exclude_is_editable is not UNSET:
            field_dict["excludeIsEditable"] = exclude_is_editable
        if exclusion_status is not UNSET:
            field_dict["exclusionStatus"] = exclusion_status
        if expansion_status is not UNSET:
            field_dict["expansionStatus"] = expansion_status
        if indent_level is not UNSET:
            field_dict["indentLevel"] = indent_level
        if is_components_only is not UNSET:
            field_dict["isComponentsOnly"] = is_components_only
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if metadata_object_type is not UNSET:
            field_dict["metadataObjectType"] = metadata_object_type
        if metadata_update_href is not UNSET:
            field_dict["metadataUpdateHref"] = metadata_update_href
        if name is not UNSET:
            field_dict["name"] = name
        if related_occurrence_paths is not UNSET:
            field_dict["relatedOccurrencePaths"] = related_occurrence_paths
        if subassembly_bom_behavior_name is not UNSET:
            field_dict["subassemblyBomBehaviorName"] = subassembly_bom_behavior_name
        if suppression_status is not UNSET:
            field_dict["suppressionStatus"] = suppression_status
        if unique_item_id is not UNSET:
            field_dict["uniqueItemId"] = unique_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bill_of_materials_unique_item_id_2029 import BTBillOfMaterialsUniqueItemId2029
        from ..models.bt_table_base_row_metadata_3181 import BTTableBaseRowMetadata3181
        from ..models.bt_table_row_1054_column_id_to_cell import BTTableRow1054ColumnIdToCell
        from ..models.bt_tree_node_20 import BTTreeNode20

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _column_id_to_cell = d.pop("columnIdToCell", UNSET)
        column_id_to_cell: BTTableRow1054ColumnIdToCell | Unset
        if isinstance(_column_id_to_cell, Unset):
            column_id_to_cell = UNSET
        else:
            column_id_to_cell = BTTableRow1054ColumnIdToCell.from_dict(_column_id_to_cell)

        id = d.pop("id", UNSET)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: BTTreeNode20 | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = BTTreeNode20.from_dict(_meta_data)

        node_id = d.pop("nodeId", UNSET)

        _row_metadata = d.pop("rowMetadata", UNSET)
        row_metadata: BTTableBaseRowMetadata3181 | Unset
        if isinstance(_row_metadata, Unset):
            row_metadata = UNSET
        else:
            row_metadata = BTTableBaseRowMetadata3181.from_dict(_row_metadata)

        exclude_is_editable = d.pop("excludeIsEditable", UNSET)

        _exclusion_status = d.pop("exclusionStatus", UNSET)
        exclusion_status: GBTBillOfMaterialsExclusionStatus | Unset
        if isinstance(_exclusion_status, Unset):
            exclusion_status = UNSET
        else:
            exclusion_status = GBTBillOfMaterialsExclusionStatus(_exclusion_status)

        _expansion_status = d.pop("expansionStatus", UNSET)
        expansion_status: GBTBillOfMaterialsExpansionStatus | Unset
        if isinstance(_expansion_status, Unset):
            expansion_status = UNSET
        else:
            expansion_status = GBTBillOfMaterialsExpansionStatus(_expansion_status)

        indent_level = d.pop("indentLevel", UNSET)

        is_components_only = d.pop("isComponentsOnly", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        metadata_object_type = d.pop("metadataObjectType", UNSET)

        metadata_update_href = d.pop("metadataUpdateHref", UNSET)

        name = d.pop("name", UNSET)

        related_occurrence_paths = cast(list[str], d.pop("relatedOccurrencePaths", UNSET))

        subassembly_bom_behavior_name = d.pop("subassemblyBomBehaviorName", UNSET)

        _suppression_status = d.pop("suppressionStatus", UNSET)
        suppression_status: GBTBillOfMaterialsSuppressionStatus | Unset
        if isinstance(_suppression_status, Unset):
            suppression_status = UNSET
        else:
            suppression_status = GBTBillOfMaterialsSuppressionStatus(_suppression_status)

        _unique_item_id = d.pop("uniqueItemId", UNSET)
        unique_item_id: BTBillOfMaterialsUniqueItemId2029 | Unset
        if isinstance(_unique_item_id, Unset):
            unique_item_id = UNSET
        else:
            unique_item_id = BTBillOfMaterialsUniqueItemId2029.from_dict(_unique_item_id)

        bt_bill_of_materials_table_row_1425 = cls(
            bt_type=bt_type,
            column_id_to_cell=column_id_to_cell,
            id=id,
            meta_data=meta_data,
            node_id=node_id,
            row_metadata=row_metadata,
            exclude_is_editable=exclude_is_editable,
            exclusion_status=exclusion_status,
            expansion_status=expansion_status,
            indent_level=indent_level,
            is_components_only=is_components_only,
            is_suppressed=is_suppressed,
            metadata_object_type=metadata_object_type,
            metadata_update_href=metadata_update_href,
            name=name,
            related_occurrence_paths=related_occurrence_paths,
            subassembly_bom_behavior_name=subassembly_bom_behavior_name,
            suppression_status=suppression_status,
            unique_item_id=unique_item_id,
        )

        bt_bill_of_materials_table_row_1425.additional_properties = d
        return bt_bill_of_materials_table_row_1425

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
