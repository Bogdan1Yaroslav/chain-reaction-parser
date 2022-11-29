from time import sleep
from datetime import date
from scraper_module.web_scraper import WebScraper
from scraper_module.data_storage import DataStorageFile


with WebScraper() as bot:
    index_number = 1

    file = DataStorageFile(f'{date.today()} CR products.xlsx')

    for page in range(1, 4):
        bot.get_page(f'https://www.chainreactioncycles.com/bestsellers?page={page}')

        print(f'Page: {page}\n')
        sleep(3)

        accept_cookies_button = bot.find_accept_cookies_btn()

        if accept_cookies_button:
            accept_cookies_button.click()

        products_urls_list = bot.find_all_products_urls()

        for product_item_url in products_urls_list:
            bot.get_page(product_item_url)
            sleep(3)

            product_category = bot.get_product_category()
            product_name = bot.get_product_name()
            product_price = bot.get_product_price()
            product_specs = bot.get_product_specification()
            product_rating = bot.get_product_rating()

            product_reviews_num = bot.get_product_reviews_number()

            data_to_add = [index_number,
                           product_name,
                           product_category,
                           product_price,
                           product_rating,
                           product_reviews_num,
                           product_specs,
                           product_item_url]

            print(f"Product name: {product_name}\n"
                  f"Product category: {product_category}\n"
                  f"Product price: {product_price}\n"
                  f"Product rating: {product_rating}\n"
                  f"Reviews number: {product_reviews_num}\n"
                  f"Product specs: {product_specs}\n"
                  f"Product url: {product_item_url}\n")

            file.add_data(data_to_add)

            index_number += 1

print("Web scraping has been processed!")
