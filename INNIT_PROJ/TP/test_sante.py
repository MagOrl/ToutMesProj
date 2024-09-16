def test_sante():
    assert sante(1.8, 80) == "normal" #indique que sante(1.8, 80) doit retourner "normal"
    assert sante(1.6, 67) == "surpoids" #indique que sante(1.6, 67) doit retourner "surpoid"
