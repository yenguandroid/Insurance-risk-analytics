import pandas as pd

from src.hypothesis_tests import (
    run_ttest,
    run_chi_square
)


def test_ttest():

    group_a = [1, 2, 3, 4, 5]

    group_b = [2, 3, 4, 5, 6]

    result = run_ttest(group_a, group_b)

    assert "p_value" in result


def test_chi_square():

    table = pd.DataFrame(
        [
            [10, 20],
            [20, 40]
        ]
    )

    result = run_chi_square(table)

    assert "p_value" in result