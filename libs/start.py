"""
author: Shiv, [please add your name if you update the script]
email: shivkj001@gmail.com
date: 20-02-2021
"""
import datetime as dt
import json
import math
import os
import pickle as pkl
import re
import shutil
import sys
from abc import abstractmethod, abstractproperty
from argparse import ArgumentParser
from collections import Counter, defaultdict, deque
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from functools import cached_property, lru_cache, partial, wraps
from glob import glob
from itertools import chain, combinations, product
from logging import getLogger
from time import time
from traceback import format_exc
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dateutil.parser import parse
from tqdm import tqdm
