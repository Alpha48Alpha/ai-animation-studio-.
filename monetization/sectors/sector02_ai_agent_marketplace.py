"""
Sector 2 — AI Agent Marketplace (engines 11–20).

Users buy specialized AI agents for research, strategy, enterprise operations,
education and autonomous discovery tasks.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

AI_AGENT_MARKETPLACE_ENGINES = [
    RevenueEngine(
        engine_id=11,
        name="Research Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="AI agents specialized in autonomous research across knowledge domains.",
    ),
    RevenueEngine(
        engine_id=12,
        name="Strategy Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
        ],
        description="Decision-making agents for competitive strategy and long-range planning.",
    ),
    RevenueEngine(
        engine_id=13,
        name="Economic Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Agents that model, simulate, and optimise economic systems.",
    ),
    RevenueEngine(
        engine_id=14,
        name="Engineering Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
        ],
        description="Autonomous engineering assistants for design, optimisation, and testing.",
    ),
    RevenueEngine(
        engine_id=15,
        name="Simulation Analysts",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Agents that interpret simulation outputs and surface actionable insights.",
    ),
    RevenueEngine(
        engine_id=16,
        name="Discovery Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Agents dedicated to autonomous hypothesis generation and scientific discovery.",
    ),
    RevenueEngine(
        engine_id=17,
        name="Enterprise Copilots",
        sector=2,
        revenue_models=[
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Integrated AI copilots deployed within enterprise workflows.",
    ),
    RevenueEngine(
        engine_id=18,
        name="Data Mining Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Agents that extract, structure, and enrich datasets from diverse sources.",
    ),
    RevenueEngine(
        engine_id=19,
        name="World-Management Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
        ],
        description="Administrative agents that maintain, evolve, and monitor simulation worlds.",
    ),
    RevenueEngine(
        engine_id=20,
        name="Education Tutor Agents",
        sector=2,
        revenue_models=[
            RevenueModel.AGENT_LICENSING,
            RevenueModel.SUBSCRIPTION_AGENTS,
        ],
        description="Personalized AI tutors that adapt curricula to individual learner needs.",
    ),
]
