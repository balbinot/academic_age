from astroquery import nasa_ads as na
import pandas as pd
import ads

MAXROWS = 999

with open('../.ads_token', 'r') as fin:
    tk = fin.read().strip()
    na.ADS.TOKEN = tk
    ads.config.token = tk


def reference(id):
    """
    ads package truncates rows to 50, need to re-implement here to 'fix' it
    TODO: write issue to https://github.com/andycasey/ads
    """
    q = ads.SearchQuery(
        q='references(id:{})'.format(id),
        fl=['id', 'bibcode'], rows=MAXROWS
    )
    return [a.bibcode for a in q]

q = 'year:2010-2021 property:refereed bibstem:ApJ'

fields = ['id', 'bibcode', 'references', 'authors', 'orcid_pub', 'first_author', 'citation_count', 'page_count', 'affil', 'author_count', 'aff']

papers = ads.SearchQuery(q=q, sort="date", rows=5, fl=fields)
OUT = []
for paper in papers:
   _a = [paper.id, paper.first_author, paper.orcid_pub[0], paper.aff[0], len(reference(paper.id)), ]
   print(_a)
   OUT.append(_a)

df = pd.DataFrame(OUT, columns=['id', 'first author', 'orcid', 'aff', 'references'])
df.to_csv('../data/ads_query.csv', sep=',', index=False)
