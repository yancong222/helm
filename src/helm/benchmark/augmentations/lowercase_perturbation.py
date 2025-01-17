from random import Random

from .perturbation import Perturbation
from .perturbation_description import PerturbationDescription


class LowerCasePerturbation(Perturbation):
    """
    Simpe perturbation turning input and references into lowercase.
    """

    name: str = "lowercase"

    @property
    def description(self) -> PerturbationDescription:
        return PerturbationDescription(name=self.name, robustness=True)

    def perturb(self, text: str, rng: Random) -> str:
        return text.lower()
