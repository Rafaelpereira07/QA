# Atividade 2: Organização da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** ADS5M26-2C
**Data:** 30/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Rafael Aires Pereira | @Rafaelpereira07 |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não existem critérios claros para considerar uma funcionalidade pronta. | Funcionalidades podem ser disponibilizadas sem atender completamente aos requisitos ou sem passar pelos testes necessários. |
| A equipe considera que somente o QA deve realizar testes. | Defeitos podem ser descobertos tarde, aumentando o retrabalho e concentrando excessivamente a responsabilidade pela qualidade em uma única pessoa. |
| Defeitos são identificados, mas nem sempre são registrados ou acompanhados. | Problemas podem ser esquecidos, voltar a ocorrer ou permanecer sem correção antes da disponibilização de uma versão. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade do LocalEats deve ser responsabilidade de toda a equipe. O QA possui responsabilidades específicas relacionadas a testes e avaliação da qualidade, mas desenvolvedores, responsáveis pelo produto, DevOps e liderança também participam da construção da qualidade. A responsabilidade compartilhada ajuda a prevenir defeitos e evita que os problemas sejam identificados somente no final do desenvolvimento.

---

## 3. Tarefa 2: Papéis e competências

> Cada integrante deve ser responsável pela análise de pelo menos um papel. Acrescentem ou removam linhas conforme a composição da equipe e os papéis escolhidos.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Rafael | Responsável pelo produto | Definir e priorizar requisitos, critérios de aceitação e prioridades de correção. | Levantamento e análise de requisitos, definição de critérios de aceitação e conhecimento do produto. | Comunicação, organização, tomada de decisão e visão do usuário. |
| Rafael | Desenvolvedor | Implementar funcionalidades, realizar testes unitários e revisar código. | Programação, testes unitários, controle de versão e revisão de código. | Organização, colaboração, atenção aos detalhes e pensamento crítico. |

---

## 4. Tarefa 3: Matriz de responsabilidades

> Substituam “Papel 1” e “Papel 2” pelos papéis definidos pela equipe. Acrescentem ou removam colunas conforme necessário.

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Papel 1 | Papel 2 |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C |
| Revisar requisitos | R/A | C |
| Implementar a funcionalidade | A | R |
| Revisar o código | I | R/A |
| Criar testes unitários | I | R/A |
| Planejar e executar testes do sistema | I | C |
| Registrar e acompanhar defeitos | I | C |
| Priorizar a correção dos defeitos | R/A | C |
| Aprovar a disponibilização da versão | A | C |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**
Concentrar a execução dos testes exclusivamente no QA. Isso pode deixar a qualidade dependente de um único papel e fazer com que defeitos sejam encontrados somente depois da implementação.

**Consequência:**
A aprovação da disponibilização da versão não deve ser atribuída simultaneamente a vários papéis, pois isso pode gerar dúvidas sobre quem possui a decisão final.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Revisão de código por outro integrante antes da integração. | Ajuda a identificar erros antes que cheguem às etapas posteriores e evita que a qualidade fique concentrada no QA. | Desenvolvedor, QA |
| Registro e acompanhamento dos defeitos em uma ferramenta compartilhada. | Evita que defeitos identificados sejam esquecidos ou deixem de ser acompanhados. | Desenvolvedor, QA, PO |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
ChatGPT

**Como foi utilizada:**
Utilizada para auxiliar na organização e formatação das respostas, mantendo a estrutura solicitada na atividade.

**Como as respostas foram verificadas:**
O material foi revisado antes da entrega.
