def test_HDL_analysis():
    from chol_analysis import HDL_analysis 
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected