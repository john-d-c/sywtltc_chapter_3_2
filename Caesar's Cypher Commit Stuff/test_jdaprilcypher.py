import jdaprilcypher


def test_encode():
    assert jdaprilcypher.encode("text",3) == "whAw"
    assert jdaprilcypher.encode("turtle",3) == "wxuwoh"
    assert jdaprilcypher.encode("GitHub",3) == "JlwKxe"
    assert jdaprilcypher.encode("Simpli.fi",3) == "Vlpsol;il"
    assert jdaprilcypher.encode("1407 Texas St",3) == "473a WhAdv Vw"
    assert jdaprilcypher.encode("soda",7) == "zvkh"
    assert jdaprilcypher.encode("bird",10) == "lsBn"
    assert jdaprilcypher.encode("rhino",12) == "DtuzA"

def text_decode():
    assert jdaprilcypher.decode("Mrkq Gdylg Frrn",3) == "John David Cook"
    assert jdaprilcypher.decode("b4a c47 ac93",3) == "817 914 7960"
    assert jdaprilcypher.decode("rqoB wkuhh pruh zrugv",3) == "only three more words"
    assert jdaprilcypher.decode("jrwwd pdnh *hp udqgrp",3) == "gotta make 'em random "
    assert jdaprilcypher.decode("Rrsv/ wrr odwh",3) == "Oops, too late"
    assert jdaprilcypher.decode("yzwyqj",5) == "turtle"
    assert jdaprilcypher.decode("zvkh",7) == "soda"
    assert jdaprilcypher.decode("lsBn",10) == "bird"
    assert jdaprilcypher.decode("DtuzA",12) == "rhino"
