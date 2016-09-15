import csv

class comp_archivos:
    num_coincidencias = 0
    def __init__(self):
        self.documento_principal()


    def documento_principal(self):
        doc_principal = open("/home/alan/Escritorio/debito/152F0805.TXT")
        for l_principal in doc_principal:
            cbu_principal = l_principal[38:68]
            rebotado_principal = l_principal[144:145]
            cbu_devulto_secundario = self.documento_secundario(cbu_principal,rebotado_principal)


    def documento_secundario(self,cbu_principal,rebotado_principal):
        doc_secundario = open("/home/alan/Escritorio/debito/152F0811.TXT")
        for l_secundario in doc_secundario:
            cbu_secundario = l_secundario[38:68]
            rebotado = l_secundario[144:145]
            if cbu_secundario == cbu_principal and rebotado_principal != "R" and rebotado != "R":
                self.num_coincidencias += 1
                print cbu_principal,cbu_secundario,rebotado_principal,rebotado,self.num_coincidencias

        return cbu_secundario


            #            for lines_doc_prin in doc_principal.readlines():
            #
            #
            #   for lines_doc_sec in  doc_secundario.readlines():
            #       cbu_primario = lines_doc_prin[38:61]
            #       cbu_secundario = lines_doc_sec[38:61]
            #       print cbu_primario, cbu_secundario
            ##       if cbu_primario == cbu_secundario:
        #          print "hola"


comp_archivos()