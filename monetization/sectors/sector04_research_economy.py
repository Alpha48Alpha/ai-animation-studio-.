"""
Sector 4 — Research Economy (engines 31–40).

Research outputs — datasets, models, discoveries, and simulations — become
commercially licensable assets on the platform.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

RESEARCH_ECONOMY_ENGINES = [
    RevenueEngine(
        engine_id=31,
        name="Dataset Licensing",
        sector=4,
        revenue_models=[
            RevenueModel.LICENSING,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Curated research datasets licensed to enterprises and academic institutions.",
    ),
    RevenueEngine(
        engine_id=32,
        name="Model Licensing",
        sector=4,
        revenue_models=[
            RevenueModel.LICENSING,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Trained AI and simulation models licensed under tiered access agreements.",
    ),
    RevenueEngine(
        engine_id=33,
        name="Simulation Results Marketplace",
        sector=4,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.LICENSING,
        ],
        description="Marketplace where researchers sell or license completed simulation results.",
    ),
    RevenueEngine(
        engine_id=34,
        name="Scientific Discovery Marketplace",
        sector=4,
        revenue_models=[
            RevenueModel.MARKETPLACE_FEES,
            RevenueModel.LICENSING,
        ],
        description="Exchange for validated AI-generated scientific findings and discoveries.",
    ),
    RevenueEngine(
        engine_id=35,
        name="Collaborative Research Hubs",
        sector=4,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
            RevenueModel.PLATFORM_TRANSACTION_CUT,
        ],
        description="Shared workspaces where multidisciplinary teams co-develop research.",
    ),
    RevenueEngine(
        engine_id=36,
        name="AI-Generated Hypotheses",
        sector=4,
        revenue_models=[
            RevenueModel.LICENSING,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Subscription access to novel, AI-generated scientific hypotheses.",
    ),
    RevenueEngine(
        engine_id=37,
        name="Academic Simulation Grants",
        sector=4,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Grant-funded compute allocations for academic simulation projects.",
    ),
    RevenueEngine(
        engine_id=38,
        name="Pharmaceutical Modeling",
        sector=4,
        revenue_models=[
            RevenueModel.LICENSING,
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
        ],
        description="Drug discovery and pharmacokinetics simulation services for pharma enterprises.",
    ),
    RevenueEngine(
        engine_id=39,
        name="Material Discovery Simulations",
        sector=4,
        revenue_models=[
            RevenueModel.LICENSING,
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
        ],
        description="AI-driven simulations for discovering novel materials and compounds.",
    ),
    RevenueEngine(
        engine_id=40,
        name="Peer-Reviewed Model Repositories",
        sector=4,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
            RevenueModel.LICENSING,
        ],
        description="Vetted repositories of peer-reviewed simulation and AI models.",
    ),
]
