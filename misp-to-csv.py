import requests
import json
import csv

# The basic URL + MISP-API-Key
url = "https://domain.com"
api_key = "API-KEY"

# Headers for the authentication
headers = {
    "Authorization": api_key,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Body of the HTTP Request,
body = {
    "returnFormat": "json",
    "page":1,
    "type": {
        "OR": [
            "ip-src",
            "ip-dst"
        ]
    },
    "tags": {
        "OR": [
            "tlp:green"
        ]
    }
}

# API call
response = requests.post(url, headers=headers, json=body)


# Verification if API call was succesfull
if response.status_code == 200:
    try:
        iocs = response.json()
        # Check if the response contains json
        if iocs:
            # Filename for the CSV file
            csv_filename = "ioc_results.csv"

            # Open the file with 'utf-8' codec
            with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
                # Make the file write able
                csv_writer = csv.writer(csv_file)

                # Write the headers with the titles of the fields
                csv_writer.writerow([
                    "ID",
                    "Org ID",
                    "Date",
                    "Info",
                    "UUID",
                    "Published",
                    "Analysis",
                    "Attribute Count",
                    "Orgc ID",
                    "Timestamp",
                    "Distribution",
                    "Sharing Group ID",
                    "Proposal Email Lock",
                    "Locked",
                    "Threat Level ID",
                    "Publish Timestamp",
                    "Sighting Timestamp",
                    "Disable Correlation",
                    "Extends UUID",
                    "Protected",
                    "Org ID",
                    "Org Name",
                    "Org UUID",
                    "Orgc ID",
                    "Orgc Name",
                    "Orgc UUID",
                    "Event Tag ID",
                    "Event ID",
                    "Tag ID",
                    "Local",
                    "Relationship Type",
                    "Tag Name",
                    "Tag Colour",
                    "Tag is Galaxy"
                ])

                # Write json to the csv file
                for ioc in iocs:
                    
                    csv_writer.writerow([
                        ioc.get("id"),
                        ioc.get("org_id"),
                        ioc.get("date"),
                        ioc.get("info"),
                        ioc.get("uuid"),
                        ioc.get("published"),
                        ioc.get("analysis"),
                        ioc.get("attribute_count"),
                        ioc.get("orgc_id"),
                        ioc.get("timestamp"),
                        ioc.get("distribution"),
                        ioc.get("sharing_group_id"),
                        ioc.get("proposal_email_lock"),
                        ioc.get("locked"),
                        ioc.get("threat_level_id"),
                        ioc.get("publish_timestamp"),
                        ioc.get("sighting_timestamp"),
                        ioc.get("disable_correlation"),
                        ioc.get("extends_uuid"),
                        ioc.get("protected"),
                        ioc.get("Org", {}).get("id"),
                        ioc.get("Org", {}).get("name"),
                        ioc.get("Org", {}).get("uuid"),
                        ioc.get("Orgc", {}).get("id"),
                        ioc.get("Orgc", {}).get("name"),
                        ioc.get("Orgc", {}).get("uuid"),
                    ])

                    # Event Tag-fields (Multiple tags for one event)
                    event_tags = ioc.get("EventTag", [])
                    for event_tag in event_tags:
                        tag = event_tag.get("Tag", {})
                        csv_writer.writerow([
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            event_tag.get("id"),
                            event_tag.get("event_id"),
                            event_tag.get("tag_id"),
                            event_tag.get("local"),
                            event_tag.get("relationship_type"),
                            tag.get("name"),
                            tag.get("colour"),
                            tag.get("is_galaxy")
                        ])

            print("Json values are written to the CSV:", csv_filename)
