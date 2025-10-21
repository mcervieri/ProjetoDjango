# FitApp — Django + AdminLTE3 + TailwindCSS (Tema Dark Glass)

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-success?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.6-purple?logo=bootstrap)](https://getbootstrap.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38BDF8?logo=tailwind-css)](https://tailwindcss.com/)
[![AdminLTE](https://img.shields.io/badge/AdminLTE-3.x-007bff?logo=html5)](https://adminlte.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📘 Sumário
1. [Visão Geral](#-visão-geral)
2. [Configuração Inicial](#-configuração-inicial-do-ambiente)
   - [Ambiente Python](#-ambiente-python)
   - [Ambiente Node (TailwindCSS)](#-ambiente-node-tailwindcss)
3. [Execução Durante o Desenvolvimento](#-execução-durante-o-desenvolvimento)
4. [Estrutura Visual](#-estrutura-visual)
5. [Observações Importantes](#-observações-importantes)

---

## 💡 Visão Geral
O **FitApp** é um projeto Django que combina o poder do **AdminLTE3** (baseado em Bootstrap 4) com a flexibilidade do **TailwindCSS**, usado exclusivamente para gerar o tema escuro personalizado `dark_theme.css`.

🔹 **AdminLTE3** fornece toda a estrutura de layout, componentes e JavaScript.  
🔹 **TailwindCSS** gera o visual *dark glass + neon green*, aplicado sobre o AdminLTE, via `dark_theme.css`.

---

## ⚙️ Configuração Inicial do Ambiente
Após clonar o repositório, execute os passos abaixo apenas na primeira vez para configurar o ambiente local.

---

### 🐍 Ambiente Python
Crie o ambiente virtual e instale as dependências do projeto:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate


### 🌿 Ambiente Node (Tailwind CSS)
O diretório node_modules/ está no .gitignore, portanto não será versionado.
Instale as dependências Node apenas na primeira vez:

npm install
npm run watch:css

---

## 🧩 Execução Durante o Desenvolvimento
Durante o desenvolvimento, use dois terminais abertos simultaneamente:

### 💻 Terminal 1 — TailwindCSS
Não é necessário ativar o .venv, pois o comando usa Node.js.
Ele recompila automaticamente o dark_theme.css ao detectar mudanças nos templates HTML ou classes Tailwind:

npm run watch:css


### 🐍 Terminal 2 — Django
Ative o ambiente virtual e execute o servidor de desenvolvimento:

source .venv/bin/activate
python manage.py runserver

Acesse o projeto em:
http://127.0.0.1:8000/

---

## 🎨 Estrutura Visual
Tecnologia - Função
AdminLTE 3 (Bootstrap 4) - Base do layout — navbar, sidebar, componentes e scripts JS.
TailwindCSS - Responsável por gerar o arquivo dark_theme.css com o tema personalizado.
FontAwesome - Ícones visuais integrados ao AdminLTE.

---

## 🧾 Observações Importantes
O arquivo dark_theme.css não deve ser editado manualmente.
Todas as mudanças visuais devem ser feitas no input.css ou via classes Tailwind nos templates.

Caso o CSS não atualize, encerre o processo npm run watch:css e execute novamente.

Em uma nova máquina ou ambiente, lembre-se de rodar:

npm install
pip install -r requirements.txt
