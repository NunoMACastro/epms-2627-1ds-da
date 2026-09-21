/**
 * Liga o formulário ao estado local e ao DOM.
 * As tarefas existem apenas neste carregamento da página; não há backend.
 * Pré-requisitos: funções, arrays e objetos diagnosticados em Fundamentos.
 */
"use strict";

const form = document.querySelector("#task-form");
const titleInput = document.querySelector("#task-title");
const areaInput = document.querySelector("#task-area");
const titleError = document.querySelector("#title-error");
const taskList = document.querySelector("#task-list");
const summary = document.querySelector("#summary");
const clearButton = document.querySelector("#clear-tasks");
const tasks = [];

/**
 * Recria a lista a partir dos dados: alterar o array não altera o DOM sozinho.
 * textContent trata a entrada como texto, sem interpretar HTML do utilizador.
 */
function renderTasks() {
  taskList.replaceChildren();
  for (const task of tasks) {
    const item = document.createElement("li");
    item.textContent = `${task.title} (${task.area})`;
    taskList.append(item);
  }
  summary.textContent = tasks.length === 0
    ? "Ainda não adicionaste tarefas."
    : `Tarefas planeadas: ${tasks.length}.`;
  clearButton.disabled = tasks.length === 0;
}

/**
 * Limpa a mensagem do exercício quando o aluno começa a corrigir o título.
 * As constraints nativas required e maxlength continuam presentes no HTML.
 */
function clearTitleError() {
  titleInput.removeAttribute("aria-invalid");
  titleError.textContent = "";
}

/**
 * Recebe o evento submit, valida espaços e simula processamento local.
 * @param {SubmitEvent} event Evento criado pelo browser na submissão válida.
 */
function addTask(event) {
  // Evita a navegação de um formulário tradicional: este laboratório é local.
  event.preventDefault();
  const title = titleInput.value.trim();
  if (title.length === 0) {
    titleError.textContent = "Escreve uma tarefa; espaços em branco não chegam.";
    titleInput.setAttribute("aria-invalid", "true");
    titleInput.focus();
    return;
  }
  tasks.push({ title, area: areaInput.value });
  renderTasks();
  form.reset();
  clearTitleError();
  titleInput.focus();
}

/** Limpa o estado e move o foco para o próximo controlo útil. */
function clearTasks() {
  tasks.length = 0;
  renderTasks();
  titleInput.focus();
}

form.addEventListener("submit", addTask);
titleInput.addEventListener("input", clearTitleError);
clearButton.addEventListener("click", clearTasks);
