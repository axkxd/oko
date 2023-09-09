import scrapy


class NekretnineSpider(scrapy.Spider):
    name = 'nekretnine'

    def start_requests(self):
        self.url = f"https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/lista/po-stranici/10/"
        return super().start_requests()