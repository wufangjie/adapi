from ..adapi import Client


class Campaigns(Client):

    def create_campaigns(self, params):
        self.method = "post"
        self.uri_path = "/v2/sp/campaigns"
        self.data = params
        return self.execute()

    def update_campaigns(self, params):
        self.method = "put"
        self.uri_path = "/v2/sp/campaigns"
        self.data = params
        return self.execute()

    def get_campaigns(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns"
        self.data = params
        return self.execute()

    def get_campaign_by_id(self, campaign_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        return self.execute()

    def delete_campaign_by_id(self, campaign_id):
        self.method = "delete"
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        return self.execute()

    def get_campaign_extended(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/extended"
        self.data = params
        return self.execute()

    def get_campaign_extended_by_id(self, campaign_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        return self.execute()
