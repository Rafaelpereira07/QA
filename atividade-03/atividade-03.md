# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats
**Modalidade:** Individual

---

# Tarefa 1: Planejamento dos testes

## 1.1 Objetivo dos testes

Verificar se o usuário consegue realizar um pedido corretamente no LocalEats e se o sistema impede ou trata adequadamente situações que possam causar pedidos incorretos ou incompletos. Os testes também devem verificar se as entradas fornecidas pelo usuário produzem os resultados esperados durante o processo de realização do pedido.

---

## 1.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado                                                                     |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------- |
| Rafael Aires Pereira | Fazer pedido            | Inclusão dos itens no pedido, preenchimento dos dados necessários e confirmação do pedido |

### Funcionalidade não incluída

| Funcionalidade    | Justificativa                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Consultar pedidos | Não faz parte diretamente do fluxo escolhido para os testes desta atividade. O foco será o processo de criação e confirmação de um novo pedido. |

---

## 1.3 Abordagem

| Item           | Decisão da equipe               | Justificativa                                                                                                                                             |
| -------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nível de teste | Sistema                         | A funcionalidade será analisada considerando o fluxo completo realizado pelo usuário na aplicação.                                                        |
| Tipo de teste  | Funcional                       | O objetivo é verificar se o sistema realiza corretamente a função de fazer um pedido.                                                                     |
| Perspectiva    | Caixa-preta                     | Os testes serão realizados considerando as entradas fornecidas pelo usuário e os resultados observáveis, sem analisar o código-fonte.                     |
| Técnica        | Particionamento de equivalência | A técnica permite dividir as entradas em grupos válidos e inválidos e selecionar valores representativos para reduzir a quantidade de testes necessários. |

---

## 1.4 Ambiente e responsabilidades

| Item                                     | Definição                                                                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ambiente necessário                      | Aplicação LocalEats disponível em https://local-eats-unisenac.vercel.app/, navegador atualizado, conexão com a internet e uma conta de usuário cadastrada. |
| Responsável pelo planejamento            | Rafael Aires Pereira                                                                                                                                                 |
| Responsável pela especificação dos casos | Rafael Aires Pereira                                                                                                                                                 |
| Responsável pela futura execução         | Rafael Aires Pereira                                                                                                                                                 |

---

## 1.5 Critérios

| Critério  | Definição da equipe                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------- |
| Entrada   | Aplicação disponível, usuário cadastrado e restaurante disponível para realização de pedido.                              |
| Saída     | Todos os três casos de teste planejados estiverem especificados e apresentarem resultados esperados claros e observáveis. |
| Suspensão | A aplicação estiver indisponível ou não houver restaurante/item disponível para realizar o fluxo necessário dos testes.   |

---

# Tarefa 2: Riscos e técnicas de teste

## 2.1 Análise dos riscos

| ID  | Integrante | Funcionalidade | Risco                                                                                | Consequência                                                                                                      | Probabilidade | Impacto | Prioridade | Justificativa                                                                                                                          |
| --- | ---------- | -------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------- | ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| R01 | Rafael Aires Pereira | Fazer pedido   | O sistema permitir a confirmação de um pedido sem os dados obrigatórios necessários. | O usuário poderá criar um pedido incompleto ou inválido, causando problemas no processamento do pedido.           | Média         | Alto    | Alta       | A confirmação de pedidos com informações incompletas pode comprometer diretamente o funcionamento da principal ação da funcionalidade. |
| R02 | Rafael Aires Pereira | Fazer pedido   | O sistema não tratar corretamente a ausência de itens no pedido.                     | O usuário poderá tentar confirmar um pedido sem produtos, gerando um pedido inválido ou comportamento inesperado. | Média         | Alto    | Alta       | A criação de um pedido sem itens representa uma situação inválida que pode afetar tanto o usuário quanto o processamento do pedido.    |

---

## 2.2 Aplicação da técnica

### Integrante responsável

**Nome:** Rafael Aires Pereira
**Funcionalidade:** Fazer pedido
**Riscos relacionados:** R01 e R02
**Técnica escolhida:** Particionamento de equivalência

### Por que a técnica foi escolhida?

O particionamento de equivalência é adequado porque permite separar as possíveis entradas do processo de realização de pedidos em classes válidas e inválidas. Dessa forma, é possível selecionar valores representativos de cada classe sem precisar testar todas as combinações possíveis.

A técnica também permite verificar situações em que os dados necessários estão preenchidos e situações em que algum dado necessário está ausente.

### Aplicação da técnica

Foram identificadas as seguintes classes de equivalência:

