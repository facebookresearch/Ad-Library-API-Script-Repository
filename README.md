# Ads-Library-API-Script-Repository
Ads-Library-API-Script-Repository is a set of code examples to help users/researchers understand how the Facebook Ads Library API works. It also provides a simple command-line interface (CLI) for users to easily use the Facebook Ads Library API.

## Examples
Here's an example of how to use the CLI:

    $ python fb_ads_library_api_cli.py -t {access_token} -f 'page_id,ad_snapshot_url,funding_entity,ad_delivery_start_time' -c 'CA' -s 'election' -v save_to_csv output.csv

This command will save the details of all political ads in Canada (CA) containing the term 'election' to a CSV file named `output.csv`.

Note: please replace the `{access_token}` with your [Facebook Developer access token](https://developers.facebook.com/tools/accesstoken/).

## Requirements
Ads-Library-API-Script-Repository requires or works with:
* Mac OS X, Linux, or Windows
* Python 3.0+
* Python Requests Library ([installation](https://docs.python-requests.org/en/master/user/install/#install))
* Python iso3166 Library ([installation](https://pypi.org/project/iso3166/))

## Features
The script provides the following features:
* Query the [Facebook Ads Library API](https://www.facebook.com/ads/library/api) to get all the Ads Library information on the Facebook platform.
* Filter ads by various parameters such as country, ad type, delivery date, audience size, and more.
* Save the results to a CSV file or perform other actions as defined by the CLI.

## Supported Parameters
The CLI supports the following parameters:

* `-t, --access-token`: The Facebook developer access token (required).
* `-f, --fields`: Fields to retrieve from the Ad Library API (required).
* `-s, --search-term`: The term you want to search for.
* `-c, --country`: Comma-separated country code (no spaces) (required).
* `--search-page-ids`: The specific Facebook Page you want to search.
* `--ad-active-status`: Filter by the current status of the ads at the moment the script runs.
* `--before-date`: Search for ads delivered before this date (inclusive).
* `--after-date`: Search for ads delivered after this date (inclusive).
* `--ad-type`: Search by type of ad (choices: `ALL`, `EMPLOYMENT_ADS`, `FINANCIAL_PRODUCTS_AND_SERVICES_ADS`, `HOUSING_ADS`, `POLITICAL_AND_ISSUE_ADS`).
* `--bylines`: Filter results for ads with a paid for by disclaimer byline.
* `--delivery-by-region`: View ads by the region where Accounts Center accounts were based or located.
* `--estimated-audience-size-max`: Search for ads with a maximum estimated audience size.
* `--estimated-audience-size-min`: Search for ads with a minimum estimated audience size.
* `--languages`: Search for ads based on the language(s) contained in the ad.
* `--media-type`: Search for ads based on whether they contain a specific type of media (choices: `ALL`, `IMAGE`, `MEME`, `VIDEO`, `NONE`).
* `--publisher-platforms`: Search for ads based on whether they appear on a particular Meta technology.
* `--search-type`: The type of search to use for the search_terms field (choices: `KEYWORD_UNORDERED`, `KEYWORD_EXACT_PHRASE`, default: `KEYWORD_UNORDERED`).
* `--unmask-removed-content`: Specify whether you would like your results to reveal content that was removed for violating our standards.
* `--batch-size`: Batch size.
* `--retry-limit`: When an error occurs, the script will abort if it fails to get the same batch this amount of times (default: 3).
* `-v, --verbose`: Enable verbose output.

## Supported Fields
The following fields can be queried from the Ad Library API:

* `id`
* `ad_creation_time`
* `ad_creative_bodies`
* `ad_creative_link_captions`
* `ad_creative_link_descriptions`
* `ad_creative_link_titles`
* `ad_delivery_start_time`
* `ad_delivery_stop_time`
* `ad_snapshot_url`
* `age_country_gender_reach_breakdown`
* `beneficiary_payers`
* `br_total_reach`
* `bylines`
* `currency`
* `delivery_by_region`
* `demographic_distribution`
* `estimated_audience_size`
* `eu_total_reach`
* `impressions`
* `languages`
* `page_id`
* `page_name`
* `publisher_platforms`
* `spend`
* `target_ages`
* `target_gender`
* `target_locations`

## Full documentation
You can find the full documentation here: (--to-be-added--)

## More about Facebook Ads Library
* Website: https://www.facebook.com/ads/library
* Report: https://www.facebook.com/ads/library/report
* API: https://www.facebook.com/ads/library/api

See the [CONTRIBUTING](CONTRIBUTING.md) file for how to help out.

## License
Ads-Library-API-Script-Repository is licensed under the Facebook Platform License, as found in the LICENSE file.
