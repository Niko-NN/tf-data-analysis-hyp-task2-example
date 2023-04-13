import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, p_value = ks_2samp(sample1, sample2)
    return p_value < 0.04
