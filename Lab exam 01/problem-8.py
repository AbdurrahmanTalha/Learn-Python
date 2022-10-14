import my_code

st = "hello"

def test_make_upper():
    ret = my_code.make_upper(st)
    assert ret == st.upper();

def test_make_upper():
    ret = my_code.make_lower(st)
    assert ret == st.lower();


def test_make_upper():
    ret = my_code.make_capital(st)
    assert ret == st.capitalize()
