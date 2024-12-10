1. Primeiro, os dados foram extraídos por meio da API do Kaggle, utilizando a chave de autenticação contida no arquivo `kaggle.json`, no notebook 01_baixar_dados.ipynb. 
o arquivo `kaggle.json` deve estar na pasta "C:\Users\seu_usuario\.kaggle".
2. Em seguida, com os dados obtidos, foi realizado o estudo das bases e a aplicação do algoritmo no notebook 02_Solucao_careercon2019.ipynb.
3. Foi criado um endpoint com servidor local com nome de app.py (O servidor estará disponível em http://127.0.0.1:5000 por padrão)
4. O servidor Flask é iniciado com app.run(debug=True) para rodar localmente em modo de desenvolvimento.
