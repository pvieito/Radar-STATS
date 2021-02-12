import datetime
from typing import *


class EFGSSourceRegionsProvider:
    _efgs_source_regions_additions = [
        # NOTE: https://twitter.com/eu_commission/status/1318149447168262144?s=21
        dict(region="DE", addition_date=datetime.date(2020, 10, 19)),
        dict(region="IE", addition_date=datetime.date(2020, 10, 19)),
        dict(region="IT", addition_date=datetime.date(2020, 10, 19)),
        # NOTE: https://twitter.com/appradarcovid/status/1322142083835142149?s=21
        dict(region="ES", addition_date=datetime.date(2020, 10, 30)),
        dict(region="LV", addition_date=datetime.date(2020, 10, 30)),
        # NOTE: https://twitter.com/dsmeu/status/1325814216285155340?s=21
        dict(region="DK", addition_date=datetime.date(2020, 11, 9)),
        # NOTE: https://twitter.com/dsmeu/status/1330104167566815234?s=21
        dict(region="HR", addition_date=datetime.date(2020, 11, 21)),
        # NOTE: https://twitter.com/dsmeu/status/1331927545768534017?s=21
        dict(region="PL", addition_date=datetime.date(2020, 11, 26)),
        # NOTE: https://twitter.com/dsmeu/status/1334152526371958784?s=21
        dict(region="NL", addition_date=datetime.date(2020, 12, 2)),
        # NOTE: https://twitter.com/dsmeu/status/1346776838010511360?s=21
        dict(region="BE", addition_date=datetime.date(2021, 1, 6)),
        # NOTE: https://twitter.com/dsmeu/status/1347223369201184770?s=21
        dict(region="FI", addition_date=datetime.date(2021, 1, 7)),
        # NOTE: https://twitter.com/dsmeu/status/1357000108366319616?s=21
        dict(region="AT", addition_date=datetime.date(2021, 2, 3)),
        # NOTE: https://twitter.com/dsmeu/status/1360234939808120832?s=21
        dict(region="SI", addition_date=datetime.date(2021, 2, 12)),
    ]

    def __init__(self, native_region, native_periods: List[datetime.date] = None):
        self.native_region = native_region
        self.native_periods = native_periods

    def source_regions_for_date(self, date):
        native_region_addition_date = None
        for source_regions_addition in self._efgs_source_regions_additions:
            if self.native_region == source_regions_addition["region"]:
                native_region_addition_date = source_regions_addition["addition_date"]

        source_regions = {self.native_region}
        if self.native_periods:
            if self.native_periods[0] <= date <= self.native_periods[1]:
                return source_regions

        if native_region_addition_date and date >= native_region_addition_date:
            for source_regions_addition in self._efgs_source_regions_additions:
                if date >= source_regions_addition["addition_date"]:
                    source_regions.add(source_regions_addition["region"])
        return source_regions
