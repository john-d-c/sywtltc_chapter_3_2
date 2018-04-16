import sample_workflow_playground


def test_encode():
    assert sample_workflow_playground.encode("text") == "whAw"

def text_decode():
    assert sample_workflow_playground.decode("whAw") == "text"


