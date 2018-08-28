"""Mapping templates for coverage gap data.

This code is automatically generated by gbd_mapping_generator/coverage_gap_builder.py

Any manual changes will be lost.
"""
from typing import Tuple, Union

from .id import reiid
from .base_template import GbdRecord, Levels, Restrictions
from .cause_template import Cause
from .risk_template import Risk


class HealthcareTechnology(GbdRecord):
    """Container for healthcare technology and metadata."""
    __slots__ = ('name', )

    def __init__(self,
                 name: str, ):
        super().__init__()
        self.name = name


class CoverageGap(GbdRecord):
    """Container for coverage gap GBD ids and metadata."""
    __slots__ = ('name', 'gbd_id', 'restrictions', 'distribution', 'levels', 'affected_causes', 'affected_risk_factors',
                 'healthcare_technologies', )

    def __init__(self,
                 name: str,
                 gbd_id: Union[reiid, None],
                 restrictions: Restrictions,
                 distribution: str,
                 levels: Levels,
                 affected_causes: Tuple[Cause, ...] = None,
                 affected_risk_factors: Tuple[Risk, ...] = None,
                 healthcare_technologies: Tuple[HealthcareTechnology, ...] = None, ):
        super().__init__()
        self.name = name
        self.gbd_id = gbd_id
        self.restrictions = restrictions
        self.distribution = distribution
        self.levels = levels
        self.affected_causes = affected_causes
        self.affected_risk_factors = affected_risk_factors
        self.healthcare_technologies = healthcare_technologies


class CoverageGaps(GbdRecord):
    """Container for coverage gap data."""
    __slots__ = ('low_measles_vaccine_coverage_first_dose', 'low_oral_rehydration_solution_coverage',
                 'lack_of_hiv_positive_antiretroviral_treatment', )

    def __init__(self,
                 low_measles_vaccine_coverage_first_dose: CoverageGap,
                 low_oral_rehydration_solution_coverage: CoverageGap,
                 lack_of_hiv_positive_antiretroviral_treatment: CoverageGap, ):
        super().__init__()
        self.low_measles_vaccine_coverage_first_dose = low_measles_vaccine_coverage_first_dose
        self.low_oral_rehydration_solution_coverage = low_oral_rehydration_solution_coverage
        self.lack_of_hiv_positive_antiretroviral_treatment = lack_of_hiv_positive_antiretroviral_treatment
