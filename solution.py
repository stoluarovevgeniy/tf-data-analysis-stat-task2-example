import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 2049733859 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    B = 2 * x - 0.083
    Bup = np.quantile(B, p)
    Bdown = 2*B.mean() - Bup
    return Bdown, Bup
