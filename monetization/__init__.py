"""
Eight Hour World — Monetization Platform Layer
Version: V10

A 100-component monetization platform organized into 10 sectors × 10 revenue
engines, transforming Eight Hour World into a self-sustaining AI economy.
"""

from monetization.engine.optimizer import MonetizationOptimizer
from monetization.flow.architecture import MonetizationFlowArchitecture
from monetization.marketplace.platform import Platform
from monetization.sectors import ALL_SECTORS

__all__ = [
    "MonetizationOptimizer",
    "MonetizationFlowArchitecture",
    "Platform",
    "ALL_SECTORS",
]

__version__ = "10.0.0"
