from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..models.gbtp_operator import GBTPOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_identifier_8 import BTPIdentifier8
    from ..models.btp_space_10 import BTPSpace10


T = TypeVar("T", bound="BTPExpressionOperator244")


@_attrs_define
class BTPExpressionOperator244:
    """
    Attributes:
        atomic (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        documentation_type (GBTPDefinitionType | Unset):
        end_source_location (int | Unset):
        node_id (str | Unset):
        short_descriptor (str | Unset):
        space_after (BTPSpace10 | Unset):
        space_before (BTPSpace10 | Unset):
        space_default (bool | Unset):
        start_source_location (int | Unset):
        for_export (bool | Unset):
        global_namespace (bool | Unset):
        import_microversion (str | Unset): Element microversion that is being imported.
        namespace (list[BTPIdentifier8] | Unset):
        operand1 (BTPExpression9 | Unset):
        operand2 (BTPExpression9 | Unset):
        operand3 (BTPExpression9 | Unset):
        operator (GBTPOperator | Unset):
        space_after_namespace (BTPSpace10 | Unset):
        space_after_operator (BTPSpace10 | Unset):
        space_before_operator (BTPSpace10 | Unset):
        written_as_function_call (bool | Unset):
    """

    atomic: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    documentation_type: GBTPDefinitionType | Unset = UNSET
    end_source_location: int | Unset = UNSET
    node_id: str | Unset = UNSET
    short_descriptor: str | Unset = UNSET
    space_after: BTPSpace10 | Unset = UNSET
    space_before: BTPSpace10 | Unset = UNSET
    space_default: bool | Unset = UNSET
    start_source_location: int | Unset = UNSET
    for_export: bool | Unset = UNSET
    global_namespace: bool | Unset = UNSET
    import_microversion: str | Unset = UNSET
    namespace: list[BTPIdentifier8] | Unset = UNSET
    operand1: BTPExpression9 | Unset = UNSET
    operand2: BTPExpression9 | Unset = UNSET
    operand3: BTPExpression9 | Unset = UNSET
    operator: GBTPOperator | Unset = UNSET
    space_after_namespace: BTPSpace10 | Unset = UNSET
    space_after_operator: BTPSpace10 | Unset = UNSET
    space_before_operator: BTPSpace10 | Unset = UNSET
    written_as_function_call: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atomic = self.atomic

        bt_type = self.bt_type

        documentation_type: str | Unset = UNSET
        if not isinstance(self.documentation_type, Unset):
            documentation_type = self.documentation_type.value

        end_source_location = self.end_source_location

        node_id = self.node_id

        short_descriptor = self.short_descriptor

        space_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after, Unset):
            space_after = self.space_after.to_dict()

        space_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before, Unset):
            space_before = self.space_before.to_dict()

        space_default = self.space_default

        start_source_location = self.start_source_location

        for_export = self.for_export

        global_namespace = self.global_namespace

        import_microversion = self.import_microversion

        namespace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.namespace, Unset):
            namespace = []
            for namespace_item_data in self.namespace:
                namespace_item = namespace_item_data.to_dict()
                namespace.append(namespace_item)

        operand1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operand1, Unset):
            operand1 = self.operand1.to_dict()

        operand2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operand2, Unset):
            operand2 = self.operand2.to_dict()

        operand3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operand3, Unset):
            operand3 = self.operand3.to_dict()

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        space_after_namespace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_namespace, Unset):
            space_after_namespace = self.space_after_namespace.to_dict()

        space_after_operator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_operator, Unset):
            space_after_operator = self.space_after_operator.to_dict()

        space_before_operator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_operator, Unset):
            space_before_operator = self.space_before_operator.to_dict()

        written_as_function_call = self.written_as_function_call

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if documentation_type is not UNSET:
            field_dict["documentationType"] = documentation_type
        if end_source_location is not UNSET:
            field_dict["endSourceLocation"] = end_source_location
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if short_descriptor is not UNSET:
            field_dict["shortDescriptor"] = short_descriptor
        if space_after is not UNSET:
            field_dict["spaceAfter"] = space_after
        if space_before is not UNSET:
            field_dict["spaceBefore"] = space_before
        if space_default is not UNSET:
            field_dict["spaceDefault"] = space_default
        if start_source_location is not UNSET:
            field_dict["startSourceLocation"] = start_source_location
        if for_export is not UNSET:
            field_dict["forExport"] = for_export
        if global_namespace is not UNSET:
            field_dict["globalNamespace"] = global_namespace
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if operand1 is not UNSET:
            field_dict["operand1"] = operand1
        if operand2 is not UNSET:
            field_dict["operand2"] = operand2
        if operand3 is not UNSET:
            field_dict["operand3"] = operand3
        if operator is not UNSET:
            field_dict["operator"] = operator
        if space_after_namespace is not UNSET:
            field_dict["spaceAfterNamespace"] = space_after_namespace
        if space_after_operator is not UNSET:
            field_dict["spaceAfterOperator"] = space_after_operator
        if space_before_operator is not UNSET:
            field_dict["spaceBeforeOperator"] = space_before_operator
        if written_as_function_call is not UNSET:
            field_dict["writtenAsFunctionCall"] = written_as_function_call

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_identifier_8 import BTPIdentifier8
        from ..models.btp_space_10 import BTPSpace10

        d = dict(src_dict)
        atomic = d.pop("atomic", UNSET)

        bt_type = d.pop("btType", UNSET)

        _documentation_type = d.pop("documentationType", UNSET)
        documentation_type: GBTPDefinitionType | Unset
        if isinstance(_documentation_type, Unset):
            documentation_type = UNSET
        else:
            documentation_type = GBTPDefinitionType(_documentation_type)

        end_source_location = d.pop("endSourceLocation", UNSET)

        node_id = d.pop("nodeId", UNSET)

        short_descriptor = d.pop("shortDescriptor", UNSET)

        _space_after = d.pop("spaceAfter", UNSET)
        space_after: BTPSpace10 | Unset
        if isinstance(_space_after, Unset):
            space_after = UNSET
        else:
            space_after = BTPSpace10.from_dict(_space_after)

        _space_before = d.pop("spaceBefore", UNSET)
        space_before: BTPSpace10 | Unset
        if isinstance(_space_before, Unset):
            space_before = UNSET
        else:
            space_before = BTPSpace10.from_dict(_space_before)

        space_default = d.pop("spaceDefault", UNSET)

        start_source_location = d.pop("startSourceLocation", UNSET)

        for_export = d.pop("forExport", UNSET)

        global_namespace = d.pop("globalNamespace", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _namespace = d.pop("namespace", UNSET)
        namespace: list[BTPIdentifier8] | Unset = UNSET
        if _namespace is not UNSET:
            namespace = []
            for namespace_item_data in _namespace:
                namespace_item = BTPIdentifier8.from_dict(namespace_item_data)

                namespace.append(namespace_item)

        _operand1 = d.pop("operand1", UNSET)
        operand1: BTPExpression9 | Unset
        if isinstance(_operand1, Unset):
            operand1 = UNSET
        else:
            operand1 = BTPExpression9.from_dict(_operand1)

        _operand2 = d.pop("operand2", UNSET)
        operand2: BTPExpression9 | Unset
        if isinstance(_operand2, Unset):
            operand2 = UNSET
        else:
            operand2 = BTPExpression9.from_dict(_operand2)

        _operand3 = d.pop("operand3", UNSET)
        operand3: BTPExpression9 | Unset
        if isinstance(_operand3, Unset):
            operand3 = UNSET
        else:
            operand3 = BTPExpression9.from_dict(_operand3)

        _operator = d.pop("operator", UNSET)
        operator: GBTPOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = GBTPOperator(_operator)

        _space_after_namespace = d.pop("spaceAfterNamespace", UNSET)
        space_after_namespace: BTPSpace10 | Unset
        if isinstance(_space_after_namespace, Unset):
            space_after_namespace = UNSET
        else:
            space_after_namespace = BTPSpace10.from_dict(_space_after_namespace)

        _space_after_operator = d.pop("spaceAfterOperator", UNSET)
        space_after_operator: BTPSpace10 | Unset
        if isinstance(_space_after_operator, Unset):
            space_after_operator = UNSET
        else:
            space_after_operator = BTPSpace10.from_dict(_space_after_operator)

        _space_before_operator = d.pop("spaceBeforeOperator", UNSET)
        space_before_operator: BTPSpace10 | Unset
        if isinstance(_space_before_operator, Unset):
            space_before_operator = UNSET
        else:
            space_before_operator = BTPSpace10.from_dict(_space_before_operator)

        written_as_function_call = d.pop("writtenAsFunctionCall", UNSET)

        btp_expression_operator_244 = cls(
            atomic=atomic,
            bt_type=bt_type,
            documentation_type=documentation_type,
            end_source_location=end_source_location,
            node_id=node_id,
            short_descriptor=short_descriptor,
            space_after=space_after,
            space_before=space_before,
            space_default=space_default,
            start_source_location=start_source_location,
            for_export=for_export,
            global_namespace=global_namespace,
            import_microversion=import_microversion,
            namespace=namespace,
            operand1=operand1,
            operand2=operand2,
            operand3=operand3,
            operator=operator,
            space_after_namespace=space_after_namespace,
            space_after_operator=space_after_operator,
            space_before_operator=space_before_operator,
            written_as_function_call=written_as_function_call,
        )

        btp_expression_operator_244.additional_properties = d
        return btp_expression_operator_244

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
