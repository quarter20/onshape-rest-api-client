import ast
import pathlib
import sys

# Checks that models/__init__.py came from templates/models_init.py.jinja, and that nothing else in
# the generated code defeats it. Run by build.sh after regeneration.
#
# The static checks use only the standard library, so this runs on whatever python3 is on PATH.
# Actually importing a model needs httpx/attrs/dateutil, so that part runs only when they happen to
# be installed -- under `poetry run`, for instance.

PACKAGE = pathlib.Path(__file__).parent / "onshape_rest_api_client"
MODELS_INIT = PACKAGE / "models" / "__init__.py"

# Resolving one model pulls in a handful of siblings it refers to at runtime; anything beyond this
# means the laziness has broken down.
MAX_LOADED_MODULES = 25


def get_exported_names() -> tuple[str, ...]:
    """Returns the names in models/__init__.py's __all__, checking it is the lazy version first."""
    tree = ast.parse(MODELS_INIT.read_text())

    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    if "__getattr__" not in functions:
        sys.exit(f"{MODELS_INIT} is not lazy -- was --custom-template-path passed to the generator?")

    exported = next(
        (
            ast.literal_eval(node.value)
            for node in tree.body
            if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "__all__"
        ),
        (),
    )
    if not exported:
        sys.exit(f"{MODELS_INIT} exports nothing")
    return exported


def check_no_package_level_model_imports():
    """Rejects `from ..models import Foo`, which would execute models/__init__.py for its side
    effects and drag in every model. The generator emits `from ..models.foo import Foo` instead,
    which stays lazy."""
    eager = [
        f"{path.relative_to(PACKAGE.parent)}:{node.lineno}"
        for path in sorted(PACKAGE.rglob("*.py"))
        if path != MODELS_INIT
        for node in ast.walk(ast.parse(path.read_text()))
        if isinstance(node, ast.ImportFrom) and node.module in ("models", "onshape_rest_api_client.models")
    ]
    if eager:
        sys.exit("generated code imports models at package level, defeating lazy imports:\n  " + "\n  ".join(eager))


def check_lazy_imports():
    exported = get_exported_names()
    check_no_package_level_model_imports()

    try:
        # this library's runtime dependencies, needed to import a model at all
        import attrs  # noqa: F401
        import dateutil  # noqa: F401
        import httpx  # noqa: F401
    except ModuleNotFoundError as exc:
        print(f"ok (static only): {len(exported)} models exported; no {exc.name} on {sys.executable}, skipped import check")
        return

    sys.path.insert(0, str(PACKAGE.parent))
    loaded = lambda: [name for name in sys.modules if name.startswith("onshape_rest_api_client.models.")]

    import onshape_rest_api_client.models as models

    if loaded():
        sys.exit(f"importing the models package eagerly loaded {len(loaded())} model modules")

    name = exported[0]
    if getattr(models, name) is not getattr(models, name):
        sys.exit(f"{name} is not cached in globals() after first access")
    if len(loaded()) > MAX_LOADED_MODULES:
        sys.exit(f"resolving {name} loaded {len(loaded())} model modules")

    from onshape_rest_api_client.api.document import get_document  # noqa: F401  -- a representative endpoint

    if len(loaded()) > MAX_LOADED_MODULES:
        sys.exit(f"importing an endpoint loaded {len(loaded())} model modules")
    print(f"ok: {len(exported)} models exported, {len(loaded())} modules loaded to resolve {name}")


if __name__ == "__main__":
    check_lazy_imports()
