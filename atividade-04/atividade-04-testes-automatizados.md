# Atividade 4: Testes Automatizados do LocalEats

- **Unidade Curricular:** Qualidade de Software
- **Projeto:** LocalEats
- **Modalidade:** Individual
- **Estudante:** Rafael Pereira
- **Endereço do Sistema:** [LocalEats Vercel](https://local-eats-unisenac.vercel.app/)

---

## 7. Identificação das Responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| :--- | :--- | :--- | :--- | :--- |
| TU01 | Rafael Pereira | Unitário | Pedido igual ou superior ao valor mínimo | `tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo` |
| TU02 | Rafael Pereira | Unitário | Pedido abaixo do valor mínimo | `tests/test_regras_localeats.py::test_pedido_abaixo_valor_minimo` |
| TU03 | Rafael Pereira | Unitário | Valores válidos e limites parametrizados | `tests/test_regras_localeats.py::test_pedido_valores_validos_limite` |
| TU04 | Rafael Pereira | Unitário | Exceção para valores negativos | `tests/test_regras_localeats.py::test_pedido_valor_negativo_lanca_excecao` |
| TF01 | Rafael Pereira | Funcional | Login e pesquisa de restaurantes por localização | `tests/test_localeats.py::test_pesquisar_restaurante_por_localizacao` |

---

## 5. Parte 1: Testes unitários e TDD

### TDD de Rafael Pereira

- **Regra escolhida:** Regra 1 (Verificar valor mínimo do pedido - `pedido_atingiu_valor_minimo`).
- **Primeiro teste escrito:** `test_pedido_abaixo_valor_minimo()`, esperando `False` para o valor `20.0`.
- **Por que o teste falhou inicialmente:** A função `pedido_atingiu_valor_minimo` ainda não havia sido criada no módulo `src/regras_localeats.py`.
- **Implementação mínima realizada:** Criação da função com a validação de que pedidos iguais ou superiores a R$ 30,00 retornam `True`.
- **Segundo teste escrito:** `test_pedido_atinge_valor_minimo()`, validando o comportamento com o valor `50.0`.
- **Melhoria ou refatoração realizada:** Adição da validação de valores negativos com `ValueError` e utilização de `@pytest.mark.parametrize` para testar diferentes valores e limites.

### Teste funcional com Playwright

- **Teste realizado:** `test_pesquisar_restaurante_por_localizacao()`.
- **Fluxo automatizado:** Acessar o LocalEats, realizar login com credenciais válidas, aguardar o redirecionamento para `index.html` e pesquisar restaurantes pela localização "Centro".
- **Validações realizadas:** Verificação do formulário de login, redirecionamento para a página principal, visibilidade dos resultados e presença da localização pesquisada.
- **Ferramenta utilizada:** Playwright com Chromium.

O teste funcional verifica o fluxo de navegação e pesquisa da aplicação, enquanto os testes unitários validam a Regra 1 de forma isolada.

---

## 10. Uso de inteligência artificial

- **Ferramentas utilizadas:** Assistentes de Inteligência Artificial (Gemini).
- **Como a ferramenta foi utilizada:** Apoio na estruturação do código e formatação do relatório em Markdown.
- **Uma sugestão que precisou ser alterada ou rejeitada:** A sugestão inicial da ferramenta foi implementar a Regra 2 (cálculo de desconto), porém alterei para a Regra 1 (valor mínimo do pedido) para se adequar melhor ao escopo escolhido para o trabalho.
- **Como o código sugerido foi verificado:** Revisão manual do código-fonte e execução local dos testes utilizando `pytest` e `Playwright`.

---

## 11. Resultado da execução

Execução realizada com Python 3.13.7, pytest 8.3.3 e Playwright.

- **Total de testes:** 7
- **Aprovados:** 7
- **Falhas:** 0
- **Tempo de execução:** 10,07 segundos.

```text
============================= test session starts =============================
tests/test_localeats.py::test_pesquisar_restaurante_por_localizacao[chromium] PASSED
tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo PASSED
tests/test_regras_localeats.py::test_pedido_abaixo_valor_minimo PASSED
tests/test_regras_localeats.py::test_pedido_valores_validos_limite[30.0] PASSED
tests/test_regras_localeats.py::test_pedido_valores_validos_limite[45.5] PASSED
tests/test_regras_localeats.py::test_pedido_valores_validos_limite[150.0] PASSED
tests/test_regras_localeats.py::test_pedido_valor_negativo_lanca_excecao PASSED

============================== 7 passed in 10.07s ==============================
```
