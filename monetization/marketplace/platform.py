"""
Platform — top-level orchestrator for the Eight Hour World Monetization Platform.

Brings together all 100 revenue engines, the 4-layer flow architecture, and the
AI-driven monetization optimizer into a unified API surface.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from monetization.engine.optimizer import AnalysisContext, MonetizationOptimizer, OpportunitySignal
from monetization.flow.architecture import MonetizationFlowArchitecture
from monetization.sectors import ALL_SECTORS, SECTOR_NAMES
from monetization.sectors.base import RevenueEngine, RevenueModel


class Platform:
    """
    Eight Hour World Monetization Platform V10.

    A self-sustaining AI economy that connects creators, researchers,
    enterprises, and AI agents through 100 revenue engines, a 4-layer
    value-flow architecture, and an AI optimization engine.

    Example usage::

        platform = Platform()
        print(f"Engines loaded: {platform.total_engines}")

        context = platform.build_context(
            high_value_worlds=["MegaCity-7", "BioSim-3"],
            market_demand_signals=["pharmaceutical AI", "climate risk"],
        )
        signals = platform.optimize(context)
        for signal in signals:
            print(signal.title, signal.priority)
    """

    def __init__(self) -> None:
        self._engines: List[RevenueEngine] = ALL_SECTORS
        self._flow = MonetizationFlowArchitecture()
        self._optimizer = MonetizationOptimizer(engines=self._engines)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def total_engines(self) -> int:
        """Total number of revenue engines registered on the platform."""
        return len(self._engines)

    @property
    def sector_names(self) -> Dict[int, str]:
        """Mapping of sector number to sector name."""
        return dict(SECTOR_NAMES)

    # ------------------------------------------------------------------
    # Query API
    # ------------------------------------------------------------------

    def get_engine(self, engine_id: int) -> Optional[RevenueEngine]:
        """Return the :class:`RevenueEngine` with the given ID, or ``None``."""
        for engine in self._engines:
            if engine.engine_id == engine_id:
                return engine
        return None

    def get_sector(self, sector: int) -> List[RevenueEngine]:
        """Return all engines in the given sector (1–10)."""
        return self._optimizer.engines_by_sector(sector)

    def get_engines_by_revenue_model(self, model: RevenueModel) -> List[RevenueEngine]:
        """Return all engines that use the specified revenue model."""
        return self._optimizer.engines_by_revenue_model(model)

    def summary(self) -> dict:
        """
        Return a high-level platform summary.

        Returns:
            Dict containing engine count, sector breakdown, flow layers, and
            the platform version.
        """
        sector_breakdown = {
            sector_num: {
                "name": name,
                "engine_count": len(self.get_sector(sector_num)),
                "engine_ids": [e.engine_id for e in self.get_sector(sector_num)],
            }
            for sector_num, name in SECTOR_NAMES.items()
        }
        return {
            "version": "V10",
            "total_engines": self.total_engines,
            "sectors": sector_breakdown,
            "flow_layers": self._flow.describe(),
        }

    # ------------------------------------------------------------------
    # Optimization API
    # ------------------------------------------------------------------

    @staticmethod
    def build_context(
        high_value_worlds: Optional[List[str]] = None,
        high_performing_simulations: Optional[List[str]] = None,
        market_demand_signals: Optional[List[str]] = None,
        discovery_value_scores: Optional[Dict[str, float]] = None,
    ) -> AnalysisContext:
        """
        Convenience factory for building an :class:`AnalysisContext`.

        Args:
            high_value_worlds: Names or IDs of worlds with elevated activity.
            high_performing_simulations: Simulation identifiers with strong results.
            market_demand_signals: Free-form demand signals.
            discovery_value_scores: Mapping of discovery ID → value score (0–1).

        Returns:
            A populated :class:`AnalysisContext` ready for ``optimize()``.
        """
        return AnalysisContext(
            high_value_worlds=high_value_worlds or [],
            high_performing_simulations=high_performing_simulations or [],
            market_demand_signals=market_demand_signals or [],
            discovery_value_scores=discovery_value_scores or {},
        )

    def optimize(self, context: AnalysisContext) -> List[OpportunitySignal]:
        """
        Run the AI optimization engine against the provided context.

        Args:
            context: Current platform state and market signals.

        Returns:
            Ranked list of :class:`OpportunitySignal` objects (highest priority first).
        """
        return self._optimizer.analyse(context)
