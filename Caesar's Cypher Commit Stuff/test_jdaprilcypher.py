import jdaprilcypher


def test_encode():
    assert jdaprilcypher.encode("text") == "whAw"
    assert jdaprilcypher.encode("turtle") == "wxuwoh"
    assert jdaprilcypher.encode("GitHub") == "JlwKxe"
    assert jdaprilcypher.encode("Simpli.fi") == "Vlpsol;il"
    assert jdaprilcypher.encode("1407 Texas St") == "473a WhAdv Vw"

def text_decode():
    assert jdaprilcypher.decode("Mrkq Gdylg Frrn") == "John David Cook"
    assert jdaprilcypher.decode("b4a c47 ac93") == "817 914 7960"
    assert jdaprilcypher.decode("rqoB wkuhh pruh zrugv") == "only three more words"
    assert jdaprilcypher.decode("jrwwd pdnh *hp udqgrp") == "gotta make 'em random "
    assert jdaprilcypher.decode("Rrsv/ wrr odwh") == "Oops, too late"
