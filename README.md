# LDES_TO_PG [WORK IN PROGRESS]

replicate coghent LDES into postgres or export as csv, xcel:


## INSTALL

LDES_TO_PG makes use of @treecg/actor-init-ldes-client, metadata harvester for Linked Data Event Streams. In order to use this program make sure to install this first. 
```
actor-init-ldes-client --parameter ${PARAMETER} ${URL}
```

## USE 
```
python3 ldes_to_pg.py --fetch --timestamp
```
for example: 
```
python3 ldes_to_pg.py --fetch DMG --timestamp 2021-07-30T15:48:12:309Z

```

| Parameter | Description | Possible values |
|---------|-----------|----------|
|fetch|define collectiions to fetch from CoGhent LDES|DMG, HVA, STAM, IM, ARCHIEF, THESAURUS, AGENTS|
|timestamp |datetime to prune relations that have a lower datetime value |for example: 2020-01-01T00:00:00, default = "2021-01-01T15:48:12.309Z"|


## License
This project is released as an open-source project under the MIT License