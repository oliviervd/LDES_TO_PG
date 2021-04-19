import subprocess
import pandas as pd
from pprint import pprint


with open("dmg_obj.json", "w") as f:
    dmg_output_obj = subprocess.run("actor-init-ldes-client --pollingInterval 5000 --mimeType application/ld+json --context /Users/oliviervandhuynslager/Documents/ldes_dash/context.jsonld --fromTime 2021-01-01T15:48:12.309Z --emitMemberOnce true https://lodi.ilabt.imec.be/coghent/dmg/objecten"
                                    , shell=True, stdout=f, text=True)

print(dmg_output_obj.stdout)
