from playwright.sync_api import Page, expect

def test_pesquisar_restaurante_por_localizacao(page: Page):
  # 1. Acessar a aplicação
  page.goto("https://local-eats-unisenac.vercel.app/")

  # 2. Validar a página de login
  login_form = page.locator("#loginForm")
  expect(login_form).to_be_visible()

  # 3. Realizar login
  page.locator("#loginEmail").fill("rafael@email.com")
  page.locator("#loginPassword").fill("rafael123")
  login_form.locator("button[type='submit']").click()

  # 4. Aguardar o redirecionamento para a página principal
  page.wait_for_url("**/index.html")

  # 5. Validar a página principal
  campo_busca = page.locator("#searchInput")
  expect(campo_busca).to_be_visible()

  # 6. Pesquisar restaurantes pela localização
  campo_busca.fill("Centro")
  page.locator("#searchBtn").click()

  # 7. Validar os resultados da pesquisa
  restaurantes = page.locator("#restaurantGrid .rest-card")

  expect(restaurantes.first).to_be_visible()
  expect(page.locator("#restaurantGrid")).to_contain_text("Centro")
