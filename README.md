# Calendário Inteligente

![Organização da Área de Trabalho antes do script](./images/screenshot.png)

![Organização da Área de Trabalho depois do script](./images/screenshot.png)

## Sobre o Projeto

O **Calendário Inteligente** é um script Python criado para automatizar a criação de eventos no seu Google Calendar com base em atividades configuráveis. Este projeto tem como objetivo facilitar a rotina dos usuários, permitindo que eles acompanhem suas atividades diárias de forma eficiente.

Neste exemplo, o script foi adaptado para programadores. Ao abrir uma IDE, ele monitora o tempo que ela permanece aberta e, automaticamente, cria um evento intitulado "Programar". Ele registra o horário em que a atividade foi realizada e, no dia seguinte, programa um novo evento para o mesmo horário. Essa funcionalidade não apenas simplifica a organização das tarefas, mas também incentiva a repetição de hábitos saudáveis, ajudando todos os usuários a manterem-se produtivos em suas rotinas.

## Por que esse projeto foi criado?

O objetivo principal deste projeto é proporcionar uma oportunidade de aprendizado sobre automação de tarefas e integração de APIs. Ao utilizar a API do Google Calendar, o script demonstra como a programação pode simplificar a criação de eventos, automatizando a organização do tempo e das atividades diárias.

Esse projeto não só ilustra a prática da automação com scripts em Python, mas também promove o entendimento sobre como trabalhar com APIs para criar soluções eficientes. Essa experiência é valiosa para aprimorar habilidades em programação e gestão do tempo.

## Instalação e Execução

### Pré-requisitos

Para rodar esse script em seu ambiente local, você precisará de:

- **Python 3.6+**: Verifique se o Python está instalado utilizando o comando `python --version`.
- Biblioteca `shutil` (inclusa na biblioteca padrão do Python)
- Biblioteca `os` (inclusa na biblioteca padrão do Python)
- Biblioteca `datetime` (inclusa na biblioteca padrão do Python)

### Instalação

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/calendario-inteligente.git

