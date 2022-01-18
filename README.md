<h1 align="center">Consulta Tempo</h1>
<p align="center">Consulta de dados meteorológicos / previsão do tempo :computer:</p>

<b>Objetivo:</b> o objetivo do programa é realizar consultas em uma API que fornece os dados de previsão do tempo para determinada cidade. O usuário seleciona o município, e a API retorna os dados. O programa também pretende exibir em gráfico as informações.

<b>Fluxo:</b> o fluxo do programa ocorre da seguinte forma<br>
<ul>
  <li>Usuário seleciona a cidade (existe uma pequena lista)</li>
  <li>O programa faz uma requisição via AJAX passando o código da cidade</li>
  <li>O programa usa o código da cidade para consultar a API</li>
  <li>O resultado é retornado e aplicado ao gráfico</li>
</ul>

<b>Ferramentas:</b> para gerar o gráfico está sendo usado a ferramenta Chart.JS e a API de consulta - por enquanto - é HG Brasil, mas pode ser alterada. A base é feita com Flask, microframework Python e outras tecnologias Web: JavaScript e HTML.

<br>

<p align="center">
  <b>Flask, Ajax, ChartJS</b><br>Guilherme Donizetti
</p>
