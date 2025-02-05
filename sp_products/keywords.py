from ..adapi import Client


class Keywords(Client):

    def get_keywords_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/{}".format(keyword_id)
        return self.execute()

    def delete_keywords_by_id(self, keyword_id):
        self.method = "delete"
        self.uri_path = "/v2/sp/keywords/{}".format(keyword_id)
        return self.execute()

    def get_keywords_extended(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/extended"
        self.data = params
        return self.execute()

    def get_keywords_extended_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/extended/{}".format(keyword_id)
        return self.execute()

    def get_keywords(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords"
        self.data = params
        return self.execute()

    def create_keywords(self, params):
        self.method = "post"
        self.uri_path = "/v2/sp/keywords"
        self.data = params
        return self.execute()

    def update_keywords(self, params):
        self.method = "put"
        self.uri_path = "/v2/sp/keywords"
        self.data = params
        return self.execute()
