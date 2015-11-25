# -*- coding: utf-8 -*-

"""
   BuzzlogixTextAnalysisAPILib.Controllers.ObjectivityController

   This file was automatically generated for buzzlogix by APIMATIC BETA v2.0 on 11/25/2015
"""
import unirest

from BuzzlogixTextAnalysisAPILib.APIHelper import APIHelper
from BuzzlogixTextAnalysisAPILib.Configuration import Configuration
from BuzzlogixTextAnalysisAPILib.APIException import APIException


class ObjectivityController(object):


    """A Controller to access Endpoints in the BuzzlogixTextAnalysisAPILib API."""

    def __init__(self,
                 apikey):
        """
        Constructor with authentication and configuration parameters
        """
        self.__apikey = apikey

    def create_return_english_objectivity(self,
                                          body):
        """Does a POST request to /objectivity.

        The text should be provided as text/plain in the body

        Args:
            body (string): Supply text to be classified.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/objectivity"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "apikey": self.__apikey,            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"            "apikey": self.__apikey
        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers,  params=body)

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("No API Key found in headers, body or querystring", 401, response.body)

        elif response.code == 403:
            raise APIException("Invalid authentication credentials", 403, response.body)

        elif response.code == 429:
            raise APIException("API rate limit exceeded", 429, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body

    def create_return_english_objectivity_form(self,
                                               body):
        """Does a POST request to /objectivity/form.

        The text should be provided as multipart/form-data with the key
        'text'. Files can be uploaded.

        Args:
            body (string): Supply text to be classified.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/objectivity/form"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "apikey": self.__apikey,            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"            "apikey": self.__apikey
        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers,  params=body)

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("No API Key found in headers, body or querystring", 401, response.body)

        elif response.code == 403:
            raise APIException("Invalid authentication credentials", 403, response.body)

        elif response.code == 429:
            raise APIException("API rate limit exceeded", 429, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        return response.body
