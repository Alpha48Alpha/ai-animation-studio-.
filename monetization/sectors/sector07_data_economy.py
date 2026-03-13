"""
Sector 7 — Data Economy (engines 61–70).

The platform's knowledge graph becomes a tradeable asset: structured APIs,
simulation archives, economic datasets, and predictive feeds.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

DATA_ECONOMY_ENGINES = [
    RevenueEngine(
        engine_id=61,
        name="Knowledge Graph Access",
        sector=7,
        revenue_models=[
            RevenueModel.API_SUBSCRIPTIONS,
            RevenueModel.DATA_LICENSING,
        ],
        description="Subscription-based access to the Eight Hour World knowledge graph.",
    ),
    RevenueEngine(
        engine_id=62,
        name="Structured Research Data APIs",
        sector=7,
        revenue_models=[
            RevenueModel.API_SUBSCRIPTIONS,
            RevenueModel.DATA_LICENSING,
        ],
        description="Programmatic access to structured, schema-validated research datasets.",
    ),
    RevenueEngine(
        engine_id=63,
        name="Simulation Result APIs",
        sector=7,
        revenue_models=[
            RevenueModel.API_SUBSCRIPTIONS,
            RevenueModel.DATA_LICENSING,
        ],
        description="REST and streaming APIs serving historical and live simulation outputs.",
    ),
    RevenueEngine(
        engine_id=64,
        name="Economic Model Datasets",
        sector=7,
        revenue_models=[
            RevenueModel.DATA_LICENSING,
            RevenueModel.API_SUBSCRIPTIONS,
        ],
        description="Licensed economic model datasets for quantitative research and finance.",
    ),
    RevenueEngine(
        engine_id=65,
        name="Environmental Datasets",
        sector=7,
        revenue_models=[
            RevenueModel.DATA_LICENSING,
            RevenueModel.API_SUBSCRIPTIONS,
        ],
        description="Climate, biodiversity, and environmental impact datasets.",
    ),
    RevenueEngine(
        engine_id=66,
        name="Predictive Analytics Feeds",
        sector=7,
        revenue_models=[
            RevenueModel.API_SUBSCRIPTIONS,
            RevenueModel.ENTERPRISE_SAAS,
        ],
        description="Real-time predictive analytics feeds derived from platform simulations.",
    ),
    RevenueEngine(
        engine_id=67,
        name="AI Training Datasets",
        sector=7,
        revenue_models=[
            RevenueModel.DATA_LICENSING,
            RevenueModel.LICENSING,
        ],
        description="High-quality curated datasets for training and fine-tuning AI models.",
    ),
    RevenueEngine(
        engine_id=68,
        name="Industry Benchmark Datasets",
        sector=7,
        revenue_models=[
            RevenueModel.DATA_LICENSING,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Cross-industry benchmark datasets for performance comparison and analysis.",
    ),
    RevenueEngine(
        engine_id=69,
        name="Global Simulation Archives",
        sector=7,
        revenue_models=[
            RevenueModel.DATA_LICENSING,
            RevenueModel.API_SUBSCRIPTIONS,
        ],
        description="Longitudinal archives of global simulation runs available for retrospective study.",
    ),
    RevenueEngine(
        engine_id=70,
        name="Data-Driven Insight Subscriptions",
        sector=7,
        revenue_models=[
            RevenueModel.API_SUBSCRIPTIONS,
            RevenueModel.ENTERPRISE_SAAS,
        ],
        description="Curated insight packages synthesised from multiple data streams.",
    ),
]
