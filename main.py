from TelefonesBR import TelefonesBR
from ValidaCPF_CNPJ import Documento
from validate_docbr import CPF,CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "45036394046"
exemplo_telefone = "05541997678581"

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
telefone_objeto = TelefonesBR(exemplo_telefone)
print(telefone_objeto)