2. Acesse o diretório do projeto:
   ```bash
   cd calendario-inteligente

3. (Opcional) Crie um ambiente virtual para gerenciar as dependências do Python:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows

4. Execute o script diretamente no terminal:
   ```bash
   python CalendarScript.py
   ```

## Passos para Configuração do Google Cloud Service

### Criar um Projeto no Google Cloud

1. **Acesse o Google Cloud Console**: 
   - Acesse [Google Cloud Console](https://console.cloud.google.com/).

2. **Criar um Novo Projeto**: 
   - Clique em "Selecionar um projeto" e, em seguida, "Novo projeto".
   - Dê um nome ao seu projeto e clique em "Criar".

### Ativar a API do Google Calendar

3. **Ativar a API**: 
   - No Google Cloud Console, vá para o menu de navegação e selecione "APIs e Serviços" > "Biblioteca".
   - Procure por "Google Calendar API" e clique nela.
   - Clique em "Ativar" para habilitar a API para o seu projeto.

### Criar Credenciais

4. **Criar Credenciais**: 
   - Após ativar a API, vá para "APIs e Serviços" > "Credenciais".
   - Clique em "Criar Credenciais" e selecione "Conta de Serviço".
   - Preencha as informações solicitadas e clique em "Criar".

### Gerar Chave de Autenticação

5. **Gerar Chave**: 
   - Após criar a conta de serviço, você terá a opção de criar uma chave. Selecione "Adicionar chave" > "Criar nova chave".
   - Escolha o formato JSON. Isso fará o download de um arquivo JSON contendo suas credenciais. **Mantenha esse arquivo em um local seguro**, pois ele contém informações sensíveis.

### Configuração do Arquivo JSON
6. **Conteúdo do Arquivo JSON**: 
   - O arquivo JSON baixado conterá informações como as abaixo, que são essenciais para autenticação:

   ```json
   {
     "type": "service_account",
     "project_id": "<seu_project_id>",
     "private_key_id": "<seu_private_key_id>",
     "private_key": "-----BEGIN PRIVATE KEY-----\n<suas_chaves_privadas>\n-----END PRIVATE KEY-----\n",
     "client_email": "<seu_email_da_conta_de_serviço>",
     "client_id": "<seu_client_id>",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<seu_email_da_conta_de_serviço>",
     "universe_domain": "googleapis.com"
   }
    ```

### Importante

Após baixar o arquivo JSON de credenciais, certifique-se de que ele esteja localizado na mesma pasta em que seu script Python está sendo executado. Isso é fundamental para que seu código consiga acessar as credenciais corretamente. Caso o arquivo esteja em um diretório diferente, você precisará ajustar o caminho no seu código para apontar para o local correto do arquivo.

## Configuração do Arquivo JSON no Código
No seu código Python, é necessário especificar o caminho do arquivo JSON de credenciais na variável credentials_file. Essa variável deve ser definida com o nome do arquivo JSON que você baixou. Por exemplo:

```bash
credentials_file = 'caminho/para/seu/arquivo.json'
```

Certifique-se de que o caminho esteja correto e que o arquivo JSON esteja na mesma pasta que o seu script, ou ajuste o caminho conforme necessário. Isso permitirá que seu código autentique a API do Google Calendar corretamente.

## Como Obter o ID do Google Calendar

Para que o seu script possa criar eventos em um calendário específico, é necessário obter o ID do Google Calendar desejado. Siga os passos abaixo:

1. **Acesse o Google Calendar**: 
   - Abra o [Google Calendar](https://calendar.google.com).

2. **Selecione o Calendário**: 
   - No painel à esquerda, localize a seção "Minhas agendas". Passe o mouse sobre o calendário que você deseja usar e clique nos três pontos que aparecem ao lado do nome.

3. **Configurações do Calendário**: 
   - Clique em "Configurações e compart" no menu que aparece.

4. **Localize o ID do Calendário**: 
   - Na página de configurações do calendário, role para baixo até encontrar a seção "Integrar agenda". O ID do calendário será exibido na opção "ID da agenda". O formato será algo como `seunome@gmail.com` ou `xxxxxxxxxx@group.calendar.google.com`.

5. **Copie o ID**: 
   - Copie o ID do calendário e cole no arquivo JSON `CalendarIDConfig` para que o seu script possa acessá-lo corretamente.

Agora você pode usar esse ID no seu código para criar eventos no calendário correto!

## Liberar Acesso ao Google Calendar

Após configurar seu projeto e obter o ID do calendário, é necessário liberar o acesso para que o script possa criar eventos no Google Calendar. Siga os passos abaixo:

1. **Obter o Email do Serviço no Google Cloud**:
   - Acesse o [Google Cloud Console](https://console.cloud.google.com/).
   - No menu lateral, clique em **IAM e Administração** e depois em **IAM**.
   - Na lista de membros, localize o usuário de serviço que você criou para seu projeto. O email deve ter um formato como `calendar-event-creator@seu-projeto.iam.gserviceaccount.com`. Copie esse email.

2. **Acesse as Configurações do Calendário**:
   - Abra o [Google Calendar](https://calendar.google.com) e localize o calendário desejado na seção "Minhas agendas".

3. **Compartilhar com Pessoas ou Grupos Específicos**:
   - Clique nos três pontos ao lado do nome do calendário e selecione "Configurações e compart".

4. **Adicionar o Email do Serviço**:
   - Na seção "Compartilhar com pessoas ou grupos específicos", insira o email que você copiou na etapa 1.

5. **Definir Permissões**:
   - Selecione o nível de permissão desejado para este email. Para permitir que o script crie eventos, escolha "Fazer alterações e gerenciar compartilhamento".

6. **Salvar Alterações**:
   - Clique em "Enviar" ou "Salvar" para confirmar as alterações.

Agora, seu script terá permissão para criar eventos no Google Calendar especificado e está pronto para uso!

## Funcionalidades



Este programa foi desenvolvido para monitorar a atividade de IDEs (Ambientes de Desenvolvimento Integrado) e criar eventos no Google Calendar com base na duração do uso dessas ferramentas. As principais funcionalidades são:

1. **Monitoramento de Atividade**:
   - O programa monitora se as seguintes IDEs estão em execução: 
     - Visual Studio Code (`Code.exe`)
     - IntelliJ IDEA (`idea64.exe`)
     - Eclipse (`eclipse.exe`)
   - Utiliza a biblioteca `psutil` para verificar se alguma dessas IDEs está ativa no sistema.

2. **Registro de Tempo de Uso**:
   - Quando uma IDE é detectada como em uso, o programa inicia um rastreamento do tempo de atividade.
   - Quando a IDE não está mais em uso, o tempo total de uso é calculado e exibido.

3. **Criação de Eventos no Google Calendar**:
   - Após o uso de uma IDE, o programa cria automaticamente um evento no Google Calendar.
   - O evento é agendado para o dia seguinte e registra o tempo de início e fim do uso da IDE.
   - As informações do evento incluem:
     - Título: "Programação"
     - Localização: "Home"
     - Descrição: "Tempo programando"
     - Horários: Data e hora de início e fim do evento, configurados para o fuso horário de São Paulo.

4. **Configuração Simples**:
   - O programa requer um arquivo de credenciais JSON do Google Cloud para autenticação e acesso à API do Google Calendar.
   - Um arquivo de configuração separado é necessário para armazenar o ID do calendário onde os eventos serão criados.

5. **Mecanismo de Erro**:
   - O programa verifica a presença dos arquivos necessários e fornece mensagens de erro descritivas caso algo esteja faltando ou mal configurado.

Essa combinação de funcionalidades permite que desenvolvedores mantenham um registro eficaz do tempo dedicado ao trabalho em IDEs, facilitando o gerenciamento de tempo e a organização de compromissos no Google Calendar.


## Como Funciona

### Estrutura do Diretório
Após executar o script, não haverá alterações na estrutura de diretórios do sistema, pois o programa é projetado para monitorar a atividade das IDEs e registrar eventos no Google Calendar sem mover arquivos ou criar novas pastas. A operação do programa é focada em registrar o tempo de uso das IDEs e criar eventos em um calendário específico.

### Execução do Script
O script deve ser executado em um ambiente que possua as IDEs especificadas (Visual Studio Code, IntelliJ IDEA ou Eclipse) e deve ter acesso ao Google Calendar através das credenciais configuradas. Ao iniciar, o programa:

1. **Monitora a Atividade das IDEs**:
   - Verifica periodicamente se alguma das IDEs está em execução.
   - Se uma IDE for detectada como ativa, o tempo de uso começa a ser rastreado.

2. **Registra o Tempo de Uso**:
   - Quando a IDE não está mais em uso, o tempo total de atividade é calculado.
   - O programa então prepara os dados para criar um evento no Google Calendar.

3. **Criação de Eventos no Google Calendar**:
   - Um evento é agendado para o dia seguinte, registrando o tempo de início e fim do uso da IDE.
   - As informações do evento incluem título, localização, descrição e horários, que são configurados para o fuso horário de São Paulo.

### Logs de Execução
O programa não gera um arquivo de log diretamente, mas você pode ver as mensagens no console informando o estado do monitoramento, como no exemplo:

```bash
IDE em uso, iniciando o rastreamento...
IDE não está mais em uso. Tempo total: 01:23:45
Evento criado: https://calendar.google.com/event?eid=...
```

Essas mensagens fornecem feedback sobre o funcionamento do programa e o sucesso na criação de eventos no Google Calendar. Caso haja erros (como a falta de arquivos de configuração), o programa informa o problema através de mensagens no console.


## Sugestões para Melhorias Futuras

1. **Interface Gráfica do Usuário (GUI)**:
   - Desenvolver uma interface gráfica para facilitar a configuração das credenciais e do ID do calendário, tornando o uso do programa mais amigável para usuários não técnicos.

2. **Notificações**:
   - Implementar notificações que alertem o usuário quando um evento for criado ou quando a IDE não estiver em uso por um período prolongado, ajudando a manter o controle do tempo.

3. **Relatório de Atividades**:
   - Criar um sistema que gere relatórios diários ou semanais das atividades monitoradas, detalhando o tempo gasto em cada IDE e os eventos criados no calendário.

4. **Customização de Eventos**:
   - Permitir que os usuários personalizem os detalhes do evento, como título, descrição, e fuso horário, por meio de um arquivo de configuração ou diretamente na interface do programa.

5. **Exportação de Dados**:
   - Adicionar a funcionalidade de exportar dados de atividades monitoradas para arquivos CSV ou outros formatos, facilitando a análise posterior.

## Fale Comigo

Se você tiver alguma dúvida, sugestão ou problema relacionado a este projeto, sinta-se à vontade para entrar em contato:

- **Email:** augusto_lordano@hotmail.com
- **LinkedIn:** [augustolordano](https://www.linkedin.com/in/augustolordano/)
- **GitHub:** [auglordano](https://github.com/auglordano)

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Espero que este projeto seja útil para você! Sinta-se à vontade para fazer um fork, contribuir com melhorias e compartilhar com outras pessoas que possam se beneficiar deste organizador de área de trabalho.
