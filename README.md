# Site de Receitas

Este é um projeto de um site de receitas desenvolvido em Python e Django. O objetivo do site é permitir que os usuários se cadastrem, façam login e compartilhem suas receitas. Os usuários podem cadastrar suas próprias receitas, incluindo informações como nome, descrição, modo de preparo e tempo necessário para preparar. Além disso, eles também têm a capacidade de editar e excluir suas próprias receitas.

Tecnologias Utilizadas
O projeto utiliza as seguintes tecnologias:

Python: uma linguagem de programação poderosa e de alto nível, utilizada para desenvolver a lógica e funcionalidades do site de receitas.

Django: um framework web em Python que simplifica o desenvolvimento de aplicações web. O Django é utilizado para criar as rotas, gerenciar a autenticação de usuários, acessar o banco de dados e renderizar as páginas HTML.

Bootstrap: um framework front-end popular e poderoso que facilita o desenvolvimento de interfaces web responsivas e com um visual moderno. O Bootstrap é utilizado para estilizar o site de receitas, garantindo uma experiência visual agradável e consistente em diferentes dispositivos.

## Funcionalidades

O site de receitas possui as seguintes funcionalidades principais:

1. Autenticação de Usuários: Os usuários podem se cadastrar e fazer login no site. A autenticação é implementada usando o sistema de autenticação embutido do Django.

2. Página Inicial: Na página inicial, são exibidas as receitas cadastradas pelos usuários. Os usuários não precisam estar logados para visualizar as receitas.

3. Cadastro de Receitas: Os usuários logados têm a opção de cadastrar suas próprias receitas. Eles podem fornecer informações como o nome da receita, uma descrição breve, o modo de preparo e o tempo necessário para preparar a receita.

4. Edição de Receitas: Os usuários têm a capacidade de editar suas próprias receitas. Eles podem atualizar qualquer informação da receita, como o nome, a descrição, o modo de preparo ou o tempo necessário.

5. Exclusão de Receitas: Os usuários também podem excluir suas próprias receitas, caso desejem removê-las do site.

## Configuração do Projeto

Para configurar e executar o projeto em sua máquina local, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python em [python.org](https://www.python.org).

2. Clone este repositório em sua máquina local usando o comando:

   ```bash
   git clone <url-do-repositorio>
   ```

3. Acesse o diretório do projeto:

   ```bash
   cd site-de-receitas
   ```

4. Crie um ambiente virtual para o projeto:

   ```bash
   python -m venv venv
   ```

5. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source venv/bin/activate
     ```

6. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

7. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

8. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

9. Abra seu navegador e acesse [http://localhost:8000](http://localhost:8000) para visualizar o site de receitas.

## Contribuição

Se você quiser contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.

2. Clone o fork em sua máquina local:

   ```bash
   git clone <url-do-fork>
   ```

3. Crie um branch para suas alterações:

   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

4. Faça as alterações desejadas no código.

Desculpe pela incompletude. Aqui está a continuação da seção de Contribuição:

5. Após fazer as alterações desejadas no código, adicione e comite suas alterações:

   ```bash
   git add .
   git commit -m "Adiciona nova funcionalidade"
   ```

6. Faça o push das alterações para o seu fork:

   ```bash
   git push origin feature/nova-funcionalidade
   ```

7. Acesse o repositório original no GitHub e clique no botão "New Pull Request" (Novo Pull Request).

8. Preencha o formulário do Pull Request com informações claras e detalhadas sobre as alterações que você fez.

9. Aguarde a revisão do seu Pull Request. Se necessário, esteja preparado para realizar ajustes com base no feedback dos mantenedores do projeto.

Agradecemos antecipadamente suas contribuições para o projeto!

## Considerações Finais

Este projeto de site de receitas é um exemplo de aplicação web desenvolvida em Python e Django. Ele demonstra o uso de recursos fundamentais do Django, como autenticação de usuários, banco de dados e criação de modelos.

Sinta-se à vontade para personalizar e estender o projeto de acordo com suas necessidades. Esperamos que este projeto seja útil para aprimorar suas habilidades de desenvolvimento web usando Python e Django.

Se você tiver alguma dúvida ou encontrar problemas com o projeto, não hesite em entrar em contato. Aproveite e divirta-se explorando o mundo das receitas culinárias!
