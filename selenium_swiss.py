# -*- coding: utf-8 -*-

"""
Simple script making use of Selenium to poll Swiss website for flight prices

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json


class SwissAirfareCrawler():

    def __init__(self, orig='ZRH', dest='CDG', out_date='2017-12-15', in_date='2017-12-18'):
        """
        Args:
            orig (str): 3 letter airport code of Origin
            dest (str): 3 letter airport code of Destination
            out_date (str): Date string of Outbound flight date
            in_date (str): Date string of Inbound flight date
        """

        self.start_url = (('https://www.swiss.com/ch/en/Book/Outbound/{}-{}/'
                           'from-{}/to-{}/adults-1/children-0/infants-0/class-economy/al-LX/')
                          .format(orig, dest, out_date, in_date))

        self._results = {}

    @property
    def results(self):
        """dictionary returning list of flights and corresponding prices"""
        return self._results

    def __connect(self):
        self.driver = webdriver.PhantomJS()

        # have to init a random window size, otherwise we get elements invisible errors
        self.driver.set_window_size(1124, 850)

    def __close_connection(self):
        self.driver.close()

    def get_prices(self):
        """Runs the driver and assigns results to property results"""

        self.__connect()

        try:
            self.driver.get(self.start_url)

            self._parse_flight_prices(self.driver, "OUTBOUND")

            # simulate selecting a flight
            (self.driver.find_elements_by_css_selector(".book_bundle > .book_bundle_row")[0]
                        .find_elements_by_css_selector(".book-bundle-button")[0]
                        .click())

            # wait for basket SELECT RETURN FLIGHT element to load
            # sleep(3)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#stickybasket button.btn-submit"))
            )

            # simulate click to load Return Flights
            self.driver.find_element_by_id("stickybasket").find_element_by_css_selector("button.btn-submit").click()

            self._parse_flight_prices(self.driver, "INBOUND")

        except Exception:

            self.__close_connection()
            raise Exception("Error loading prices")

        self.__close_connection()

    def print_results(self):
        print(json.dumps(self._results, sort_keys=True, indent=4))

    def _parse_flight_prices(self, driver, key):

        dep = driver.find_elements_by_css_selector(
            (".book_bundle > .book_bundle_row .book-bundle-flightentry--departure")
        )

        # replace new line characters
        dep = [x.text.replace("\n", " ") for x in dep]

        arr = driver.find_elements_by_css_selector(
            (".book_bundle > .book_bundle_row .book-bundle-flightentry--arrival")
        )

        # replace new line characters
        arr = [x.text.replace("\n", " ") for x in arr]

        price_eco = driver.find_elements_by_css_selector(
            (".book_bundle > .book_bundle_row > "
             ".book_bundle_row--header .book-bundle-button.is-type-economy > .book-bundle-button--price")
        )

        price_eco = [x.text for x in price_eco]

        price_bus = driver.find_elements_by_css_selector(
            (".book_bundle > .book_bundle_row > "
             ".book_bundle_row--header .book-bundle-button.is-type-business > .book-bundle-button--price")
        )

        price_bus = [x.text for x in price_bus]

        if (len(dep) == len(arr) == len(price_eco) == len(price_bus)):

            self._results.update(
                {key: []}
            )

            for i in range(len(dep)):
                self._results[key].append(
                    {
                        "dep_flight": dep[i],
                        "arr_flight": arr[i],
                        "price_eco": price_eco[i],
                        "price_bus": price_bus[i],
                    }
                )

        else:
            raise Exception("Length of results do not match!")
