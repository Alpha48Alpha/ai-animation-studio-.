"""
Tests for the Eight Hour World Monetization Platform Layer V10.

Covers:
- Revenue engine data integrity (100 engines, correct IDs and sectors)
- All sector modules (10 sectors × 10 engines)
- Monetization Flow Architecture (4 layers)
- AI-driven optimizer (signal generation and ranking)
- Platform top-level orchestrator (query API and summary)
"""

import pytest

from monetization.engine.optimizer import AnalysisContext, MonetizationOptimizer, OpportunitySignal
from monetization.flow.architecture import FlowLayer, MonetizationFlowArchitecture
from monetization.marketplace.platform import Platform
from monetization.sectors import (
    ALL_SECTORS,
    SECTOR_NAMES,
    AI_AGENT_MARKETPLACE_ENGINES,
    CREATOR_ECONOMY_ENGINES,
    DATA_ECONOMY_ENGINES,
    DEVELOPER_ECOSYSTEM_ENGINES,
    DISCOVERY_ECONOMY_ENGINES,
    EDUCATION_PLATFORMS_ENGINES,
    ENTERPRISE_INTELLIGENCE_ENGINES,
    INFRASTRUCTURE_SERVICES_ENGINES,
    RESEARCH_ECONOMY_ENGINES,
    SIMULATION_SERVICES_ENGINES,
)
from monetization.sectors.base import RevenueEngine, RevenueModel


# ---------------------------------------------------------------------------
# Revenue engine data integrity
# ---------------------------------------------------------------------------


class TestRevenueEngine:
    def test_engine_count_is_100(self):
        assert len(ALL_SECTORS) == 100

    def test_engine_ids_are_unique(self):
        ids = [e.engine_id for e in ALL_SECTORS]
        assert len(ids) == len(set(ids)), "Duplicate engine IDs found"

    def test_engine_ids_are_1_to_100(self):
        ids = sorted(e.engine_id for e in ALL_SECTORS)
        assert ids == list(range(1, 101))

    def test_all_engines_have_names(self):
        for engine in ALL_SECTORS:
            assert engine.name, f"Engine {engine.engine_id} has no name"

    def test_all_engines_have_at_least_one_revenue_model(self):
        for engine in ALL_SECTORS:
            assert engine.revenue_models, f"Engine {engine.engine_id} has no revenue models"

    def test_invalid_engine_id_raises(self):
        with pytest.raises(ValueError):
            RevenueEngine(engine_id=0, name="Bad", sector=1, revenue_models=[])

    def test_invalid_sector_raises(self):
        with pytest.raises(ValueError):
            RevenueEngine(engine_id=1, name="Bad", sector=11, revenue_models=[])

    def test_to_dict_returns_expected_keys(self):
        engine = ALL_SECTORS[0]
        d = engine.to_dict()
        assert set(d.keys()) == {"engine_id", "name", "sector", "revenue_models", "description"}

    def test_revenue_models_are_enum_values(self):
        for engine in ALL_SECTORS:
            for rm in engine.revenue_models:
                assert isinstance(rm, RevenueModel)


# ---------------------------------------------------------------------------
# Sector-level tests
# ---------------------------------------------------------------------------


