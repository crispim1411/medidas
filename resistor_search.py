#-*- coding: utf-8 -*-
import click, re


@click.command()
@click.argument('vin',type=click.FLOAT)
@click.argument('vout',type=click.FLOAT)
@click.option('--max-error','-e',
    default=0.01,
    help='Valor máximo de erro (default 0.01)'
)
@click.option('--greater-than-equal','-gte',
    type=click.Choice(['10','100','1k','10k','100k','1M']),
    help='Retornar valores maiores ou iguais que'
)
def resistor_search(vin, vout, max_error,greater_than_equal):
    """Função de busca de valores de resistores para um divisor de tensão
    utilizando resistores de valores comerciais. Apresentado em verde as escolhas
    até 30% do erro máximo, em amarelo até 90% e em vermelho as que excedem
    90% da margem de erro.

    Parâmetros:

        vin(float): Valor de entrada do divisor de tensão.

        vout(float): Valor de saída do divisor de tensão.
    """
    try:
        val_tab = [1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1]
        pot_symbol = {'1':1,'10':10,'100':100,'1k':1000,'10k':10**4,'100k':10**5,'1M':10**6}

        if greater_than_equal:
            gte_val = pot_symbol[greater_than_equal]
            pot = [p for p in pot_symbol.values() if p >= gte_val]
        else:
            pot = pot_symbol.values()
        valores = [round(i*m,2) for i in val_tab for m in pot]

        resistores = []
        for r1 in valores:
            for r2 in valores:
                error = abs(vout - vin*(r2/(r1+r2)))/vout
                if error <= max_error:
                    doc = {'R1':resistor_symbol(r1),'R2':resistor_symbol(r2),'Error':round(error,4)}
                    if doc not in resistores:
                        resistores.append(doc)

        resistores = sorted(resistores, key=lambda x: x['Error'])
        if len(resistores)==0:
            print('Falha, não encontrado resistores que atendam os requisitos.')

        for r in resistores:
            if r['Error']/max_error>0.9:
                click.echo(click.style(str(r),fg='red'))
            elif r['Error']/max_error>0.3:
                click.echo(click.style(str(r),fg='yellow'))
            elif r['Error']/max_error>=0:
                click.echo(click.style(str(r),fg='green'))

        print(f'{len(resistores)} Resultados.')
        print('Faixa de erro (teórico):')
        print('verde: até 30%')
        print('amarelo: 30% ~ 90%')
        print('vermelho: acima 90%')

    except Exception as e:
        print(f'Error: {e}')


def resistor_symbol(resistor):
    """Função para converter valor resistor para notação comercial.
    Exemplo: 2700 -> 2.7k

    Parâmetros:
        resistor (float) : Resistor a ser convertido em notação.

    Retorna :
        str_resistor (str) : String com a notação comercial do resistor.
    """

    m = re.search('[0-9]+', str(resistor))
    if m:
        digits = m.end()
        if digits > 6:
            str_resistor = str(resistor/10**6).split('.0')[0] + 'M'
        elif digits > 3:
            str_resistor = str(resistor/1000).split('.0')[0] + 'k'
        else:
            str_resistor = str(resistor).split('.0')[0]

        return str_resistor


if __name__ == '__main__':
    resistor_search()
