import pandas as pd
import numpy as np
import storage_char as sc

#Example Asset
FirstBatt = sc.Asset(
    dod = .86
    , mw_cap = 15
    , roundtrip = .9
    , mwh_cap = 60
    , degrad = .99)
