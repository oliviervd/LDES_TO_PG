# LDES_TO_PG [WORK IN PROGRESS]

replicate coghent Linked Data Event Streams into PostgreSQL docker container or export as csv, xcel. 

Available collections: 
* Design Museum Gent (DMG)
* Huis van Alijn (HVA)
* Industriemuseum (IM)
* STAM
* Archief Gent (ARCHIEF)
* Thesaurus (conceptlist)
* Agent list: agents (creators, persons and intstitutions) that are related to the published objects.

## USAGE 

for example if you want to fetch data from Design Museum Gent en Huis Van Alijn you use the following line of code in CLI:
`python3 main.py --fetch DMG --fetch HVA`

## License
This project is released as an open-source project under the MIT License
