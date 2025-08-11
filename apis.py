# Zillow API Configurations
# This file contains all the API configurations for different property types

import re

# ============================================================================
# RENTAL PROPERTIES API CONFIGURATION
# ============================================================================

RENTAL_API_CONFIG = {
    'cookies': {
        'zguid': '24|%24d3ed6805-67ad-4f44-993d-f0605eeb3807',
        '_pxvid': '7579bded-2754-11f0-9b79-3255226966c4',
        'zgsession': '1|36c27b66-bc20-4721-914b-f675f642a676',
        'pxcts': '378a3d14-7620-11f0-ae2a-ccbd89e259f3',
        'JSESSIONID': 'E5FEA32730E4AC46A568B0E5471956C2',
        'web-platform-data': '%7B%22wp-dd-rum-session%22%3A%7B%22doNotTrack%22%3Atrue%7D%7D',
        '_px3': '7deee4f3adb8d628108c600c88142746f167ca594dabd7fb7f1e3f9b48b9c816:RuE9fcgy2fRIA1frb3RhRPYg96BXXR/mWVeC4FSYl2vVeVy2SSicNmbOxuJEP/bfmWt64u9BZRQz4hrrb0ibWQ==:1000:JwPvbxXN0ePKve+KUGALehUSnx1ex1CQypjN+NPrcPHPf0r50nxsIudu6sg/+7tN+kJs2T/PzBYGd16oSza2/7jNIBm09m0zjDccXCQ9QRhr+2RMedsJHYDbkCrvm0MwMORmMS3Kdc2s7ThIUdiv0MQ1ToFA9TLyiOEy1Zf/8orolxi/PFo8wHDcdQBIf9LoLiw6xBO02bGuBgwbG51AU8cE200jACG2ecOEvYcwru8=',
        'AWSALB': 'qxmyAeMWhJrkbS1dNK4wU1d9UmvSTB+1Ms9mAMYYhwVUvH/Cg6BCeL/LmEi9eJRQCpkgEwjX/jH8FC1OqwQRLkIOmP03j0uLFmmu4XecLKjZjczIFXUv9AXeasvM',
        'AWSALBCORS': 'qxmyAeMWhJrkbS1dNK4wU1d9UmvSTB+1Ms9mAMYYhwVUvH/Cg6BCeL/LmEi9eJRQCpkgEwjX/jH8FC1OqwQRLkIOmP03j0uLFmmu4XecLKjZjczIFXUv9AXeasvM',
        'search': '6|1757447320500%7Crect%3D56.31070203749593%2C-59.868983875%2C15.951214741982747%2C-128.951015125%26rid%3D54%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26listPriceActive%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26ita%3D0%26stl%3D0%26fur%3D0%26os%3D0%26ca%3D0%26np%3D0%26hasDisabledAccess%3D0%26hasHardwoodFloor%3D0%26areUtilitiesIncluded%3D0%26highSpeedInternetAvailable%3D0%26elevatorAccessAvailable%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0954%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    },
    
    'headers': {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.zillow.com',
        'priority': 'u=1, i',
        'referer': 'https://www.zillow.com/tx/rentals/2_p/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A67.19995615543698%2C%22south%22%3A-7.1113315072861685%2C%22east%22%3A-64.04378856249998%2C%22west%22%3A-124.77621043749998%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22usersSearchTerm%22%3A%22texas%22%2C%22category%22%3A%22cat1%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    },
    
    'base_json_data': {
        'searchQueryState': {
            'isMapVisible': True,
            'mapBounds': {
                'north': 67.19995615543698,
                'south': -7.1113315072861685,
                'east': -64.04378856249998,
                'west': -124.77621043749998,
            },
            'filterState': {
                'isForRent': {
                    'value': True,
                },
                'isForSaleByAgent': {
                    'value': False,
                },
                'isForSaleByOwner': {
                    'value': False,
                },
                'isNewConstruction': {
                    'value': False,
                },
                'isComingSoon': {
                    'value': False,
                },
                'isAuction': {
                    'value': False,
                },
                'isForSaleForeclosure': {
                    'value': False,
                },
            },
            'isListVisible': True,
            'mapZoom': 4,
            'usersSearchTerm': 'texas',
            'category': 'cat1',
            'regionSelection': [
                {
                    'regionId': 54,
                    'regionType': 2,
                },
            ],
        },
        'wants': {
            'cat1': [
                'listResults',
                'mapResults',
            ],
        },
        'isDebugRequest': False,
    },
    
    'search_cookie_pattern': r'p%3D\d+',
    'referer_pattern': r'currentPage%22%3A\d+',
    'output_filename': 'zillow_rental_data.json'
}

# ============================================================================
# PROPERTIES FOR SALE API CONFIGURATION
# ============================================================================

SALE_API_CONFIG = {
    'cookies': {
        'zguid': '24|%24d3ed6805-67ad-4f44-993d-f0605eeb3807',
        '_pxvid': '7579bded-2754-11f0-9b79-3255226966c4',
        'zgsession': '1|36c27b66-bc20-4721-914b-f675f642a676',
        'pxcts': '378a3d14-7620-11f0-ae2a-ccbd89e259f3',
        'JSESSIONID': 'E5FEA32730E4AC46A568B0E5471956C2',
        'web-platform-data': '%7B%22wp-dd-rum-session%22%3A%7B%22doNotTrack%22%3Atrue%7D%7D',
        'AWSALB': 'UuicCyc1sEs+XElAVh5Hn4d96ogtKE5vk9iengzio7LS+j9T+v+r7/RnqJtH27ebfe9jbbIDnz3U37Grg82ejdM+KmU0xAYmfp64MaF57VEFFtcxKNQFzGiocraD',
        'AWSALBCORS': 'UuicCyc1sEs+XElAVh5Hn4d96ogtKE5vk9iengzio7LS+j9T+v+r7/RnqJtH27ebfe9jbbIDnz3U37Grg82ejdM+KmU0xAYmfp64MaF57VEFFtcxKNQFzGiocraD',
        '_px3': 'd82917d01ef5aeb70e022a3334bc0c4e4fce60a0bba58227baa66395ec605087:aJDEvTTUhu14W+li0VaOeF4os4lrvM4bjWr/bjT6q7dYt5SfFu57yVKqPQjpU9jWBsO9uqAOkoJXIyFo05BaTQ==:1000:POH6hO3tGHJ3qTgUXbFHu74kstyUhThsskERxLP7As5LtE6EY3VJvgZIjsWohoVpcSieCXcdSwqCC/X4Rd6tQuK1tmZeaVX+Wb3T2g1C6VSrFYsHSkbl62PyeTb8swHpQfSyFw3nPIn8q+JEa/Vuy/AlKhNOz4qDtkY/dxFegj/bag/y98r9l0Lpov3Y423FM8H/sAtIPN4Bi+IKE2R7mTHmlXhP2O2UdwYFEYBBVgM=',
        'search': '6|1757447984488%7Crect%3D36.7334139283621%2C-91.44158859375%2C25.57592845806913%2C-108.71209640625%26rid%3D54%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0954%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    },
    
    'headers': {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.zillow.com',
        'priority': 'u=1, i',
        'referer': 'https://www.zillow.com/homes/for_sale/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    },
    
    'base_json_data': {
        'searchQueryState': {
            'pagination': {},
            'isMapVisible': True,
            'mapBounds': {
                'west': -108.71209640625,
                'east': -91.44158859375,
                'south': 25.57592845806913,
                'north': 36.7334139283621,
            },
            'regionSelection': [
                {
                    'regionId': 54,
                    'regionType': 2,
                },
            ],
            'filterState': {
                'sortSelection': {
                    'value': 'globalrelevanceex',
                },
            },
            'isListVisible': True,
            'mapZoom': 6,
        },
        'wants': {
            'cat1': [
                'listResults',
                'mapResults',
            ],
            'cat2': [
                'total',
            ],
        },
        'isDebugRequest': False,
    },
    
    'search_cookie_pattern': r'p%3D\d+',
    'referer_pattern': r'currentPage%22%3A\d+',
    'output_filename': 'zillow_sale_data.json'
}

# ============================================================================
# AGENT DATA API CONFIGURATION (via ZPID)
# ============================================================================

AGENT_API_CONFIG = {
    'cookies': {
        'zguid': '24|%24d3ed6805-67ad-4f44-993d-f0605eeb3807',
        '_pxvid': '7579bded-2754-11f0-9b79-3255226966c4',
        'zgsession': '1|36c27b66-bc20-4721-914b-f675f642a676',
        'pxcts': '378a3d14-7620-11f0-ae2a-ccbd89e259f3',
        'JSESSIONID': '7981C36C86F405D5894410EBE692DA42',
        'web-platform-data': '%7B%22wp-dd-rum-session%22%3A%7B%22doNotTrack%22%3Atrue%7D%7D',
        '_ga': 'GA1.2.1957018760.1754939164',
        '_gid': 'GA1.2.206482151.1754939164',
        'zjs_anonymous_id': '%22d3ed6805-67ad-4f44-993d-f0605eeb3807%22',
        'zjs_user_id': 'null',
        'zg_anonymous_id': '%22c181f8e0-4f2e-4cbe-84bd-ae579f15549b%22',
        'zjs_user_id_type': '%22encoded_zuid%22',
        '_px3': 'ae6a21e62243d6a2ca6919c8914885c03a3daca5ad9d5a11caee8e55da5f4532:cqqJS/o9ImsGnC077aDfkAySK5UXMt816hEt+PfAadsLxKUB+SU0GBdBT0PQuMBUyN9KdKDfCZewZl6I5m4KUA==:1000:vHNJgeTPGH188/wpkcqTQ/DfvcQrqLCUrAa6oJT/oZODR4UQmXqsRD3pVNtHQhrsQ3pmIcs8SrPFvINsrqOaLxMcPZumDM2W+RBy0U1l/PDOfiOpN0K396mZvPNk07XTS4CqqN6E1DEHf4cGgqRK8nLepfvHjn3IZgG947Rz5GWxbXdwjUB34j1nZsVBbQu52wlfRgGlm8IO+UdeMayHEn8iG8h7NrRjf45Ow8YCYeM=',
        'AWSALB': 'D1i1x86iPNJ1AwJw5sPLUmC1RjtINTEGygQjTlDLqn6bAyVhRrugOGP/6akVupxRhG4Ukerloz824lKtSON7QpQWdUsC6CJAB7fjyiBB6kNpHZtLeQtTUSpkls1o',
        'AWSALBCORS': 'D1i1x86iPNJ1AwJw5sPLUmC1RjtINTEGygQjTlDLqn6bAyVhRrugOGP/6akVupxRhG4Ukerloz824lKtSON7QpQWdUsC6CJAB7fjyiBB6kNpHZtLeQtTUSpkls1o',
        'search': '6|1757533888885%7Crect%3D29.743943159601614%2C-95.49833307885743%2C29.65522206889638%2C-95.63325892114258%26rid%3D39051%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0939051%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    },
    
    'headers': {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'client-id': 'showcase-subapp-client_contact-form-graphql-loader_contact-form-graphql-loader',
        'content-type': 'application/json',
        'origin': 'https://www.zillow.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.zillow.com/homedetails/10555-Turtlewood-Ct-UNIT-804-Houston-TX-77072/28393293_zpid/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
        'x-z-enable-oauth-conversion': 'true',
    },
    
    'params': {
        'zpid': '28393293',
        'platform': 'DESKTOP_WEB',
        'formType': 'OPAQUE',
        'contactFormRenderParameter': '',
        'skipCFRD': 'false',
        'operationName': 'DeferredContactFormQuery',
    },
    
    'base_json_data': {
        'operationName': 'DeferredContactFormQuery',
        'variables': {
            'zpid': 28393293,
            'platform': 'DESKTOP_WEB',
            'formType': 'OPAQUE',
            'contactFormRenderParameter': {
                'zpid': 28393293,
                'platform': 'desktop',
                'isDoubleScroll': True,
            },
            'skipCFRD': False,
        },
        'query': 'query DeferredContactFormQuery($zpid: ID, $platform: ContactFormPlatform, $formType: FormType, $contactFormRenderParameter: ContactFormRenderParameter, $skipCFRD: Boolean = false) {\n  viewer {\n    ...ContactForm_viewer\n  }\n  property(zpid: $zpid) {\n    ...ContactForm_property\n  }\n  abTests {\n    ...abTestManager_abTests\n    ...ContactForm_abTests\n  }\n  showcase(zpid: $zpid) {\n    ...ContactForm_showcase\n  }\n}\n\nfragment abTestManager_abTests on ABTests {\n  AB_DASHBOARD_AA_TEST: abTest(trial: "AB_DASHBOARD_AA_TEST")\n  ACTIVATION_ENABLED: abTest(trial: "Activation_Enabled")\n  ACTIVATION_ONBOARDING: abTest(trial: "Activation_Onboarding")\n  ACTIVATION_ONBOARDING_ENABLED: abTest(trial: "Activation_Onboarding_Enabled")\n  ACTIVATION_GA_METRICS_ENABLED: abTest(trial: "Activation_GA_Metrics_Enabled")\n  AIPERS_SIMILAR_HOMES_GDP: abTest(trial: "AIPERS_SIMILAR_HOMES_GDP")\n  AR_CSAT_ONSITE_HDP: abTest(trial: "AR_CSAT_ONSITE_HDP")\n  AR_CSAT_MODAL_HDP_LOAD_DELAY: abTest(trial: "AR_CSAT_MODAL_HDP_LOAD_DELAY")\n  AR_SHOWCASE_HDP_WIDGET: abTest(trial: "AR_SHOWCASE_HDP_WIDGET")\n  ARCS_CLIENT_GEN_LEAD_ID: abTest(trial: "ARCS_CLIENT_GEN_LEAD_ID")\n  ARCS_DIRECT_LINK_CF: abTest(trial: "ARCS_DIRECT_LINK_CF")\n  ARCS_FEATURED_IMAGE: abTest(trial: "ARCS_FEATURED_IMAGE")\n  ARCS_MY_AGENT_A11Y_UI: abTest(trial: "ARCS_MY_AGENT_A11Y_UI")\n  ARCS_PREAPPROVAL_CHECK: abTest(trial: "ARCS_PREAPPROVAL_CHECK")\n  ARCS_REGION_PHONE: abTest(trial: "ARCS_REGION_PHONE")\n  ARCS_DESKTOP_PHONE: abTest(trial: "ARCS_DESKTOP_PHONE")\n  HDP_CONSTELLATION_PROPERTY_CARD: abTest(\n    trial: "HDP_CONSTELLATION_PROPERTY_CARD"\n  )\n  HDP_DESKTOP_LAYOUT_TOPNAV: abTest(trial: "HDP_DESKTOP_LAYOUT_TOPNAV")\n  HDP_EARLY_TRIAGE_REORDER: abTest(trial: "HDP_EARLY_TRIAGE_REORDER")\n  HDP_EARLY_TRIAGE_REORDER_APP: abTest(trial: "HDP_EARLY_TRIAGE_REORDER_APP")\n  HDP_FNF_BULLETS: abTest(trial: "HDP_FNF_BULLETS")\n  HDP_HFF_ACCORDION: abTest(trial: "HDP_HFF_ACCORDION")\n  HDP_HIGHLIGHT_OFFER_REVIEW: abTest(trial: "HDP_HIGHLIGHT_OFFER_REVIEW")\n  HDP_HOLLYWOOD_FS_SUBTYPES: abTest(trial: "HDP_HOLLYWOOD_FS_SUBTYPES")\n  HDP_HOME_INSIGHTS: abTest(trial: "HDP_HOME_INSIGHTS")\n  HDP_INSIGHTS_VERSION: abTest(trial: "HDP_INSIGHTS_VERSION")\n  HDP_REORDER_AT_A_GLANCE: abTest(trial: "HDP_REORDER_AT_A_GLANCE")\n  HDP_SELLING_SOON_MSG: abTest(trial: "HDP_SELLING_SOON_MSG")\n  HDP_SELLING_SOON_V2_TEST: abTest(trial: "HDP_SELLING_SOON_V2_TEST")\n  HDP_TOP_SLOT: abTest(trial: "HDP_TOP_SLOT")\n  HDP_UPDATED_FNF: abTest(trial: "HDP_UPDATED_FNF")\n  HDP_ZHVI_CHART_MIGRATION: abTest(trial: "HDP_ZHVI_CHART_MIGRATION")\n  MIGHTY_MONTH_2022_HOLDOUT: abTest(trial: "MIGHTY_MONTH_2022_HOLDOUT")\n  MTT_GDP_PVS_CALL_GATE: abTest(trial: "MTT_GDP_PVS_CALL_GATE")\n  NFSHDP_OWNER_OPTIONS_GOOGLE_AD: abTest(trial: "NFSHDP_OWNER_OPTIONS_GOOGLE_AD")\n  PERF_DEFER_PHOTOS: abTest(trial: "PERF_DEFER_PHOTOS")\n  PERF_PRELOAD_HDP_IMAGE: abTest(trial: "PERF_PRELOAD_HDP_IMAGE")\n  RE_CANADA_CTA: abTest(trial: "RE_CANADA_CTA")\n  RE_HDP_HOME_INSIGHTS: abTest(trial: "RE_HDP_HOME_INSIGHTS")\n  RE_HDP_HOME_INSIGHTS_VERSION: abTest(trial: "RE_HDP_HOME_INSIGHTS_VERSION")\n  RE_VARIANT_HDP_DEFERRED_HYDRATION: abTest(\n    trial: "RE_VARIANT_HDP_DEFERRED_HYDRATION"\n  )\n  RE_NON_VARIANT_HDP_DEFERRED_HYDRATION: abTest(\n    trial: "RE_NON_VARIANT_HDP_DEFERRED_HYDRATION"\n  )\n  SI_DownPaymentAssistance: abTest(trial: "SI_DownPaymentAssistance")\n  SI_DPA_Apps: abTest(trial: "SI_DPA_Apps")\n  SI_CostAndFees_HDP_Triage: abTest(trial: "SI_CostAndFees_HDP_Triage")\n  SPT_RENDER_FOR_RENT_PAGE: abTest(trial: "SPT_RENDER_FOR_RENT_PAGE")\n  SXP_HDP_BLUE_TO_RED: abTest(trial: "SXP_HDP_BLUE_TO_RED")\n  TRACK_HOME_VALUE_V1: abTest(trial: "TRACK_HOME_VALUE_V1")\n  UnassistedHomeShowingWeb: abTest(trial: "UnassistedHomeShowingWeb")\n  SPT_RENDER_FOR_SALE_PAGE: abTest(trial: "SPT_RENDER_FOR_SALE_PAGE")\n  VL_BDP_NEW_TAB: abTest(trial: "VL_BDP_NEW_TAB")\n  HDP_NEW_ZESTIMATE_CHART: abTest(trial: "HDP_NEW_ZESTIMATE_CHART")\n  ZEXP_HOLDOUT_ES_PILOT: abTest(trial: "ZEXP_HOLDOUT_ES_PILOT")\n  ZHL_HDP_CHIP_PERSONALIZE_PAYMENT_CTAS: abTest(\n    trial: "ZHL_HDP_CHIP_PERSONALIZE_PAYMENT_CTAS"\n  )\n  ZHL_HDP_CHIP_PERSONALIZE_PAYMENT_PERSISTENCE: abTest(\n    trial: "ZHL_HDP_CHIP_PERSONALIZE_PAYMENT_PERSISTENCE"\n  )\n  ZHL_PERSONALIZED_PAYMENT_WEB_MVP: abTest(\n    trial: "ZHL_PERSONALIZED_PAYMENT_WEB_MVP"\n  )\n  ZHL_PERSONALIZED_PAYMENT_MODULE: abTest(\n    trial: "ZHL_PERSONALIZED_PAYMENT_MODULE"\n  )\n}\n\nfragment ContactForm_viewer on Viewer {\n  name\n  email\n}\n\nfragment ContactForm_property on Property {\n  country\n  state\n  homeStatus\n  homeType\n  livingArea\n  hdpUrl\n  streetAddress\n  city\n  zipcode\n  price\n  mlsid\n  ouid\n  zestimate\n  propertyTypeDimension\n  bathrooms\n  bedrooms\n  zpid\n  hiResImageLink\n  isPremierBuilder\n  isShowcaseListing\n  listing_sub_type {\n    is_FSBA\n    is_FSBO\n    is_pending\n    is_newHome\n    is_foreclosure\n    is_comingSoon\n    is_bankOwned\n    is_forAuction\n  }\n  timeZone\n  tourEligibility(\n    platform: WEB\n    useAsyncAb: false\n    supportedTourTypes: [STANDARD, INSTANT, INSTANT_BOOK]\n  ) {\n    isPropertyTourEligible\n    propertyTourOptions {\n      isFinal\n      tourAvailability {\n        date\n        status\n        times\n      }\n      tourType\n    }\n  }\n  tourAppointmentsForCurrentLoggedInUser(limit: 1) {\n    formattedBuyerTourStatusWithDate\n    tourManagementPageUrl(context: HDP_WEB_EMBEDDED)\n  }\n  contactFormRenderData(contactFormRenderParameter: $contactFormRenderParameter) @skip(if: $skipCFRD) {\n    data\n  }\n  responsivePhotos: photos {\n    mixedSources(aspectRatio: FourThirds) {\n      jpeg {\n        url\n        width\n      }\n    }\n  }\n  listingMetadata {\n    isAdsRestricted\n  }\n  ...PropertyLeadSubmitForm_property\n}\n\nfragment PropertyLeadSubmitForm_property on Property {\n  submitFlow(platform: $platform, formType: $formType) {\n    __typename\n    ... on PropertyLeadSubmitForm {\n      ...PropertyLeadSubmitFormStep\n    }\n    ... on AuthOTP {\n      authStyle\n      isInZIBSMarket\n    }\n  }\n}\n\nfragment PropertyLeadSubmitFormStep on PropertyLeadSubmitForm {\n  __typename\n  title\n  heading\n  subheading\n  headingIcon\n  buttonText\n  disclosure\n  inputFields {\n    label\n    placeholder\n    validationRegex\n    isRequired\n    inputType\n    clientSideValidationErrorMessage\n    inputName\n    isUserInputDisabled\n    value\n    defaultSubmitValue\n    maxCharacters\n    error {\n      isRecoverable\n      message\n      type\n    }\n  }\n  componentPositionOrder\n  cta {\n    label\n    action {\n      ... on LaunchUrlCTAAction {\n        url\n      }\n    }\n    clickstreamMetadata {\n      onClick\n      onError\n      onSuccess\n    }\n    isSticky\n    helpText\n  }\n  financingCheckbox {\n    initialClickstreamMetadata {\n      onPageView\n    }\n    isCheckedInitialState\n    leadFieldName\n    label\n    financingType\n  }\n  checkboxes {\n    ... on TCPACheckbox {\n      clickstreamInputName\n      clickstreamMetadata {\n        onPageView\n      }\n      isCheckedInitialState\n      label\n      isRequired\n      clientSideValidationErrorMessage\n    }\n    ... on FinancingCheckbox {\n      initialClickstreamMetadata {\n        onPageView\n      }\n      isCheckedInitialState\n      leadFieldName\n      label\n      financingType\n    }\n  }\n  telephoneConsumerProtectionActDisclaimer {\n    text\n    textAttributes {\n      __typename\n      ... on TourViewModuleTextLinkAttribute {\n        tokenEndIndex\n        tokenStartIndex\n        url\n      }\n      ... on TourViewModuleTextTooltipAttribute {\n        tokenEndIndex\n        tokenStartIndex\n        tooltipText\n      }\n    }\n  }\n  tcpa {\n    telephoneConsumerProtectionActDisclaimer {\n      text\n      textAttributes {\n        __typename\n        ... on TourViewModuleTextLinkAttribute {\n          tokenEndIndex\n          tokenStartIndex\n          url\n        }\n        ... on TourViewModuleTextTooltipAttribute {\n          tokenEndIndex\n          tokenStartIndex\n          tooltipText\n        }\n      }\n    }\n    clickstreamMetadata {\n      onPageView\n    }\n  }\n  error {\n    isRecoverable\n    message\n    type\n  }\n  clickstreamMetadata {\n    onPageView\n  }\n}\n\nfragment ContactForm_abTests on ABTests {\n  ARCS_CONTACT_FORM_MFE_DATA_FETCHING: abTest(\n    trial: "ARCS_CONTACT_FORM_MFE_DATA_FETCHING"\n  )\n  ARCS_DATADOG_FEATURE_FLAG: abTest(trial: "ARCS_DATADOG_FEATURE_FLAG")\n  ARCS_DATADOG_FEATURE_FLAG_LIGHTBOX: abTest(\n    trial: "ARCS_DATADOG_FEATURE_FLAG_LIGHTBOX"\n  )\n  ARCS_DATADOG_FEATURE_FLAG_MOBILE_APP_MODAL_POST_SUBMIT: abTest(\n    trial: "ARCS_DATADOG_FEATURE_FLAG_MOBILE_APP_MODAL_POST_SUBMIT"\n  )\n  ARCS_SUBMIT_FLOW_LEAD_STRATEGY: abTest(trial: "ARCS_SUBMIT_FLOW_LEAD_STRATEGY")\n  ARCS_SPLIT: abTest(trial: "ARCS_SPLIT")\n  FSHDP_OPTIMIZATION: abTest(trial: "FSHDP_OPTIMIZATION")\n  ARCS_ELEVATING_ALAN_INLINE_TOUR_UPDATE: abTest(\n    trial: "ARCS_ELEVATING_ALAN_INLINE_TOUR_UPDATE"\n  )\n}\n\nfragment ContactForm_showcase on Showcase {\n  showingTimePlusAgent {\n    email\n    firstName\n    agentPhotoUrl\n    lastName\n    phone\n  }\n}\n',
        'isDebugRequest': False,
    },
    
    'endpoint': 'https://www.zillow.com/graphql/',
    'method': 'POST',
    'output_filename': 'zillow_agent_data.json'
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_api_config(property_type):
    """
    Get the API configuration for a specific property type
    
    Args:
        property_type (str): 'rental', 'sale', or 'agent'
    
    Returns:
        dict: API configuration
    """
    configs = {
        'rental': RENTAL_API_CONFIG,
        'sale': SALE_API_CONFIG,
        'agent': AGENT_API_CONFIG
    }
    
    if property_type.lower() not in configs:
        raise ValueError(f"Invalid property type: {property_type}. Use 'rental', 'sale', or 'agent'")
    
    return configs[property_type.lower()]

def update_search_cookie(base_search, page_number, pattern):
    """Update the search cookie with the correct page number"""
    updated_search = re.sub(pattern, f'p%3D{page_number}', base_search)
    return updated_search

def update_referer_header(base_referer, page_number, pattern):
    """Update the referer header with the correct page number"""
    updated_referer = re.sub(pattern, f'currentPage%22%3A{page_number}', base_referer)
    return updated_referer

def get_available_property_types():
    """Get list of available property types"""
    return ['rental', 'sale', 'agent'] 