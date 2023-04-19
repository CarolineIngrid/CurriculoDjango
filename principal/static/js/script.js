const openModalBtn = document.getElementById("open-modal");
const modal = document.getElementById("modal");
const closeModalBtn = document.getElementsByClassName("close")[0];

// Abrir o modal ao clicar no botão
openModalBtn.addEventListener("click", function() {
  modal.style.display = "block";
});

// Fechar o modal ao clicar no botão de fechar
closeModalBtn.addEventListener("click", function() {
  modal.style.display = "none";
});

// Fechar o modal ao clicar fora do modal
window.addEventListener("click", function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
});