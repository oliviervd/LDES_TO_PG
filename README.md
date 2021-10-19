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

| Parameter | Description | Possible values |
|---------|-----------|----------|
|--fetch|define collections to fetch from CoGhent LDES |DMG, HVA, STAM, IM, ARCHIEF, THESAURUS, AGENTS|
|--timestamp |datetime to prune relations that have a lower datetime value |for example: 2020-01-01T00:00:00, default = "2021-01-01T15:48:12.309Z"|
|--result |define the wished for result (pg=postrgres)|pg, csv, xlsx|

for example if you want to fetch data from Design Museum Gent en Huis Van Alijn starting from 15 november 2021 you use the following line of code in CLI:

`python3 main.py --fetch DMG --fetch HVA --timestamp 2021-10-10T15:48:12.309Z`

## License
This project is released as an open-source project under the MIT License