class TestSectors:
    @pytest.mark.parametrize(
        "sector_engines",
        [
            CREATOR_ECONOMY_ENGINES,
            AI_AGENT_MARKETPLACE_ENGINES,
            SIMULATION_SERVICES_ENGINES,
            RESEARCH_ECONOMY_ENGINES,
            EDUCATION_PLATFORMS_ENGINES,
            ENTERPRISE_INTELLIGENCE_ENGINES,
            DATA_ECONOMY_ENGINES,
            DEVELOPER_ECOSYSTEM_ENGINES,
            INFRASTRUCTURE_SERVICES_ENGINES,
            DISCOVERY_ECONOMY_ENGINES,
        ],
    )
    def test_sector_engine_count(self, sector_engines):
        assert len(sector_engines) == 10

    @pytest.mark.parametrize(
        "sector_engines, expected_range",
        [
            (CREATOR_ECONOMY_ENGINES, range(1, 11)),
            (AI_AGENT_MARKETPLACE_ENGINES, range(11, 21)),
            (SIMULATION_SERVICES_ENGINES, range(21, 31)),
            (RESEARCH_ECONOMY_ENGINES, range(31, 41)),
            (EDUCATION_PLATFORMS_ENGINES, range(41, 51)),
            (ENTERPRISE_INTELLIGENCE_ENGINES, range(51, 61)),
            (DATA_ECONOMY_ENGINES, range(61, 71)),
            (DEVELOPER_ECOSYSTEM_ENGINES, range(71, 81)),
            (INFRASTRUCTURE_SERVICES_ENGINES, range(81, 91)),
            (DISCOVERY_ECONOMY_ENGINES, range(91, 101)),
        ],
    )
    def test_sector_ids_in_range(self, sector_engines, expected_range):
        for engine in sector_engines:
            assert engine.engine_id in expected_range

    @pytest.mark.parametrize(
        "sector_engines, expected_sector",
        [
            (CREATOR_ECONOMY_ENGINES, 1),
            (AI_AGENT_MARKETPLACE_ENGINES, 2),
            (SIMULATION_SERVICES_ENGINES, 3),
            (RESEARCH_ECONOMY_ENGINES, 4),
            (EDUCATION_PLATFORMS_ENGINES, 5),
            (ENTERPRISE_INTELLIGENCE_ENGINES, 6),
            (DATA_ECONOMY_ENGINES, 7),
            (DEVELOPER_ECOSYSTEM_ENGINES, 8),
            (INFRASTRUCTURE_SERVICES_ENGINES, 9),
            (DISCOVERY_ECONOMY_ENGINES, 10),
        ],
    )
    def test_sector_number_correct(self, sector_engines, expected_sector):
        for engine in sector_engines:
            assert engine.sector == expected_sector

    def test_sector_names_coverage(self):
        assert len(SECTOR_NAMES) == 10
        for i in range(1, 11):
            assert i in SECTOR_NAMES
            assert SECTOR_NAMES[i]


# ---------------------------------------------------------------------------
# Monetization Flow Architecture
# ---------------------------------------------------------------------------


class TestMonetizationFlowArchitecture:
    def setup_method(self):
        self.flow = MonetizationFlowArchitecture()

    def test_four_layers_exist(self):
        assert len(self.flow.layers) == 4

    def test_all_flow_layers_present(self):
        layer_enums = {layer.layer for layer in self.flow.layers}
        assert layer_enums == set(FlowLayer)

    def test_describe_returns_list_of_dicts(self):
        descriptions = self.flow.describe()
        assert isinstance(descriptions, list)
        assert len(descriptions) == 4
        for d in descriptions:
            assert "name" in d
            assert "description" in d
            assert "participants" in d
            assert "outputs" in d

    def test_creation_layer_has_participants(self):
        layer = self.flow.get_layer(FlowLayer.CREATION)
        assert len(layer.participants) > 0

    def test_enterprise_layer_has_outputs(self):
        layer = self.flow.get_layer(FlowLayer.ENTERPRISE_INTEGRATION)
        assert len(layer.outputs) > 0


# ---------------------------------------------------------------------------
# Monetization Optimizer
# ---------------------------------------------------------------------------


