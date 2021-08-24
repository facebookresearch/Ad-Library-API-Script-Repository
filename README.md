# Ads-Library-API-Script-Repository
Ads-Library-API-Script-Repository is a set of code examples to help user/researchers understand how the Facebook Ads Library API works. It also provides a simple command-line interface(CLI) for users to easily use the Facebook Ads Library API.

## Examples
Here's an example on how to use the CLI:

    $ python fb_ads_library_api_cli.py -t {access_token} -f 'page_id,ad_snapshot_url,funding_entity,ad_delivery_start_time' -c 'CA' -s '.' -v count

It would count the number of all polictical ads in CA(Canada);

Note: please replace the '{access_token}' with your [Facebook Developer access token](https://developers.facebook.com/tools/accesstoken/).

## Requirements
Ads-Library-API-Script-Repository requires or works with
* Mac OS X or Linux or Window
* Python 3.0+
* Python Requests Library ([installation](https://docs.python-requests.org/en/master/user/install/#install))
* Python iso3166 Library ([installation](https://pypi.org/project/iso3166/))


## How Ads-Library-API-Script-Repository works
The script will query the [Facebook Ads library API](https://www.facebook.com/ads/library/api) to get all the Ads Library information on the Facebook platform;

## Full documentation
You can find the full documentation here: (--to-be-added--)

## More about Facebook Ads Library
* Website: https://www.facebook.com/ads/library
* Report: https://www.facebook.com/ads/library/report
* API: https://www.facebook.com/ads/library/api

See the [CONTRIBUTING](CONTRIBUTING.md) file for how to help out.

## License
Ads-Library-API-Script-Repository is licensed under the Facebook Platform License, as found in the LICENSE file.
