from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_billing_plan_info import BTBillingPlanInfo
    from ..models.bt_card_info import BTCardInfo
    from ..models.bt_plan_subscriber_info import BTPlanSubscriberInfo
    from ..models.btapi_application_summary_info import BTAPIApplicationSummaryInfo
    from ..models.next_charge import NextCharge
    from ..models.prorated_charges import ProratedCharges


T = TypeVar("T", bound="BTPurchaseInfo")


@_attrs_define
class BTPurchaseInfo:
    """
    Attributes:
        account_id (str | Unset):
        actual_amount_paid_cents (int | Unset):
        amount_cents (int | Unset):
        api_allocation_by_plan (int | Unset): Represents the default annual API call allocation defined by the user's
            Onshape billing plan.
        api_allocation_end_date (datetime.datetime | Unset):
        api_allocation_override (int | Unset): Manual override set by Onshape admin; when non-zero takes precedence over
            apiAllocationByPlan.
        api_allocation_start_date (datetime.datetime | Unset):
        application (BTAPIApplicationSummaryInfo | Unset):
        canceled_at (datetime.datetime | Unset):
        card (BTCardInfo | Unset):
        client_id (str | Unset):
        coupon_amount_off (int | Unset):
        coupon_percent_off (int | Unset):
        created_by (str | Unset):
        currency (str | Unset):
        duration (int | Unset):
        duration_months (int | Unset):
        group (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        last_modified (datetime.datetime | Unset):
        last_modified_by (str | Unset):
        light_seats (int | Unset):
        name (str | Unset): Name of the resource.
        next_charge (NextCharge | Unset):
        overage_enabled (bool | Unset):
        payment_type (int | Unset):
        pending_cancelation (bool | Unset):
        plan (BTBillingPlanInfo | Unset):
        plan_id (str | Unset):
        plan_name (str | Unset):
        plan_type (int | Unset):
        pre_trial_plan_id (str | Unset):
        prorated_charges (list[ProratedCharges] | Unset):
        prorated_total (int | Unset):
        purchase_date (datetime.datetime | Unset):
        reseller_name (str | Unset):
        seats (int | Unset):
        state (int | Unset):
        subscribers (list[BTPlanSubscriberInfo] | Unset):
        subscription_begin_at (datetime.datetime | Unset):
        subscription_end_at (datetime.datetime | Unset):
        subscription_id (str | Unset):
        subscription_type (int | Unset):
        tax_amount_cents (int | Unset):
        trial_end (datetime.datetime | Unset):
        trial_initiated_by (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    account_id: str | Unset = UNSET
    actual_amount_paid_cents: int | Unset = UNSET
    amount_cents: int | Unset = UNSET
    api_allocation_by_plan: int | Unset = UNSET
    api_allocation_end_date: datetime.datetime | Unset = UNSET
    api_allocation_override: int | Unset = UNSET
    api_allocation_start_date: datetime.datetime | Unset = UNSET
    application: BTAPIApplicationSummaryInfo | Unset = UNSET
    canceled_at: datetime.datetime | Unset = UNSET
    card: BTCardInfo | Unset = UNSET
    client_id: str | Unset = UNSET
    coupon_amount_off: int | Unset = UNSET
    coupon_percent_off: int | Unset = UNSET
    created_by: str | Unset = UNSET
    currency: str | Unset = UNSET
    duration: int | Unset = UNSET
    duration_months: int | Unset = UNSET
    group: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    last_modified_by: str | Unset = UNSET
    light_seats: int | Unset = UNSET
    name: str | Unset = UNSET
    next_charge: NextCharge | Unset = UNSET
    overage_enabled: bool | Unset = UNSET
    payment_type: int | Unset = UNSET
    pending_cancelation: bool | Unset = UNSET
    plan: BTBillingPlanInfo | Unset = UNSET
    plan_id: str | Unset = UNSET
    plan_name: str | Unset = UNSET
    plan_type: int | Unset = UNSET
    pre_trial_plan_id: str | Unset = UNSET
    prorated_charges: list[ProratedCharges] | Unset = UNSET
    prorated_total: int | Unset = UNSET
    purchase_date: datetime.datetime | Unset = UNSET
    reseller_name: str | Unset = UNSET
    seats: int | Unset = UNSET
    state: int | Unset = UNSET
    subscribers: list[BTPlanSubscriberInfo] | Unset = UNSET
    subscription_begin_at: datetime.datetime | Unset = UNSET
    subscription_end_at: datetime.datetime | Unset = UNSET
    subscription_id: str | Unset = UNSET
    subscription_type: int | Unset = UNSET
    tax_amount_cents: int | Unset = UNSET
    trial_end: datetime.datetime | Unset = UNSET
    trial_initiated_by: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        actual_amount_paid_cents = self.actual_amount_paid_cents

        amount_cents = self.amount_cents

        api_allocation_by_plan = self.api_allocation_by_plan

        api_allocation_end_date: str | Unset = UNSET
        if not isinstance(self.api_allocation_end_date, Unset):
            api_allocation_end_date = self.api_allocation_end_date.isoformat()

        api_allocation_override = self.api_allocation_override

        api_allocation_start_date: str | Unset = UNSET
        if not isinstance(self.api_allocation_start_date, Unset):
            api_allocation_start_date = self.api_allocation_start_date.isoformat()

        application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        canceled_at: str | Unset = UNSET
        if not isinstance(self.canceled_at, Unset):
            canceled_at = self.canceled_at.isoformat()

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        client_id = self.client_id

        coupon_amount_off = self.coupon_amount_off

        coupon_percent_off = self.coupon_percent_off

        created_by = self.created_by

        currency = self.currency

        duration = self.duration

        duration_months = self.duration_months

        group = self.group

        href = self.href

        id = self.id

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        last_modified_by = self.last_modified_by

        light_seats = self.light_seats

        name = self.name

        next_charge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_charge, Unset):
            next_charge = self.next_charge.to_dict()

        overage_enabled = self.overage_enabled

        payment_type = self.payment_type

        pending_cancelation = self.pending_cancelation

        plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        plan_id = self.plan_id

        plan_name = self.plan_name

        plan_type = self.plan_type

        pre_trial_plan_id = self.pre_trial_plan_id

        prorated_charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prorated_charges, Unset):
            prorated_charges = []
            for prorated_charges_item_data in self.prorated_charges:
                prorated_charges_item = prorated_charges_item_data.to_dict()
                prorated_charges.append(prorated_charges_item)

        prorated_total = self.prorated_total

        purchase_date: str | Unset = UNSET
        if not isinstance(self.purchase_date, Unset):
            purchase_date = self.purchase_date.isoformat()

        reseller_name = self.reseller_name

        seats = self.seats

        state = self.state

        subscribers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = []
            for subscribers_item_data in self.subscribers:
                subscribers_item = subscribers_item_data.to_dict()
                subscribers.append(subscribers_item)

        subscription_begin_at: str | Unset = UNSET
        if not isinstance(self.subscription_begin_at, Unset):
            subscription_begin_at = self.subscription_begin_at.isoformat()

        subscription_end_at: str | Unset = UNSET
        if not isinstance(self.subscription_end_at, Unset):
            subscription_end_at = self.subscription_end_at.isoformat()

        subscription_id = self.subscription_id

        subscription_type = self.subscription_type

        tax_amount_cents = self.tax_amount_cents

        trial_end: str | Unset = UNSET
        if not isinstance(self.trial_end, Unset):
            trial_end = self.trial_end.isoformat()

        trial_initiated_by = self.trial_initiated_by

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if actual_amount_paid_cents is not UNSET:
            field_dict["actualAmountPaidCents"] = actual_amount_paid_cents
        if amount_cents is not UNSET:
            field_dict["amountCents"] = amount_cents
        if api_allocation_by_plan is not UNSET:
            field_dict["apiAllocationByPlan"] = api_allocation_by_plan
        if api_allocation_end_date is not UNSET:
            field_dict["apiAllocationEndDate"] = api_allocation_end_date
        if api_allocation_override is not UNSET:
            field_dict["apiAllocationOverride"] = api_allocation_override
        if api_allocation_start_date is not UNSET:
            field_dict["apiAllocationStartDate"] = api_allocation_start_date
        if application is not UNSET:
            field_dict["application"] = application
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if card is not UNSET:
            field_dict["card"] = card
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if coupon_amount_off is not UNSET:
            field_dict["couponAmountOff"] = coupon_amount_off
        if coupon_percent_off is not UNSET:
            field_dict["couponPercentOff"] = coupon_percent_off
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if currency is not UNSET:
            field_dict["currency"] = currency
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_months is not UNSET:
            field_dict["durationMonths"] = duration_months
        if group is not UNSET:
            field_dict["group"] = group
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if light_seats is not UNSET:
            field_dict["lightSeats"] = light_seats
        if name is not UNSET:
            field_dict["name"] = name
        if next_charge is not UNSET:
            field_dict["nextCharge"] = next_charge
        if overage_enabled is not UNSET:
            field_dict["overageEnabled"] = overage_enabled
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type
        if pending_cancelation is not UNSET:
            field_dict["pendingCancelation"] = pending_cancelation
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id
        if plan_name is not UNSET:
            field_dict["planName"] = plan_name
        if plan_type is not UNSET:
            field_dict["planType"] = plan_type
        if pre_trial_plan_id is not UNSET:
            field_dict["preTrialPlanId"] = pre_trial_plan_id
        if prorated_charges is not UNSET:
            field_dict["proratedCharges"] = prorated_charges
        if prorated_total is not UNSET:
            field_dict["proratedTotal"] = prorated_total
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if reseller_name is not UNSET:
            field_dict["resellerName"] = reseller_name
        if seats is not UNSET:
            field_dict["seats"] = seats
        if state is not UNSET:
            field_dict["state"] = state
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if subscription_begin_at is not UNSET:
            field_dict["subscriptionBeginAt"] = subscription_begin_at
        if subscription_end_at is not UNSET:
            field_dict["subscriptionEndAt"] = subscription_end_at
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_type is not UNSET:
            field_dict["subscriptionType"] = subscription_type
        if tax_amount_cents is not UNSET:
            field_dict["taxAmountCents"] = tax_amount_cents
        if trial_end is not UNSET:
            field_dict["trialEnd"] = trial_end
        if trial_initiated_by is not UNSET:
            field_dict["trialInitiatedBy"] = trial_initiated_by
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_billing_plan_info import BTBillingPlanInfo
        from ..models.bt_card_info import BTCardInfo
        from ..models.bt_plan_subscriber_info import BTPlanSubscriberInfo
        from ..models.btapi_application_summary_info import BTAPIApplicationSummaryInfo
        from ..models.next_charge import NextCharge
        from ..models.prorated_charges import ProratedCharges

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        actual_amount_paid_cents = d.pop("actualAmountPaidCents", UNSET)

        amount_cents = d.pop("amountCents", UNSET)

        api_allocation_by_plan = d.pop("apiAllocationByPlan", UNSET)

        _api_allocation_end_date = d.pop("apiAllocationEndDate", UNSET)
        api_allocation_end_date: datetime.datetime | Unset
        if isinstance(_api_allocation_end_date, Unset):
            api_allocation_end_date = UNSET
        else:
            api_allocation_end_date = isoparse(_api_allocation_end_date)

        api_allocation_override = d.pop("apiAllocationOverride", UNSET)

        _api_allocation_start_date = d.pop("apiAllocationStartDate", UNSET)
        api_allocation_start_date: datetime.datetime | Unset
        if isinstance(_api_allocation_start_date, Unset):
            api_allocation_start_date = UNSET
        else:
            api_allocation_start_date = isoparse(_api_allocation_start_date)

        _application = d.pop("application", UNSET)
        application: BTAPIApplicationSummaryInfo | Unset
        if isinstance(_application, Unset):
            application = UNSET
        else:
            application = BTAPIApplicationSummaryInfo.from_dict(_application)

        _canceled_at = d.pop("canceledAt", UNSET)
        canceled_at: datetime.datetime | Unset
        if isinstance(_canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = isoparse(_canceled_at)

        _card = d.pop("card", UNSET)
        card: BTCardInfo | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = BTCardInfo.from_dict(_card)

        client_id = d.pop("clientId", UNSET)

        coupon_amount_off = d.pop("couponAmountOff", UNSET)

        coupon_percent_off = d.pop("couponPercentOff", UNSET)

        created_by = d.pop("createdBy", UNSET)

        currency = d.pop("currency", UNSET)

        duration = d.pop("duration", UNSET)

        duration_months = d.pop("durationMonths", UNSET)

        group = d.pop("group", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        last_modified_by = d.pop("lastModifiedBy", UNSET)

        light_seats = d.pop("lightSeats", UNSET)

        name = d.pop("name", UNSET)

        _next_charge = d.pop("nextCharge", UNSET)
        next_charge: NextCharge | Unset
        if isinstance(_next_charge, Unset):
            next_charge = UNSET
        else:
            next_charge = NextCharge.from_dict(_next_charge)

        overage_enabled = d.pop("overageEnabled", UNSET)

        payment_type = d.pop("paymentType", UNSET)

        pending_cancelation = d.pop("pendingCancelation", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: BTBillingPlanInfo | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = BTBillingPlanInfo.from_dict(_plan)

        plan_id = d.pop("planId", UNSET)

        plan_name = d.pop("planName", UNSET)

        plan_type = d.pop("planType", UNSET)

        pre_trial_plan_id = d.pop("preTrialPlanId", UNSET)

        _prorated_charges = d.pop("proratedCharges", UNSET)
        prorated_charges: list[ProratedCharges] | Unset = UNSET
        if _prorated_charges is not UNSET:
            prorated_charges = []
            for prorated_charges_item_data in _prorated_charges:
                prorated_charges_item = ProratedCharges.from_dict(prorated_charges_item_data)

                prorated_charges.append(prorated_charges_item)

        prorated_total = d.pop("proratedTotal", UNSET)

        _purchase_date = d.pop("purchaseDate", UNSET)
        purchase_date: datetime.datetime | Unset
        if isinstance(_purchase_date, Unset):
            purchase_date = UNSET
        else:
            purchase_date = isoparse(_purchase_date)

        reseller_name = d.pop("resellerName", UNSET)

        seats = d.pop("seats", UNSET)

        state = d.pop("state", UNSET)

        _subscribers = d.pop("subscribers", UNSET)
        subscribers: list[BTPlanSubscriberInfo] | Unset = UNSET
        if _subscribers is not UNSET:
            subscribers = []
            for subscribers_item_data in _subscribers:
                subscribers_item = BTPlanSubscriberInfo.from_dict(subscribers_item_data)

                subscribers.append(subscribers_item)

        _subscription_begin_at = d.pop("subscriptionBeginAt", UNSET)
        subscription_begin_at: datetime.datetime | Unset
        if isinstance(_subscription_begin_at, Unset):
            subscription_begin_at = UNSET
        else:
            subscription_begin_at = isoparse(_subscription_begin_at)

        _subscription_end_at = d.pop("subscriptionEndAt", UNSET)
        subscription_end_at: datetime.datetime | Unset
        if isinstance(_subscription_end_at, Unset):
            subscription_end_at = UNSET
        else:
            subscription_end_at = isoparse(_subscription_end_at)

        subscription_id = d.pop("subscriptionId", UNSET)

        subscription_type = d.pop("subscriptionType", UNSET)

        tax_amount_cents = d.pop("taxAmountCents", UNSET)

        _trial_end = d.pop("trialEnd", UNSET)
        trial_end: datetime.datetime | Unset
        if isinstance(_trial_end, Unset):
            trial_end = UNSET
        else:
            trial_end = isoparse(_trial_end)

        trial_initiated_by = d.pop("trialInitiatedBy", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_purchase_info = cls(
            account_id=account_id,
            actual_amount_paid_cents=actual_amount_paid_cents,
            amount_cents=amount_cents,
            api_allocation_by_plan=api_allocation_by_plan,
            api_allocation_end_date=api_allocation_end_date,
            api_allocation_override=api_allocation_override,
            api_allocation_start_date=api_allocation_start_date,
            application=application,
            canceled_at=canceled_at,
            card=card,
            client_id=client_id,
            coupon_amount_off=coupon_amount_off,
            coupon_percent_off=coupon_percent_off,
            created_by=created_by,
            currency=currency,
            duration=duration,
            duration_months=duration_months,
            group=group,
            href=href,
            id=id,
            last_modified=last_modified,
            last_modified_by=last_modified_by,
            light_seats=light_seats,
            name=name,
            next_charge=next_charge,
            overage_enabled=overage_enabled,
            payment_type=payment_type,
            pending_cancelation=pending_cancelation,
            plan=plan,
            plan_id=plan_id,
            plan_name=plan_name,
            plan_type=plan_type,
            pre_trial_plan_id=pre_trial_plan_id,
            prorated_charges=prorated_charges,
            prorated_total=prorated_total,
            purchase_date=purchase_date,
            reseller_name=reseller_name,
            seats=seats,
            state=state,
            subscribers=subscribers,
            subscription_begin_at=subscription_begin_at,
            subscription_end_at=subscription_end_at,
            subscription_id=subscription_id,
            subscription_type=subscription_type,
            tax_amount_cents=tax_amount_cents,
            trial_end=trial_end,
            trial_initiated_by=trial_initiated_by,
            view_ref=view_ref,
        )

        bt_purchase_info.additional_properties = d
        return bt_purchase_info

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
