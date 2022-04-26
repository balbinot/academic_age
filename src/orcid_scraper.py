import orcid


class orcidScraper():

    def __init__(self):
        self._getCredentials()
        self.api = orcid.PublicAPI(self.user, self.secret, sandbox=False)
        self.token = self.api.get_search_token_from_orcid()

    def _getCredentials(self):
        with open('../.orcid_user') as f:
            self.user = f.read().strip()
        with open('../.orcid_secret') as f:
            self.secret = f.read().strip()
        self.redirect_uri = "https://pub.orcid.org"

    def get_phd_year(self, oid):
        search_results = self.api.read_record_public(oid, 'educations', self.token)
        latest_edu = search_results['education-summary'][0]

        type = latest_edu['role-title']
        startYear = latest_edu['start-date']['year']['value']
        endYear = latest_edu['end-date']['year']['value']

        return type, startYear, endYear


