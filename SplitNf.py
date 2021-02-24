# MODELO 33 2102 14.564.469/0006-72 55 001 000091965 1 00233526  2
#        UF A/M  CNPJ               MD SER Nº NOTA   T COD NUM   V

# UNIDADE FEDERAL 
# ANO/MÊS
# CNPJ
# MODELO DO DOCUMENTO (55 - NF-e / 57 - CT-e / 58 - MDF-e)
# SÉRIE DO DOCUMENTO
# Nº DA NOTA
# TIPO DE EMISSÃO
# CÓDIGO NUMÉRICO
# DÍGITO VERIFICADOR
# 33210214564469000672550010000919651002335262

codigos_uf = [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]
nf_list = []

def split_nf(nf_list):

    for nf in nf_list:

        uf_nf = nf[0:2]
        date_nf = nf[2:6]
        cnpj_nf = nf[6:20]
        mod_nf = nf[20:22]
        serie_nf = nf[22:25]
        nota_nf = nf[25:34]
        tipo_nf = nf[34:35]
        codnum_nf = nf[35:43]
        verif_nf = nf[43]

        data = date_nf[2:4] + '/' + date_nf[0:2]
    
        cnpj = cnpj_nf[0:2] + '.' + cnpj_nf[2:5] + '.' + cnpj_nf[5:8] + '/' + cnpj_nf[8:12] + '-' + cnpj_nf[12:]


        return uf_nf, data, cnpj, mod_nf, serie_nf, nota_nf, tipo_nf, codnum_nf, verif_nf, 0, 2, 3, 4, 5, 6


def split_nf_list(cod_nf='00000000000000000000000000000000000000000000'):

    if len(cod_nf) > 44:
        nf_list.append(cod_nf.split(';'))

    elif len(cod_nf) < 44:
        return 1
    
    split_nf(nf_list)
    
    pass


print(split_nf_list)
