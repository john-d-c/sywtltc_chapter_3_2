import JD_april11_cypher


def test_encode():
    assert JD_april11_cypher.encode("text") == "whAw"
    assert JD_april11_cypher.encode("turtle") == "wxuwoh"
    assert JD_april11_cypher.encode("GitHub") == "JlwKxe"
    assert JD_april11_cypher.encode("Simpli.fi") == "Vlpsol;il"
    assert JD_april11_cypher.encode("1407 Texas St") == "473a WhAdv Vw"

def text_decode():
    assert JD_april11_cypher.decode("Mrkq Gdylg Frrn") == "John David Cook"
    assert JD_april11_cypher.decode("b4a c47 ac93") == "817 914 7960"
    assert JD_april11_cypher.decode("rqoB wkuhh pruh zrugv") == "only three more words"
    assert JD_april11_cypher.decode("jrwwd pdnh *hp udqgrp") == "gotta make 'em random "
    assert JD_april11_cypher.decode("Rrsv/ wrr odwh") == "Oops, too late"
