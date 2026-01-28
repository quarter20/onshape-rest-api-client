from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..models.gbtp_type import GBTPType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_annotation_231 import BTPAnnotation231
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_identifier_8 import BTPIdentifier8
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_statement_269 import BTPStatement269


T = TypeVar("T", bound="BTPStatementLoopForIn279")


@_attrs_define
class BTPStatementLoopForIn279:
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
        body (BTPStatement269 | Unset):
        space_after_loop_type (BTPSpace10 | Unset):
        container (BTPExpression9 | Unset):
        identifiers (list[BTPIdentifier8] | Unset):
        is_var_declared_here (bool | Unset):
        key_var (BTPIdentifier8 | Unset):
        space_before_var (BTPSpace10 | Unset):
        standard_types (list[GBTPType] | Unset):
        type_names (list[str] | Unset):
        var (BTPIdentifier8 | Unset):
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
    body: BTPStatement269 | Unset = UNSET
    space_after_loop_type: BTPSpace10 | Unset = UNSET
    container: BTPExpression9 | Unset = UNSET
    identifiers: list[BTPIdentifier8] | Unset = UNSET
    is_var_declared_here: bool | Unset = UNSET
    key_var: BTPIdentifier8 | Unset = UNSET
    space_before_var: BTPSpace10 | Unset = UNSET
    standard_types: list[GBTPType] | Unset = UNSET
    type_names: list[str] | Unset = UNSET
    var: BTPIdentifier8 | Unset = UNSET
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

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        space_after_loop_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_loop_type, Unset):
            space_after_loop_type = self.space_after_loop_type.to_dict()

        container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.container, Unset):
            container = self.container.to_dict()

        identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        is_var_declared_here = self.is_var_declared_here

        key_var: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_var, Unset):
            key_var = self.key_var.to_dict()

        space_before_var: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_var, Unset):
            space_before_var = self.space_before_var.to_dict()

        standard_types: list[str] | Unset = UNSET
        if not isinstance(self.standard_types, Unset):
            standard_types = []
            for standard_types_item_data in self.standard_types:
                standard_types_item = standard_types_item_data.value
                standard_types.append(standard_types_item)

        type_names: list[str] | Unset = UNSET
        if not isinstance(self.type_names, Unset):
            type_names = self.type_names

        var: dict[str, Any] | Unset = UNSET
        if not isinstance(self.var, Unset):
            var = self.var.to_dict()

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
        if body is not UNSET:
            field_dict["body"] = body
        if space_after_loop_type is not UNSET:
            field_dict["spaceAfterLoopType"] = space_after_loop_type
        if container is not UNSET:
            field_dict["container"] = container
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if is_var_declared_here is not UNSET:
            field_dict["isVarDeclaredHere"] = is_var_declared_here
        if key_var is not UNSET:
            field_dict["keyVar"] = key_var
        if space_before_var is not UNSET:
            field_dict["spaceBeforeVar"] = space_before_var
        if standard_types is not UNSET:
            field_dict["standardTypes"] = standard_types
        if type_names is not UNSET:
            field_dict["typeNames"] = type_names
        if var is not UNSET:
            field_dict["var"] = var

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_identifier_8 import BTPIdentifier8
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

        _body = d.pop("body", UNSET)
        body: BTPStatement269 | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = BTPStatement269.from_dict(_body)

        _space_after_loop_type = d.pop("spaceAfterLoopType", UNSET)
        space_after_loop_type: BTPSpace10 | Unset
        if isinstance(_space_after_loop_type, Unset):
            space_after_loop_type = UNSET
        else:
            space_after_loop_type = BTPSpace10.from_dict(_space_after_loop_type)

        _container = d.pop("container", UNSET)
        container: BTPExpression9 | Unset
        if isinstance(_container, Unset):
            container = UNSET
        else:
            container = BTPExpression9.from_dict(_container)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: list[BTPIdentifier8] | Unset = UNSET
        if _identifiers is not UNSET:
            identifiers = []
            for identifiers_item_data in _identifiers:
                identifiers_item = BTPIdentifier8.from_dict(identifiers_item_data)

                identifiers.append(identifiers_item)

        is_var_declared_here = d.pop("isVarDeclaredHere", UNSET)

        _key_var = d.pop("keyVar", UNSET)
        key_var: BTPIdentifier8 | Unset
        if isinstance(_key_var, Unset):
            key_var = UNSET
        else:
            key_var = BTPIdentifier8.from_dict(_key_var)

        _space_before_var = d.pop("spaceBeforeVar", UNSET)
        space_before_var: BTPSpace10 | Unset
        if isinstance(_space_before_var, Unset):
            space_before_var = UNSET
        else:
            space_before_var = BTPSpace10.from_dict(_space_before_var)

        _standard_types = d.pop("standardTypes", UNSET)
        standard_types: list[GBTPType] | Unset = UNSET
        if _standard_types is not UNSET:
            standard_types = []
            for standard_types_item_data in _standard_types:
                standard_types_item = GBTPType(standard_types_item_data)

                standard_types.append(standard_types_item)

        type_names = cast(list[str], d.pop("typeNames", UNSET))

        _var = d.pop("var", UNSET)
        var: BTPIdentifier8 | Unset
        if isinstance(_var, Unset):
            var = UNSET
        else:
            var = BTPIdentifier8.from_dict(_var)

        btp_statement_loop_for_in_279 = cls(
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
            body=body,
            space_after_loop_type=space_after_loop_type,
            container=container,
            identifiers=identifiers,
            is_var_declared_here=is_var_declared_here,
            key_var=key_var,
            space_before_var=space_before_var,
            standard_types=standard_types,
            type_names=type_names,
            var=var,
        )

        btp_statement_loop_for_in_279.additional_properties = d
        return btp_statement_loop_for_in_279

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
