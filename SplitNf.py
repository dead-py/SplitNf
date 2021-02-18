# MODELO 33 2102 14564469000672 55 001 000091965 1 00233526 2
#        UF A/M  CNPJ           MD SER Nº NOTA   T COD NUM   V

# UNIDADE FEDERAL 
# ANO/MÊS
# CNPJ
# MODELO DO DOCUMENTO (55 - NF-e / 57 - CT-e / 58 - MDF-e)
# SÉRIE DO DOCUMENTO
# Nº DA NOTA
# TIPO DE EMISSÃO
# CÓDIGO NUMÉRICO
# DÍGITO VERIFICADOR

codigos_uf = [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]

def split_nf(cod_nf='33210214564469000672550010000919651002335262'):

    modelo_nf = ''

    while len(cod_nf) < 44:
        return 1
    
    uf_nf = cod_nf[0:2]
    date_nf = cod_nf[2:6]
    cnpj_nf = cod_nf[6:20]
    mod_nf = cod_nf[20:22]
    serie_nf = cod_nf[22:25]
    nota_nf = cod_nf[25:34]
    tipo_nf = cod_nf[34:35]
    codnum_nf = cod_nf[35:43]
    verif_nf = cod_nf[43]

    if int(mod_nf) == 55:
        modelo_nf = "NF-e"
    
    elif int(mod_nf) == 57:
        modelo_nf = "CT-e"
    
    elif int(mod_nf) == 58:
        modelo_nf = "MDF-e"
    
    else:
        modelo_nf = "CÓDIGO DE DOCUMENTO INVÁLIDO"


    if int(uf_nf) not in codigos_uf:
        codigo_uf = "CÓDIGO DE UF INVÁLIDO"

    pass

split_nf()
