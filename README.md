# Gerenciamento e Processamento de Arquivos

## Descrição do Projeto
Este projeto implementa uma fila para armazenar e processar arquivos TXT, além de fornecer funcionalidades para importar, processar, remover e buscar palavras nos arquivos. A fila segue a estrutura FIFO (First In, First Out) e inclui uma fila de prioridade para arquivos pequenos. Também são fornecidos testes automatizados para garantir a funcionalidade correta.

## Funcionalidades Implementadas

### 1. Fila (Queue) (`queue.py`)
- **Objetivo:** Implementar uma fila FIFO.
- **Métodos:**
  - `enqueue`: Adiciona um elemento à fila.
  - `dequeue`: Remove o elemento mais antigo da fila.
  - `search`: Busca um elemento na fila pelo índice.
  - `__len__`: Retorna o tamanho da fila.
- **Tratamento de Exceções:**
  - `search` lança `IndexError` com a mensagem "Índice Inválido ou Inexistente" para índices inválidos.

### 2. Importação de Arquivos TXT (`file_management`)
- **Função `txt_importer`:**
  - Importa notícias de um arquivo TXT utilizando "\n" como separador.
  - Lança mensagem de erro na `stderr` se o arquivo não existir ou tiver formato inválido.
  - Retorna uma lista com as linhas do arquivo.

### 3. Processamento de Arquivos (`file_process`)
- **Função `process`:**
  - Transforma o conteúdo da lista gerada pela função `txt_importer` em um dicionário.
  - Registra o processamento dos arquivos na fila.
  - Ignora arquivos que já tenham sido processados anteriormente.
  - Exibe dados processados via `stdout`.

### 4. Remoção de Arquivos Processados (`file_process`)
- **Função `remove`:**
  - Remove o primeiro arquivo processado da fila.
  - Exibe mensagem via `stdout` se não houver arquivos na fila ou em caso de remoção bem-sucedida.

### 5. Metadados de Arquivos Processados (`file_process`)
- **Função `file_metadata`:**
  - Apresenta informações superficiais de um arquivo processado.
  - Exibe mensagem de erro na `stderr` se a posição for inválida.
  - Exibe informações relacionadas ao arquivo via `stdout` se a posição for válida.

### 6. Testes para Fila de Prioridade (`tests/priority_queue/test_priority_queue.py`)
- **Objetivo:** Implementar testes para a classe `PriorityQueue` que armazena arquivos pequenos de forma prioritária.
- **Métodos Testados:**
  - `enqueue`: Adiciona elementos com prioridade.
  - `dequeue`: Remove elementos respeitando a prioridade.
  - `search`: Busca elementos respeitando a prioridade.
- **Validações:**
  - Respeito à lógica de prioridades.
  - Levantamento de exceções para índices inválidos.

### 7. Verificação de Existência de Palavra (`word_search`)
- **Função `exists_word`:**
  - Verifica a existência de uma palavra em todos os arquivos processados.
  - Retorna uma lista com informações de cada arquivo e linhas onde a palavra foi encontrada.
  - Realiza busca _case insensitive_.
  - Não modifica a fila durante a busca.

### 8. Busca por Palavra com Conteúdo da Linha (`word_search`)
- **Função `search_by_word`:**
  - Segue os mesmos critérios da função `exists_word`.
  - Inclui na saída o conteúdo das linhas encontradas.
