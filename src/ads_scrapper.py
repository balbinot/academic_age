from astroquery import nasa_ads as na

with open('../.ads_token', 'r') as fin:
    tk = fin.read().strip()
    na.ADS.TOKEN = tk

na.ADS.NROWS = 1000
na.ADS.SORT = 'asc bibcode'
na.ADS.ADS_FIELDS = ['author', 'title', 'pubdate', 'bibcode', 'citation_count', 'doctype', 'bibstem', 'orcid']
results = na.ADS.query_simple('year:2010-2021 property:refereed bibstem:ApJ')
results.sort(['pubdate'], reverse=True)


#I think astroquery is limited by ADS_FIELDS. Try the official ADS API python module.
