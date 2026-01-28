from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_discount_info import BTDiscountInfo


T = TypeVar("T", bound="BTBillingPlanInfo")


@_attrs_define
class BTBillingPlanInfo:
    """
    Attributes:
        amount_cents (int | Unset):
        application_id (str | Unset):
        client_id (str | Unset):
        company_plan (bool | Unset):
        consumable_quantity (int | Unset):
        deprecated (bool | Unset):
        description (str | Unset):
        discount_info (BTDiscountInfo | Unset):
        group (str | Unset):
        hidden (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        interval (str | Unset):
        name (str | Unset): Name of the resource.
        onshape_plan (bool | Unset):
        plan_type (int | Unset):
        trial_period_days (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    amount_cents: int | Unset = UNSET
    application_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    company_plan: bool | Unset = UNSET
    consumable_quantity: int | Unset = UNSET
    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    discount_info: BTDiscountInfo | Unset = UNSET
    group: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    interval: str | Unset = UNSET
    name: str | Unset = UNSET
    onshape_plan: bool | Unset = UNSET
    plan_type: int | Unset = UNSET
    trial_period_days: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        application_id = self.application_id

        client_id = self.client_id

        company_plan = self.company_plan

        consumable_quantity = self.consumable_quantity

        deprecated = self.deprecated

        description = self.description

        discount_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount_info, Unset):
            discount_info = self.discount_info.to_dict()

        group = self.group

        hidden = self.hidden

        href = self.href

        id = self.id

        interval = self.interval

        name = self.name

        onshape_plan = self.onshape_plan

        plan_type = self.plan_type

        trial_period_days = self.trial_period_days

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_cents is not UNSET:
            field_dict["amountCents"] = amount_cents
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if company_plan is not UNSET:
            field_dict["companyPlan"] = company_plan
        if consumable_quantity is not UNSET:
            field_dict["consumableQuantity"] = consumable_quantity
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if description is not UNSET:
            field_dict["description"] = description
        if discount_info is not UNSET:
            field_dict["discountInfo"] = discount_info
        if group is not UNSET:
            field_dict["group"] = group
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if name is not UNSET:
            field_dict["name"] = name
        if onshape_plan is not UNSET:
            field_dict["onshapePlan"] = onshape_plan
        if plan_type is not UNSET:
            field_dict["planType"] = plan_type
        if trial_period_days is not UNSET:
            field_dict["trialPeriodDays"] = trial_period_days
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_discount_info import BTDiscountInfo

        d = dict(src_dict)
        amount_cents = d.pop("amountCents", UNSET)

        application_id = d.pop("applicationId", UNSET)

        client_id = d.pop("clientId", UNSET)

        company_plan = d.pop("companyPlan", UNSET)

        consumable_quantity = d.pop("consumableQuantity", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        _discount_info = d.pop("discountInfo", UNSET)
        discount_info: BTDiscountInfo | Unset
        if isinstance(_discount_info, Unset):
            discount_info = UNSET
        else:
            discount_info = BTDiscountInfo.from_dict(_discount_info)

        group = d.pop("group", UNSET)

        hidden = d.pop("hidden", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        interval = d.pop("interval", UNSET)

        name = d.pop("name", UNSET)

        onshape_plan = d.pop("onshapePlan", UNSET)

        plan_type = d.pop("planType", UNSET)

        trial_period_days = d.pop("trialPeriodDays", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_billing_plan_info = cls(
            amount_cents=amount_cents,
            application_id=application_id,
            client_id=client_id,
            company_plan=company_plan,
            consumable_quantity=consumable_quantity,
            deprecated=deprecated,
            description=description,
            discount_info=discount_info,
            group=group,
            hidden=hidden,
            href=href,
            id=id,
            interval=interval,
            name=name,
            onshape_plan=onshape_plan,
            plan_type=plan_type,
            trial_period_days=trial_period_days,
            view_ref=view_ref,
        )

        bt_billing_plan_info.additional_properties = d
        return bt_billing_plan_info

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
