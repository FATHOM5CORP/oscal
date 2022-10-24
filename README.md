# FATHOM5 EXTENDS OSCAL

## Purpose

FATHOM5 supports the community advancement of NIST's OSCAL initiatives. This repo provides custom OSCAL content and supporting tools that enable compliance automation. Our first release includes an OSCAL Catalog, OSCAL Profile, and supporting data transformation scripts for NIST 800-171, forming the basis for compliance automation for US Controlled Unclassified Information. 

## Background

The [Open Security Controls Assessment Language (OSCAL)](https://pages.nist.gov/OSCAL/) created and maintained by NIST is the state of the art for compliance automation. OSCAL provides a mechanism for turning cybersecurity artifacts from static PDFs, Excel spreadsheets, and Word documents into machine-readable code. Reformating the data in this way is a critical first step to unlock the power of automation. 

| ![oscal-models](https://user-images.githubusercontent.com/103941493/196271319-7b26d9b5-ae15-41cf-8592-8f8eb5335810.png) |
|:--:|
| <b> Image Credits - NIST </b> |

As illustrated above, all OSCAL models must derive content from an OSCAL Catalog and OSCAL Profile.

[NIST provides this source material for SP 800-53](https://github.com/usnistgov/oscal-content/tree/main/nist.gov) (AKA Risk Management Framework). 

| <img width="964" alt="profile-catalog-example" src="https://user-images.githubusercontent.com/103941493/196271507-93f1c165-6f26-448e-b40c-4c5d4e42add3.png"> |
|:--:|
| <b> Image Credits - NIST </b> |

## Challenge for US Controlled Unclassified Information Compliance Automation

All DoD contractors processing, storing, or transmitting CUI must follow [NIST SP 800-171 (Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations)](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final). However, unlike for RMF, NIST has not yet published similar OSCAL content for SP 800-171.

## Solution for US CUI Compliance Automation

If DoD contractors want to leverage the state of the art to automate CUI Protection compliance, this project provides the fundamental building blocks.

Under <code>/tools</code>, you'll find a parser we wrote to take a raw tab-delimeted CSV of the 800-171 requirements and reformat the data into OSCAL-compliant JSON.

Under <code>/content/SP800-171</code>, you'll find a resulting OSCAL Catalog and OSCAL Profile for 800-171.

This content is being freely distributed under CC0 to help you automate your compliance for CUI.

## Viewing the SP 800-171 OSCAL Content

We developed this OSCAL Content to be readily ingestable by [EasyDynamics' OSCAL Viewer tool](https://oscal-viewer.msd.easydynamics.com/catalog/). Viewing it is as simple as navigating to their tool, replacing the URL in the OSCAL Catalog URL field with https://raw.githubusercontent.com/FATHOM5/oscal/main/content/SP800-171/oscal-content/catalogs/NIST_SP-800-171_rev2_catalog.json, and hitting Reload. You may also utilize [EasyDynamics' containerized deployment of the OSCAL Viewer](https://github.com/EasyDynamics/oscal-editor-deployment/tree/main/all-in-one) to edit locally and build your organization-specific OSCAL models from there. If running locally with the OSCAL Viewer from EasyDynamics, just clone this project and run the following command:

<code>$ docker run -p 8080:8080 -v "\<direct path to project\>\oscal\content\SP800-171\oscal-content":/app/oscal-content ghcr.io/easydynamics/oscal-editor-all-in-one</code>

NOTE: The above command uses backslashes for the local working directory, assuming you're running from Windows. If running from Linux, use forward slashes.

Then open up a browser to <code>localhost:8080</code>.

In either case, you'll see our OSCAL content for 800-171.

![oscal-800-171-viewed](https://user-images.githubusercontent.com/103941493/196277327-8e3d9204-f8c6-4a54-a032-fc52406cc557.png)

We also include a [copy of the Catalog converted to HTML](https://github.com/FATHOM5/oscal/blob/main/content/SP800-171/oscal-content/catalogs/NIST_SP-800-171_rev2_html_preview.html), which may be downloaded and viewed in any web browser.
  
## Including the SP 800-171 OSCAL Content in your Organization's OSCAL Models

You can follow NIST's guidance to import the 800-171 OSCAL Profile into your organization's OSCAL Models. For instance, [this page describes how to import a profile for your System Security Plan](https://pages.nist.gov/OSCAL/reference/latest/system-security-plan/json-reference/#/system-security-plan/import-profile).


