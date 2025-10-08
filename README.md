⚙️ Configuração inicial do ambiente Após clonar o repositório, execute os passos abaixo apenas na primeira vez para configurar o ambiente local

🐍 Ambiente Python Crie o ambiente virtual: python -m venv .venv source .venv/bin/activate Instale as dependências do projeto: pip install -r requirements.txt python manage.py migrate

🌿 Ambiente Node (Tailwind CSS): O diretório node_modules está no .gitignore, portanto não será versionado. Isso significa que é necessário instalar as dependências Node apenas na primeira vez. Instale as dependências do Tailwind: npm install Após isso, o comando abaixo ficará disponível: npm run watch:css

---

🧩 Execução durante o desenvolvimento Durante o desenvolvimento, use dois terminais abertos simultaneamente: um para o Tailwind (CSS) e outro para o Django (Python).

💻 Terminal 1 — Tailwind CSS Não precisa ativar o .venv, pois o comando usa o Node.js. Ele recompila automaticamente o CSS sempre que você alterar um arquivo HTML, template ou classe do Tailwind. npm run watch:css

🐍 Terminal 2 — Django Aqui é necessário ativar o ambiente virtual (.venv), pois esse terminal executa o servidor do Django. source .venv/bin/activate python manage.py runserver

Depois disso, acesse o projeto em: http://127.0.0.1:8000/
