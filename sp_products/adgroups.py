from ..adapi import Client


class AdGroup(Client):

    def create_ad_group(self, params):
        self.method = "post"
        self.uri_path = "/v2/sp/adGroups"
        self.data = params
        return self.execute()

    def update_ad_group(self, params):
        self.method = "put"
        self.uri_path = "/v2/sp/adGroups"
        self.data = params
        return self.execute()

    def get_ad_group(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups"
        self.data = params
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        return self.execute()

    def delete_ad_group_by_id(self, ad_group_id):
        self.method = "delete"
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        return self.execute()

    def get_ad_group_extended(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/extended"
        self.data = params
        return self.execute()

    def get_ad_group_extended_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/extended/{}".format(ad_group_id)
        return self.execute()
