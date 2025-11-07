"""
market_analysis_dashboard.py

This tool provides AI product managers with a simple dashboard to evaluate market opportunities by calculating scores for product ideas based on market size, growth rate, competition and strategic fit. It calculates a weighted total score to help prioritize ideas for development.

Usage:
    Define a list of product ideas with metrics (market_size, growth_rate, competition, strategic_fit).
    The script will compute weighted scores and rank them.
"""
from dataclasses import dataclass
from typing import List

@dataclass
class ProductIdea:
    name: str
# Clarify commit message
    market_size: float
    growth_rate: float
    competition: float
    strategic_fit: float

    def score(self, weights=None) -> float:
        if weights is None:
            weights = {'market_size': 0.3, 'growth_rate': 0.3, 'competition': 0.2, 'strategic_fit': 0.2}
        total = (self.market_size * weights['market_size'] +
                 self.growth_rate * weights['growth_rate'] -
                 self.competition * weights['competition'] +
                 self.strategic_fit * weights['strategic_fit'])
        return total

def rank_product_ideas(ideas: List[ProductIdea], weights=None) -> List[ProductIdea]:
    return sorted(ideas, key=lambda idea: idea.score(weights), reverse=True)

if __name__ == "__main__":
    ideas = [
        ProductIdea("Idea A", market_size=8, growth_rate=7, competition=5, strategic_fit=6),
        ProductIdea("Idea B", market_size=6, growth_rate=8, competition=4, strategic_fit=5),
        ProductIdea("Idea C", market_size=7, growth_rate=6, competition=3, strategic_fit=7)
    ]
    ranked = rank_product_ideas(ideas)
    for idea in ranked:
        print(f"{idea.name}: score={idea.score():.2f}")