| Classe   | Situação                                                              | Valor representativo                                     |
| -------- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| Válida   | Pedido contendo pelo menos um item e os dados necessários preenchidos | Pedido com um item e informações válidas                 |
| Inválida | Pedido sem nenhum item                                                | Pedido vazio                                             |
| Inválida | Pedido com informação obrigatória ausente                             | Pedido com item, mas com dado obrigatório não preenchido |

### Casos derivados

* **CT01:** Realizar pedido com dados válidos.
* **CT02:** Tentar realizar pedido sem itens.
* **CT03:** Tentar realizar pedido com informação obrigatória ausente.

---

# Tarefa 3: Casos de teste e rastreabilidade

## 3.1 Especificação dos casos de teste

### CT01: Realizar pedido com dados válidos

**Integrante responsável:** Rafael Aires Pereira
**Funcionalidade:** Fazer pedido
**Risco ou requisito relacionado:** R01
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**

O usuário está cadastrado e autenticado no sistema. Existe um restaurante disponível e pelo menos um item disponível para ser adicionado ao pedido.

**Dados de entrada:**

* Restaurante disponível;
* Pelo menos um item disponível;
* Dados necessários para a realização do pedido preenchidos corretamente.

**Passos:**

1. Acessar a aplicação LocalEats.
2. Entrar no sistema com uma conta cadastrada.
3. Selecionar um restaurante disponível.
4. Selecionar um item do restaurante.
5. Adicionar o item ao pedido.
6. Preencher os dados necessários para o pedido.
7. Confirmar o pedido.

**Resultado esperado:**

O sistema deve aceitar os dados fornecidos e realizar a confirmação do pedido, apresentando ao usuário a confirmação de que o pedido foi realizado.

---

### CT02: Impedir pedido sem itens

**Integrante responsável:** Rafael Aires Pereira
**Funcionalidade:** Fazer pedido
**Risco ou requisito relacionado:** R02
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**

O usuário está cadastrado e autenticado no sistema e possui acesso ao fluxo de realização de pedido.

**Dados de entrada:**

* Pedido sem nenhum item adicionado.

**Passos:**

1. Acessar a aplicação LocalEats.
2. Entrar no sistema com uma conta cadastrada.
3. Acessar o fluxo de realização de pedido.
4. Não adicionar nenhum item ao pedido.
5. Tentar confirmar o pedido.

**Resultado esperado:**

O sistema deve impedir a confirmação de um pedido sem itens e informar ao usuário que é necessário adicionar pelo menos um item antes de realizar o pedido.

---

### CT03: Impedir pedido com informação obrigatória ausente

**Integrante responsável:** Rafael Aires Pereira
**Funcionalidade:** Fazer pedido
**Risco ou requisito relacionado:** R01
**Técnica utilizada:** Particionamento de equivalência

**Pré-condição:**

O usuário está cadastrado e autenticado no sistema. Existe um restaurante disponível e pelo menos um item disponível para realizar um pedido.

**Dados de entrada:**

* Pelo menos um item adicionado ao pedido;
* Uma das informações obrigatórias não preenchida.

**Passos:**

1. Acessar a aplicação LocalEats.
2. Entrar no sistema com uma conta cadastrada.
3. Selecionar um restaurante disponível.
4. Selecionar um item.
5. Adicionar o item ao pedido.
6. Deixar uma informação obrigatória sem preenchimento.
7. Tentar confirmar o pedido.

**Resultado esperado:**

O sistema deve impedir a confirmação do pedido e informar ao usuário que a informação obrigatória precisa ser preenchida antes da confirmação.

---

# 3.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito                                            | Técnica utilizada               | Casos de teste |
| ---------- | -------------- | ------------------------------------------------------------- | ------------------------------- | -------------- |
| Rafael Aires Pereira | Fazer pedido   | R01: confirmação de pedido com informação obrigatória ausente | Particionamento de equivalência | CT01 e CT03    |
| Rafael Aires Pereira | Fazer pedido   | R02: confirmação de pedido sem itens                          | Particionamento de equivalência | CT02           |

A matriz demonstra a relação entre a funcionalidade selecionada, os riscos identificados, a técnica utilizada e os casos de teste derivados.

---

# Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT

**Como foi utilizada:**

A ferramenta foi utilizada como apoio na organização do planejamento dos testes, para auxiliar na organização e formatação das respostas, mantendo a estrutura solicitada na atividade.

**Uma sugestão que precisou ser alterada ou rejeitada:**

As sugestões foram adaptadas para considerar somente as funcionalidades apresentadas no enunciado da atividade e evitar a criação de regras específicas que não foram informadas sobre o funcionamento do LocalEats.

**Como as respostas foram verificadas:**

O material foi revisado antes da entrega.
