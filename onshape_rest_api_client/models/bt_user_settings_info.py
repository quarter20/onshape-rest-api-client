from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_common_units_info import BTCommonUnitsInfo
    from ..models.bt_default_units_info import BTDefaultUnitsInfo
    from ..models.bt_material_library_settings_info import BTMaterialLibrarySettingsInfo
    from ..models.bt_select_item_view_state_info import BTSelectItemViewStateInfo
    from ..models.bt_substitute_approver_info import BTSubstituteApproverInfo
    from ..models.bt_units_maximum_display_precision_info import BTUnitsMaximumDisplayPrecisionInfo
    from ..models.bt_user_settings_info_units_display_precision import BTUserSettingsInfoUnitsDisplayPrecision
    from ..models.bt_view_manipulation_mouse_key_mapping_info import BTViewManipulationMouseKeyMappingInfo


T = TypeVar("T", bound="BTUserSettingsInfo")


@_attrs_define
class BTUserSettingsInfo:
    """
    Attributes:
        axis_rotation_lock (bool | Unset):
        common_units (BTCommonUnitsInfo | Unset):
        custom_colors (list[str] | Unset):
        default_units (BTDefaultUnitsInfo | Unset):
        display_assembly_properties (bool | Unset):
        drawing_background_id (int | Unset):
        enforce_application_acl (bool | Unset):
        export_drawing_options (str | Unset):
        export_solid_options (str | Unset):
        graphics_render_mode (str | Unset):
        graphics_smooth_edge (str | Unset):
        highlight_laminar_edges (str | Unset):
        id (str | Unset):
        import_options (str | Unset):
        isolate_enable_selection_desire (bool | Unset):
        isolate_hide_transparent (str | Unset):
        isolate_opacity_slider_value (float | Unset):
        locale (str | Unset):
        make_transparent_enable_selection_desire (bool | Unset):
        make_transparent_opacity_slider_value (float | Unset):
        material_library_settings (BTMaterialLibrarySettingsInfo | Unset):
        mini_toolbar_settings (str | Unset):
        mouse_actions (str | Unset):
        perspective_mode_on (str | Unset):
        previous_sketch_font (str | Unset):
        reverse_scroll_wheel_zoom_direction (bool | Unset):
        select_item_view_state_infos (list[BTSelectItemViewStateInfo] | Unset):
        sketch_show_constraints (bool | Unset):
        sketch_show_errors (bool | Unset):
        sketch_show_expressions (bool | Unset):
        startup_page (int | Unset):
        substitute_approvers (list[BTSubstituteApproverInfo] | Unset):
        theme (int | Unset):
        units_display_precision (BTUserSettingsInfoUnitsDisplayPrecision | Unset):
        units_maximum_display_precision (BTUnitsMaximumDisplayPrecisionInfo | Unset):
        use_24_hour_time (bool | Unset):
        use_decimal_comma (bool | Unset):
        view_manipulation_mouse_key_mapping (BTViewManipulationMouseKeyMappingInfo | Unset):
        view_mapping_id (int | Unset):
    """

    axis_rotation_lock: bool | Unset = UNSET
    common_units: BTCommonUnitsInfo | Unset = UNSET
    custom_colors: list[str] | Unset = UNSET
    default_units: BTDefaultUnitsInfo | Unset = UNSET
    display_assembly_properties: bool | Unset = UNSET
    drawing_background_id: int | Unset = UNSET
    enforce_application_acl: bool | Unset = UNSET
    export_drawing_options: str | Unset = UNSET
    export_solid_options: str | Unset = UNSET
    graphics_render_mode: str | Unset = UNSET
    graphics_smooth_edge: str | Unset = UNSET
    highlight_laminar_edges: str | Unset = UNSET
    id: str | Unset = UNSET
    import_options: str | Unset = UNSET
    isolate_enable_selection_desire: bool | Unset = UNSET
    isolate_hide_transparent: str | Unset = UNSET
    isolate_opacity_slider_value: float | Unset = UNSET
    locale: str | Unset = UNSET
    make_transparent_enable_selection_desire: bool | Unset = UNSET
    make_transparent_opacity_slider_value: float | Unset = UNSET
    material_library_settings: BTMaterialLibrarySettingsInfo | Unset = UNSET
    mini_toolbar_settings: str | Unset = UNSET
    mouse_actions: str | Unset = UNSET
    perspective_mode_on: str | Unset = UNSET
    previous_sketch_font: str | Unset = UNSET
    reverse_scroll_wheel_zoom_direction: bool | Unset = UNSET
    select_item_view_state_infos: list[BTSelectItemViewStateInfo] | Unset = UNSET
    sketch_show_constraints: bool | Unset = UNSET
    sketch_show_errors: bool | Unset = UNSET
    sketch_show_expressions: bool | Unset = UNSET
    startup_page: int | Unset = UNSET
    substitute_approvers: list[BTSubstituteApproverInfo] | Unset = UNSET
    theme: int | Unset = UNSET
    units_display_precision: BTUserSettingsInfoUnitsDisplayPrecision | Unset = UNSET
    units_maximum_display_precision: BTUnitsMaximumDisplayPrecisionInfo | Unset = UNSET
    use_24_hour_time: bool | Unset = UNSET
    use_decimal_comma: bool | Unset = UNSET
    view_manipulation_mouse_key_mapping: BTViewManipulationMouseKeyMappingInfo | Unset = UNSET
    view_mapping_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        axis_rotation_lock = self.axis_rotation_lock

        common_units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.common_units, Unset):
            common_units = self.common_units.to_dict()

        custom_colors: list[str] | Unset = UNSET
        if not isinstance(self.custom_colors, Unset):
            custom_colors = self.custom_colors

        default_units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_units, Unset):
            default_units = self.default_units.to_dict()

        display_assembly_properties = self.display_assembly_properties

        drawing_background_id = self.drawing_background_id

        enforce_application_acl = self.enforce_application_acl

        export_drawing_options = self.export_drawing_options

        export_solid_options = self.export_solid_options

        graphics_render_mode = self.graphics_render_mode

        graphics_smooth_edge = self.graphics_smooth_edge

        highlight_laminar_edges = self.highlight_laminar_edges

        id = self.id

        import_options = self.import_options

        isolate_enable_selection_desire = self.isolate_enable_selection_desire

        isolate_hide_transparent = self.isolate_hide_transparent

        isolate_opacity_slider_value = self.isolate_opacity_slider_value

        locale = self.locale

        make_transparent_enable_selection_desire = self.make_transparent_enable_selection_desire

        make_transparent_opacity_slider_value = self.make_transparent_opacity_slider_value

        material_library_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.material_library_settings, Unset):
            material_library_settings = self.material_library_settings.to_dict()

        mini_toolbar_settings = self.mini_toolbar_settings

        mouse_actions = self.mouse_actions

        perspective_mode_on = self.perspective_mode_on

        previous_sketch_font = self.previous_sketch_font

        reverse_scroll_wheel_zoom_direction = self.reverse_scroll_wheel_zoom_direction

        select_item_view_state_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.select_item_view_state_infos, Unset):
            select_item_view_state_infos = []
            for select_item_view_state_infos_item_data in self.select_item_view_state_infos:
                select_item_view_state_infos_item = select_item_view_state_infos_item_data.to_dict()
                select_item_view_state_infos.append(select_item_view_state_infos_item)

        sketch_show_constraints = self.sketch_show_constraints

        sketch_show_errors = self.sketch_show_errors

        sketch_show_expressions = self.sketch_show_expressions

        startup_page = self.startup_page

        substitute_approvers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.substitute_approvers, Unset):
            substitute_approvers = []
            for substitute_approvers_item_data in self.substitute_approvers:
                substitute_approvers_item = substitute_approvers_item_data.to_dict()
                substitute_approvers.append(substitute_approvers_item)

        theme = self.theme

        units_display_precision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_display_precision, Unset):
            units_display_precision = self.units_display_precision.to_dict()

        units_maximum_display_precision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_maximum_display_precision, Unset):
            units_maximum_display_precision = self.units_maximum_display_precision.to_dict()

        use_24_hour_time = self.use_24_hour_time

        use_decimal_comma = self.use_decimal_comma

        view_manipulation_mouse_key_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_manipulation_mouse_key_mapping, Unset):
            view_manipulation_mouse_key_mapping = self.view_manipulation_mouse_key_mapping.to_dict()

        view_mapping_id = self.view_mapping_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axis_rotation_lock is not UNSET:
            field_dict["axisRotationLock"] = axis_rotation_lock
        if common_units is not UNSET:
            field_dict["commonUnits"] = common_units
        if custom_colors is not UNSET:
            field_dict["customColors"] = custom_colors
        if default_units is not UNSET:
            field_dict["defaultUnits"] = default_units
        if display_assembly_properties is not UNSET:
            field_dict["displayAssemblyProperties"] = display_assembly_properties
        if drawing_background_id is not UNSET:
            field_dict["drawingBackgroundId"] = drawing_background_id
        if enforce_application_acl is not UNSET:
            field_dict["enforceApplicationAcl"] = enforce_application_acl
        if export_drawing_options is not UNSET:
            field_dict["exportDrawingOptions"] = export_drawing_options
        if export_solid_options is not UNSET:
            field_dict["exportSolidOptions"] = export_solid_options
        if graphics_render_mode is not UNSET:
            field_dict["graphicsRenderMode"] = graphics_render_mode
        if graphics_smooth_edge is not UNSET:
            field_dict["graphicsSmoothEdge"] = graphics_smooth_edge
        if highlight_laminar_edges is not UNSET:
            field_dict["highlightLaminarEdges"] = highlight_laminar_edges
        if id is not UNSET:
            field_dict["id"] = id
        if import_options is not UNSET:
            field_dict["importOptions"] = import_options
        if isolate_enable_selection_desire is not UNSET:
            field_dict["isolateEnableSelectionDesire"] = isolate_enable_selection_desire
        if isolate_hide_transparent is not UNSET:
            field_dict["isolateHideTransparent"] = isolate_hide_transparent
        if isolate_opacity_slider_value is not UNSET:
            field_dict["isolateOpacitySliderValue"] = isolate_opacity_slider_value
        if locale is not UNSET:
            field_dict["locale"] = locale
        if make_transparent_enable_selection_desire is not UNSET:
            field_dict["makeTransparentEnableSelectionDesire"] = make_transparent_enable_selection_desire
        if make_transparent_opacity_slider_value is not UNSET:
            field_dict["makeTransparentOpacitySliderValue"] = make_transparent_opacity_slider_value
        if material_library_settings is not UNSET:
            field_dict["materialLibrarySettings"] = material_library_settings
        if mini_toolbar_settings is not UNSET:
            field_dict["miniToolbarSettings"] = mini_toolbar_settings
        if mouse_actions is not UNSET:
            field_dict["mouseActions"] = mouse_actions
        if perspective_mode_on is not UNSET:
            field_dict["perspectiveModeOn"] = perspective_mode_on
        if previous_sketch_font is not UNSET:
            field_dict["previousSketchFont"] = previous_sketch_font
        if reverse_scroll_wheel_zoom_direction is not UNSET:
            field_dict["reverseScrollWheelZoomDirection"] = reverse_scroll_wheel_zoom_direction
        if select_item_view_state_infos is not UNSET:
            field_dict["selectItemViewStateInfos"] = select_item_view_state_infos
        if sketch_show_constraints is not UNSET:
            field_dict["sketchShowConstraints"] = sketch_show_constraints
        if sketch_show_errors is not UNSET:
            field_dict["sketchShowErrors"] = sketch_show_errors
        if sketch_show_expressions is not UNSET:
            field_dict["sketchShowExpressions"] = sketch_show_expressions
        if startup_page is not UNSET:
            field_dict["startupPage"] = startup_page
        if substitute_approvers is not UNSET:
            field_dict["substituteApprovers"] = substitute_approvers
        if theme is not UNSET:
            field_dict["theme"] = theme
        if units_display_precision is not UNSET:
            field_dict["unitsDisplayPrecision"] = units_display_precision
        if units_maximum_display_precision is not UNSET:
            field_dict["unitsMaximumDisplayPrecision"] = units_maximum_display_precision
        if use_24_hour_time is not UNSET:
            field_dict["use24HourTime"] = use_24_hour_time
        if use_decimal_comma is not UNSET:
            field_dict["useDecimalComma"] = use_decimal_comma
        if view_manipulation_mouse_key_mapping is not UNSET:
            field_dict["viewManipulationMouseKeyMapping"] = view_manipulation_mouse_key_mapping
        if view_mapping_id is not UNSET:
            field_dict["viewMappingId"] = view_mapping_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_common_units_info import BTCommonUnitsInfo
        from ..models.bt_default_units_info import BTDefaultUnitsInfo
        from ..models.bt_material_library_settings_info import BTMaterialLibrarySettingsInfo
        from ..models.bt_select_item_view_state_info import BTSelectItemViewStateInfo
        from ..models.bt_substitute_approver_info import BTSubstituteApproverInfo
        from ..models.bt_units_maximum_display_precision_info import BTUnitsMaximumDisplayPrecisionInfo
        from ..models.bt_user_settings_info_units_display_precision import BTUserSettingsInfoUnitsDisplayPrecision
        from ..models.bt_view_manipulation_mouse_key_mapping_info import BTViewManipulationMouseKeyMappingInfo

        d = dict(src_dict)
        axis_rotation_lock = d.pop("axisRotationLock", UNSET)

        _common_units = d.pop("commonUnits", UNSET)
        common_units: BTCommonUnitsInfo | Unset
        if isinstance(_common_units, Unset):
            common_units = UNSET
        else:
            common_units = BTCommonUnitsInfo.from_dict(_common_units)

        custom_colors = cast(list[str], d.pop("customColors", UNSET))

        _default_units = d.pop("defaultUnits", UNSET)
        default_units: BTDefaultUnitsInfo | Unset
        if isinstance(_default_units, Unset):
            default_units = UNSET
        else:
            default_units = BTDefaultUnitsInfo.from_dict(_default_units)

        display_assembly_properties = d.pop("displayAssemblyProperties", UNSET)

        drawing_background_id = d.pop("drawingBackgroundId", UNSET)

        enforce_application_acl = d.pop("enforceApplicationAcl", UNSET)

        export_drawing_options = d.pop("exportDrawingOptions", UNSET)

        export_solid_options = d.pop("exportSolidOptions", UNSET)

        graphics_render_mode = d.pop("graphicsRenderMode", UNSET)

        graphics_smooth_edge = d.pop("graphicsSmoothEdge", UNSET)

        highlight_laminar_edges = d.pop("highlightLaminarEdges", UNSET)

        id = d.pop("id", UNSET)

        import_options = d.pop("importOptions", UNSET)

        isolate_enable_selection_desire = d.pop("isolateEnableSelectionDesire", UNSET)

        isolate_hide_transparent = d.pop("isolateHideTransparent", UNSET)

        isolate_opacity_slider_value = d.pop("isolateOpacitySliderValue", UNSET)

        locale = d.pop("locale", UNSET)

        make_transparent_enable_selection_desire = d.pop("makeTransparentEnableSelectionDesire", UNSET)

        make_transparent_opacity_slider_value = d.pop("makeTransparentOpacitySliderValue", UNSET)

        _material_library_settings = d.pop("materialLibrarySettings", UNSET)
        material_library_settings: BTMaterialLibrarySettingsInfo | Unset
        if isinstance(_material_library_settings, Unset):
            material_library_settings = UNSET
        else:
            material_library_settings = BTMaterialLibrarySettingsInfo.from_dict(_material_library_settings)

        mini_toolbar_settings = d.pop("miniToolbarSettings", UNSET)

        mouse_actions = d.pop("mouseActions", UNSET)

        perspective_mode_on = d.pop("perspectiveModeOn", UNSET)

        previous_sketch_font = d.pop("previousSketchFont", UNSET)

        reverse_scroll_wheel_zoom_direction = d.pop("reverseScrollWheelZoomDirection", UNSET)

        _select_item_view_state_infos = d.pop("selectItemViewStateInfos", UNSET)
        select_item_view_state_infos: list[BTSelectItemViewStateInfo] | Unset = UNSET
        if _select_item_view_state_infos is not UNSET:
            select_item_view_state_infos = []
            for select_item_view_state_infos_item_data in _select_item_view_state_infos:
                select_item_view_state_infos_item = BTSelectItemViewStateInfo.from_dict(
                    select_item_view_state_infos_item_data
                )

                select_item_view_state_infos.append(select_item_view_state_infos_item)

        sketch_show_constraints = d.pop("sketchShowConstraints", UNSET)

        sketch_show_errors = d.pop("sketchShowErrors", UNSET)

        sketch_show_expressions = d.pop("sketchShowExpressions", UNSET)

        startup_page = d.pop("startupPage", UNSET)

        _substitute_approvers = d.pop("substituteApprovers", UNSET)
        substitute_approvers: list[BTSubstituteApproverInfo] | Unset = UNSET
        if _substitute_approvers is not UNSET:
            substitute_approvers = []
            for substitute_approvers_item_data in _substitute_approvers:
                substitute_approvers_item = BTSubstituteApproverInfo.from_dict(substitute_approvers_item_data)

                substitute_approvers.append(substitute_approvers_item)

        theme = d.pop("theme", UNSET)

        _units_display_precision = d.pop("unitsDisplayPrecision", UNSET)
        units_display_precision: BTUserSettingsInfoUnitsDisplayPrecision | Unset
        if isinstance(_units_display_precision, Unset):
            units_display_precision = UNSET
        else:
            units_display_precision = BTUserSettingsInfoUnitsDisplayPrecision.from_dict(_units_display_precision)

        _units_maximum_display_precision = d.pop("unitsMaximumDisplayPrecision", UNSET)
        units_maximum_display_precision: BTUnitsMaximumDisplayPrecisionInfo | Unset
        if isinstance(_units_maximum_display_precision, Unset):
            units_maximum_display_precision = UNSET
        else:
            units_maximum_display_precision = BTUnitsMaximumDisplayPrecisionInfo.from_dict(
                _units_maximum_display_precision
            )

        use_24_hour_time = d.pop("use24HourTime", UNSET)

        use_decimal_comma = d.pop("useDecimalComma", UNSET)

        _view_manipulation_mouse_key_mapping = d.pop("viewManipulationMouseKeyMapping", UNSET)
        view_manipulation_mouse_key_mapping: BTViewManipulationMouseKeyMappingInfo | Unset
        if isinstance(_view_manipulation_mouse_key_mapping, Unset):
            view_manipulation_mouse_key_mapping = UNSET
        else:
            view_manipulation_mouse_key_mapping = BTViewManipulationMouseKeyMappingInfo.from_dict(
                _view_manipulation_mouse_key_mapping
            )

        view_mapping_id = d.pop("viewMappingId", UNSET)

        bt_user_settings_info = cls(
            axis_rotation_lock=axis_rotation_lock,
            common_units=common_units,
            custom_colors=custom_colors,
            default_units=default_units,
            display_assembly_properties=display_assembly_properties,
            drawing_background_id=drawing_background_id,
            enforce_application_acl=enforce_application_acl,
            export_drawing_options=export_drawing_options,
            export_solid_options=export_solid_options,
            graphics_render_mode=graphics_render_mode,
            graphics_smooth_edge=graphics_smooth_edge,
            highlight_laminar_edges=highlight_laminar_edges,
            id=id,
            import_options=import_options,
            isolate_enable_selection_desire=isolate_enable_selection_desire,
            isolate_hide_transparent=isolate_hide_transparent,
            isolate_opacity_slider_value=isolate_opacity_slider_value,
            locale=locale,
            make_transparent_enable_selection_desire=make_transparent_enable_selection_desire,
            make_transparent_opacity_slider_value=make_transparent_opacity_slider_value,
            material_library_settings=material_library_settings,
            mini_toolbar_settings=mini_toolbar_settings,
            mouse_actions=mouse_actions,
            perspective_mode_on=perspective_mode_on,
            previous_sketch_font=previous_sketch_font,
            reverse_scroll_wheel_zoom_direction=reverse_scroll_wheel_zoom_direction,
            select_item_view_state_infos=select_item_view_state_infos,
            sketch_show_constraints=sketch_show_constraints,
            sketch_show_errors=sketch_show_errors,
            sketch_show_expressions=sketch_show_expressions,
            startup_page=startup_page,
            substitute_approvers=substitute_approvers,
            theme=theme,
            units_display_precision=units_display_precision,
            units_maximum_display_precision=units_maximum_display_precision,
            use_24_hour_time=use_24_hour_time,
            use_decimal_comma=use_decimal_comma,
            view_manipulation_mouse_key_mapping=view_manipulation_mouse_key_mapping,
            view_mapping_id=view_mapping_id,
        )

        bt_user_settings_info.additional_properties = d
        return bt_user_settings_info

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
