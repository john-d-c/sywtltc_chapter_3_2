import JD_april11_cypher


def test_encode():
    assert JD_april11_cypher.encode("text") == "whAw"

def text_decode():
    assert JD_april11_cypher.decode("whAw") == "text"


