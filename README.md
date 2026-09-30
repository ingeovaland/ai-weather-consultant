README 

# AI Weather Consultant 

AI Weather Consultant é um assistente meteorológico desenvolvido em Python com interface em html e css que permite aos usuários fazer perguntas sobre o tempo e obter informações
meteorológicas com base na sua localização atual ou numa cidade informada pelo utilizador.

O assistente utiliza um agente de inteligência artificial para interpretar
as perguntas e decidir quais ferramentas deve utilizar para obter as informações
necessárias e manter uma conversa.

Durante a utilização da aplicação, o histórico da conversa é mantido para que
o utilizador possa visualizar as mensagens anteriores da sessão.

# Funcionalidades

- Consulta as condições meteorológicas atuais;
- Consulta a localização atual do usuário através de coordenadas geográficas;
- Responder a perguntas utilizando um agente de inteligência artificial;
- Manter o histórico das mensagens durante a sessão;
- Apresentar as mensagens do utilizador e do assistente numa interface web;
- Utilizar dados meteorológicos obtidos através da OpenWeather API.

# As tecnologias utilizadas, foram:
Python
Flask
LangChain
LangGraph
Google Gemini
OpenWeather API
Nominatim
SQLite
HTML
CSS
JavaScript

# Funcionamento 

O funcionamento da app acontece através de uma web application desenvolvida com Flask

Quando o utilizador faz uma pergunta:

1. A aplicação recebe a mensagem através do Flask;
2. A localização do utilizador pode ser obtida através do navegador ou do próprio utilizador que pode informar ao agente;
3. A mensagem é enviada para o agente de inteligência artificial;
4. O agente interpreta a pergunta e decide qual ferramenta utilizar;
5. Quando necessário, a aplicação consulta a localização através do Nominatim
   e os dados meteorológicos através da OpenWeather API;
6. A resposta é devolvida ao utilizador que consegue continuar a conversa em um ritmo uma vez que mensagens anteriores são mantidas na sessão atua.



# A Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd ai-weather-consultant
