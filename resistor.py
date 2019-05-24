#-*- coding: utf-8 -*-
def resistor_search(vin, vout, max_error=0.01):
  """Função de busca de valores de resistores para um divisor de tensão de
  tensão utilizando valores comerciais.

  Parâmetros
  ==========
  vin : float
    Valor de entrada do resistor de tensão.
  vout : float
    Valor de saída do resistor de tensão.
  max_error : float
    Valor máximo de erro do sistema. (default 0.01)

  Retorna
  =======
  resistores : list
    Lista de documentos contendo as possíveis combinações que atendam
    os requisitos.
  """
  try:
    val_tab = [1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1]
    pot = [10,10**2,10**3,10**4,10**5, 10**6]
    valores = [round(i*m,2) for i in val_tab for m in pot]

    resistores = []
    for r1 in valores:
        for r2 in valores:
            error = abs(vout - vin*(r2/(r1+r2)))
            if error <= max_error:
              doc = {'R1':r1,'R2':r2,'Error':error}
              if doc not in resistores:
                resistores.append(doc)

    if len(resistores)>0:
      print(f'Sucesso.')
    else:
      print('Falha, não encontrado resistores que atendam os requisitos.')

    return resistores

  except Exception as e:
    print(f'Error: {e}')


if __name__ == '__main__':
  try:
    resistores = resistor_search(vin=22, vout=5, max_error=0.01)
    for r in resistores:
      print(r)

  except Exception as e:
    print(f'Error: {e}')
