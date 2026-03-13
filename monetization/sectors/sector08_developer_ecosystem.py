"""
Sector 8 — Developer Ecosystem (engines 71–80).

Developers extend the platform through plugins, integrations, visualisation
modules, automation tools, and enterprise connectors.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

DEVELOPER_ECOSYSTEM_ENGINES = [
    RevenueEngine(
        engine_id=71,
        name="Simulation Plugins",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Modular simulation extensions sold through the developer plugin marketplace.",
    ),
    RevenueEngine(
        engine_id=72,
        name="AI Model Integrations",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Connectors that bring third-party AI models into the platform ecosystem.",
    ),
    RevenueEngine(
        engine_id=73,
        name="Visualization Modules",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Data visualisation components and rendering engines for simulation output.",
    ),
    RevenueEngine(
        engine_id=74,
        name="Dashboard Frameworks",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Configurable analytics dashboard frameworks for simulation monitoring.",
    ),
    RevenueEngine(
        engine_id=75,
        name="Automation Scripts",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Pre-built automation scripts for repeatable simulation workflows.",
    ),
    RevenueEngine(
        engine_id=76,
        name="World-Generation Engines",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Procedural and AI-driven world generation engines for rapid environment creation.",
    ),
    RevenueEngine(
        engine_id=77,
        name="AI Workflow Tools",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="No-code and low-code tools for building AI-driven simulation workflows.",
    ),
    RevenueEngine(
        engine_id=78,
        name="Simulation Debugging Tools",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Developer tools for identifying, diagnosing, and resolving simulation anomalies.",
    ),
    RevenueEngine(
        engine_id=79,
        name="Data Pipeline Integrations",
        sector=8,
        revenue_models=[
            RevenueModel.PLUGIN_MARKETPLACE,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Connectors and adapters for ingesting and exporting data across systems.",
    ),
    RevenueEngine(
        engine_id=80,
        name="Enterprise Connectors",
        sector=8,
        revenue_models=[
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
            RevenueModel.DEVELOPER_REVENUE_SHARING,
        ],
        description="Certified enterprise system connectors (ERP, CRM, BI) for platform integration.",
    ),
]
