"""
Sector 1 — Creator Economy (engines 1–10).

Creators build assets for the ecosystem: world templates, simulation models,
AI agent packs, environment libraries and more.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

CREATOR_ECONOMY_ENGINES = [
    RevenueEngine(
        engine_id=1,
        name="World Template Marketplace",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Pre-built world templates sold and licensed across the platform.",
    ),
    RevenueEngine(
        engine_id=2,
        name="Simulation Model Sales",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.PLATFORM_TRANSACTION_CUT,
        ],
        description="Ready-to-run simulation models available for direct purchase.",
    ),
    RevenueEngine(
        engine_id=3,
        name="AI Agent Packs",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Bundled AI agent collections created and sold by platform contributors.",
    ),
    RevenueEngine(
        engine_id=4,
        name="Environment Asset Libraries",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Environmental and visual asset packs for world-building.",
    ),
    RevenueEngine(
        engine_id=5,
        name="City Builder Templates",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.PLATFORM_TRANSACTION_CUT,
        ],
        description="Configurable city simulation templates for urban planning use cases.",
    ),
    RevenueEngine(
        engine_id=6,
        name="Research Simulation Kits",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Packaged research-ready simulation environments for academic and industry use.",
    ),
    RevenueEngine(
        engine_id=7,
        name="Governance Model Packages",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Governance and policy simulation models for public sector and enterprise.",
    ),
    RevenueEngine(
        engine_id=8,
        name="Game Economy Models",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.PLATFORM_TRANSACTION_CUT,
        ],
        description="Virtual economy models for game developers and simulation designers.",
    ),
    RevenueEngine(
        engine_id=9,
        name="Virtual Infrastructure Packs",
        sector=1,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.CREATOR_ROYALTIES,
        ],
        description="Digital infrastructure assets and networks for world simulation.",
    ),
    RevenueEngine(
        engine_id=10,
        name="Subscription Creator Channels",
        sector=1,
        revenue_models=[
            RevenueModel.CREATOR_ROYALTIES,
            RevenueModel.PLATFORM_TRANSACTION_CUT,
        ],
        description="Subscription-based channels where creators publish exclusive content.",
    ),
]
