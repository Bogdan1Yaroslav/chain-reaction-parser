from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .params import PATH
from selenium import webdriver


class WebScraper(webdriver.Chrome):
    def __init__(self, driver_path=PATH,
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(WebScraper, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_page(self, url):
        self.get(url)

    def find_all_products_urls(self):
        products_urls_lst = [elem.get_attribute('href') for elem in self.find_elements(
            By.CSS_SELECTOR, 'div.products_details_container>div.products_details>ul>li.description>a')]

        return products_urls_lst

    def find_accept_cookies_btn(self):
        try:
            accept_cookies_button = self.find_element(By.CSS_SELECTOR, 'button.truste-button1')
            return accept_cookies_button
        except NoSuchElementException:
            return None

    def get_product_category(self):

        try:
            product_category = self.find_element(By.XPATH, '//div[@class="breadcrumb"]').text
        except NoSuchElementException:
            product_category = None

        return product_category

    def get_product_name(self):

        try:
            product_name = self.find_element(By.XPATH, '//h2[@class="from-description-field"]').text
        except NoSuchElementException:
            product_name = None

        return product_name

    def get_product_price(self):

        try:
            product_price = self.find_element(By.XPATH, '//div[@class="crcPDPPriceCurrent"]').text
        except NoSuchElementException:
            product_price = 'Not defined'

        return product_price

    def get_product_specification(self):

        try:
            product_specs = self.find_element(By.XPATH, '//ul[@class="crcPDPList"]').text
        except NoSuchElementException:
            product_specs = 'Not defined'

        return product_specs

    def get_product_rating(self):

        try:
            product_rating = self.find_element(By.XPATH, '//div[@itemprop="ratingValue"]').text
        except NoSuchElementException:
            product_rating = 0

        return product_rating

    def get_product_reviews_number(self):
        product_reviews_num = self.find_element(By.XPATH, '//div[@class="bv_numReviews_text"]').text

        product_reviews_num = product_reviews_num.replace('(', '').replace(')', '')
        return product_reviews_num

    # def set_currency(self, currency=None):
    #     '''default currency is GBP.'''
    #     pass
