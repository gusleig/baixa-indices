from bcb import sgs
import datetime
import pandas as pd
from bcb import Expectativas
from bcb import TaxaJuros
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_data(dt='2002-01-01'):

    sns.set_theme()

    # https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
    # occupied people = codigo 7420 (2000 - 2015)
    occup = sgs.get({'Occupied people': 7420}, start=dt)
    occup.plot(figsize=(15, 10))
    plt.show()

    caged = sgs.get({'Caged Total': 28763}, start=dt)

    pnad = sgs.get({'Unemployment rate - PNADC': 24369}, start=dt)

    pnad.plot(figsize=(15, 10))
    plt.show()

    # Busca a série da SELIC no SGS
    selic = sgs.get({'selic': 432}, start=dt)
    print(selic)

    # Busca a série do IPCA e IGP-M
    ifl_month = sgs.get({'ipca': 433,
                     'igp-m': 189}, start=dt)

    # Transforma a frequência da data em mensal
    ifl_month.index = ifl_month.index.to_period('M')
    print(ifl_month)


def taxa_juros():
    # Descreve as informações

    juros = TaxaJuros()

    juros.describe()


def expectativas():

    """
    Indices
    ['Balança comercial' 'Conta corrente' 'Resultado primário' 'IPCA-15'
     'PIB Agropecuária' 'PIB Indústria' 'PIB Serviços' 'PIB Total'
     'IPCA Administrados' 'Investimento direto no país' 'Resultado nominal'
     'Dívida líquida do setor público' 'Dívida bruta do governo geral'
     'IGP-DI' 'IGP-M' 'INPC' 'IPA-DI' 'IPA-M' 'IPCA' 'IPC-Fipe'
     'Produção industrial' 'Selic' 'Câmbio' 'Taxa de desocupação'
     'PIB Despesa de consumo da administração pública'
     'PIB Formação Bruta de Capital Fixo' 'PIB Exportação de bens e serviços'
     'PIB Importação de bens e serviços' 'IPCA Livres' 'IPCA Serviços'
     'IPCA Bens industrializados' 'IPCA Alimentação no domicílio'
     'PIB Despesa de consumo das famílias']

    :return:
    """

    # Obtém as informações do API

    expec = Expectativas()

    # Realiza a leitura dos endpoints

    expec.describe()
    print("todos indicadores")

    expec.describe('ExpectativasMercadoAnuais')

    ep = expec.get_endpoint('ExpectativasMercadoAnuais')

    # mostra todos indicadores anuais

    # print(ep.query().collect()['Indicador'].unique())

    ep.query().filter(ep.Indicador =='Selic').collect()

    # 'Taxa de desocupação'

    ep.query().filter(ep.Indicador =='Taxa de desocupação').collect()


if __name__ == '__main__':
    get_data()
    expectativas()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
