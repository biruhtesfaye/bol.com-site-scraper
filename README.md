# bol.com site scraper

<a href="bol.com">bol.com</a> is an e-commerce site and the scraper I made will receive a keyword to search and a file name to put the resulting dataset. Then it will parse through all the pages and scrape the products listed.

## Usage

Install scrapy:

```
pip install scrapy
```

Run Job:

```
cd bol_com
 scrapy crawl items_scraper \
 -a keyword="hp laptop" \
 -o dataset/hp_laptop.json
```

Params:
- **keyword**: Search term for a product

The program requires one keyword-argument (keyword). which is the term to be searched on bol.com. It may be 'hp laptop', 'Goorin Bros Cap', 'The Alchemist Book', etc...

## Output

The fields for one sample product.

```
{
    "product_name": "HP", 
    "product_title": "HP 15-fc0751nd - Laptop - 15.6 inch", 
    "product_rating": 4.8, 
    "product_review_count": 8, 
    "product_price": 479.0
}
```

Enjoy it! Any comments are welcome!
