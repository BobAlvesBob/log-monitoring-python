# Secure Logging Blockchain - README

## Visão Geral

Este projeto tem como objetivo criar um sistema seguro de logging utilizando blockchain para garantir a integridade dos logs produzidos. A solução captura eventos de log do terminal e os armazena em uma blockchain, garantindo assim que as informações sejam imutáveis e protegidas contra alterações indevidas.

O sistema utiliza Python, Docker, e é composto por duas principais partes: um servidor que executa um backend e um cliente que monitora e envia logs para a blockchain. O projeto foi desenvolvido com o uso de containers Docker para facilitar o ambiente de execução e isolação dos processos.

## Estrutura do Projeto

- **Blockchain**: A blockchain foi desenvolvida em Python e cada bloco armazena dados de logs gerados pela máquina local.
- **Docker**: O projeto utiliza `docker-compose` para criar containers separados para o servidor e o cliente.
- **Logging**: Logs gerados no terminal (stdin) são transformados em hashes e armazenados na blockchain para garantir a integridade e imutabilidade dos dados.

## Como Funciona

1. **Criação do Bloco Gênese**: Ao inicializar, uma instância da blockchain é criada, com o primeiro bloco (“Bloco Gênese”).
2. **Captura dos Logs do Terminal**: Um logger é configurado para capturar entradas feitas pelo usuário no terminal. A cada log inserido, uma nova entrada é criada na blockchain, gerando um novo bloco com um hash calculado com base nas informações do log.
3. **Docker**: Dois containers são criados, um para o servidor e outro para o cliente, garantindo o isolamento e uma execução consistente.

## Instruções de Execução

### Pré-Requisitos

- **Docker** e **docker-compose** devem estar instalados.
- **Python 3.8+** com suporte a `venv`.

### Instalando o Ambiente Localmente

1. Clone o repositório:
   ```bash
   git clone <URL do Repositório>
   cd secure_logging_blockchain
   ```

2. Crie e ative o ambiente virtual Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### Executando com Docker

1. Construa e inicie os containers Docker:
   ```bash
   docker-compose up --build
   ```

2. Acompanhe a saída dos logs do cliente e servidor nos containers criados.

### Testando a Captura de Logs

- Com o projeto rodando, é possível adicionar mensagens de log digitando-as diretamente no terminal:
  ```
  Digite uma mensagem de log (ou 'sair' para terminar): Este é um exemplo de log
  ```
- Cada mensagem inserida será registrada na blockchain, com o terminal exibindo a confirmação de que um novo bloco foi adicionado.

### Verificando os Logs

- Para verificar o arquivo de logs (`local_logs.log`), use o comando:
  ```bash
  cat local_logs.log
  ```
- Os dados também são registrados na blockchain, que pode ser consultada imprimindo o objeto da blockchain:
  ```python
  blockchain.get_chain()
  ```

## Estrutura do Código

- **blockchain.py**: Contém a implementação da blockchain e a lógica de adição de novos blocos.
- **logger.py**: Captura logs do terminal e os envia para a blockchain.
- **Dockerfile** e **docker-compose.yml**: Configurações para criar os containers Docker do servidor e do cliente.

## Problemas e Soluções Encontradas

- **Criação Automática de Blocos**: Inicialmente, blocos eram criados automaticamente em intervalos fixos, resultando em registros indesejados e repetitivos. Isso foi corrigido para que os blocos sejam adicionados apenas quando um log é inserido manualmente no terminal.
- **Erros de Importação**: Houve problemas com o módulo `watchdog`, que foram resolvidos ao garantir que a dependência estivesse corretamente instalada tanto localmente quanto nos containers.

## Futuras Melhorias

- **Monitoramento Automático**: Adicionar suporte para monitorar logs de outras aplicações automaticamente, como arquivos de log do sistema.
- **Integração com uma Interface Web**: Desenvolver uma interface web para visualizar a blockchain e os logs armazenados.
- **Segurança Adicional**: Implementar autenticação e criptografia dos logs antes de enviá-los para a blockchain.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

