# -*- coding: utf-8 -*-

"""
   BuzzlogixTextAnalysisAPILib.Controllers.TwittersentimentController

   This file was automatically generated for buzzlogix by APIMATIC BETA v2.0 on 12/06/2015
"""
import unirest

from BuzzlogixTextAnalysisAPILib.APIHelper import APIHelper
from BuzzlogixTextAnalysisAPILib.Configuration import Configuration
from BuzzlogixTextAnalysisAPILib.APIException import APIException


class TwittersentimentController(object):


    """A Controller to access Endpoints in the BuzzlogixTextAnalysisAPILib API."""

    def __init__(self,
                 x_mashape_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__x_mashape_key = x_mashape_key

    def create_return_english_twitter_sentiment_plaintext(self,
                                                          body):
        """Does a POST request to /twittersentiment.

        The Tweet should be provided as text/plain in the body

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
        query_builder += "/twittersentiment"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "X-Mashape-Key": self.__x_mashape_key,            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"            "X-Mashape-Key": self.__x_mashape_key
        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers,  params=body)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_return_english_twitter_sentiment_multipart_form(self,
                                                               text):
        """Does a POST request to /twittersentiment.

        The Tweet should be provided as multipart/form-data with the key
        'text'. Files can be uploaded.

        Args:
            text (string): Supply text to be classified.

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
        query_builder += "/twittersentiment"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "X-Mashape-Key": self.__x_mashape_key,            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"            "X-Mashape-Key": self.__x_mashape_key
        }

        # Prepare parameters
        parameters = {
            "text":  open(text, mode="r") if text is not None else None
        }
        # Send the form body as url encoded data
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        
        form_encoded_params = dict()
        for (key, value) in parameters.items():
            if isinstance(value, list):
                # Loop through each item in the list and add it by number
                i = 0
                for entry in value:
                    form_encoded_params.update(APIHelper.form_encode(entry, key + "[" + str(i) + "]"))
                    i += 1
            elif isinstance(value, dict):
                # Loop through each item in the dictionary and add it
                form_encoded_params.update(APIHelper.form_encode(value, key))
            else:
                # Add the current item
                form_encoded_params[key] = value
        
        parameters = ''
        for (key, value) in form_encoded_params.items():
            separator = '&' if len(parameters) > 0 else '' 
            parameters = parameters + '{0}{1}={2}'.format(separator, key, value)

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_return_english_twitter_sentiment_encoded_form(self,
                                                             text):
        """Does a POST request to /twittersentiment.

        Return the sentiment of an English Tweet supplied in an encoded form
        using key 'text'.

        Args:
            text (string): Supply the Tweet to be classified.

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
        query_builder += "/twittersentiment"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "X-Mashape-Key": self.__x_mashape_key,            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"            "X-Mashape-Key": self.__x_mashape_key
        }

        # Prepare parameters
        parameters = {
            "text": text
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body
