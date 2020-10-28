
def salario():
    print("**********************************")
    print("Cálculo salário/hora com impostos!")
    print("**********************************")

    valor = float(input("Informe o valor da hora: "))
    horas = float(input("Informe a quantidade de horas trabalhadas: "))
    salario_bruto = round(valor * horas, 2)
    valor_ir = salario_bruto * 0.11
    valor_inss = salario_bruto * 0.08
    valor_sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - valor_ir - valor_inss - valor_sindicato

    print("+ Salário Bruto  : R$ {}".format(salario_bruto))
    print("- IR (11%)       : R$ {}".format(valor_ir))
    print("- INSS (8%)      : R$ {}".format(valor_inss))
    print("- Sindicato (5%) : R$ {}".format(valor_sindicato))
    print("= Salário Líquido: R$ {}".format(salario_liquido))

if __name__ == "__main__":
    salario()