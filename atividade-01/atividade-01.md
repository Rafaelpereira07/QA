# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** ADS5M26-2C
**Data:** 23/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Rafael Aires Pereira | [@Rafaelpereira07] |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | O usuário deve conseguir criar uma conta no LocalEats. | Usuário | O usuário não consegue se cadastrar e utilizar os recursos que dependem de uma conta. |
| Explícita | O usuário deve conseguir pesquisar restaurantes por especialidade ou localização. | Usuário | O usuário terá dificuldade para encontrar restaurantes de acordo com o que procura. |
| Implícita | Os dados informados pelo usuário durante o cadastro e login devem ser tratados de forma segura. | Usuário e negócio | Pode ocorrer exposição ou uso indevido de informações, comprometendo a confiança no sistema. |
| Implícita | O sistema deve apresentar informações e resultados de forma clara e compreensível. | Usuário | O usuário pode ter dificuldade para entender as opções disponíveis e realizar ações corretamente. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim. Um sistema pode implementar todas as funcionalidades solicitadas e ainda apresentar baixa qualidade. Isso acontece porque qualidade não depende apenas da existência das funcionalidades, mas também do atendimento às necessidades implícitas dos usuários. Por exemplo, mesmo que o sistema permita criar uma conta, se os dados do usuário não forem tratados de forma segura, a necessidade implícita de segurança não será atendida.

---

## 3. Tarefa 2: Exploração da aplicação

> Cada integrante deve explorar uma funcionalidade, realizando uma utilização esperada e uma utilização alternativa, inválida ou incompleta. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Rafael | Login | Foi realizada uma tentativa de acesso utilizando credenciais inválidas. | O sistema não realizou o acesso e apresentou a mensagem “Invalid credentials” em destaque na tela de login. | [ver evidência](evidencia-login-erro.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

> Cada integrante deve formular um requisito de qualidade relacionado à mesma funcionalidade explorada na Tarefa 2. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Rafael | Ao receber credenciais inválidas, o sistema deve informar ao usuário de forma clara que a tentativa de autenticação não foi realizada. | Usabilidade — proteção contra erros do usuário | No LocalEats, uma tentativa de login pode ocorrer com credenciais incorretas. Uma indicação clara do problema ajuda o usuário a compreender que o acesso não foi realizado e a corrigir os dados informados. | Realizar tentativas de login com credenciais inválidas e verificar se o sistema apresenta uma mensagem de erro clara e perceptível ao usuário. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
ChatGPT

**Como foi utilizada:**
Utilizada para auxiliar na organização e formatação das respostas, mantendo a estrutura solicitada na atividade.

**Como as respostas foram verificadas:**
O material foi revisado antes da entrega.
