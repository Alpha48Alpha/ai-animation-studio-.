"""
Revenue engine base class used by every sector.

Each revenue engine represents one of the 100 monetization mechanisms in the
Eight Hour World platform.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class RevenueModel(Enum):
    MARKETPLACE_FEES = "marketplace_fees"
    CREATOR_ROYALTIES = "creator_royalties"
    PLATFORM_TRANSACTION_CUT = "platform_transaction_cut"
    AGENT_LICENSING = "agent_licensing"
    SUBSCRIPTION_AGENTS = "subscription_agents"
    ENTERPRISE_DEPLOYMENT_FEES = "enterprise_deployment_fees"
    ENTERPRISE_SUBSCRIPTIONS = "enterprise_subscriptions"
    SIMULATION_COMPUTE_BILLING = "simulation_compute_billing"
    LICENSING = "licensing"
    INSTITUTIONAL_SUBSCRIPTIONS = "institutional_subscriptions"
    INSTITUTIONAL_CONTRACTS = "institutional_contracts"
    COURSE_LICENSING = "course_licensing"
    ENTERPRISE_SAAS = "enterprise_saas"
    API_SUBSCRIPTIONS = "api_subscriptions"
    DATA_LICENSING = "data_licensing"
    PLUGIN_MARKETPLACE = "plugin_marketplace"
    DEVELOPER_REVENUE_SHARING = "developer_revenue_sharing"
    CLOUD_COMPUTE_BILLING = "cloud_compute_billing"
    INFRASTRUCTURE_SUBSCRIPTIONS = "infrastructure_subscriptions"
    VENTURE_PARTNERSHIPS = "venture_partnerships"
    IP_ROYALTIES = "ip_royalties"


@dataclass
class RevenueEngine:
    """
    Represents a single monetization mechanism (one of 100 total).

    Attributes:
        engine_id: Global unique identifier (1–100).
        name: Human-readable name of the revenue mechanism.
        sector: The sector this engine belongs to (1–10).
        revenue_models: List of applicable revenue models.
        description: Optional description of the mechanism.
    """

    engine_id: int
    name: str
    sector: int
    revenue_models: List[RevenueModel] = field(default_factory=list)
    description: str = ""

    def __post_init__(self) -> None:
        if not (1 <= self.engine_id <= 100):
            raise ValueError(f"engine_id must be between 1 and 100, got {self.engine_id}")
        if not (1 <= self.sector <= 10):
            raise ValueError(f"sector must be between 1 and 10, got {self.sector}")

    def to_dict(self) -> dict:
        return {
            "engine_id": self.engine_id,
            "name": self.name,
            "sector": self.sector,
            "revenue_models": [rm.value for rm in self.revenue_models],
            "description": self.description,
        }
