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

codigos_uf = [11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 41, 42, 43, 50, 51, 52, 53]
nomes_uf = ['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF']
series = {
    1:'NF-e',
    2:'CT-e',
    3:'NFS-e',
    4:'NFC-e',
    5:'CF-e',
    6:'MF-e',
    7:'MDF-e',
    8:'NFAe',
    9:'NF Complementar',
    10:'NF Denegada',
    11:'NF Rejeitada',
    12:'NF de Exportação',
    13:'NF de Remessa'
    }

def split_nf(cod_nf='33210214564469000672550010000919651002335262'):

    modelo_nf = ''
    unid_federal = ''


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

    if int(mod_nf) == 55:  # Checa o modelo do documento
        modelo_nf = "NF-e"
    
    elif int(mod_nf) == 57:
        modelo_nf = "CT-e"
    
    elif int(mod_nf) == 58:
        modelo_nf = "MDF-e"
    
    else:
        modelo_nf = "CÓDIGO DE DOCUMENTO INVÁLIDO"


    if int(uf_nf) not in codigos_uf:  # Checa a unidade federal
        codigo_uf = "CÓDIGO DE UF INVÁLIDO"

    else:
        uf_index = codigos_uf.index(int(uf_nf))

        unid_federal = nomes_uf[uf_index]


    data = date_nf[2:4] + '/' + date_nf[0:2]
    
    cnpj = cnpj_nf[0:2] + '.' + cnpj_nf[2:5] + '.' + cnpj_nf[5:8] + '/' + cnpj_nf[8:12] + '-' + cnpj_nf[12:]


    return uf_nf, unid_federal,  data, cnpj, modelo_nf, serie_nf, nota_nf, tipo_nf, codnum_nf, verif_nf

print(split_nf())
