"""
Sector 6 — Enterprise Intelligence (engines 51–60).

Corporations subscribe to intelligence systems powered by platform simulations,
AI models, and knowledge-graph data for strategic decision-making.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

ENTERPRISE_INTELLIGENCE_ENGINES = [
    RevenueEngine(
        engine_id=51,
        name="Strategy Simulation Dashboards",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Real-time dashboards combining live simulation outputs with strategic analytics.",
    ),
    RevenueEngine(
        engine_id=52,
        name="Market Prediction Engines",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="AI-driven market forecasting engines integrated into corporate planning tools.",
    ),
    RevenueEngine(
        engine_id=53,
        name="Supply Chain Intelligence",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Continuous supply chain monitoring, risk scoring, and optimisation intelligence.",
    ),
    RevenueEngine(
        engine_id=54,
        name="Innovation Scouting",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Automated scanning and scoring of emerging technologies and startup activity.",
    ),
    RevenueEngine(
        engine_id=55,
        name="Technology Landscape Analysis",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Comprehensive AI-mapped technology landscape reports updated in near real-time.",
    ),
    RevenueEngine(
        engine_id=56,
        name="Competitor Modeling",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Simulation-based competitor behaviour and market-share modeling.",
    ),
    RevenueEngine(
        engine_id=57,
        name="Industry Trend Forecasting",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Long-horizon industry trend forecasts derived from cross-sector simulations.",
    ),
    RevenueEngine(
        engine_id=58,
        name="Product Launch Simulations",
        sector=6,
        revenue_models=[
            RevenueModel.ENTERPRISE_SAAS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Pre-launch market simulation environments to test product strategies.",
    ),
    RevenueEngine(
        engine_id=59,
        name="Risk Analysis Systems",
        sector=6,
        revenue_models=[RevenueModel.ENTERPRISE_SAAS],
        description="Integrated enterprise risk scoring using simulation and predictive analytics.",
    ),
    RevenueEngine(
        engine_id=60,
        name="Corporate Research Platforms",
        sector=6,
        revenue_models=[
            RevenueModel.ENTERPRISE_SAAS,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Private research environments for corporate R&D teams.",
    ),
]
