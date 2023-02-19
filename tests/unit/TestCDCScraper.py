import unittest

class TestCDCScraper(unittest.TestCase):

    def test_getVaccines_cdcSiteDoesNotLoad(self):
        # TODO 404

    def test_getVaccines_vaccinesAndMedicinesTableHtmlIdNotFound(self):
        # TODO 404

    def test_getVaccines_clinicianDiseasesHtmlClassNotFound(self):
        # TODO 404

    def test_getVaccines_countryDoesNotExist(self):
        # TODO 404

    def test_getVaccines_countryHas0Vaccines(self):
        # TODO 

    def test_getVaccines_countryHasManyVaccines(self):
        # TODO 
    
    def test_getVaccines_countryHasManyVaccinesNoRecommendations(self):
        # TODO 

    def test_getVaccines_countryHasManyVaccinesSomeHaveRecommendations(self):
        # TODO 

    def test_getVaccines_countryHasManyVaccinesAllHaveRecommendations(self):
        # TODO 

if __name__ == '__main__':
    unittest.main()