"""
Sector 3 — Simulation Services (engines 21–30).

Organizations run high-fidelity simulations spanning economics, climate,
infrastructure, logistics, and geopolitical scenarios.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

SIMULATION_SERVICES_ENGINES = [
    RevenueEngine(
        engine_id=21,
        name="Economic Forecasting",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Macro and micro-economic forecasting simulations for governments and enterprises.",
    ),
    RevenueEngine(
        engine_id=22,
        name="Supply Chain Simulations",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="End-to-end supply chain stress testing and optimisation simulations.",
    ),
    RevenueEngine(
        engine_id=23,
        name="Climate Modeling",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="High-resolution climate change impact and mitigation modeling.",
    ),
    RevenueEngine(
        engine_id=24,
        name="City Planning Models",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Urban growth, transit, and infrastructure planning simulations.",
    ),
    RevenueEngine(
        engine_id=25,
        name="Infrastructure Simulations",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Physical and digital infrastructure resilience and expansion simulations.",
    ),
    RevenueEngine(
        engine_id=26,
        name="Geopolitical Scenario Modeling",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Multi-actor geopolitical scenario and conflict-resolution simulations.",
    ),
    RevenueEngine(
        engine_id=27,
        name="Energy Grid Simulations",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Renewable and conventional energy grid balancing and expansion simulations.",
    ),
    RevenueEngine(
        engine_id=28,
        name="Logistics Optimization",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Route, warehouse, and last-mile logistics optimisation engines.",
    ),
    RevenueEngine(
        engine_id=29,
        name="Financial Market Modeling",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Synthetic financial market simulations for risk modelling and strategy testing.",
    ),
    RevenueEngine(
        engine_id=30,
        name="Disaster Preparedness Modeling",
        sector=3,
        revenue_models=[
            RevenueModel.ENTERPRISE_SUBSCRIPTIONS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Emergency response, evacuation, and recovery planning simulations.",
    ),
]
