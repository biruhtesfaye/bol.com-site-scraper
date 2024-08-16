# bol.com site scraper

<a href="bol.com">bol.com</a> is an ecommerce site and the scraper I made will receive for keyword to search and a file name to put the resulting dataset. Then it will parse through all the pages and scrapes the products listed.

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
- **city**: city name

The program require one keyword argument (keyword). which is the term to be searched on bol.com. It may be 'hp laptop', 'Goorin Bros Cap', 'The Alchemist Book', etc...

## Output

The Fields for one sample product.

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