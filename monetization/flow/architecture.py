"""
Monetization Flow Architecture — 4-layer value flow model.

Value moves through four layers:

  Layer 1 — Creation    : creators build worlds, agents, and simulations.
  Layer 2 — Discovery   : AI generates new knowledge.
  Layer 3 — Marketplaces: assets are traded across marketplaces.
  Layer 4 — Enterprise  : organisations license simulations, insights, and technologies.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List


class FlowLayer(Enum):
    CREATION = 1
    DISCOVERY = 2
    MARKETPLACES = 3
    ENTERPRISE_INTEGRATION = 4


@dataclass
class LayerDescriptor:
    """Describes a single layer in the monetization flow."""

    layer: FlowLayer
    name: str
    description: str
    participants: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "layer": self.layer.value,
            "name": self.name,
            "description": self.description,
            "participants": self.participants,
            "outputs": self.outputs,
        }


_LAYERS: Dict[FlowLayer, LayerDescriptor] = {
    FlowLayer.CREATION: LayerDescriptor(
        layer=FlowLayer.CREATION,
        name="Creation",
        description="Creators build worlds, agents, and simulations that seed the platform economy.",
        participants=["creators", "developers", "researchers"],
        outputs=[
            "world templates",
            "simulation models",
            "AI agents",
            "datasets",
            "tools and plugins",
        ],
    ),
    FlowLayer.DISCOVERY: LayerDescriptor(
        layer=FlowLayer.DISCOVERY,
        name="Discovery",
        description=(
            "AI agents and simulation engines generate new knowledge, hypotheses, and innovations "
            "that were previously inaccessible or unknown."
        ),
        participants=["AI agents", "research agents", "discovery agents"],
        outputs=[
            "scientific hypotheses",
            "material discoveries",
            "economic insights",
            "patentable innovations",
            "benchmark datasets",
        ],
    ),
    FlowLayer.MARKETPLACES: LayerDescriptor(
        layer=FlowLayer.MARKETPLACES,
        name="Marketplaces",
        description=(
            "Created and discovered assets flow into structured marketplaces where they are "
            "priced, traded, and licensed across buyers and sellers."
        ),
        participants=["creators", "developers", "enterprises", "investors"],
        outputs=[
            "asset transactions",
            "licensing agreements",
            "data subscriptions",
            "IP deals",
            "compute allocations",
        ],
    ),
    FlowLayer.ENTERPRISE_INTEGRATION: LayerDescriptor(
        layer=FlowLayer.ENTERPRISE_INTEGRATION,
        name="Enterprise Integration",
        description=(
            "Organisations license simulations, intelligence systems, datasets, and discoveries, "
            "embedding them into their own operations and products."
        ),
        participants=["enterprises", "governments", "universities", "investors"],
        outputs=[
            "SaaS subscriptions",
            "institutional contracts",
            "API deployments",
            "R&D pipelines",
            "venture portfolios",
        ],
    ),
}


class MonetizationFlowArchitecture:
    """
    Represents the four-layer value flow of the Eight Hour World platform.

    Value moves sequentially from Creation → Discovery → Marketplaces →
    Enterprise Integration, reinforcing itself at each stage.
    """

    @property
    def layers(self) -> List[LayerDescriptor]:
        return list(_LAYERS.values())

    def get_layer(self, layer: FlowLayer) -> LayerDescriptor:
        return _LAYERS[layer]

    def describe(self) -> List[dict]:
        """Return a serialisable summary of all layers."""
        return [layer.to_dict() for layer in self.layers]
