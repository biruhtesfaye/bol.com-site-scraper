import scrapy


class ItemsScraperSpider(scrapy.Spider):
    name = "items_scraper"
    allowed_domains = ["www.bol.com"]
    start_urls = ["https://www.bol.com/"]

    page_num = 1

    def start_requests(self):
        if self.keyword:
            while self.page_num:
                search_url = f'https://www.bol.com/nl/nl/s/?page={self.page_num}&searchtext={self.keyword}&view=list'
                yield scrapy.Request(url=search_url, callback=self.parse)
        else:
            scrapy.log("Please insert a correct keyword.")

    def parse(self, response):

        if response.status == 404:
            self.page_num = 0
            raise scrapy.exceptions.CloseSpider("No more pages.")

        items = response.xpath('//li[contains(@class, "product-item--row")]')
        for item in items:
            name = item.xpath('.//ul[@class="product-creator"]//a/text()').get()
            title = item.xpath('.//div[@class="product-title--inline"]//a/text()').get()
            rating = item.xpath('.//div[contains(@aria-label, "Gemiddeld")]/@aria-label').re(r'Gemiddeld\s(.*)\svan.*')
            review_count = item.xpath('.//div[contains(@aria-label, "Gemiddeld")]/@aria-label').re(r'.*\s(.*)\sreviews$')
            price = eval(item.xpath('.//meta/@content').get())

            yield {
                "product_name": name,
                "product_title": title,
                "product_rating": rating,
                "product_review_count": review_count,
                "product_price": price,
            }

        self.page_num += 1
        