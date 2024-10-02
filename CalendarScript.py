"""
Este script monitora a atividade de uso de IDEs no sistema e cria eventos no Google Calendar com base no tempo de uso registrado. 
O script utiliza a API do Google Calendar para criar eventos de forma automatizada e é configurado para usar credenciais de serviço.

Antes de usar:
Siga o passo a passo detalhado no README para configurar corretamente o ambiente, credenciais e IDs necessários.
"""

import os
import datetime
import pytz
import json
import psutil
import time

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Definições e configurações do script
scopes = ['https://www.googleapis.com/auth/calendar']
credentialsFile = 'utility-range-437213-@example.json'  # Substitua pelo nome do arquivo JSON de credenciais do Google
calendarIdFile = 'CalendarIdConfig.json'  # Arquivo de configuração para o Calendar ID

def loadCalendarId():
    """
    Carrega o ID do calendário a partir de um arquivo JSON.

    O ID do calendário deve ser fornecido no arquivo `CalendarIdConfig.json` no seguinte formato:
    {
        "calendarId": "seu_calendar_id_aqui"
    }

    Retorna:
        str: O ID do calendário se o arquivo e o ID estiverem configurados corretamente, ou None caso contrário.
    """
    if not os.path.exists(calendarIdFile):
        print(f"Arquivo '{calendarIdFile}' não encontrado. Certifique-se de criar este arquivo e adicionar o seu Calendar ID.")
        return None

    try:
        with open(calendarIdFile, 'r') as f:
            config = json.load(f)
            calendarId = config.get("calendarId", None)

            if not calendarId:
                print(f"O arquivo '{calendarIdFile}' está presente, mas o 'calendarId' não foi configurado corretamente.")
                return None

            return calendarId
    except json.JSONDecodeError:
        print(f"O arquivo '{calendarIdFile}' não está formatado corretamente como JSON.")
        return None

def createEvent(startTime, endTime):
    """
    Cria um evento no Google Calendar com base no tempo de uso monitorado.

    Parâmetros:
        startTime (datetime.datetime): O horário de início do evento.
        endTime (datetime.datetime): O horário de término do evento.

    O evento é criado no calendário especificado no arquivo `CalendarIdConfig.json` com o título "Programação" e uma breve descrição.
    Certifique-se de que o arquivo de credenciais e o Calendar ID estejam configurados corretamente.
    """

    # Verifica se o arquivo de credenciais foi configurado
    if not os.path.exists(credentialsFile):
        print(f"Arquivo de credenciais '{credentialsFile}' não encontrado. Certifique-se de configurar o seu arquivo JSON do Google Cloud.")
        return

    # Carrega as credenciais
    creds = service_account.Credentials.from_service_account_file(
        credentialsFile, scopes=scopes
    )

    # Carrega o Calendar ID
    calendarId = loadCalendarId()
    if not calendarId:
        print(f"Erro ao carregar o Calendar ID. Verifique se o arquivo '{calendarIdFile}' está configurado corretamente.")
        return

    # Configuração da API do Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    timezone = pytz.timezone('America/Sao_Paulo')
    startTime = timezone.localize(startTime)
    endTime = timezone.localize(endTime)

    event = {
        'summary': 'Programação',
        'location': 'Home',
        'description': 'Tempo programando',
        'start': {
            'dateTime': startTime.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': endTime.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
    }

    try:
        event = service.events().insert(calendarId=calendarId, body=event).execute()
        print(f'Evento criado: {event.get("htmlLink")}')
    except Exception as e:
        print(f'Ocorreu um erro ao criar o evento: {e}')

def monitorActivity():
    """
    Monitora a atividade das IDEs especificadas e cria um evento no Google Calendar quando o uso de IDEs é interrompido.

    As seguintes IDEs são monitoradas:
    - Visual Studio Code (`Code.exe`)
    - IntelliJ IDEA (`idea64.exe`)
    - Eclipse (`eclipse.exe`)

    O script verifica periodicamente se alguma das IDEs está sendo executada. Quando uma IDE começa a ser usada, 
    o tempo de início é registrado. Quando nenhuma IDE está em execução, o tempo total é calculado e um evento é criado no Google Calendar.
    """
    ideExecutables = ['Code.exe', 'idea64.exe', 'eclipse.exe']
    activeStartTime = None

    while True:
        ideRunning = any(
            executable in (p.name() for p in psutil.process_iter()) for executable in ideExecutables
        )

        if ideRunning:
            if activeStartTime is None:
                activeStartTime = datetime.datetime.now()
                print("IDE em uso, iniciando o rastreamento...")

        else: 
            if activeStartTime is not None: 
                endTime = datetime.datetime.now()
                print(f"IDE não está mais em uso. Tempo total: {endTime - activeStartTime}")

                # Cria o evento no Google Calendar no dia seguinte
                next_day_start = activeStartTime + datetime.timedelta(days=1)
                next_day_end = endTime + datetime.timedelta(days=1)

                createEvent(next_day_start, next_day_end)

                activeStartTime = None

        time.sleep(10)

if __name__ == '__main__':
    """
    Função principal que executa o monitoramento da atividade das IDEs.

    O monitoramento é contínuo e verifica a cada 10 segundos se as IDEs especificadas estão em uso.
    Quando o uso é interrompido, um evento é criado no Google Calendar para registrar o tempo total de uso.
    """
    monitorActivity()
