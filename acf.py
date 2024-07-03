import pandas as pd

import os
from typing import Union


def transform_acf(in_path: Union[str, os.PathLike]) -> pd.DataFrame:
    with open(in_path) as in_file:
        data = in_file.read().split('Data:\n')[1].splitlines(keepends=False)
    # print(data)
    results = []
    for idx in range(0, len(data), 2):
        r, g, b = [int(float(x)) for x in data[idx].split(' ')]
        results.append(dict(
            sample_name=data[idx+1],
            r=r,
            g=g,
            b=b
        ))
    return pd.json_normalize(results)


if __name__ == "__main__":
    print(transform_acf('/home/gluck/Никольский_Листья/Волгоградский_пр-т_1.acf'))
