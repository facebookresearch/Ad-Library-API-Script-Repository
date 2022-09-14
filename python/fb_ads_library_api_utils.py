#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from iso3166 import countries

supported_countries = [
    "AT",
    "BE",
    "BG",
    "CA",
    "CY",
    "CZ",
    "DE",
    "DK",
    "EE",
    "ES",
    "FI",
    "FR",
    "GB",
    "GR",
    "HR",
    "HU",
    "IE",
    "IL",
    "IN",
    "IT",
    "LT",
    "LU",
    "LV",
    "MT",
    "NL",
    "PL",
    "PT",
    "RO",
    "SE",
    "SI",
    "SK",
    "UA",
    "US",
]
valid_query_fields = [
    "ad_creation_time",
    "ad_creative_body",
    "ad_creative_bodies",
    "ad_creative_link_caption",
    "ad_creative_link_captions",
    "ad_creative_link_description",
    "ad_creative_link_descriptions",
    "ad_creative_link_title",
    "ad_creative_link_titles",
    "ad_delivery_start_time",
    "ad_delivery_stop_time",
    "ad_snapshot_url",
    "currency",
    "delivery_by_region",
    "demographic_distribution",
    "bylines",
    "id",
    "impressions",
    "languages",
    "page_id",
    "page_name",
    "potential_reach",
    "publisher_platforms",
    "region_distribution",
    "spend",
]


def get_country_code(country_str):
    """
    Convert the country input to valid country code
    """
    global supported_countries
    try:
        country = countries.get(country_str)
    except Exception:
        country = None
    if not country or country.alpha2 not in supported_countries:
        return None
    return country.alpha2


def is_valid_fields(field):
    """
    The Facebook Ads Library API has a list of supported fields
    """
    global valid_query_fields
    return field in valid_query_fields
