class CreateFPLibResponse(object):
    
    def __init__(self, requestURL, statusCode, statusString, subStatusCode, errorCode, errorMsg, FDID):
        self.requestURL = requestURL
        self.statusCode = statusCode
        self.statusString = statusString
        self.subStatusCode = subStatusCode
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        self.FDID = FDID