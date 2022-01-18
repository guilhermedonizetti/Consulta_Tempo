<h1 align="center">Consulta Tempo</h1>
<p align="center">Consulta de dados meteorológicos / previsão do tempo :computer:</p>

<b>Objetivo:</b> o objetivo do programa é realizar consultas em uma API que fornece os dados de previsão do tempo para determinada cidade. O usuário seleciona o município, e a API retorna os dados referente aos 10 próximos dias. O programa também exibe as informações de temperatura mínima :snowflake: e máxima :fire: em um gráfico.

<b>Fluxo:</b> o fluxo do programa ocorre da seguinte forma<br>
<ul>
  <li>Usuário seleciona a cidade (existe uma pequena lista)</li>
  <li>O programa faz uma requisição via AJAX passando o código da cidade</li>
  <li>O programa usa o código da cidade para consultar a API</li>
  <li>O resultado é retornado e aplicado ao gráfico</li>
  <li>O usuário tem a opção de baixar o gráfico em PNG</li>
</ul>

<br>

<p align="center">
  <img src="https://github.com/guilhermedonizetti/Consulta_Tempo/blob/master/images/prev_tempo.png" width="800" height="410">
</p>

<b>Ferramentas:</b> para gerar o gráfico está sendo usado a ferramenta Chart.JS e a API de consulta - por enquanto - é HG Brasil, mas pode ser alterada. A base é feita com Flask, microframework Python e outras tecnologias Web: JavaScript e HTML.

<br>

Uma coisa legal sobre o programa é a <b>atualização do gráfico sem refresh na página</b>. Na verdade, o que acontece é: o canvas do gráfico é removido e criado novamente com os novos valores, como no código abaixo:
```javascript
$("#myChart").remove()
var area = document.getElementById('areaGrafico')
area.innerHTML = '<canvas id="myChart" width="300" height="150"></canvas>'
```

<b>Obs.:</b> na hora de fazer a requisição na API, é obrigatório informar uma chave no parâmetro. A HG Brasil permite criar chaves gratuitas com limites de requisição, mas o suficiente para usar aqui. Crie uma conta (<a target="_blank" href="https://console.hgbrasil.com/">HG Brasil</a>) e gere a sua chave!


<br>

<p align="center">
  <b>Flask, Ajax, ChartJS</b><br>Guilherme Donizetti
</p>
