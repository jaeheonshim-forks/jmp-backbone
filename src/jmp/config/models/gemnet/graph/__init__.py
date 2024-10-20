__codegen__ = True

from typing import TYPE_CHECKING

# Config/alias imports

if TYPE_CHECKING:
    from jmp.models.gemnet.graph import CutoffsConfig as CutoffsConfig
    from jmp.models.gemnet.graph import GraphComputerConfig as GraphComputerConfig
    from jmp.models.gemnet.graph import MaxNeighborsConfig as MaxNeighborsConfig
else:

    def __getattr__(name):
        import importlib

        if name in globals():
            return globals()[name]
        if name == "MaxNeighborsConfig":
            return importlib.import_module("jmp.models.gemnet.graph").MaxNeighborsConfig
        if name == "GraphComputerConfig":
            return importlib.import_module(
                "jmp.models.gemnet.graph"
            ).GraphComputerConfig
        if name == "CutoffsConfig":
            return importlib.import_module("jmp.models.gemnet.graph").CutoffsConfig
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Submodule exports
