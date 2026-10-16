/**
 * app.js: o comportamento do Plano de estudo local.
 * Recebe o envio do formulário, guarda cada tarefa numa lista em memória
 * e volta a mostrar essa lista na página. Não há servidor: as tarefas
 * desaparecem quando a página se recarrega.
 */

// Modo estrito: o browser passa a dar erro em vez de aceitar alguns enganos
// em silêncio, como usar uma variável que nunca foi declarada.
"use strict";

// Os elementos da página que o código usa, encontrados uma só vez pelo id.
const formulario = document.querySelector("#formulario-tarefa");
const campoTitulo = document.querySelector("#titulo-tarefa");
const campoArea = document.querySelector("#area-tarefa");
const erroTitulo = document.querySelector("#erro-titulo");
const listaTarefas = document.querySelector("#lista-tarefas");
const resumo = document.querySelector("#resumo");
const botaoLimpar = document.querySelector("#limpar-tarefas");

// Os dados: um array com um objeto por tarefa, com o título e a área.
// A lista da página desenha-se sempre a partir deste array.
const tarefas = [];

/**
 * Volta a desenhar a lista da página a partir do array tarefas e atualiza
 * o resumo e o botão de limpar.
 * Não devolve nada: muda o DOM. Chama-se depois de cada mudança no array,
 * porque mudar o array não muda a página sozinho.
 */
function mostrarTarefas() {
  // Apaga os itens que a lista já tinha. Sem esta linha, cada tarefa nova
  // voltava a acrescentar todas as anteriores, e a lista ficava repetida.
  listaTarefas.replaceChildren();
  for (const tarefa of tarefas) {
    const item = document.createElement("li");
    // As crases deixam pôr o valor de uma variável dentro do texto, com ${...}.
    // O textContent mostra o texto tal como foi escrito: se alguém escrever
    // <strong>teste</strong>, aparecem as etiquetas, e não um negrito.
    item.textContent = `${tarefa.titulo} (${tarefa.area})`;
    listaTarefas.append(item);
  }
  if (tarefas.length === 0) {
    resumo.textContent = "Ainda não adicionaste tarefas.";
  } else {
    resumo.textContent = `Tarefas planeadas: ${tarefas.length}.`;
  }
  // Com a lista vazia, não há nada para limpar, e o botão fica desativado.
  botaoLimpar.disabled = tarefas.length === 0;
}

/**
 * Tira a mensagem de erro do título e a marca de campo inválido.
 * Não devolve nada: muda o DOM. Corre a cada letra escrita no campo, para a
 * mensagem desaparecer logo que a pessoa começa a corrigir.
 * As restrições do HTML, required e maxlength, continuam no campo.
 */
function limparErroTitulo() {
  campoTitulo.removeAttribute("aria-invalid");
  erroTitulo.textContent = "";
}

/**
 * Trata o envio do formulário: valida o título, guarda a tarefa e mostra a lista.
 * Não devolve nada. Se o título só tiver espaços, mostra a mensagem de erro
 * e não guarda nada. Se for válido, acrescenta uma tarefa ao array tarefas,
 * volta a desenhar a lista e limpa o formulário.
 * @param {SubmitEvent} evento o envio do formulário, criado pelo browser.
 *   Só chega aqui depois de o browser aceitar as restrições do HTML.
 */
function adicionarTarefa(evento) {
  // Sem esta linha, o browser enviava o formulário e recarregava a página,
  // e a tarefa perdia-se. Aqui, tudo acontece na própria página.
  evento.preventDefault();
  // O trim() tira os espaços do princípio e do fim. Um título só com espaços
  // passa no required do HTML, mas fica vazio depois do trim().
  const titulo = campoTitulo.value.trim();
  if (titulo.length === 0) {
    erroTitulo.textContent = "Escreve uma tarefa; espaços em branco não chegam.";
    // O aria-invalid diz ao leitor de ecrã que o campo tem um erro,
    // e o CSS usa-o para desenhar a borda vermelha.
    campoTitulo.setAttribute("aria-invalid", "true");
    campoTitulo.focus();
    return;
  }
  tarefas.push({ titulo: titulo, area: campoArea.value });
  mostrarTarefas();
  // O reset() põe o formulário como estava ao abrir a página.
  formulario.reset();
  limparErroTitulo();
  // O foco volta ao campo, para se escrever a tarefa seguinte sem usar o rato.
  campoTitulo.focus();
}

/**
 * Apaga todas as tarefas e volta a desenhar a lista, que fica vazia.
 * Não devolve nada. O foco vai para o campo do título, porque o botão
 * de limpar fica desativado, e o foco não pode ficar num botão desativado.
 */
function limparTarefas() {
  // Pôr o comprimento a 0 esvazia o array. Não se pode escrever tarefas = [],
  // porque tarefas é uma constante.
  tarefas.length = 0;
  mostrarTarefas();
  campoTitulo.focus();
}

// O que a pessoa faz na página e a função que responde a cada coisa.
formulario.addEventListener("submit", adicionarTarefa);
campoTitulo.addEventListener("input", limparErroTitulo);
botaoLimpar.addEventListener("click", limparTarefas);
