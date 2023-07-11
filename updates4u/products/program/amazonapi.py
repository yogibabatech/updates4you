from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource

def search_items():
    
    access_key = "AKIAJYNRU23XWXZGDCPA"

    secret_key = "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"

    partner_tag = "updates4you0d-21"

    host = "webservices.amazon.in"

    region = "eu-west-1"

    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    keywords = input("What you want to search for?")

    search_index = "All"

    item_count = int(input("How many Items you want?"))

    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
        SearchItemsResource.IMAGES_PRIMARY_LARGE,
        SearchItemsResource.CUSTOMERREVIEWS_COUNT,
        SearchItemsResource.CUSTOMERREVIEWS_STARRATING,
    ]



    """ Forming request """
    try:
        search_items_request = SearchItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keywords,
            search_index=search_index,
            item_count=item_count,
            resources=search_items_resource,
        )
    except ValueError as exception:
        print("Error in forming SearchItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.search_items(search_items_request)

        print("API called Successfully")
        
        print("Complete Response: this is response")
        # print(response.search_result)

        for i in range(item_count):
            if response.search_result is not None:
                print("Printing first item information in SearchResult:")
                item_0 = response.search_result.items[i]
                if item_0 is not None:
                    if item_0.asin is not None:
                        print("ASIN: ", item_0.asin)
                    if item_0.detail_page_url is not None:
                        print("DetailPageURL: ", item_0.detail_page_url)
                    if item_0.images is not None:
                        print("Imag Url: ", item_0.images.primary.large.url)
                    if (
                        item_0.item_info is not None
                        and item_0.item_info.title is not None
                        and item_0.item_info.title.display_value is not None
                    ):
                        print("Title: ", item_0.item_info.title.display_value)
                    if (
                        item_0.offers is not None
                        and item_0.offers.listings is not None
                        and item_0.offers.listings[0].price is not None
                        and item_0.offers.listings[0].price.display_amount is not None
                    ):
                        print(
                            "Buying Price: ", item_0.offers.listings[0].price.display_amount
                        )

                print(item_0.customer_reviews.count)

                print("*****************************************************************\n****************\n*****\n***")
            if response.errors is not None:
                print("\nPrinting Errors:\nPrinting First Error Object from list of Errors")
                print("Error code", response.errors[0].code)
                print("Error message", response.errors[0].message)

    except ApiException as exception:
        print("Error calling PA-API 5.0!")
        print("Status code:", exception.status)
        print("Errors :", exception.body)
        print("Request ID:", exception.headers["x-amzn-RequestId"])

    except TypeError as exception:
        print("TypeError :", exception)

    except ValueError as exception:
        print("ValueError :", exception)

    except Exception as exception:
        print("Exception :", exception)



search_items()