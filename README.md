# mims-keeper

Service intended to handle presave enrichment through slim agents and 
saving data for the mims system to the datastore.

Initial Functionality:

- Service will provide an endpoint for clients to send a keep request. 
- Service will provide a response on successful save 

Next Stage Functionality:

- Enrichment of saving data with. (Note: I am wondering if we ultimately end up with an enrichment service and a data service.)
  - Tags
  - Topic

- Potentially async response for enrichment status.

async response on enrichment status.