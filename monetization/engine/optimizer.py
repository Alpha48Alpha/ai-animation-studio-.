"""
AI-Driven Monetization Optimization Engine.

Continuously analyses high-value worlds, high-performing simulations, market
demand, and discovery value to suggest new business models, research
investments, and commercialisation opportunities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from monetization.sectors.base import RevenueEngine, RevenueModel


@dataclass
class OpportunitySignal:
    """
    A single signal surfaced by the optimizer.

    Attributes:
        signal_type: Category of opportunity (e.g. 'new_business_model').
        title: Short title describing the opportunity.
        rationale: Explanation of why this opportunity was surfaced.
        related_engines: Engine IDs relevant to this opportunity.
        priority: Normalised priority score between 0.0 and 1.0.
    """

    signal_type: str
    title: str
    rationale: str
    related_engines: List[int] = field(default_factory=list)
    priority: float = 0.5

    def __post_init__(self) -> None:
        if not (0.0 <= self.priority <= 1.0):
            raise ValueError(f"priority must be between 0.0 and 1.0, got {self.priority}")

    def to_dict(self) -> dict:
        return {
            "signal_type": self.signal_type,
            "title": self.title,
            "rationale": self.rationale,
            "related_engines": self.related_engines,
            "priority": self.priority,
        }


@dataclass
class AnalysisContext:
    """
    Runtime context supplied to the optimizer for a given analysis cycle.

    Attributes:
        high_value_worlds: Names or IDs of worlds with elevated activity.
        high_performing_simulations: Simulation identifiers with strong results.
        market_demand_signals: Free-form demand signals from external markets.
        discovery_value_scores: Mapping of discovery ID to its assessed value (0–1).
    """

    high_value_worlds: List[str] = field(default_factory=list)
    high_performing_simulations: List[str] = field(default_factory=list)
    market_demand_signals: List[str] = field(default_factory=list)
    discovery_value_scores: Dict[str, float] = field(default_factory=dict)


class MonetizationOptimizer:
    """
    AI-driven engine that analyses platform signals and recommends monetization
    actions aligned to the 100 revenue engines.

    The optimizer operates on an :class:`AnalysisContext` and produces a ranked
    list of :class:`OpportunitySignal` objects.
    """

    def __init__(self, engines: Optional[List[RevenueEngine]] = None) -> None:
        from monetization.sectors import ALL_SECTORS

        self._engines: List[RevenueEngine] = engines if engines is not None else ALL_SECTORS

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyse(self, context: AnalysisContext) -> List[OpportunitySignal]:
        """
        Run a full analysis cycle and return ranked opportunity signals.

        Args:
            context: Current platform state and market signals.

        Returns:
            List of :class:`OpportunitySignal` objects sorted by priority
            descending (highest priority first).
        """
        signals: List[OpportunitySignal] = []

        signals.extend(self._analyse_high_value_worlds(context))
        signals.extend(self._analyse_market_demand(context))
        signals.extend(self._analyse_discoveries(context))
        signals.extend(self._analyse_compute_demand(context))

        signals.sort(key=lambda s: s.priority, reverse=True)
        return signals

    def suggest_business_models(self, context: AnalysisContext) -> List[str]:
        """Return a list of suggested business model labels for the current context."""
        signals = self.analyse(context)
        return [s.title for s in signals if s.signal_type == "new_business_model"]

    def suggest_research_investments(self, context: AnalysisContext) -> List[str]:
        """Return a list of recommended research investment areas."""
        signals = self.analyse(context)
        return [s.title for s in signals if s.signal_type == "research_investment"]

    def suggest_commercialization_opportunities(self, context: AnalysisContext) -> List[str]:
        """Return a list of commercialisation opportunities."""
        signals = self.analyse(context)
        return [s.title for s in signals if s.signal_type == "commercialization"]

    # ------------------------------------------------------------------
    # Internal analysis helpers
    # ------------------------------------------------------------------

    def _analyse_high_value_worlds(self, context: AnalysisContext) -> List[OpportunitySignal]:
        signals: List[OpportunitySignal] = []
        if context.high_value_worlds:
            signals.append(
                OpportunitySignal(
                    signal_type="new_business_model",
                    title="World Template Monetization Expansion",
                    rationale=(
                        f"{len(context.high_value_worlds)} high-value world(s) detected. "
                        "Convert top-performing worlds into licensable templates and "
                        "subscription creator channels."
                    ),
                    related_engines=[1, 10, 82],
                    priority=min(0.5 + len(context.high_value_worlds) * 0.05, 1.0),
                )
            )
        if context.high_performing_simulations:
            signals.append(
                OpportunitySignal(
                    signal_type="commercialization",
                    title="Simulation Results Marketplace Listing",
                    rationale=(
                        f"{len(context.high_performing_simulations)} high-performing simulation(s) "
                        "identified. Package results for sale on the Simulation Results Marketplace."
                    ),
                    related_engines=[33, 63, 69],
                    priority=min(0.6 + len(context.high_performing_simulations) * 0.04, 1.0),
                )
            )
        return signals

    def _analyse_market_demand(self, context: AnalysisContext) -> List[OpportunitySignal]:
        signals: List[OpportunitySignal] = []
        demand_count = len(context.market_demand_signals)
        if demand_count == 0:
            return signals

        # Map revenue models that are under-represented in current engines
        model_coverage: Dict[str, int] = {}
        for engine in self._engines:
            for rm in engine.revenue_models:
                model_coverage[rm.value] = model_coverage.get(rm.value, 0) + 1

        low_coverage_models = [m for m, cnt in model_coverage.items() if cnt <= 2]
        if low_coverage_models:
            signals.append(
                OpportunitySignal(
                    signal_type="new_business_model",
                    title="Under-Served Revenue Model Expansion",
                    rationale=(
                        f"Market demand signals ({demand_count}) combined with low coverage of "
                        f"revenue models: {', '.join(low_coverage_models[:3])}. "
                        "Introduce new engines targeting these models."
                    ),
                    related_engines=[e.engine_id for e in self._engines[:5]],
                    priority=min(0.4 + demand_count * 0.06, 1.0),
                )
            )

        signals.append(
            OpportunitySignal(
                signal_type="research_investment",
                title="Market-Driven Simulation R&D",
                rationale=(
                    f"Demand signals indicate {demand_count} emerging market need(s). "
                    "Prioritise simulation R&D in corresponding domains."
                ),
                related_engines=[21, 34, 52, 57],
                priority=min(0.35 + demand_count * 0.05, 0.9),
            )
        )
        return signals

    def _analyse_discoveries(self, context: AnalysisContext) -> List[OpportunitySignal]:
        signals: List[OpportunitySignal] = []
        high_value = {
            k: v for k, v in context.discovery_value_scores.items() if v >= 0.7
        }
        if not high_value:
            return signals

        top_discovery = max(high_value, key=lambda k: high_value[k])
        signals.append(
            OpportunitySignal(
                signal_type="commercialization",
                title="High-Value Discovery Commercialization",
                rationale=(
                    f"Discovery '{top_discovery}' scored {high_value[top_discovery]:.2f}. "
                    "Route through Patent Discovery Licensing and the Global Innovation Exchange."
                ),
                related_engines=[91, 92, 99, 100],
                priority=high_value[top_discovery],
            )
        )
        if len(high_value) >= 3:
            signals.append(
                OpportunitySignal(
                    signal_type="new_business_model",
                    title="Discovery Portfolio Auction Bundle",
                    rationale=(
                        f"{len(high_value)} high-value discoveries available. "
                        "Bundle into a timed portfolio auction on the Breakthrough Discovery Auctions engine."
                    ),
                    related_engines=[99, 100, 96],
                    priority=min(0.7 + len(high_value) * 0.02, 1.0),
                )
            )
        return signals

    def _analyse_compute_demand(self, context: AnalysisContext) -> List[OpportunitySignal]:
        signals: List[OpportunitySignal] = []
        total_load = len(context.high_performing_simulations) + len(context.high_value_worlds)
        if total_load >= 5:
            signals.append(
                OpportunitySignal(
                    signal_type="research_investment",
                    title="Infrastructure Scaling Investment",
                    rationale=(
                        f"Combined simulation and world load ({total_load} items) approaching "
                        "capacity thresholds. Invest in GPU Simulation Compute and "
                        "High-Scale Simulation Clusters."
                    ),
                    related_engines=[81, 86, 89, 90],
                    priority=min(0.5 + total_load * 0.03, 0.95),
                )
            )
        return signals

    # ------------------------------------------------------------------
    # Introspection helpers
    # ------------------------------------------------------------------

    def engines_by_sector(self, sector: int) -> List[RevenueEngine]:
        """Return all engines for the given sector number (1–10)."""
        return [e for e in self._engines if e.sector == sector]

    def engines_by_revenue_model(self, model: RevenueModel) -> List[RevenueEngine]:
        """Return all engines that include the specified revenue model."""
        return [e for e in self._engines if model in e.revenue_models]

    @property
    def total_engines(self) -> int:
        return len(self._engines)
