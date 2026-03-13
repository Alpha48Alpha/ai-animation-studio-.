"""
Sector 9 — Infrastructure Services (engines 81–90).

Heavy simulation workloads require scalable compute, persistent hosting,
AI training infrastructure, and distributed edge nodes.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

INFRASTRUCTURE_SERVICES_ENGINES = [
    RevenueEngine(
        engine_id=81,
        name="GPU Simulation Compute",
        sector=9,
        revenue_models=[
            RevenueModel.CLOUD_COMPUTE_BILLING,
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
        ],
        description="On-demand GPU compute for running large-scale simulation workloads.",
    ),
    RevenueEngine(
        engine_id=82,
        name="Persistent World Hosting",
        sector=9,
        revenue_models=[
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
            RevenueModel.CLOUD_COMPUTE_BILLING,
        ],
        description="Always-on hosting for persistent simulation worlds and digital environments.",
    ),
    RevenueEngine(
        engine_id=83,
        name="Enterprise Private Environments",
        sector=9,
        revenue_models=[
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
        ],
        description="Dedicated private cloud environments for enterprise simulation deployments.",
    ),
    RevenueEngine(
        engine_id=84,
        name="Research Cluster Hosting",
        sector=9,
        revenue_models=[
            RevenueModel.CLOUD_COMPUTE_BILLING,
            RevenueModel.INSTITUTIONAL_SUBSCRIPTIONS,
        ],
        description="Managed HPC clusters tailored for academic and research simulation workloads.",
    ),
    RevenueEngine(
        engine_id=85,
        name="AI Training Infrastructure",
        sector=9,
        revenue_models=[
            RevenueModel.CLOUD_COMPUTE_BILLING,
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
        ],
        description="Optimised compute infrastructure for training large AI and simulation models.",
    ),
    RevenueEngine(
        engine_id=86,
        name="High-Scale Simulation Clusters",
        sector=9,
        revenue_models=[
            RevenueModel.CLOUD_COMPUTE_BILLING,
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
        ],
        description="Auto-scaling simulation clusters for peak demand and burst workloads.",
    ),
    RevenueEngine(
        engine_id=87,
        name="Storage for Simulation Archives",
        sector=9,
        revenue_models=[
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
            RevenueModel.CLOUD_COMPUTE_BILLING,
        ],
        description="Long-term, cost-optimised storage solutions for simulation result archives.",
    ),
    RevenueEngine(
        engine_id=88,
        name="Enterprise Secure Deployments",
        sector=9,
        revenue_models=[
            RevenueModel.ENTERPRISE_DEPLOYMENT_FEES,
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
        ],
        description="Security-hardened, compliance-ready simulation deployments for regulated industries.",
    ),
    RevenueEngine(
        engine_id=89,
        name="Edge Simulation Nodes",
        sector=9,
        revenue_models=[
            RevenueModel.INFRASTRUCTURE_SUBSCRIPTIONS,
            RevenueModel.CLOUD_COMPUTE_BILLING,
        ],
        description="Low-latency edge compute nodes that run lightweight simulations close to users.",
    ),
    RevenueEngine(
        engine_id=90,
        name="Distributed Compute Markets",
        sector=9,
        revenue_models=[
            RevenueModel.CLOUD_COMPUTE_BILLING,
            RevenueModel.MARKETPLACE_FEES,
        ],
        description="Peer-to-peer compute marketplace for renting and monetising idle simulation capacity.",
    ),
]
