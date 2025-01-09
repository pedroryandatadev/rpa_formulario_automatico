# Formulário automático

O objetivo do projeto e tornar o cadastro de informações em um formulário de uma página web automático sem precisar de qualquer interação humana.

## Passo a passo

- Abrir navegador 
- Abrir site
- Fazer login no site
- Cadastrar informações

## Requisitos

Instalar no terminal a biblioteca de automação `pyautogui`:

``` python
pip install pyautogui
```

Instalar no terminal a biblioteca de dados `pandas`:

```
pip install pandas
```

## Descrição

A inicializar o projeto ele irá abrir o navegador que está especificado "Edge", isso pode ser alterado ao substituir o nome Edge por outro navegador de exemplo Chrome.

Com o navegador aberto ele fará a digitação da URL do site e abri-la em seguida.

O site leva a uma página onde tem campos de login e senha que serão digitados, se estiverem inforamdos corretamente irá efetuar o login no site.

Com o login efetivado o usuário será levado a página de cadastro, na tela de cadastro tem quatro campos a ser preenchidos. Nessa etapa o código entra em loop usando uma base de dados como especificação, será registrado as informações dentro dela nos inputs da página de cadastro. Quando o sistema registrar o último dado da base o loop será encerrado finalizando o projeto. 


## Como iniciar o projeto

Use o código no terminal:

``` python
python main.py
```