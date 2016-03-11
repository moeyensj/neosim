import os
import numpy as np
import pandas as pd

def readTracklet(tracklet):
    return np.fromstring(tracklet, sep=" ", dtype=int) 

def readTrack(track):
    return np.fromstring(track, sep=" ", dtype=int)

def readIds(ids):
    return np.fromstring(track, sep=" ", dtype=int)

def readDetectionsIntoDataframe(detsFile, header=None):
    return pd.read_csv(detsFile, header=header, names=["diaId", "visitId", "ssmId", "ra", "dec", "mjd", "mag", "snr"], index_col="diaId", delim_whitespace=True)

def readNight(detFile):
    return int(os.path.basename(detFile).split(".")[0])

def readWindow(trackFile):
    window = os.path.basename(trackFile).split(".")[0].split("_")
    return int(window[1]), int(window[3])