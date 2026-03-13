"""
Sectors package — aggregates all 100 revenue engines across 10 sectors.
"""

from monetization.sectors.sector01_creator_economy import CREATOR_ECONOMY_ENGINES
from monetization.sectors.sector02_ai_agent_marketplace import AI_AGENT_MARKETPLACE_ENGINES
from monetization.sectors.sector03_simulation_services import SIMULATION_SERVICES_ENGINES
from monetization.sectors.sector04_research_economy import RESEARCH_ECONOMY_ENGINES
from monetization.sectors.sector05_education_platforms import EDUCATION_PLATFORMS_ENGINES
from monetization.sectors.sector06_enterprise_intelligence import ENTERPRISE_INTELLIGENCE_ENGINES
from monetization.sectors.sector07_data_economy import DATA_ECONOMY_ENGINES
from monetization.sectors.sector08_developer_ecosystem import DEVELOPER_ECOSYSTEM_ENGINES
from monetization.sectors.sector09_infrastructure_services import INFRASTRUCTURE_SERVICES_ENGINES
from monetization.sectors.sector10_discovery_economy import DISCOVERY_ECONOMY_ENGINES

ALL_SECTORS = (
    CREATOR_ECONOMY_ENGINES
    + AI_AGENT_MARKETPLACE_ENGINES
    + SIMULATION_SERVICES_ENGINES
    + RESEARCH_ECONOMY_ENGINES
    + EDUCATION_PLATFORMS_ENGINES
    + ENTERPRISE_INTELLIGENCE_ENGINES
    + DATA_ECONOMY_ENGINES
    + DEVELOPER_ECOSYSTEM_ENGINES
    + INFRASTRUCTURE_SERVICES_ENGINES
    + DISCOVERY_ECONOMY_ENGINES
)

SECTOR_NAMES = {
    1: "Creator Economy",
    2: "AI Agent Marketplace",
    3: "Simulation Services",
    4: "Research Economy",
    5: "Education Platforms",
    6: "Enterprise Intelligence",
    7: "Data Economy",
    8: "Developer Ecosystem",
    9: "Infrastructure Services",
    10: "Discovery Economy",
}

__all__ = [
    "ALL_SECTORS",
    "SECTOR_NAMES",
    "CREATOR_ECONOMY_ENGINES",
    "AI_AGENT_MARKETPLACE_ENGINES",
    "SIMULATION_SERVICES_ENGINES",
    "RESEARCH_ECONOMY_ENGINES",
    "EDUCATION_PLATFORMS_ENGINES",
    "ENTERPRISE_INTELLIGENCE_ENGINES",
    "DATA_ECONOMY_ENGINES",
    "DEVELOPER_ECOSYSTEM_ENGINES",
    "INFRASTRUCTURE_SERVICES_ENGINES",
    "DISCOVERY_ECONOMY_ENGINES",
]
