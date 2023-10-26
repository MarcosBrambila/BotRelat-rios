import  win32com.client as win32
import Indicadores

outlook = win32.Dispatch('outlook.application')
anexo_RelatorioVendas = "C://Users/USER/Desktop/Documento/Relatorio_Gerencial.xlsm"

#cria um e-mail
email = outlook.CreateItem(0)

email.To =  "mb.construart@gmail.com; mv.brambilas@gmail.com"
email.Subject = "Relatório de vendas"
email.HTMLBody = f"""
<p>Bom dia,</p>

<p>Segue anexo do relatório de vendas até a data {Indicadores.dataAtualEmail}.</p>

<p>Favor, não responder este e-mail.</p>

<p>Grato.</p>
"""

email.Attachments.Add(anexo_RelatorioVendas)
email.Send()

print("Email enviado")


