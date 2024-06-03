
def flowchart_logic(a, b, c):
    if a > b:
        if a > c:
            return(c)
        else:
            return(a)
    elif b > c:
        return(b)
    else:
        return(c)

def test_flowchart_logic():
    #test cases in form (a, b, c, expected_result)
    # 4 outcomes ignoring edge cases
    test_cases = [
        (3, 2, 1, 1),
        (3, 2, 4, 3),
        (1, 2, 3, 3),
        (1, 2, 1, 2)
    ]

    for i, (a, b, c, expected) in enumerate(test_cases):
        result = flowchart_logic(a, b, c)
        assert result == expected, f"Test case {i+1} failed"

    print("all test cases passed!")

#run the test function
test_flowchart_logic()

