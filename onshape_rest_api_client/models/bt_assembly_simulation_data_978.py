from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_simulation_contact_behavior import GBTSimulationContactBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_simulation_2246 import BTAssemblySimulation2246
    from ..models.bt_assembly_simulation_data_978_loads_by_node_id import BTAssemblySimulationData978LoadsByNodeId
    from ..models.btm_load_3538 import BTMLoad3538


T = TypeVar("T", bound="BTAssemblySimulationData978")


@_attrs_define
class BTAssemblySimulationData978:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        contact_behavior (GBTSimulationContactBehavior | Unset):
        loads (list[BTMLoad3538] | Unset):
        loads_by_node_id (BTAssemblySimulationData978LoadsByNodeId | Unset):
        simulations (list[BTAssemblySimulation2246] | Unset):
        structural_loads (list[BTMLoad3538] | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    contact_behavior: GBTSimulationContactBehavior | Unset = UNSET
    loads: list[BTMLoad3538] | Unset = UNSET
    loads_by_node_id: BTAssemblySimulationData978LoadsByNodeId | Unset = UNSET
    simulations: list[BTAssemblySimulation2246] | Unset = UNSET
    structural_loads: list[BTMLoad3538] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        contact_behavior: str | Unset = UNSET
        if not isinstance(self.contact_behavior, Unset):
            contact_behavior = self.contact_behavior.value

        loads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.loads, Unset):
            loads = []
            for loads_item_data in self.loads:
                loads_item = loads_item_data.to_dict()
                loads.append(loads_item)

        loads_by_node_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loads_by_node_id, Unset):
            loads_by_node_id = self.loads_by_node_id.to_dict()

        simulations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.simulations, Unset):
            simulations = []
            for simulations_item_data in self.simulations:
                simulations_item = simulations_item_data.to_dict()
                simulations.append(simulations_item)

        structural_loads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.structural_loads, Unset):
            structural_loads = []
            for structural_loads_item_data in self.structural_loads:
                structural_loads_item = structural_loads_item_data.to_dict()
                structural_loads.append(structural_loads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if contact_behavior is not UNSET:
            field_dict["contactBehavior"] = contact_behavior
        if loads is not UNSET:
            field_dict["loads"] = loads
        if loads_by_node_id is not UNSET:
            field_dict["loadsByNodeId"] = loads_by_node_id
        if simulations is not UNSET:
            field_dict["simulations"] = simulations
        if structural_loads is not UNSET:
            field_dict["structuralLoads"] = structural_loads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_simulation_2246 import BTAssemblySimulation2246
        from ..models.bt_assembly_simulation_data_978_loads_by_node_id import BTAssemblySimulationData978LoadsByNodeId
        from ..models.btm_load_3538 import BTMLoad3538

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _contact_behavior = d.pop("contactBehavior", UNSET)
        contact_behavior: GBTSimulationContactBehavior | Unset
        if isinstance(_contact_behavior, Unset):
            contact_behavior = UNSET
        else:
            contact_behavior = GBTSimulationContactBehavior(_contact_behavior)

        _loads = d.pop("loads", UNSET)
        loads: list[BTMLoad3538] | Unset = UNSET
        if _loads is not UNSET:
            loads = []
            for loads_item_data in _loads:
                loads_item = BTMLoad3538.from_dict(loads_item_data)

                loads.append(loads_item)

        _loads_by_node_id = d.pop("loadsByNodeId", UNSET)
        loads_by_node_id: BTAssemblySimulationData978LoadsByNodeId | Unset
        if isinstance(_loads_by_node_id, Unset):
            loads_by_node_id = UNSET
        else:
            loads_by_node_id = BTAssemblySimulationData978LoadsByNodeId.from_dict(_loads_by_node_id)

        _simulations = d.pop("simulations", UNSET)
        simulations: list[BTAssemblySimulation2246] | Unset = UNSET
        if _simulations is not UNSET:
            simulations = []
            for simulations_item_data in _simulations:
                simulations_item = BTAssemblySimulation2246.from_dict(simulations_item_data)

                simulations.append(simulations_item)

        _structural_loads = d.pop("structuralLoads", UNSET)
        structural_loads: list[BTMLoad3538] | Unset = UNSET
        if _structural_loads is not UNSET:
            structural_loads = []
            for structural_loads_item_data in _structural_loads:
                structural_loads_item = BTMLoad3538.from_dict(structural_loads_item_data)

                structural_loads.append(structural_loads_item)

        bt_assembly_simulation_data_978 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            contact_behavior=contact_behavior,
            loads=loads,
            loads_by_node_id=loads_by_node_id,
            simulations=simulations,
            structural_loads=structural_loads,
        )

        bt_assembly_simulation_data_978.additional_properties = d
        return bt_assembly_simulation_data_978

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
