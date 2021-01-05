class BaseSourceRegionsProvider:
    def source_regions_for_date(self, date):
        raise NotImplementedError()
