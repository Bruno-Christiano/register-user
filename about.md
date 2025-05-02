# requirements.txt

# Para instalar as dependências, execute:

# pip install -r requirements.txt

# Certifique-se de ter ativado o ambiente virtual antes de rodar o comando.

# Comando para ativar o ambiente:

# Linux/Mac: source venv/bin/activate

# Windows: .\venv\Scripts\activate

Dica: como manter atualizado
Sempre que instalar algo novo com pip install nome-da-lib, rode novamente:

## pip freeze > requirements.txt

Assim você mantém tudo sincronizado para futuras instalações ou deploys. Quer que eu adicione isso como um comentário no topo do seu requirements.txt para lembrar?

🔹 ROTA (Controller)
Recebe o request e chama o serviço

          |
          ▼

🔹 SERVICE
✔️ Aplica regras de negócio
✔️ Manipula os dados se necessário
✔️ Valida antes de salvar
❗ Pode retornar erro ou resposta final

          |
          ▼

🔹 REPOSITORY
🔄 Acessa o banco (CRUD puro)
🔙 Retorna dados salvos / encontrados

          |
          ▼

🔹 SERVICE
(de novo)
✏️ Pega o que o repo retornou e transforma (se precisar)

          |
          ▼

🔹 ROTA (Controller)
Retorna a resposta formatada pro cliente (DTO ou JSON)
