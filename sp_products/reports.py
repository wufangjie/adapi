from ..adapi import Client


class Reports(Client):

    def request_report(self, record_type, params):
        self.method = "post"
        self.uri_path = "/v2/sp/{}/report".format(record_type)
        self.data = params
        return self.execute()

    def get_report(self, report_id):
        self.method = "get"
        self.uri_path = "/v2/reports/{}".format(report_id)
        return self.execute()

    def get_report_download_url(self, reportId):
        self.method = "get"
        self.uri_path = "/v2/reports/{}/download".format(reportId)
        return self.execute_download(self.domain + self.uri_path)
