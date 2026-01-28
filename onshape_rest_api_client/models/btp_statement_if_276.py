from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_annotation_231 import BTPAnnotation231
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_statement_269 import BTPStatement269


T = TypeVar("T", bound="BTPStatementIf276")


@_attrs_define
class BTPStatementIf276:
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
        annotation (BTPAnnotation231 | Unset):
        condition (BTPExpression9 | Unset):
        else_body (BTPStatement269 | Unset):
        space_after_if (BTPSpace10 | Unset):
        then_body (BTPStatement269 | Unset):
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
    annotation: BTPAnnotation231 | Unset = UNSET
    condition: BTPExpression9 | Unset = UNSET
    else_body: BTPStatement269 | Unset = UNSET
    space_after_if: BTPSpace10 | Unset = UNSET
    then_body: BTPStatement269 | Unset = UNSET
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

        annotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        else_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.else_body, Unset):
            else_body = self.else_body.to_dict()

        space_after_if: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_if, Unset):
            space_after_if = self.space_after_if.to_dict()

        then_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.then_body, Unset):
            then_body = self.then_body.to_dict()

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
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if condition is not UNSET:
            field_dict["condition"] = condition
        if else_body is not UNSET:
            field_dict["elseBody"] = else_body
        if space_after_if is not UNSET:
            field_dict["spaceAfterIf"] = space_after_if
        if then_body is not UNSET:
            field_dict["thenBody"] = then_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_statement_269 import BTPStatement269

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

        _annotation = d.pop("annotation", UNSET)
        annotation: BTPAnnotation231 | Unset
        if isinstance(_annotation, Unset):
            annotation = UNSET
        else:
            annotation = BTPAnnotation231.from_dict(_annotation)

        _condition = d.pop("condition", UNSET)
        condition: BTPExpression9 | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = BTPExpression9.from_dict(_condition)

        _else_body = d.pop("elseBody", UNSET)
        else_body: BTPStatement269 | Unset
        if isinstance(_else_body, Unset):
            else_body = UNSET
        else:
            else_body = BTPStatement269.from_dict(_else_body)

        _space_after_if = d.pop("spaceAfterIf", UNSET)
        space_after_if: BTPSpace10 | Unset
        if isinstance(_space_after_if, Unset):
            space_after_if = UNSET
        else:
            space_after_if = BTPSpace10.from_dict(_space_after_if)

        _then_body = d.pop("thenBody", UNSET)
        then_body: BTPStatement269 | Unset
        if isinstance(_then_body, Unset):
            then_body = UNSET
        else:
            then_body = BTPStatement269.from_dict(_then_body)

        btp_statement_if_276 = cls(
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
            annotation=annotation,
            condition=condition,
            else_body=else_body,
            space_after_if=space_after_if,
            then_body=then_body,
        )

        btp_statement_if_276.additional_properties = d
        return btp_statement_if_276

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
