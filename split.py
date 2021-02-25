
def split_nf(nf_list):

    if len(nf_list) > 1:
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

            return uf_nf, data, cnpj, mod_nf, serie_nf, nota_nf, tipo_nf, codnum_nf, verif_nf
    else:
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

            return uf_nf, data, cnpj, mod_nf, serie_nf, nota_nf, tipo_nf, codnum_nf, verif_nf
    pass


def split_nf_list(cod_nf='00000000000000000000000000000000000000000000'):

    if len(cod_nf) > 44:
        nf_lista = cod_nf.split(';')
        return(split_nf(nf_lista))
    
    elif len(cod_nf) == 44:
        print(split_nf(str(cod_nf)))
        #return(split_nf(str(cod_nf)))
    
    else:
        return(1)

    pass