class TestMonetizationOptimizer:
    def setup_method(self):
        self.optimizer = MonetizationOptimizer()

    def test_total_engines_is_100(self):
        assert self.optimizer.total_engines == 100

    def test_analyse_returns_list(self):
        ctx = AnalysisContext()
        result = self.optimizer.analyse(ctx)
        assert isinstance(result, list)

    def test_analyse_empty_context_returns_no_signals(self):
        ctx = AnalysisContext()
        result = self.optimizer.analyse(ctx)
        assert result == []

    def test_analyse_high_value_worlds_produces_signals(self):
        ctx = AnalysisContext(high_value_worlds=["World-A", "World-B"])
        result = self.optimizer.analyse(ctx)
        assert len(result) > 0

    def test_analyse_signals_sorted_by_priority_descending(self):
        ctx = AnalysisContext(
            high_value_worlds=["World-A"],
            high_performing_simulations=["Sim-1", "Sim-2"],
            market_demand_signals=["pharma", "climate"],
            discovery_value_scores={"discovery-X": 0.9, "discovery-Y": 0.75},
        )
        signals = self.optimizer.analyse(ctx)
        priorities = [s.priority for s in signals]
        assert priorities == sorted(priorities, reverse=True)

    def test_opportunity_signal_priority_bounds(self):
        ctx = AnalysisContext(
            high_value_worlds=["W"] * 20,
            market_demand_signals=["x"] * 20,
        )
        for signal in self.optimizer.analyse(ctx):
            assert 0.0 <= signal.priority <= 1.0

    def test_invalid_priority_raises(self):
        with pytest.raises(ValueError):
            OpportunitySignal(
                signal_type="test",
                title="Bad",
                rationale="Bad priority",
                priority=1.5,
            )

    def test_engines_by_sector_count(self):
        for sector in range(1, 11):
            engines = self.optimizer.engines_by_sector(sector)
            assert len(engines) == 10

    def test_engines_by_revenue_model_marketplace_fees(self):
        engines = self.optimizer.engines_by_revenue_model(RevenueModel.MARKETPLACE_FEES)
        assert len(engines) > 0
        for engine in engines:
            assert RevenueModel.MARKETPLACE_FEES in engine.revenue_models

    def test_suggest_business_models_returns_strings(self):
        ctx = AnalysisContext(high_value_worlds=["W1"])
        result = self.optimizer.suggest_business_models(ctx)
        assert all(isinstance(s, str) for s in result)

    def test_suggest_research_investments_returns_strings(self):
        ctx = AnalysisContext(market_demand_signals=["climate"])
        result = self.optimizer.suggest_research_investments(ctx)
        assert all(isinstance(s, str) for s in result)

    def test_discovery_signals_fired_for_high_scores(self):
        ctx = AnalysisContext(
            discovery_value_scores={"disc-1": 0.95, "disc-2": 0.80, "disc-3": 0.72}
        )
        signals = self.optimizer.analyse(ctx)
        assert any(s.signal_type == "commercialization" for s in signals)

    def test_infrastructure_signal_fired_for_high_load(self):
        ctx = AnalysisContext(
            high_value_worlds=["W1", "W2", "W3"],
            high_performing_simulations=["S1", "S2", "S3"],
        )
        signals = self.optimizer.analyse(ctx)
        assert any("Infrastructure" in s.title for s in signals)


# ---------------------------------------------------------------------------
# Platform orchestrator
# ---------------------------------------------------------------------------


class TestPlatform:
    def setup_method(self):
        self.platform = Platform()

    def test_total_engines_is_100(self):
        assert self.platform.total_engines == 100

    def test_get_engine_returns_correct_engine(self):
        engine = self.platform.get_engine(1)
        assert engine is not None
        assert engine.engine_id == 1

    def test_get_engine_returns_none_for_invalid_id(self):
        assert self.platform.get_engine(999) is None

    def test_get_sector_returns_10_engines(self):
        for sector in range(1, 11):
            engines = self.platform.get_sector(sector)
            assert len(engines) == 10

    def test_summary_structure(self):
        summary = self.platform.summary()
        assert summary["version"] == "V10"
        assert summary["total_engines"] == 100
        assert len(summary["sectors"]) == 10
        assert len(summary["flow_layers"]) == 4

    def test_summary_sector_engine_counts(self):
        summary = self.platform.summary()
        for sector_num in range(1, 11):
            sector_data = summary["sectors"][sector_num]
            assert sector_data["engine_count"] == 10
            assert len(sector_data["engine_ids"]) == 10

    def test_build_context_defaults(self):
        ctx = Platform.build_context()
        assert ctx.high_value_worlds == []
        assert ctx.high_performing_simulations == []
        assert ctx.market_demand_signals == []
        assert ctx.discovery_value_scores == {}

    def test_optimize_returns_signals(self):
        ctx = self.platform.build_context(
            high_value_worlds=["World-1"],
            market_demand_signals=["renewable energy"],
        )
        signals = self.platform.optimize(ctx)
        assert len(signals) > 0

    def test_optimize_signal_types_are_known(self):
        known_types = {"new_business_model", "research_investment", "commercialization"}
        ctx = self.platform.build_context(
            high_value_worlds=["W1", "W2"],
            high_performing_simulations=["S1", "S2", "S3"],
            market_demand_signals=["climate", "pharma"],
            discovery_value_scores={"d1": 0.85},
        )
        for signal in self.platform.optimize(ctx):
            assert signal.signal_type in known_types

    def test_get_engines_by_revenue_model(self):
        engines = self.platform.get_engines_by_revenue_model(RevenueModel.ENTERPRISE_SAAS)
        assert len(engines) > 0

    def test_sector_names_complete(self):
        names = self.platform.sector_names
        assert len(names) == 10
        for i in range(1, 11):
            assert i in names
