from datetime import datetime, timedelta

#dataFormatada = datetime.now() data e hora atual
#dataAtual = dataFormatada.strftime('%d-%m-%Y %H.%M') formatado
data = datetime.now()
dataAtual = data.strftime('%d/%m/%Y') #pega a data atual e corrige para o formato correto
dataAnterior = data - timedelta(days=1) #calcula a data de acordo com o número desejado
dataAnterior = dataAnterior.strftime('%d/%m/%Y') #pega a data anterior e corrige para o formato desejado
dataInicial = ""
dataFinal = ""
dataAtualEmail = data.strftime('%d/%m/%Y')