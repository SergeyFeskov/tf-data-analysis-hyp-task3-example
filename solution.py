import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 875744266  # Ваш chat ID, не меняйте название переменной

def solution(control_sample, test_sample) -> bool:
    return (
        ttest_ind(
            test_sample, control_sample, alternative="less", equal_var=True
        ).pvalue
        < 0.01
    )
