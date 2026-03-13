"""
Sector 5 — Education Platforms (engines 41–50).

Universities, schools, and corporate training programs integrate Eight Hour
World simulations as interactive learning environments.
"""

from monetization.sectors.base import RevenueEngine, RevenueModel

EDUCATION_PLATFORMS_ENGINES = [
    RevenueEngine(
        engine_id=41,
        name="Virtual Labs",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.COURSE_LICENSING,
        ],
        description="Immersive virtual laboratory environments for science and engineering education.",
    ),
    RevenueEngine(
        engine_id=42,
        name="AI-Guided Courses",
        sector=5,
        revenue_models=[
            RevenueModel.COURSE_LICENSING,
            RevenueModel.INSTITUTIONAL_CONTRACTS,
        ],
        description="Adaptive AI-curated courses that adjust to learner progress and style.",
    ),
    RevenueEngine(
        engine_id=43,
        name="Simulation Classrooms",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.COURSE_LICENSING,
        ],
        description="Classroom-scale simulation environments for experiential learning.",
    ),
    RevenueEngine(
        engine_id=44,
        name="Digital Campus Worlds",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.ENTERPRISE_SAAS,
        ],
        description="Full virtual campus environments replicating real-world academic experiences.",
    ),
    RevenueEngine(
        engine_id=45,
        name="Student Research Platforms",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.SIMULATION_COMPUTE_BILLING,
        ],
        description="Managed platforms where students conduct and publish simulation research.",
    ),
    RevenueEngine(
        engine_id=46,
        name="Certification Programs",
        sector=5,
        revenue_models=[
            RevenueModel.COURSE_LICENSING,
            RevenueModel.INSTITUTIONAL_CONTRACTS,
        ],
        description="Accredited certification tracks built on platform simulations and AI assessments.",
    ),
    RevenueEngine(
        engine_id=47,
        name="Professional Training Simulations",
        sector=5,
        revenue_models=[
            RevenueModel.COURSE_LICENSING,
            RevenueModel.ENTERPRISE_SAAS,
        ],
        description="Scenario-based professional skills training via high-fidelity simulation.",
    ),
    RevenueEngine(
        engine_id=48,
        name="Corporate Education Portals",
        sector=5,
        revenue_models=[
            RevenueModel.ENTERPRISE_SAAS,
            RevenueModel.INSTITUTIONAL_CONTRACTS,
        ],
        description="Enterprise-branded education portals powered by platform content and AI tutors.",
    ),
    RevenueEngine(
        engine_id=49,
        name="AI Curriculum Generation",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.COURSE_LICENSING,
        ],
        description="Automated AI-generated curricula aligned to institutional learning objectives.",
    ),
    RevenueEngine(
        engine_id=50,
        name="Academic Publishing Platforms",
        sector=5,
        revenue_models=[
            RevenueModel.INSTITUTIONAL_CONTRACTS,
            RevenueModel.LICENSING,
        ],
        description="Publishing and distribution platforms for academic simulation studies.",
    ),
]
